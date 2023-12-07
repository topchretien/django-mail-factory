# -*- coding: utf-8 -*-
"""URLconf for mail_factory admin interface."""
from django.urls import re_path

from django.conf import settings

from mail_factory.views import mail_list, form, preview_message, html_not_found


LANGUAGE_CODES = '|'.join([code for code, name in settings.LANGUAGES])


urlpatterns = [
    re_path(r'^$',
        mail_list,
        name='mail_factory_list'),
    re_path(r'^detail/(?P<mail_name>.*)/$',
        form,
        name='mail_factory_form'),
    re_path(r'^preview/(?P<lang>(%s))/(?P<mail_name>.*)/$' % LANGUAGE_CODES,
        preview_message,
        name='mail_factory_preview_message'),
    re_path(r'^html_not_found/(?P<mail_name>.*)/$',
        html_not_found,
        name='mail_factory_html_not_found'),
]
