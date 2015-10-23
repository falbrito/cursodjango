from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings


# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # djando admin
    url(r'^admin/', include(admin.site.urls)),

    url(r'^aula3/$', 'aula3.views.index', name='aula3_index'),
    url(r'^aula3/(?P<id>\d+)/$', 'aula3.views.detail_id'),
    url(r'^aula3/(?P<username>[\w-]+)/$', 'aula3.views.detail_username'),

    url(r'^aula4/$', 'aula4.views.index', name='aula4_index'),

    url(r'^aula6/$', 'aula6.views.index', name='aula6_index'),
	url(r'^aula6/(?P<id>\d+)/$', 'aula6.views.detail', name='aula6_detail'),

    url(r'^aula7/$', 'aula7.views.index', name='aula7_index'),
    url(r'^aula7/sair/$', 'aula7.views.sair', name='aula7_sair'),    
    url(r'^aula7/view_protegida/$', 'aula7.views.view_protegida', name='aula7_view_protegida'),    
    url(r'^aula7/view_protegida2/$', 'aula7.views.view_protegida2', name='aula7_view_protegida2'),    

    url(r'^aula9/$', 'aula9.views.index', name='aula9_index'),
)

if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve',
         {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
        )

urlpatterns += staticfiles_urlpatterns()