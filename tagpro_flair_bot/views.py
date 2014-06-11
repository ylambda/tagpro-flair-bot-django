from BeautifulSoup import BeautifulSoup
import praw
import requests
from django.conf import settings
from django.contrib import messages
from django.core.urlresolvers import reverse
from django.shortcuts import redirect
from django.views.generic import TemplateView
from social_auth.pipeline import deauth_tagpro as deauth_tagpro_pipeline


reddit_api = praw.Reddit(user_agent=settings.BOT_USER_AGENT)
reddit_api.login(username=settings.REDDIT_MOD_USERNAME, password=settings.REDDIT_MOD_PASSWORD)


FLAIRS_BY_KEY = {v[1]: v[0] for k, v in settings.FLAIRS_BY_POSITION.iteritems()}


class HomeView(TemplateView):
    template_name = "home.html"
    
    def get_context_data(self):
        context = super(HomeView, self).get_context_data()
        context.update({'FLAIRS_BY_KEY': FLAIRS_BY_KEY})
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
            flairs.append(settings.FLAIRS_BY_POSITION[position][1])
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


def set_flair(request, flair):
    """
    Set the user's flair for the subreddit.
    """
    if 'available_flair' in request.session and flair in request.session['available_flair'] and flair in FLAIRS_BY_KEY.keys():
        flair_data = reddit_api.get_flair(
            settings.REDDIT_MOD_SUBREDDIT, request.user.username) or {}
        flair_text = flair_data.get('flair_text', '')
        reddit_api.set_flair(
            settings.REDDIT_MOD_SUBREDDIT,
            request.user.username,
            flair_css_class=flair, flair_text=flair_text)
        messages.success(request, "Flair set!")
    else:
        messages.error(request, "Sorry, you can't have that flair :(")
    return redirect(reverse("home"))
