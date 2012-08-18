from django.conf.urls import patterns, include, url
from tDjango.strOutToResponse.views import hello,current_time,plustime,plusdays
from tDjango.template.views import current_time,current_ttime ,render_res_current_time,plus_days

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
                       ('^hello/',hello),
                       ('^time/$',current_time),
                       ('^plustime/(\d{1,2})$',plustime),
                       ('^plusdays/(\d{1,2})$',plusdays),
                       ('^temTime$',current_time),
                       ('^temTTime$',current_ttime),
                       ('^renTime$',render_res_current_time),
                       ('^addDays/(\d{1,2})$',plus_days),
    # Examples:
    # url(r'^$', 'testDjango.views.home', name='home'),
    # url(r'^testDjango/', include('testDjango.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
