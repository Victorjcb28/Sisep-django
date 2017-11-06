
from .models import Postulante,Educacion,Direccion,ExperienciaLaboral,Examen,Cargo,Pregunta,Respuesta
from django import forms
from django.core.exceptions import ValidationError
from django.contrib import messages


class PostulanteForm(forms.ModelForm):

	class Meta:
		model = Postulante
		fields = [
			'id',
			'nombre',
			'apellidos',
			'cedula',
			'edad',
			'telefono',
			'sexo',
			'email',
			
			'fecha_nacimiento',
			
		]
		labels = {
			'id':'id',
			'nombre': 'Nombre',
			'apellidos': 'Apellidos',
			'cedula':'cedula',
			'edad':'edad',
			'telefono': 'Telefono',
			'sexo':'sexo',
			'email': 'Correo electronico',
			
			'fecha_nacimiento':'fecha',
			
		}
		
		widgets = {
			'id':forms.TextInput(attrs={'class':'form-control'}),
			'nombre':forms.TextInput(attrs={'class':'form-control'}),
			'apellidos':forms.TextInput(attrs={'class':'form-control'}),
			'cedula':forms.TextInput(attrs={'class':'form-control'}),
			'edad':forms.TextInput(attrs={'class':'form-control','id':'edad'}),
			'telefono':forms.TextInput(attrs={'class':'form-control'}),
			'email':forms.TextInput(attrs={'class':'form-control'}),
			'sexo':forms.TextInput(attrs={'class':'form-control'}),
			'fecha_nacimiento':forms.TextInput(attrs={'class':'form-control','id':'datepicker'}),
			
			
		}


class EducacionForm(forms.ModelForm):

	class Meta:
		model = Educacion
		fields = [
			'instruccion',
			'agraduacion',
			'contabilidad',
			'titulo',
			'merito',
			'curso',
			'idioma',
			'office',
			
		]

		labels = {
			'instruccion': 'Nivel Instruccion',
			'agraduacion': 'Graduacion',
			'contabilidad':'Contabilidad',
			'titulo':'Titulo',
			'merito': 'Orden de Merito',
			'curso': 'Ultimo Curso Realizado',
			'idioma': 'Idioma',
			'office':'Paquete Office',
			
		}
		
		widgets = {
			'instruccion':forms.TextInput(attrs={'class':'form-control','placeholder':'Nombre'}),
			'agraduacion':forms.TextInput(attrs={'class':'form-control'}),
			'contabilidad':forms.TextInput(attrs={'class':'form-control'}),
			'titulo':forms.TextInput(attrs={'class':'form-control'}),
			'merito':forms.TextInput(attrs={'class':'form-control'}),
			'curso':forms.TextInput(attrs={'class':'form-control'}),
			'idioma':forms.TextInput(attrs={'class':'form-control'}),
			'office':forms.TextInput(attrs={'class':'form-control'}),
			
		}


class DireccionForm(forms.ModelForm):

	class Meta:
		model = Direccion
		fields = [
			'estado',
			'municipio',
			'parroquia',
			'direccion',
			
		]

		labels = {
			'estado':'Estado',
			'municipio':'Municipio',
			'parroquia':'Parroquia',
			'direccion':'Direccion',
			
		}
		
		widgets = {
			'estado':forms.TextInput(attrs={'class':'form-control'}),
			'municipio':forms.TextInput(attrs={'class':'form-control'}),
			'parroquia':forms.TextInput(attrs={'class':'form-control'}),
			'direccion':forms.TextInput(attrs={'class':'form-control'}),
			
		}
		

class ExperienciaForm(forms.ModelForm):

	class Meta:
		model = ExperienciaLaboral
		fields = [
			'tempresa',
			'cargov',
			'vempresa',
			'anos',
			
		]

		labels = {
			'tempresa':'Trabaja en la empresa',
			'cargov':'Cargo',
			'vempresa':'Empresa donde Trabajo',
			'anos':'Anos de trabajo',

			
		}
		
		widgets = {
			'tempresa':forms.TextInput(attrs={'class':'form-control'}),
			'cargov':forms.TextInput(attrs={'class':'form-control'}),
			'vempresa':forms.TextInput(attrs={'class':'form-control'}),
			'anos':forms.TextInput(attrs={'class':'form-control'}),
			
		}

class ExamenForm(forms.ModelForm):

	class Meta:
		model = Examen
		fields = [
			
			'puntuacion',
			'realizado',
			'p1',
			'p2',
			'p3',
			'p4',
			'p5',
			'p6',
			'p7',
			'p8',
			'p9',
			'p10',			
		]

		labels = {
			
			'puntuacion':'puntuacion',
			'realizado':'realizado',
			'p1':'p1',
			'p2':'p2',
			'p3':'p1',
			'p4':'p2',
			'p5':'p1',
			'p6':'p2',
			'p7':'p1',
			'p8':'p2',
			'p9':'p1',
			'p10':'p2',
			
		}
		
		widgets = {
			
			'puntuacion':forms.TextInput(attrs={'class':'form-control','value':'0','readonly':'readonly'}),
			'realizado':forms.TextInput(attrs={'class':'form-control','value':'NO','readonly':'readonly'}),
			'p1':forms.Select(attrs={'class':'form-control'}),
			'p2':forms.Select(attrs={'class':'form-control'}),
			'p3':forms.Select(attrs={'class':'form-control'}),
			'p4':forms.Select(attrs={'class':'form-control'}),
			'p5':forms.Select(attrs={'class':'form-control'}),
			'p6':forms.Select(attrs={'class':'form-control'}),
			'p7':forms.Select(attrs={'class':'form-control'}),
			'p8':forms.Select(attrs={'class':'form-control'}),
			'p9':forms.Select(attrs={'class':'form-control'}),
			'p10':forms.Select(attrs={'class':'form-control'}),
		}
		
	
	
	


