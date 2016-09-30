from django.shortcuts import render
from django.shortcuts import render_to_response
from .models import Post


# Create your views here.
from django.http import HttpResponse

#Запрос страницы с ссылками
def page_link(request):
	posts = Post.objects.order_by('name_document')
	return render(request, 'saledoc/page_link.html', {'posts': posts})

def documents(request, arg2, arg3):
	if(request.GET.get('mybtn')):
		document_select="7"
	else:	
		document_select=arg3
	return render_to_response('saledoc/page_content.html', {'document_selected': document_select})

def request_page(request):
	datas=request.GET.get('CountOrgShortName')
	print(datas)
	return render(request,'saledoc/page_download.html', {'inform': datas})


