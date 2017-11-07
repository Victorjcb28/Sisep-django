# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView,ListView,UpdateView,DeleteView
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render,redirect
from django.contrib import messages

from .forms import RegistroUsuarioForm,ProfileForm
from .models import Profile



# Create your views here.

class UsuarioCreate(CreateView):
	model= User
	template_name="usuario/registrarusuario.html"
	form_class=RegistroUsuarioForm
	success_url=reverse_lazy('usuarios:usuario_listar')

	def post(self, request, *args, **kwargs):
		self.object = self.get_object
		form = self.form_class(request.POST or None)
		
		if form.is_valid() :
			instance=form.cleaned_data
			instance=form.save(commit=False)
			#segunda linea captura el campo email
			form_data=form.cleaned_data
			abc=form_data.get('email')

			if "hola" not in abc:
				context={
					"form":form,
				}
				##contexto para reiniciar la pantalla si hay error
				messages.error(request,"Verifique email")
				return render(request,'usuario/registrarusuario.html',context)
			else:
				messages.success(request,"Muy bien")
				instance.save()
		return redirect('usuarios:usuario_listar')


class UsuarioList(ListView):
	model= User
	template_name= 'usuario/usuario_list.html'

#class UsuarioList(ListView):
#	model=Profile
#	template_name='usuario/usuario_list.html'


#def Usuariocre(request):
	#form= ProfileForm(request.POST or None,request.FILES or None)
	#context={

		#"form":form,
			#}
	#if form.is_valid():
		#instance=form.save(commit=False)
		#form.save()
		#abc=form.cleaned_data.get("tipo")
		#abc1=form.cleaned_data.get('image')
		#obj=Profile.objects.create(	user_id="1",tipo=abc,image=abc1)


	#return render(request,'usuario/usuario_update.html',context)

#def UsuarioUpdate(request, id_user):
#	profile=Profile.objects.get(id=id_user)	
#
#	if request.method=='GET':
#		form=ProfileForm(instance=profile)
#	else:
#		form=ProfileForm(request.POST,request.Files)
#		if form.is_valid():
#			form.save()
#		return redirect('usuarios:usuario_listar')
#	return render(request,'usuario/usuario_update.html',{'form':form})


class UsuarioUpdate(UpdateView):
	model= Profile
	second_model=User
	form_class=ProfileForm
	second_form_class=RegistroUsuarioForm
	template_name= 'usuario/usuario_update.html'
	success_url= reverse_lazy('usuarios:usuario_listar')

	def get_context_data(self, **kwargs):
		context= super(UsuarioUpdate,self).get_context_data(**kwargs)
		pk = self.kwargs.get('pk', 0)
		profile= self.model.objects.get(id = pk)
		user= self.second_model.objects.get(id=profile.user_id)
		if 'form'not in context:
			context['form']= self.form_class()
		if 'form2' not in context:
			context['form2']= self.second_form_class(instance=user)
		context['id']=pk


		return context


	def post(self,request,*args,**kwargs):
		self.object = self.get_object
		id_profile=kwargs['pk']

		profile=self.model.objects.get(id=id_profile)
		user= self.second_model.objects.get(id=profile.user_id)
		form=self.form_class(request.POST,request.FILES,instance=profile)
		form2= self.second_form_class(request.POST, instance=user)

		if form.is_valid() and form2.is_valid():
			form.save()
			form2.save()

			return HttpResponseRedirect(self.get_success_url())
		else:
			return HttpResponseRedirect(self.get_success_url())


class UsuarioDelete(DeleteView):
	model= User

	template_name='usuario/usuario_delete.html'
	success_url=reverse_lazy('usuarios:usuario_listar')




