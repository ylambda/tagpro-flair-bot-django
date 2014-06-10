import requests
from BeautifulSoup import BeautifulSoup
from django.shortcuts import redirect
from django.core.urlresolvers import reverse
from social_auth.pipeline import deauth_tagpro as deauth_tagpro_pipeline

def get_flairs(html):
    flair_table = html.findAll('table')[2]
    rows = flair_table.findAll('tr')
    flairs = []
    for tr in rows:
        if tr.get('class', '') == "fade" or tr.find('th'):
            # No faded rows or the heading
            continue
        flairs.append(tr.findAll('td')[1].getString())
    return flairs

def auth_tagpro(request):
    profile_url = request.POST.get('profile_url')
    token = request.session.get('tagpro_token')
    response = requests.get(profile_url)
    parsed = BeautifulSoup(response.text)
    tagpro_name = parsed.title.getString()[len("TagPro Ball: "):]
    if tagpro_name == token:
        request.session['tp_authenticated'] = True
        request.session['tp_profile'] = profile_url
        request.session['available_flair'] = get_flairs(parsed)
    return redirect(reverse('home'))

def deauth_tagpro(request):
    deauth_tagpro_pipeline(request=request)
    return redirect(reverse('home'))