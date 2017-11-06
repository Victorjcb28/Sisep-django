# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render,redirect
from django.views.generic import CreateView,ListView,UpdateView,DeleteView,TemplateView
from django.http import HttpResponse, HttpResponseRedirect
from .forms import PostulanteForm, EducacionForm,DireccionForm,ExperienciaForm,ExamenForm,CargoForm,PreguntaForm,RespuestaForm
from .models import Postulante, Educacion,Direccion,ExperienciaLaboral,Examen,Cargo,Pregunta,Respuesta,RespuestaCo
from django.core.urlresolvers import reverse_lazy
from django.contrib import messages
# Create your views here.

	


def PostulanteSeleccion(request):
	cargo1=Cargo.objects.all()[0:3]
	cargo2=Cargo.objects.all()[3:6]
	cargo3=Cargo.objects.all()[6:9]
	contexto={
			'cargo1':cargo1,
			'cargo2':cargo2,
			'cargo3':cargo3
		}
	return render(request,'postulante/selecargo_list.html',contexto)

class CargoListAll(ListView):
	model= Cargo
	template_name= 'postulante/selectcargoall_list.html'




class PreguntasSeleccion(TemplateView):
	model=Cargo
	form_class=CargoForm
	template_name='postulante/preguntas_seleccion.html'

# <------ Vistas de Cargos -------->
class CargoCreate(CreateView):
	model = Cargo
	second_model=Pregunta
	third_model=Respuesta
	fourth_model=RespuestaCo
	
	form_class = CargoForm
	second_form_class=PreguntaForm
	third_form_class=RespuestaForm

	template_name = 'postulante/cargo_create.html'	
	success_url = reverse_lazy('postulante:cargo_listar')

	def get_context_data(self, **kwargs):
		context = super(CargoCreate, self).get_context_data(**kwargs)
		
		if 'form' not in context:
			context['form'] = self.form_class(self.request.GET)
		if 'form2' not in context:
			context['form2'] = self.second_form_class(self.request.GET)
		if 'form3' not in context:
			context['form3'] = self.third_form_class(self.request.GET)
		return context

	def post(self, request, *args, **kwargs):
		self.object = self.get_object
		
		form = self.form_class(request.POST,request.FILES)
		form2 = self.second_form_class(request.POST)
		form3 = self.third_form_class(request.POST)
		

		if form.is_valid() and form2.is_valid() and form3.is_valid():
			cargo=form.save(commit=False)
			pregunta=form2.save(commit=False)
			respuesta=form3.save(commit=False)
			
			form_data=form3.cleaned_data
			r1=form_data.get('r1')
			r2=form_data.get('r5')
			r3=form_data.get('r9')
			r4=form_data.get('r10')
			r5=form_data.get('r14')
			r6=form_data.get('r18')
			r7=form_data.get('r19')
			r8=form_data.get('r23')
			r9=form_data.get('r27')
			r10=form_data.get('r28')

			pregunta.cargo=form.save()
			respuesta.pregunta=form2.save()

			pregunta.save()
			respuesta.save()		
			
			obj=RespuestaCo.objects.create(r1=r1,r2=r2,r3=r3,r4=r4,r5=r5,r6=r6,r7=r7,r8=r8,r9=r9,r10=r10)
			return HttpResponseRedirect(self.get_success_url())
			
		else:
			return self.render_to_response(self.get_context_data(form=form, form2=form2,form3=form3))


class CargoList(ListView):
	model= Cargo
	template_name= 'postulante/cargo_list.html'

class CargoUpdate(UpdateView):
	model = Cargo
	second_model=Pregunta
	third_model=Respuesta
	
	form_class = CargoForm
	second_form_class=PreguntaForm
	third_form_class=RespuestaForm

	template_name= 'postulante/cargo_update.html'
	success_url= reverse_lazy('postulante:cargo_listar')

	def get_context_data(self, **kwargs):
		context= super(CargoUpdate,self).get_context_data(**kwargs)
		pk = self.kwargs.get('pk', 0)
		cargo=self.model.objects.get(id=pk)
		pregunta=self.second_model.objects.get(id=pk)
		respuesta=self.third_model.objects.get(id=pk)
		
		if 'form' not in context:
			context['form']= self.form_class()
		if 'form2' not in context:
			context['form2']= self.second_form_class(instance=pregunta)
			
		if 'form3' not in context:
			context['form3']= self.third_form_class(instance=respuesta)
			
		context['id']=pk


		return context


	def post(self,request,*args,**kwargs):
		self.object = self.get_object
		id_cargo=kwargs['pk']
		
		cargo=self.model.objects.get(id=id_cargo)		
		pregunta= self.second_model.objects.get(id=id_cargo)		
		respuesta=self.third_model.objects.get(id=id_cargo)
		
		

		form=self.form_class(request.POST, request.FILES, instance=cargo)		
		form2= self.second_form_class(request.POST, instance=pregunta)		
		form3=self.third_form_class(request.POST,instance=respuesta)
		
		

		if form3.is_valid() and form.is_valid() and form2.is_valid() :
			form.save()
			form2.save()
			form3.save()
			

			return HttpResponseRedirect(self.get_success_url())
		else:
			return HttpResponseRedirect(self.get_success_url())

