from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.core.exceptions import ValidationError
from .models import Profile



class RegistroUsuarioForm(UserCreationForm):

	class Meta:
		model= User
		fields=[
			'username',
			'first_name',
			'last_name',
			'email',
					

		]

		labels={
			'username':'Nombre de Usuario',
			'first_name':'Nombre',
			'last_name':'Apellido',
			'email':'Email',		
			
			
		}
		
		widgets={

			'username':forms.TextInput(attrs={'class':'form-control'}),
			'first_name':forms.TextInput(attrs={'class':'form-control'}),
			'last_name':forms.TextInput(attrs={'class':'form-control'}),
			'email':forms.TextInput(attrs={'class':'form-control'}),
			
			
			
		
		}


MY_CHOICES = (
        ('opt0', 'ADMINISTRADOR'),
        ('opt1', 'SECRETARIA'),
    )
class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = [
        	'tipo',
        	'image',
        ]

        labels={
			'tipo':'Tipo de Usuario',
			'image':'Cargar Img',
			
			
		}
		
	widgets={

			
  
			
			
			
		
		}
