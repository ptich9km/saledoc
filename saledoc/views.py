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
	xyi=data_vremya()
	if(request.GET.get('mybtn')):
		document_select="6"
		namedoc=arg3
		data_dogovora=request.GET.get('data_dogovor')
		CustOrgShortName=request.GET.get('CustOrgShortName')
		CustBankDetails=request.GET.get('CustBankDetails')
		CustOrgFullName=request.GET.get('CustOrgFullName')
		RCustFullName=request.GET.get('RCustFullName')
		CustInitials=request.GET.get('CustInitials')
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
		VatRate_keyboard=request.GET.get('VatRate_keyboard')

		

		writedata_indocfile(namedoc, data_dogovora, RCustFullName, CustOrgShortName, CustBankDetails, CustOrgFullName, CustInitials, place, CountOrgShortName, VatRate, AgrCurrency, CurrencyPayment, podpis_name, CustPost, RCustPost, CustLastName, CustBase, number_dogovor, summa_dogovor, VatRate_keyboard)
	else:	
		document_select=arg3
	return render_to_response('saledoc/page_content.html', {'document_selected': document_select, 'xyi1': xyi})


def request_page(request):
	datas=request.GET.get('CountOrgShortName')
	print(datas)
	return render(request,'saledoc/page_download.html', {'inform': datas})


def data_vremya():
	datatime =  localtime()

	data1 = datatime[0]
	data2 = datatime[1]
	data3 = datatime[2]
	data4 = datatime[3]
	data5 = datatime[4]
	data = []
	data.append(data1)
	data.append(data2)
	data.append(data3)
	data.append(data4)
	data.append(data5)

	datavalue = ''.join(str(v) for v in data)

	return datavalue


def send_file(request):
	filename     = "C:\Projects\saledoc\saledoc\static\doc.docx" # Select your file here.
	download_name ="doc.docx"
	wrapper      = FileWrapper(open(filename))
	content_type = mimetypes.guess_type(filename)[0]
	response     = HttpResponse(wrapper,content_type=content_type)
	response['Content-Length']      = os.path.getsize(filename)    
	response['Content-Disposition'] = "attachment; filename=%s"%download_name
	return response

def writedata_indocfile(namedoc, data_dogovora, CustOrgFullName, CustOrgShortName, CustBankDetails, RCustFullName, CustInitials, place, CountOrgShortName, VatRate, AgrCurrency, CurrencyPayment, podpis_name, CustPost, RCustPost, CustLastName, CustBase, number_dogovor, summa_dogovor, VatRate_keyboard):
	document = Document()
	
	# Proverka chemu raven parametr namedoc i formirovanie Imeni documenta.
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

	
	document.add_heading('1. Номер договора №{}{}'.format(number_dogovor, data_vremya()), level=1)

	# Proverka chemu raven parametr CountOrgShortName i formirovanie Uridicheckogo lica.
	document.add_heading('2. Юридическое лицо со стороны исполнителя', level=1)

	if int(CountOrgShortName) == 1: 
		document.add_paragraph('ЧУП Промвад')
	elif int(CountOrgShortName) == 2:
		document.add_paragraph('ООО Промвад Софт')
	else:
		document.add_paragraph('ПРВ Инжиниринг')

	# Proverka chemu raven parametr podpis_name i formirovanie Podpisivauchego lica.
	document.add_heading('3. Выбор подписанта со стороны исполнителя {}'.format(podpis_name), level=1)
	if int(podpis_name) == 1: 
		document.add_paragraph('Якубович Д.М.')
	elif int(podpis_name) == 2:
		document.add_paragraph('Ковалев С.Н.')
	elif int(podpis_name) == 3:
		document.add_paragraph('Мозолевский В.В.')
	elif int(podpis_name) == 4:
		document.add_paragraph('Лиштван Ю.Н.')
	elif int(podpis_name) == 5:
		document.add_paragraph('Кутень И.С.')
	else:
		document.add_paragraph('Ковалев С.К.')

	# Proverka chemu raven parametr place i formirovanie Mesta sostavleniya dogovora.
	document.add_heading('4. Место составления договора {}'.format(place), level=1)
	if int(place) == 1: 
		document.add_paragraph('Минск')
	else:
		document.add_paragraph('Москва')

	document.add_heading('5. Дата договора {} {}'.format(data_dogovora, data_vremya()), level=1)

	# Formirovanie informacii o zakazchike.
	document.add_heading('6. Информация о Заказчике:', level=1)
	document.add_paragraph(CustOrgFullName)
	document.add_paragraph(CustOrgShortName)
	document.add_paragraph(CustBankDetails)


	# Proverka chemu raven parametr CustBase i formirovanie informacii o predstavitele zakazchika.
	document.add_heading('7. Информация о представителе Заказчика', level=1)
	document.add_paragraph(CustPost)
	document.add_paragraph(RCustPost)
	document.add_paragraph(CustLastName)
	document.add_paragraph(RCustFullName)
	document.add_paragraph(CustInitials)
	if int(CustBase) == 1: 
		document.add_paragraph('Устава')
	else:
		document.add_paragraph('доверенности №')

	# Proverka chemu raven parametr VatRate informacia o NDS.
	document.add_heading('8. НДС {}'.format(VatRate), level=1)
	if int(VatRate) == 1: 
		document.add_paragraph('Стоимость работ без НДС')
	elif int(VatRate) == 2:
		document.add_paragraph('18% (для РФ)')
	else:
		document.add_paragraph('20% (для РБ )')
	document.add_paragraph(VatRate_keyboard)

	# Informaziya o valute i summe po dogovory.
	document.add_heading('9. Валюта платежа', level=1)
	document.add_paragraph('Валюта по договору')
	if int(AgrCurrency) == 1: 
		document.add_paragraph('USD')
	elif int(AgrCurrency) == 2:
		document.add_paragraph('EUR')
	elif int(AgrCurrency) == 3:
		document.add_paragraph('RUR')
	else:
		document.add_paragraph('BRB')

	document.add_paragraph('Валюта платежа')
	if int(CurrencyPayment) == 1: 
		document.add_paragraph('USD')
	elif int(CurrencyPayment) == 2:
		document.add_paragraph('EUR')
	elif int(CurrencyPayment) == 3:
		document.add_paragraph('RUR')
	else:
		document.add_paragraph('BRB')

	# Informaziya o summe dogovora.
	document.add_heading('10.Сумма по  договору {}', level=1)
	document.add_paragraph(write_price(summa_dogovor))

	document.add_page_break()
	document.save('saledoc/static/doc{}.docx'.format(data_vremya()))

	return

