from BeautifulSoup import BeautifulSoup
import json
import praw
import requests
from django.conf import settings
from django.contrib import messages
from django.core.urlresolvers import reverse
from django.http import HttpResponse
from django.shortcuts import redirect
from django.views.generic import TemplateView
from social_auth.pipeline import deauth_tagpro as deauth_tagpro_pipeline
from tpflair.flair import FLAIR_DATA, FLAIR, FLAIR_BY_POSITION


reddit_api = praw.Reddit(user_agent=settings.BOT_USER_AGENT)
reddit_api.login(username=settings.REDDIT_MOD_USERNAME, password=settings.REDDIT_MOD_PASSWORD)


def json_response(data):
    return HttpResponse(json.dumps(data), content_type="application/json")


class HomeView(TemplateView):
    template_name = "home.html"
    
    def get_context_data(self):
        context = super(HomeView, self).get_context_data()
        context.update({'FLAIR_DATA': FLAIR_DATA})
        return context


def parse_available_flair(html):
    """
    Helper function which pulls the active flairs from the parsed HTML of a
    user's profile page.
    """
    flair_table = html.findAll('table')[2]
    rows = flair_table.findAll('tr')
    flairs = []
    for row in rows:
        icon = row.find('div')
        if icon and row.get("class", "") != "fade":
            position = icon['style'][len('background-position: '):]
            flairs.append(FLAIR_BY_POSITION[position]['id'])
    return flairs


def auth_tagpro(request):
    """
    Verify that the user owns the specified TagPro profile.
    """
    profile_url = request.POST.get('profile_url')
    token = request.session.get('tagpro_token')
    response = requests.get(profile_url)
    parsed = BeautifulSoup(response.text)
    tagpro_name = parsed.title.getString()[len("TagPro Ball: "):]
    if tagpro_name == token:
        request.session['tp_authenticated'] = True
        request.session['tp_profile'] = profile_url
        request.session['current_flair'] = get_current_flair(request)
        request.session['available_flair'] = parse_available_flair(parsed)
    else:
        messages.error(request, "Your name doesn't match the token!")
    return redirect(reverse('home'))


def deauth_tagpro(request):
    """
    Unlink the session from the specified TagPro profile.
    """
    deauth_tagpro_pipeline(request=request)
    return redirect(reverse('home'))


def get_current_flair(request):
    return reddit_api.get_flair(
        settings.REDDIT_MOD_SUBREDDIT, request.user.username) or {}

def set_flair(request):
    """
    Set the user's flair for the subreddit.
    """
    flair = request.POST.get('flair', None)
    if (
            'available_flair' in request.session and 
            flair in request.session['available_flair'] and 
            flair in FLAIR.keys()):
        request.session['current_flair'] = request.session['current_flair'] or get_current_flair(request)
        flair_text = request.session['current_flair'].get('flair_text', '')
        reddit_api.set_flair(
            settings.REDDIT_MOD_SUBREDDIT,
            request.user.username,
            flair_css_class=flair, flair_text=flair_text)
        request.session['current_flair']['flair_css_class'] = flair
        if request.is_ajax():
            return json_response({'success': True})
        else:
            messages.success(request, "Flair set!")
    else:
        error = "Sorry, you can't have that flair :("
        if request.is_ajax():
            return json_response({'success': False, 'error': error})
        messages.error(request, error)
    return redirect(reverse("home"))
