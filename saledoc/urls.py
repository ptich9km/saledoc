from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.page_link, name='page_link'),
]

'''
urlpatterns = [
    # Examples:
    # url(r'^$', 'sale.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    #url(r'^saledoc/', include('saledoc.urls')),
    #url(r'^admin/', include(admin.site.urls)),

    #url(r'', include('saledoc.urls')),

]
'''
