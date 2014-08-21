/r/TagPro Flair Bot
===================

This is a Django project to allow users to assign their own Reddit flair based
on what they have earned with their TagPro profile.

The following environmental variables need to be set to run the app:

* ``SOCIAL_AUTH_REDDIT_KEY`` and ``SOCIAL_AUTH_REDDIT_SECRET``
    * Obtained through Reddit. You must create an app in your
    [Reddit preferences](https://ssl.reddit.com/prefs/apps/).
* ``REDDIT_MOD_SUBREDDIT``
    * Subreddit flairs are assigned for.
* ``REDDIT_MOD_USERNAME``
    * Username of the user the bot uses to assign the flair. Must be a
    moderator of ``REDDIT_MOD_SUBREDDIT``.
* ``REDDIT_MOD_PASSWORD``
    * Reddit password for ``REDDIT_MOD_USERNAME``.
* ``RAVEN_PUBLIC_KEY``, ``RAVEN_PRIVATE_KEY``, ``RAVEN_PROJECT_ID``
    * If you're running your own instance and you want error reporting through
    Sentry, set these to what Sentry provides for your DSN. The format is
    ``https://RAVEN_PUBLIC_KEY:RAVEN_PRIVATE_KEY@app.getsentry.com/RAVEN_PROJECT_ID``


# Authentication

## Reddit

Reddit authentication is managed with Reddit's own OAuth2 API.  A new user in
the app is created with their Reddit username when they authenticate through 
Reddit.

## TagPro

Right now TagPro authentication is a bit hacky.  After a user authenticates with
Reddit, they are assigned a 12-character token.  To prove they own a profile,
they change their name to this token and supply the app with their profile URL.
The app decides that the user owns the profile if the name of the user on the
profile matches the generated token.

In the future this hack could be avoided if there was a TagPro-blessed way of
confirming that a user owns a TagPro profile. One option discussed with Lucky
was an API key available on your profile only when logged in which you could
supply to apps. Then there would be a URL on TagPro the app would post the key
to which would return whether the key was valid for the profile or not.