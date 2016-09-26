from django.shortcuts import render
from .models import Post

# Create your views here.
from django.http import HttpResponse

#Запрос страницы с ссылками
def page_link(request):
	posts = Post.objects.order_by('name_document')
	return render(request, 'saledoc/page_link.html', {'posts': posts})

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

#Простой запрос времени
def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)
