from social.backends.reddit import RedditOAuth2 as DefaultRedditOAuth2
from django.conf import settings

class RedditOAuth2(DefaultRedditOAuth2):
    def auth_headers(self):
        headers = super(RedditOAuth2, self).auth_headers()
        headers.update({
            'User-Agent': settings.BOT_USER_AGENT
        })
        return headers
