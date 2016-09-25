from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'sale.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    #ссылка что любой запрос '' вызовет URL адреса с моего проекта saledoc
    url(r'', include('saledoc.urls')),
]
