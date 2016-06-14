# -*- coding: utf-8 -*-
from django.conf.urls import include, url
from django.contrib import admin
from StaticReport.views import *
urlpatterns = [
    # Examples:
    # url(r'^$', 'fundbi.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    #url(r'^chart/', include(admin.site.urls)),
    url(r'^ecreport/', ecchart),#电商汇总报表
    url(r'^ecreport_trade/', ecchart_trade),#交易量报表
]
