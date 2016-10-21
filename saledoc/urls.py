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

'''
http://10.54.4.73:8000/saledoc/Document1/?CustOrgFullName=&CustOrgShortName=&CustBankDetails=&CustPost=&RCustPost=&CustLastName=&RCustFullName=&CustInitials=&VatRate=&mybtn=Click#

urlpatterns = ['',
	url(r'^$', views.page_link, name='page_link'),
	url(r'^saledoc/(Document(\d+))/$', views.documents),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
'''
