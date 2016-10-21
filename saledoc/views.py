import os, tempfile, zipfile
from django.shortcuts import render
from django.shortcuts import render_to_response
from .models import Post
from django.utils.encoding import smart_str
from django.core.servers.basehttp import FileWrapper
from django.conf import settings
import mimetypes
from docx import Document
from docx.shared import Inches
from time import localtime

# Create your views here.
from django.http import HttpResponse

#Запрос страницы с ссылками
def page_link(request):
	posts = Post.objects.order_by('name_document')
	return render(request, 'saledoc/page_link.html', {'posts': posts})

def documents(request, arg2, arg3):
	if(request.GET.get('mybtn')):
		document_select="6"
		namedoc=arg3
		data_dogovora=request.GET.get('data_dogovor')
		CustOrgFullName=request.GET.get('CustOrgFullName')
		CustOrgShortName=request.GET.get('CustOrgShortName')
		CustBankDetails=request.GET.get('CustBankDetails')
		place=request.GET.get('place')
		CountOrgShortName=request.GET.get('CountOrgShortName')
		VatRate=request.GET.get('VatRate')
		AgrCurrency=request.GET.get('AgrCurrency')
		CurrencyPayment=request.GET.get('CurrencyPayment')
		podpis_name=request.GET.get('podpis_name')
		CustPost=request.GET.get('CustPost')
		RCustPost=request.GET.get('RCustPost')
		CustLastName=request.GET.get('CustLastName')
		CustBase=request.GET.get('CustBase')
		number_dogovor=request.GET.get('number_dogovor')
		summa_dogovor=request.GET.get('summa_dogovor')

		writedata_indocfile(namedoc, data_dogovora, CustOrgFullName, CustOrgShortName, CustBankDetails, place, CountOrgShortName, VatRate, AgrCurrency, CurrencyPayment, podpis_name, CustPost, RCustPost, CustLastName, CustBase, number_dogovor, summa_dogovor)
	else:	
		document_select=arg3
	return render_to_response('saledoc/page_content.html', {'document_selected': document_select})


def request_page(request):
	datas=request.GET.get('CountOrgShortName')
	print(datas)
	return render(request,'saledoc/page_download.html', {'inform': datas})


def send_file(request):
	filename     = "C:\Projects\saledoc\saledoc\static\doc.docx" # Select your file here.
	download_name ="doc.docx"
	wrapper      = FileWrapper(open(filename))
	content_type = mimetypes.guess_type(filename)[0]
	response     = HttpResponse(wrapper,content_type=content_type)
	response['Content-Length']      = os.path.getsize(filename)    
	response['Content-Disposition'] = "attachment; filename=%s"%download_name
	return response

def writedata_indocfile(namedoc, data_dogovora, CustOrgFullName, CustOrgShortName, CustBankDetails, place, CountOrgShortName, VatRate, AgrCurrency, CurrencyPayment, podpis_name, CustPost, RCustPost, CustLastName, CustBase, number_dogovor, summa_dogovor):
	document = Document()

	if int(namedoc) == 1: 
		document.add_heading('Шаблон договора на разработку рамочный', 0)
	elif int(namedoc) == 2:
		document.add_heading('Шаблон договора на разработку c фиксированной стоимостью', 0)
	elif int(namedoc) == 3:
		document.add_heading('Шаблон договора на разработку по схеме t&m', 0)
	elif int(namedoc) == 4:
		document.add_heading('Шаблон договора-оферты', 0)
	elif int(namedoc) == 5:
		document.add_heading('Шаблон договора на услуги (консультацию)', 0)
	else:
		document.add_heading('Шаблон договора на разработку дизайна', 0)

	
	document.add_heading('1. Номер договора {}'.format(number_dogovor), level=1)


	document.add_heading('2. Юридическое лицо со стороны исполнителя {}'.format(CountOrgShortName), level=1)
	document.add_heading('3. Выбор подписанта со стороны исполнителя {}'.format(podpis_name), level=1)
	document.add_heading('4. Место составления договора {}'.format(place), level=1)
	document.add_heading('5. Дата договора {}'.format(data_dogovora), level=1)
	document.add_heading('6. Информация о Заказчике {} {} {}'.format(CustOrgFullName, CustOrgShortName, CustBankDetails, RCustFullName, CustInitials), level=1)
	document.add_heading('7. Информация о представителе Заказчика {} {} {} {}'.format(CustPost, RCustPost, CustLastName, CustBase), level=1)
	document.add_heading('8. НДС {}'.format(VatRate), level=1)
	document.add_heading('9. Валюта платежа {} {}'.format(AgrCurrency, CurrencyPayment), level=1)
	document.add_heading('10.Сумма по  договору {}'.format(summa_dogovor), level=1)


	p = document.add_paragraph('A plain paragraph having some ')
	p.add_run('bold').bold = True
	p.add_run(' and some ')
	p.add_run('italic.').italic = True

	document.add_heading('Heading, level 1', level=1)
	document.add_paragraph('Intense quote', style='IntenseQuote')

	document.add_paragraph(
	    'first item in unordered list', style='ListBullet'
	)
	document.add_paragraph(
	    'first item in ordered list', style='ListNumber'
	)

	table = document.add_table(rows=1, cols=3)
	hdr_cells = table.rows[0].cells
	hdr_cells[0].text = 'Qty'
	hdr_cells[1].text = 'Id'
	hdr_cells[2].text = 'Desc'

	document.add_page_break()

	document.save('saledoc/static/doc.docx')
	return

