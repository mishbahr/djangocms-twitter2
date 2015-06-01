=============================
djangocms-twitter2
=============================

.. image:: http://img.shields.io/travis/mishbahr/djangocms-twitter2.svg?style=flat-square
    :target: https://travis-ci.org/mishbahr/djangocms-twitter2/

.. image:: http://img.shields.io/pypi/v/djangocms-twitter2.svg?style=flat-square
    :target: https://pypi.python.org/pypi/djangocms-twitter2/
    :alt: Latest Version

.. image:: http://img.shields.io/pypi/dm/djangocms-twitter2.svg?style=flat-square
    :target: https://pypi.python.org/pypi/djangocms-twitter2/
    :alt: Downloads

.. image:: http://img.shields.io/pypi/l/djangocms-twitter2.svg?style=flat-square
    :target: https://pypi.python.org/pypi/djangocms-twitter2/
    :alt: License

.. image:: http://img.shields.io/coveralls/mishbahr/djangocms-twitter2.svg?style=flat-square
  :target: https://coveralls.io/r/mishbahr/djangocms-twitter2?branch=master


Use ``djangocms-twitter2`` to embed a timeline for Tweets from an individual user, a user’s favorites or any search query or hashtag.

This project requires `django-connected <https://github.com/mishbahr/django-connected>`_ and ``django-cms`` v3.0 or higher to be properly installed and configured. When installing the ``djangocms-twitter2`` using pip, ``django-connected`` will also be installed automatically.


Preview
--------

Please click on thumbnail for bigger image.

.. image:: http://mishbahr.github.io/djangocms-twitter2/assets/resized/djangocms-twitter2_001.jpeg
  :target: http://mishbahr.github.io/djangocms-twitter2/assets/djangocms-twitter2_001.png
  :width: 768px
  :align: center

Quickstart
----------

1. Install `djangocms-twitter2`::

    pip install djangocms-twitter2

2. Add `djangocms_twitter` to `INSTALLED_APPS`::

    INSTALLED_APPS = (
        ...
        'connected_accounts',
        'connected_accounts.providers',
        'djangocms_twitter',
        ...
    )

3. To enable ``Twitter`` as a provider for ``django-connected``::

    CONNECTED_ACCOUNTS_TWITTER_CONSUMER_KEY = '<twitter_consumer_key>'
    CONNECTED_ACCOUNTS_TWITTER_CONSUMER_SECRET = '<twitter_consumer_secret>'

You can register an app on Twitter via https://apps.twitter.com/app/new


4. Sync database (requires south>=1.0.1 if you are using Django 1.6.x)::

    python manage.py migrate


Configuration
--------------

Plugin(s) Module - If module is None, plugin is grouped Generic group::

    DJANGOCMS_TWITTER_PLUGIN_MODULE = _('Generic')

Name of the plugin::

    DJANGOCMS_TWITTER_PLUGIN_NAME = _('Twitter')

Can this plugin only be attached to a placeholder that is attached to a page::

    DJANGOCMS_TWITTER_PAGE_ONLY = False

A list of Plugin Class Names. If this is set, this plugin may only be added to plugins listed here::

    DJANGOCMS_TWITTER_PARENT_CLASSES = None

Is it required that this plugin is a child of another plugin? Or can it be added to any placeholder::

    DJANGOCMS_TWITTER_REQUIRE_PARENT = False

Whether this plugin can be used in text plugins or not::

    DJANGOCMS_TWITTER_TEXT_ENABLED = False

The path to the default template used to render the template::

   DJANGOCMS_TWITTER_DEFAULT_TEMPLATE = 'djangocms_twitter/default.html'

or override the ``Design`` dropdown choices to have different design options::

    DJANGOCMS_TWITTER_TEMPLATES = (
        ('djangocms_twitter/default.html', _('Default')),
    )

