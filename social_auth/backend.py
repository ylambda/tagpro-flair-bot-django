from social.backends.base import BaseAuth
from social.backends.reddit import RedditOAuth2 as DefaultRedditOAuth2

from django.conf import settings

class RedditOAuth2(DefaultRedditOAuth2):
    def auth_headers(self):
        headers = super(RedditOAuth2, self).auth_headers()
        headers.update({
            'User-Agent': settings.BOT_USER_AGENT
        })
        return headers

    def user_data(self, access_token, *args, **kwargs):
        retry_count = 0
        exc = None
        while retry_count < settings.REDDIT_MAX_RETRIES:
            try:
                return super(RedditOAuth2, self).user_data(access_token, *args, **kwargs)
            except Exception, e:
                exc = e
                pass
        raise exc

