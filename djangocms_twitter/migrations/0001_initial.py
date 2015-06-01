# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import connected_accounts.fields
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('connected_accounts', '0001_initial'),
        ('cms', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Twitter',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='cms.CMSPlugin')),
                ('screen_name', models.CharField(help_text='You may create an embedded timeline for any public Twitter user. By default, the "Connected Account" tweets are fetched.', max_length=100, null=True, verbose_name='Twitter Username', blank=True)),
                ('search_query', models.CharField(help_text='You may create a search timeline for any query or #hashtag..', max_length=255, verbose_name='Search Query', blank=True)),
                ('no_of_items', models.IntegerField(default=20, help_text='Select the number of items this block should display (max 20)', verbose_name='Items to Display', validators=[django.core.validators.MaxValueValidator(20), django.core.validators.MinValueValidator(1)])),
                ('timeline_source', models.CharField(default='user', help_text="You can embed a timeline for Tweets from an individual user, a user's favorites or any search query or hashtag.", max_length=50, verbose_name='Available Timelines', choices=[('user', 'User Timeline'), ('favorites', 'Favorites'), ('search', 'Search Query')])),
                ('show_avatar', models.BooleanField(default=True, help_text='Shows or hides the avatar image.', verbose_name='Show Avatar?')),
                ('show_username', models.BooleanField(default=True, help_text='Shows or hides the username text.', verbose_name='Show Username?')),
                ('follow_button', models.BooleanField(default=True, help_text='Append a follow button to the listing.', verbose_name='Show Follow Button?')),
                ('plugin_template', models.CharField(default=b'djangocms_twitter/default.html', max_length=150, verbose_name='Design', choices=[(b'djangocms_twitter/default.html', 'Default')])),
                ('account', connected_accounts.fields.AccountField(verbose_name='Connected Account', to='connected_accounts.Account', provider='twitter', help_text='Select a connected Twitter account or connect to a new account.')),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
    ]
