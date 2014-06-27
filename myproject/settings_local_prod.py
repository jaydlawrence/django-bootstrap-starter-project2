import os

# BUG:  THESE KEYS NEED SOCIAL PREFIX . FIX THEM LATER

# OAuth keys for Social Auth
TWITTER_CONSUMER_KEY = ''
TWITTER_CONSUMER_SECRET = ''
FACEBOOK_APP_ID = os.environ['FACEBOOK_APP_ID']
FACEBOOK_API_SECRET = os.environ['FACEBOOK_API_SECRET']
LINKEDIN_CONSUMER_KEY = ''
LINKEDIN_CONSUMER_SECRET = ''
ORKUT_CONSUMER_KEY = ''
ORKUT_CONSUMER_SECRET = ''
GOOGLE_CONSUMER_KEY = ''
GOOGLE_CONSUMER_SECRET = ''

SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = os.environ['SOCIAL_AUTH_GOOGLE_OAUTH2_KEY']
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = os.environ['SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET']

FOURSQUARE_CONSUMER_KEY = ''
FOURSQUARE_CONSUMER_SECRET = ''
VK_APP_ID = ''
VK_API_SECRET = ''
LIVE_CLIENT_ID = ''
LIVE_CLIENT_SECRET = ''
SKYROCK_CONSUMER_KEY = ''
SKYROCK_CONSUMER_SECRET = ''
YAHOO_CONSUMER_KEY = ''
YAHOO_CONSUMER_SECRET = ''

GOOGLE_OAUTH2_AUTH_EXTRA_ARGUMENTS = {'access_type': 'offline'}
GOOGLE_EXTRA_DATA = [('oauth_token', 'oauth_token')]
GOOGLE_SREG_EXTRA_DATA = [('oauth_token', 'oauth_token')]
GOOGLE_AX_EXTRA_DATA = [('oauth_token', 'oauth_token')]

AWS_ACCESS_KEY_ID = os.environ['S3_KEY']
AWS_SECRET_ACCESS_KEY = os.environ['S3_SECRET']

# Make this unique, and don't share it with anybody.
SECRET_KEY = os.environ['SECRET_KEY']  # DJANGO secret key

# Stripe Keys
STRIPE_KEY = os.environ['STRIPE_KEY']
STRIPE_PUBLISHABLE_KEY = os.environ['STRIPE_PUBLISHABLE_KEY']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': '',                      # Or path to database file if using sqlite3.
        # The following settings are not used with sqlite3:
        'USER': '',
        'PASSWORD': '',
        'HOST': '',                      # Empty for localhost through domain sockets or '127.0.0.1' for localhost through TCP.
        'PORT': '',                      # Set to empty string for default.
    }
}