from django import forms
from .models import Person, Image

class Form(forms.ModelForm):
	class Meta:
		model = Person
		fields = ['name', 'age']

class ImageForm(forms.ModelForm):
	class Meta:
		model = Image
		fields = ['title','image']


class UpploadFileForm(forms.Form):
	file_path = forms.FilePathField(label="Выберите файл",
	path="templates", allow_files="True", allow_folders="True")
	
class InputNumForm(forms.Form):
	num = forms.IntegerField(label="Введите число", help_text="Не юзай буковы молю")
	