class CargoForm(forms.ModelForm):

	class Meta:
		model = Cargo
		fields = [
			'cargo',
			'image',
			
			
		]

		labels = {
			'cargo':'Cargo',
			'image':'Imagen Cargo',
			
			
		}
		
		widgets = {
			'cargo':forms.TextInput(attrs={'class':'form-control'}),
			
		}

class PreguntaForm(forms.ModelForm):

	class Meta:
		model = Pregunta
		fields = [			
			
			'p1',
			'p2',
			'p3',
			'p4',
			'p5',
			'p6',
			'p7',
			'p8',
			'p9',
			'p10',			
		]

		labels = {
			
		
			'p1':'p1',
			'p2':'p2',
			'p3':'p1',
			'p4':'p2',
			'p5':'p1',
			'p6':'p2',
			'p7':'p1',
			'p8':'p2',
			'p9':'p1',
			'p10':'p2',
			
		}
		
		widgets = {
			
			
			'p1':forms.TextInput(attrs={'class':'form-control'}),
			'p2':forms.TextInput(attrs={'class':'form-control'}),
			'p3':forms.TextInput(attrs={'class':'form-control'}),
			'p4':forms.TextInput(attrs={'class':'form-control'}),
			'p5':forms.TextInput(attrs={'class':'form-control'}),
			'p6':forms.TextInput(attrs={'class':'form-control'}),
			'p7':forms.TextInput(attrs={'class':'form-control'}),
			'p8':forms.TextInput(attrs={'class':'form-control'}),
			'p9':forms.TextInput(attrs={'class':'form-control'}),
			'p10':forms.TextInput(attrs={'class':'form-control'}),
		}
		

class RespuestaForm(forms.ModelForm):

	class Meta:
		model = Respuesta
		fields = [			
			
			'r1',
			'r2',
			'r3',
			'r4',
			'r5',
			'r6',
			'r7',
			'r8',
			'r9',
			'r10',
			'r11',
			'r12',
			'r13',
			'r14',
			'r15',
			'r16',
			'r17',
			'r18',
			'r19',
			'r20',
			'r21',
			'r22',
			'r23',
			'r24',
			'r25',
			'r26',
			'r27',
			'r28',
			'r29',
			'r30',
				]

		labels = {
			
		
			'r1':'r1',
			'r2':'r2',
			'r3':'r3',
			'r4':'r3',
			'r5':'r3',
			'r6':'r3',
			'r7':'r3',
			'r8':'r3',
			'r9':'r3',
			'r10':'r3',
			'r11':'r3',
			'r12':'r3',
			'r13':'r3',
			'r14':'r3',
			'r15':'r3',
			'r16':'r3',
			'r17':'r3',
			'r18':'r3',
			'r19':'r3',
			'r20':'r3',
			'r21':'r3',
			'r22':'r3',
			'r23':'r3',
			'r24':'r3',
			'r25':'r3',
			'r26':'r3',
			'r27':'r3',
			'r28':'r3',
			'r29':'r3',
			'r30':'r3',
		}
		
		widgets = {
			
			
			'r1':forms.TextInput(attrs={'class':'form-control','placeholder':'Ingrese respuesta correcta'}),
			'r2':forms.TextInput(attrs={'class':'form-control'}),
			'r3':forms.TextInput(attrs={'class':'form-control'}),
			'r4':forms.TextInput(attrs={'class':'form-control'}),
			'r5':forms.TextInput(attrs={'class':'form-control','placeholder':'Ingrese respuesta correcta'}),
			'r6':forms.TextInput(attrs={'class':'form-control'}),
			'r7':forms.TextInput(attrs={'class':'form-control'}),
			'r8':forms.TextInput(attrs={'class':'form-control'}),
			'r9':forms.TextInput(attrs={'class':'form-control','placeholder':'Ingrese respuesta correcta'}),
			'r10':forms.TextInput(attrs={'class':'form-control','placeholder':'Ingrese respuesta correcta'}),
			'r11':forms.TextInput(attrs={'class':'form-control'}),
			'r12':forms.TextInput(attrs={'class':'form-control'}),
			'r13':forms.TextInput(attrs={'class':'form-control'}),
			'r14':forms.TextInput(attrs={'class':'form-control','placeholder':'Ingrese respuesta correcta'}),
			'r15':forms.TextInput(attrs={'class':'form-control'}),
			'r16':forms.TextInput(attrs={'class':'form-control'}),
			'r17':forms.TextInput(attrs={'class':'form-control'}),
			'r18':forms.TextInput(attrs={'class':'form-control','placeholder':'Ingrese respuesta correcta'}),
			'r19':forms.TextInput(attrs={'class':'form-control','placeholder':'Ingrese respuesta correcta'}),
			'r20':forms.TextInput(attrs={'class':'form-control'}),
			'r21':forms.TextInput(attrs={'class':'form-control'}),
			'r22':forms.TextInput(attrs={'class':'form-control'}),
			'r23':forms.TextInput(attrs={'class':'form-control','placeholder':'Ingrese respuesta correcta'}),
			'r24':forms.TextInput(attrs={'class':'form-control'}),
			'r25':forms.TextInput(attrs={'class':'form-control'}),
			'r26':forms.TextInput(attrs={'class':'form-control'}),
			'r27':forms.TextInput(attrs={'class':'form-control','placeholder':'Ingrese respuesta correcta'}),
			'r28':forms.TextInput(attrs={'class':'form-control','placeholder':'Ingrese respuesta correcta'}),
			'r29':forms.TextInput(attrs={'class':'form-control'}),
			'r30':forms.TextInput(attrs={'class':'form-control'}),
		}
		