from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

#Формирую URL на свой проект 


urlpatterns = [
	url(r'^$', views.page_link, name='page_link'),
	url(r'^saledoc/(Document(\d+))/$', views.documents),
]


if settings.DEBUG:
	urlpatterns += ('',
		(settings.STATIC_URL, document_root=settings.STATIC_ROOT),
    )

'''
urlpatterns = ['',
	url(r'^$', views.page_link, name='page_link'),
	url(r'^saledoc/(Document(\d+))/$', views.documents),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
'''
