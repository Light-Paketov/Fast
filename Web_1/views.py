from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound
from .forms import UpploadFileForm, InputNumForm, Form, ImageForm
from .models import Person, Image

def index(request):
 my_kv = ['I квартал ->', 'II квартал ->', 'III квартал->',
 'IV квартал->']
 my_month = ['Январь', 'Февраль', 'Март',
 'Апрель', 'Май', 'Июнь',
 'Июль', 'Август', 'Сентябрь',
 'Октябрь', 'Ноябрь', 'Декабрь']
 context = {'my_month': my_month, 'my_kv': my_kv}
 return render(request, "index.html", context)

def about(request):
	return render(request,'about.html')

def contact(request):
	return render(request,'contact.html')

def form(request):
	if request.method == "POST":
	 	form = Form(request.POST)
	 	if form.is_valid():
	 		form.save()

	my_text = 'Сведения о клиентах'
	people = Person.object_person.all()
	form = Form()
	context = {'my_text': my_text, "people": people, "form": form}
	return render(request, "my_forms.html", context)

def edit_form(request, id):
	person = Person.object_person.get(id=id)
	if request.method == "POST":
		person.name = request.POST.get("name")
		person.age = request.POST.get("age")
		person.save()
		return redirect('form')

	data = {"person": person}
	return render(request, "edit_form.html", context=data)

def delete(request, id):
	try:
		person = Person.object_person.get(id=id)
		person.delete()
		return redirect('form')
	except Person.DoesNotExist:
		return HttpResponseNotFound("<h2>Объект не найден</h2>")

def form_up_img(request):
	if request.method == 'POST':
		form = ImageForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			my_text = 'Загруженные изображения'
			my_img = Image.obj_img.all()
			form = ImageForm()
			context = {'my_text': my_text, "my_img": my_img, "form": form}
			return render(request, 'form_up_img.html', context)
		else:
			return HttpResponse("Форма не валидна.")
	else:
		return HttpResponse("Неверный метод запроса.")


def delete_img(request, id):
	try:
		img = Image.obj_img.get(id=id)
		img.delete()
		return redirect('form_up_img')
	except Person.DoesNotExist:
		return HttpResponseNotFound("<h2>Объект не найден</h2>")

def upload_file(request):
	if request.method == 'POST':
		form = UpploadFileForm(request.POST, request.FILES)
		if form.is_valid():
			pass
	else:
		form = UpploadFileForm()

	return render(request, 'upload_form.html', {'form': form})

def input_num(request):
	if request.method == 'POST':
		form = InputNumForm(request.POST, request.FILES)
		if form.is_valid():
			pass
	else:
		form = InputNumForm()
	
	return render(request, 'input_num.html', {'form': form})



