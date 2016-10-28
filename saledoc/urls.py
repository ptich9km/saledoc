from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

#Формирую URL на свой проект 
urlpatterns = [
	url(r'^$', views.page_link, name='page_link'),
	url(r'^saledoc/(Document(\d+))/$', views.documents),
	url(r'^static/doc.docx', views.send_file),
	
]

#	url(r'^static/static', views.send_file),
#	url(r'^saledoc/static/example.txt', views.send_file),