ZERO = "ноль"

L_1_HE = HE = [ZERO, "один", "два", "три", "четыре", "пять", "шесть", "семь", "восемь", "девять", "десять",
    "одинадцать", "двенадцать", "тринадцать", "четырнадцать", "пятнадцать",
    "шестнадцать", "семнадцать", "восемнадцать", "девятнадцать"]
    
L_1_SHE = SHE = [ZERO, "одна", "две"] + L_1_HE[3:]
    
L_10 = [ZERO, "десять", "двадцать", "тридцать", "сорок", "пятьдесят",
    "шестьдесят", "семьдесят", "восемьдесят", "девяносто"]
    
L_100 = [ZERO, "сто", "двести", "триста", "четыреста", "пятьсот",
    "шестьсот", "семьсот", "восемьсот", "девятьсот"]
    
N_ROUBLE = "рубл"
N_COP = "копе"
RUR = (N_ROUBLE, N_COP)

N_DOLLAR = "доллар"
N_CENT = "цент"
USD = (N_DOLLAR, N_CENT)

GENDER = {
    N_ROUBLE: HE,
    N_COP: SHE,
    N_DOLLAR: HE,
    N_CENT: HE,
}

N_1000 = "тысяч"
N_MILLION = "миллион"
N_BILLION = "миллиард"

ENDINGS = {
    N_ROUBLE:     ["ей", "ь", "я", "я", "я"] + 30 * ["ей"],
    N_COP:    ["ек", "йка", "йки", "йки", "йки"] + 30 * ["ек"],
    N_DOLLAR:    ["ов", "", "а", "а", "а"] + 30 * ["ов"],
    N_CENT:    ["ов", "", "а", "а", "а"] + 30 * ["ов"],
    N_1000:    ["", "а", "и", "и", "и"] + 30 * [""],
    N_MILLION:    ["ов", "", "а", "а", "а"] + 30 * ["ов"],
    N_BILLION:    ["ов", "", "а", "а", "а"] + 30 * ["ов"],
}

def write_1_to_999(n, gender_digits=HE):
    assert n <= 999
    
    if n == 0:
        return ZERO
    
    n_100 = n // 100
    n_10 = n % 100 // 10 
    n_1 = n % 10
    
    res = []
    res.append(L_100[n_100])
    
    if n_10 == 1:
        res.append(gender_digits[10 * n_10 + n_1])
    else:
        res.append(L_10[n_10])
        res.append(gender_digits[n_1])
    return " ".join([s for s in res if s != ZERO])

def ending_index(n):
    n_2 = n % 100
    return n_2 if n_2 < 20 else n_2 % 10

def form_group_name(group, n):
    return group + ENDINGS[group][ending_index(n)]
    
def form_group(group, n, gender_digits=HE):
    return ("%s %s" % (write_1_to_999(n, gender_digits), form_group_name(group, n))) if n else ZERO

def write_number(n, gender_digits=HE):
    assert type(n) in (int, float)
    if n == 0:
        return ZERO
    
    n_3 = n % 10 ** 3
    n_6 = n % 10 ** 6 // 10 ** 3
    n_9 = n % 10 ** 9 // 10 ** 6
    n_12 = n % 10 ** 12 // 10 ** 9
    
    # print n_12, n_9, n_6, n_3
    res = []
    
    res.append(form_group(N_BILLION, n_12))
    res.append(form_group(N_MILLION, n_9))
    res.append(form_group(N_1000, n_6, SHE))
    res.append(write_1_to_999(n_3, gender_digits))
    
    return ", ".join([s for s in res if s != ZERO])

def write_price(n_rub, n_cop=0, currency=RUR):
    rub_id, cop_id = currency
    n = int(n_rub)
    res = []
    res.append("%s %s" % (write_number(n, GENDER[rub_id]), form_group_name(rub_id, n)))
    res.append(form_group(cop_id, n_cop, GENDER[cop_id]))
    
    return " и ".join([s for s in res if s != ZERO])


