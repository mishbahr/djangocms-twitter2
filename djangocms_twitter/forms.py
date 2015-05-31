import requests

from django import forms
from django.contrib.admin.widgets import AdminRadioSelect
from django.utils.translation import ugettext_lazy as _

from .models import Twitter


class TwitterForm(forms.ModelForm):

    def clean_screen_name(self):
        screen_name = self.cleaned_data['screen_name']
        screen_name = screen_name.lstrip('@').strip()
        url = 'https://twitter.com/%s/' % screen_name
        response = requests.head(url)
        if not response.status_code == 200:
            raise forms.ValidationError('Sorry, that username does not exist!')
        return screen_name

    def clean(self):
        cleaned_data = super(TwitterForm, self).clean()
        timeline_source = cleaned_data.get('timeline_source')
        search_query = cleaned_data.get('search_query')

        if not search_query and timeline_source == 'search':
            msg = _('This field is required.')
            self._errors['search_query'] = self.error_class([msg])

        return cleaned_data

    class Meta:
        model = Twitter
        fields = '__all__'
        error_messages = {
            'account': {
                'required': _('A connected account is required to display tweets.'),
            },
        }
        widgets = {
            'timeline_source': AdminRadioSelect(attrs={'class': 'radiolist'})
        }