class CargoDelete(DeleteView):
	model= Cargo
	second_model=Pregunta
	third_model=Respuesta

	template_name='postulante/cargo_delete.html'
	success_url=reverse_lazy('postulante:cargo_listar')

# <------ Vistas de Postulantes -------->
class PostulanteCreate(CreateView):
	model = Direccion
	second_model=Examen

	
	form_class = DireccionForm
	second_form_class = EducacionForm
	third_form_class=PostulanteForm
	fourth_form_class=ExperienciaForm
	fifth_form_class=CargoForm
	sexto_form_class=ExamenForm

	template_name = 'postulante/postulante_create.html'
	success_url = reverse_lazy('postulante:postulante_listar')

	

	def get_context_data(self, **kwargs):
		context = super(PostulanteCreate, self).get_context_data(**kwargs)
		pk = self.kwargs.get('pk', 0)
		if 'form' not in context:
			context['form'] = self.form_class(self.request.GET)
		if 'form2' not in context:
			context['form2'] = self.second_form_class(self.request.GET)
		if 'form3' not in context:
			context['form3'] = self.third_form_class(self.request.GET)
		if 'form4' not in context:
			context['form4'] = self.fourth_form_class(self.request.GET)
		if 'form5' not in context:
			context['form5']= self.fifth_form_class(self.request.GET)
		if 'form6' not in context:
			context['form6']= self.sexto_form_class(self.request.GET)
		return context

	def post(self, request, *args, **kwargs):
		self.object = self.get_object
		pkk=kwargs['pk']
		form = self.form_class(request.POST)
		form2 = self.second_form_class(request.POST)
		form3=self.third_form_class(request.POST)
		form4=self.fourth_form_class(request.POST)
		form5=self.fifth_form_class(request.POST)
		form6=self.sexto_form_class(request.POST)

		if form.is_valid() and form2.is_valid() and form3.is_valid() and form4.is_valid() :
			experiencia=form4.save(commit=False)
			educacion = form2.save(commit=False)
			direccion=form.save(commit=False)
			
			
			abc=request.POST.get('cargo')

			educacion.postulante=form3.save()
			direccion.postulante=form3.save()
			experiencia.postulante=form3.save()
			
			

			experiencia.save()
			educacion.save()
			direccion.save()
			
			
			#prueba de examen
			obj=Examen.objects.create(cargo_id=pkk,postulante=educacion.postulante,puntuacion="puntuacion",p1="p1",p2="p2",p3="p3",p4="p4",p5="p5",p6="p6",p7="p7",p8="p8",p9="p9",p10="p10")
			
			return HttpResponseRedirect(self.get_success_url())
				
		else:
			return self.render_to_response(self.get_context_data(form=form, form2=form2,form3=form3,form4=form4,form5=form5,form6=form6))

class PostulanteList(ListView):
	model= Postulante
	template_name= 'postulante/postulante_list.html'

