# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import logging
import tweepy

from django.core.cache import cache
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.utils.encoding import python_2_unicode_compatible, force_text
from django.utils.translation import ugettext_lazy as _

from cms.models import CMSPlugin
from connected_accounts.fields import AccountField
from tweepy.error import TweepError
from tweepy.parsers import JSONParser

from .conf import settings

logger = logging.getLogger('djangocms_twitter')


@python_2_unicode_compatible
class Twitter(CMSPlugin):
    USER_TIMELINE = 'user'
    USER_FAVORITES = 'favorites'
    SEARCH_QUERY = 'search'

    TIMELINE_CHOICES = (
        (USER_TIMELINE, _('User Timeline')),
        (USER_FAVORITES, _('Favorites')),
        (SEARCH_QUERY, _('Search Query')),
    )

    account = AccountField(
        'twitter', verbose_name=_('Connected Account'),
        help_text=_('Select a connected Twitter account or connect to a new account.'))
    screen_name = models.CharField(
        _('Twitter Username'), max_length=100, blank=True, null=True,
        help_text=_('You may create an embedded timeline for any public '
                    'Twitter user. By default, the "Connected Account" tweets are fetched.'))
    search_query = models.CharField(
        _('Search Query'), max_length=255, blank=True,
        help_text=_('You may create a search timeline for any query or #hashtag..'))
    no_of_items = models.IntegerField(
        _('Items to Display'), default=20,
        validators=[MaxValueValidator(20), MinValueValidator(1)],
        help_text=_('Select the number of items this block '
                    'should display (max 20)'))
    timeline_source = models.CharField(
        _('Available Timelines'), max_length=50,
        choices=TIMELINE_CHOICES, default=USER_TIMELINE,
        help_text=_('You can embed a timeline for Tweets from an individual user, '
                    'a user\'s favorites or any search query or hashtag.'))
    show_avatar = models.BooleanField(
        _('Show Avatar?'), default=True,
        help_text=_('Shows or hides the avatar image.'))
    show_username = models.BooleanField(
        _('Show Username?'), default=True,
        help_text=_('Shows or hides the username text.'))
    follow_button = models.BooleanField(
        _('Show Follow Button?'), default=True,
        help_text=_('Append a follow button to the listing.'))
    plugin_template = models.CharField(
        _('Design'), max_length=150,
        choices=settings.DJANGOCMS_TWITTER_TEMPLATES,
        default=settings.DJANGOCMS_TWITTER_DEFAULT_TEMPLATE,
    )

    def __str__(self):
        profile_data = self.get_profile()
        name = profile_data.get('name', 'No name')
        screen_name = profile_data.get('screen_name', 'yourhandle')

        if self.timeline_source == self.USER_FAVORITES:
            return _('Favorite Tweets by {0} @{1}').format(name, screen_name)
        elif self.timeline_source == self.SEARCH_QUERY:
            return _('Tweets about "{0}"').format(self.search_query)
        return _('Tweets by {0} @{1}').format(name, screen_name)

    def get_api(self):
        if not hasattr(self, '_api'):
            oauth = tweepy.OAuthHandler(
                settings.CONNECTED_ACCOUNTS_TWITTER_CONSUMER_KEY,
                settings.CONNECTED_ACCOUNTS_TWITTER_CONSUMER_SECRET)

            oauth.set_access_token(
                self.account.get_token(),
                self.account.get_token_secret())

            self._api = tweepy.API(oauth, parser=JSONParser())

        return self._api

    def save(self, *args, **kwargs):
        super(Twitter, self).save(*args, **kwargs)
        cache_keys = (
            self.get_cache_key(prefix='profile'),
            self.get_cache_key(prefix='tweets'),
        )
        cache.delete_many(cache_keys)

    def get_cache_key(self, prefix=''):
        return 'djangocms-twitter-{0}-{1}'.format(prefix, str(self.id))

    def get_tweets(self):
        cache_key = self.get_cache_key(prefix='tweets')
        tweets = cache.get(cache_key)
        if not tweets:
            api = self.get_api()
            screen_name = self.screen_name.lstrip('@').strip() or \
                self.account.get_common_data().get('username')
            tweets = []

            try:
                if self.timeline_source == self.USER_FAVORITES:
                    tweets = api.favorites(screen_name, count=self.no_of_items)
                elif self.timeline_source == self.SEARCH_QUERY:
                    tweets = api.search(self.search_query, count=self.no_of_items).get('statuses')
                else:
                    tweets = api.user_timeline(screen_name, count=self.no_of_items)
            except TweepError as e:
                msg = _('Failed to retrieve {0} - Reason: {1}').format(force_text(self), e)
                logger.error(msg)
            else:
                cache.set(cache_key, tweets, settings.DJANGOCMS_TWITTER_CACHE_DURATION)

        return tweets

    def get_profile(self):
        cache_key = self.get_cache_key(prefix='profile')
        profile_data = cache.get(cache_key)

        if not profile_data:
            api = self.get_api()
            screen_name = self.screen_name.lstrip('@').strip() or \
                self.account.get_common_data().get('username')

            profile_data = {
                'screen_name': screen_name
            }

            try:
                profile_data = api.get_user(screen_name)
            except TweepError as e:
                msg = _('Failed to retrieve information '
                        'about @{0} - Reason: {1}').format(screen_name, e)
                logger.error(msg)
            else:
                profile_data = {
                    'name': profile_data.get('name'),
                    'screen_name': profile_data.get('screen_name'),
                    'is_verified': profile_data.get('verified'),
                    'profile_image_url': profile_data.get('profile_image_url', '').replace('_normal', ''),
                    'description': profile_data.get('description'),
                    'location': profile_data.get('location'),
                    'followers_count': profile_data.get('followers_count'),
                    'following_count': profile_data.get('friends_count'),
                    'statuses_count': profile_data.get('statuses_count'),
                    'favourites_count': profile_data.get('favourites_count'),
                }
                cache.set(cache_key, profile_data, settings.DJANGOCMS_TWITTER_CACHE_DURATION)
        return profile_data
