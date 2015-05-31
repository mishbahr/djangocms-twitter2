from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool

from django.template.loader import select_template
from connected_accounts.admin import ConnectedAccountAdminMixin

from .conf import settings
from .forms import TwitterForm
from .models import Twitter


class TwitterPlugin(ConnectedAccountAdminMixin, CMSPluginBase):
    model = Twitter
    cache = False
    form = TwitterForm

    module = settings.DJANGOCMS_TWITTER_PLUGIN_MODULE
    name = settings.DJANGOCMS_TWITTER_PLUGIN_NAME
    render_template = settings.DJANGOCMS_TWITTER_DEFAULT_TEMPLATE

    text_enabled = settings.DJANGOCMS_TWITTER_TEXT_ENABLED
    page_only = settings.DJANGOCMS_TWITTER_PAGE_ONLY
    require_parent = settings.DJANGOCMS_TWITTER_REQUIRE_PARENT
    parent_classes = settings.DJANGOCMS_TWITTER_PARENT_CLASSES

    fieldsets = (
        (None, {
            'fields': ('account',)
        }),
        (None, {
            'fields': ('timeline_source', 'screen_name', 'search_query',)
        }),
        (None, {
            'fields': ('no_of_items', 'plugin_template', )
        }),
        (None, {
            'fields': ('show_avatar', 'show_username', 'follow_button', )
        }),
    )

    def get_render_template(self, context, instance, placeholder):
        # returns the first template that exists, falling back to bundled template
        return select_template([
            instance.plugin_template,
            settings.DJANGOCMS_TWITTER_DEFAULT_TEMPLATE,
            'djangocms_twitter/default.html'
        ])

    def icon_src(self, instance):
        return settings.STATIC_URL + 'img/djangocms_twitter/twitter.png'

    class Media:
        js = ('js/djangocms_twitter/admin/djangocms_twitter.js', )

plugin_pool.register_plugin(TwitterPlugin)