class PostulanteUpdate(UpdateView):
	model= Direccion
	second_model=Educacion
	third_model=Postulante
	fourth_model=ExperienciaLaboral

	form_class=DireccionForm
	second_form_class=EducacionForm
	third_form_class=PostulanteForm
	fourth_form_class=ExperienciaForm

	template_name= 'postulante/postulante_update.html'
	success_url= reverse_lazy('postulante:postulante_listar')

	def get_context_data(self, **kwargs):
		context= super(PostulanteUpdate,self).get_context_data(**kwargs)
		pk = self.kwargs.get('pk', 0)
		direccion=self.model.objects.get(id=pk)
		educacion=self.second_model.objects.get(id=pk)
		postulante=self.third_model.objects.get(id=pk)
		experiencia=self.fourth_model.objects.get(id=pk)
		if 'form' not in context:
			context['form']= self.form_class()
		if 'form2' not in context:
			context['form2']= self.second_form_class(instance=educacion)
			
		if 'form3' not in context:
			context['form3']= self.third_form_class(instance=postulante)
			
		if 'form4' not in context:
			context['form4']= self.fourth_form_class(instance=experiencia)
			
		
		context['id']=pk


		return context


	def post(self,request,*args,**kwargs):
		self.object = self.get_object
		id_direccion=kwargs['pk']
		
		direccion=self.model.objects.get(id=id_direccion)		
		educacion= self.second_model.objects.get(id=direccion.postulante_id)		
		postulante=self.third_model.objects.get(id=direccion.postulante_id)	
		experiencia=self.fourth_model.objects.get(id=direccion.postulante_id)

		form=self.form_class(request.POST, instance=direccion)
		form2= self.second_form_class(request.POST, instance=educacion)		
		form3=self.third_form_class(request.POST,instance=postulante)		
		form4=self.fourth_form_class(request.POST,instance=experiencia)

		if form3.is_valid() and form.is_valid() and form2.is_valid() and form4.is_valid():
			form.save()
			form2.save()
			form3.save()
			form4.save()

			return HttpResponseRedirect(self.get_success_url())
		else:
			return HttpResponseRedirect(self.get_success_url())

class PostulanteDelete(DeleteView):
	model= Postulante
	second_model=Educacion

	template_name='postulante/postulante_delete.html'
	success_url=reverse_lazy('postulante:postulante_listar')


#<------- Examenes ------>


def ExamenList(request):
	examen=Examen.objects.exclude(realizado="SI").order_by('id')
	contexto={'examens':examen}
	return render(request, 'postulante/examen_list.html',contexto)



class ExamenAdminCreate(UpdateView):
	model= Examen
	second_model=Postulante
	third_model=Cargo
	fourth_model=Pregunta
	fifth_model=Respuesta

	form_class=ExamenForm
	second_form_class=PostulanteForm
	third_form_class=CargoForm
	fourth_form_class=PreguntaForm
	fifth_form_class=RespuestaForm
	
	template_name= 'postulante/examen_admin.html'
	success_url= reverse_lazy('postulante:postulante_listar')
	
	


	def get_context_data(self, **kwargs):
		context= super(ExamenAdminCreate,self).get_context_data(**kwargs)
		pk = self.kwargs.get('pk', 0)
		cargo=self.kwargs.get('cargo',0)
		
				
		postulante=self.second_model.objects.get(id=pk)
		cargo=self.third_model.objects.get(id=cargo)
		pregunta=self.fourth_model.objects.get(id=cargo.id)
		respuesta=self.fifth_model.objects.get(id=cargo.id)
		
		
		if 'form'not in context:
			context['form']= self.form_class()
		if 'form2' not in context:
			context['form2']= self.second_form_class(instance=postulante)
		
		if 'form3' not in context:
			context['form3']= self.third_form_class(instance=cargo)
		if 'form4' not in context:
			context['form4']=self.fourth_form_class(instance=pregunta)

		if 'form5' not in context:
			context['form5']=self.fifth_form_class(instance=respuesta)

		context['id']= pk		
		return context


	def post(self, request, *args, **kwargs):
		self.object = self.get_object
		id_examen=kwargs['pk']
		cargo=kwargs['cargo']
		examen= self.model.objects.get(id=id_examen)
		form = self.form_class(request.POST,instance=examen)

		#Data formulario
		p1=request.POST.get('p1')
		p2=request.POST.get('p2')
		p3=request.POST.get('p3')
		p4=request.POST.get('p4')
		p5=request.POST.get('p5')
		p6=request.POST.get('p6')
		p7=request.POST.get('p7')
		p8=request.POST.get('p8')
		p9=request.POST.get('p9')
		p10=request.POST.get('p10')

		query=RespuestaCo.objects.filter(id=cargo)
		
		for obj in query:
			r1= obj.r1
			r2= obj.r2
			r3= obj.r3
			r4= obj.r4
			r5= obj.r5
			r6= obj.r6
			r7= obj.r7
			r8= obj.r8
			r9= obj.r9
			r10= obj.r10

		
			
		lista1=[p1,p2,p3,p4,p5,p6,p7,p8,p9,p10]
		lista2=[r1,r2,r3,r4,r5,r6,r7,r8,r9,r10]
		puntaje=0

		for i in lista1:
			if i in lista2:
				puntaje=puntaje+10

			
		examen.save()
		obj=Examen.objects.filter(id=id_examen).update(realizado="SI",puntuacion=puntaje)
		messages.info(request,puntaje)		
		return HttpResponseRedirect(self.get_success_url())
			
		


	


	
	




	
