# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class Postulante(models.Model):
	nombre=models.CharField(max_length=50,blank=True)
	apellidos=models.CharField(max_length=70)
	cedula=models.IntegerField(default=0)
	sexo=models.CharField(max_length=1,default="")
	fecha_nacimiento=models.CharField(max_length=100,default=0)
	edad=models.IntegerField()
	email=models.EmailField()
	telefono=models.CharField(max_length=12)	


class Educacion(models.Model):
	postulante=models.ForeignKey(Postulante,blank=True,null=True)
	instruccion=models.CharField(max_length=100)
	agraduacion=models.IntegerField()
	contabilidad=models.CharField(max_length=100)
	titulo=models.CharField(max_length=100)
	merito=models.IntegerField()
	curso=models.CharField(max_length=150)
	idioma=models.CharField(max_length=100)
	office=models.CharField(max_length=100)



class Direccion(models.Model):
	postulante=models.ForeignKey(Postulante,blank=True,null=True)
	estado=models.CharField(max_length=200,blank=True)
	municipio=models.CharField(max_length=200)
	parroquia=models.CharField(max_length=200)
	direccion=models.CharField(max_length=200)

class ExperienciaLaboral(models.Model):
	postulante=models.ForeignKey(Postulante,blank=True,null=True)
	tempresa=models.CharField(max_length=200)
	cargov=models.CharField(max_length=200)
	vempresa=models.CharField(max_length=200)
	anos=models.IntegerField(default=0)

class Cargo(models.Model):
	
	cargo=models.CharField(max_length=200)
	image=models.FileField(blank=True,null=True)#no colocar barra primero
	def __unicode__(self):
		return self.cargo

MY_CHOICES = (
        ('opt0', 'ADMINISTRADOR'),
        ('opt1', 'SECRETARIA'),
    )
	


class Pregunta(models.Model):
	cargo=models.ForeignKey(Cargo,blank=True,null=True)
	p1=models.CharField(max_length=200)	
	p2=models.CharField(max_length=200,blank=True,null=True)
	p3=models.CharField(max_length=200,blank=True,null=True)
	p4=models.CharField(max_length=200,blank=True,null=True)
	p5=models.CharField(max_length=200,blank=True,null=True)
	p6=models.CharField(max_length=200,blank=True,null=True)
	p7=models.CharField(max_length=200,blank=True,null=True)
	p8=models.CharField(max_length=200,blank=True,null=True)
	p9=models.CharField(max_length=200,blank=True,null=True)
	p10=models.CharField(max_length=200,blank=True,null=True)

class RespuestaCo(models.Model):
	cargo=models.ForeignKey(Cargo,blank=True,null=True)
	r1=models.CharField(max_length=200,blank=True,null=True)
	r2=models.CharField(max_length=200,blank=True,null=True)
	r3=models.CharField(max_length=200,blank=True,null=True)
	r4=models.CharField(max_length=200,blank=True,null=True)
	r5=models.CharField(max_length=200,blank=True,null=True)
	r6=models.CharField(max_length=200,blank=True,null=True)
	r7=models.CharField(max_length=200,blank=True,null=True)
	r8=models.CharField(max_length=200,blank=True,null=True)
	r9=models.CharField(max_length=200,blank=True,null=True)
	r10=models.CharField(max_length=200,blank=True,null=True)

class Respuesta(models.Model):
	cargo=models.ForeignKey(Cargo,blank=True,null=True)
	r1=models.CharField(max_length=200,blank=True,null=True)
	r2=models.CharField(max_length=200,blank=True,null=True)
	r3=models.CharField(max_length=200,blank=True,null=True)
	r4=models.CharField(max_length=200,blank=True,null=True)
	r5=models.CharField(max_length=200,blank=True,null=True)
	r6=models.CharField(max_length=200,blank=True,null=True)
	r7=models.CharField(max_length=200,blank=True,null=True)
	r8=models.CharField(max_length=200,blank=True,null=True)
	r9=models.CharField(max_length=200,blank=True,null=True)
	r10=models.CharField(max_length=200,blank=True,null=True)
	r11=models.CharField(max_length=200,blank=True,null=True)
	r12=models.CharField(max_length=200,blank=True,null=True)
	r13=models.CharField(max_length=200,blank=True,null=True)
	r14=models.CharField(max_length=200,blank=True,null=True)
	r15=models.CharField(max_length=200,blank=True,null=True)
	r16=models.CharField(max_length=200,blank=True,null=True)
	r17=models.CharField(max_length=200,blank=True,null=True)
	r18=models.CharField(max_length=200,blank=True,null=True)
	r19=models.CharField(max_length=200,blank=True,null=True)
	r20=models.CharField(max_length=200,blank=True,null=True)
	r21=models.CharField(max_length=200,blank=True,null=True)
	r22=models.CharField(max_length=200,blank=True,null=True)
	r23=models.CharField(max_length=200,blank=True,null=True)
	r24=models.CharField(max_length=200,blank=True,null=True)
	r25=models.CharField(max_length=200,blank=True,null=True)
	r26=models.CharField(max_length=200,blank=True,null=True)
	r27=models.CharField(max_length=200,blank=True,null=True)
	r28=models.CharField(max_length=200,blank=True,null=True)
	r29=models.CharField(max_length=200,blank=True,null=True)
	r30=models.CharField(max_length=200,blank=True,null=True)

class Examen(models.Model):
	postulante=models.ForeignKey(Postulante,blank=True,null=True)
	cargo=models.ForeignKey(Cargo,blank=True,null=True)
	
	puntuacion=models.CharField(max_length=200)	
	p1=models.CharField(max_length=200,blank=True,null=True,)	
	p2=models.CharField(max_length=200,blank=True,null=True)
	p3=models.CharField(max_length=200,blank=True,null=True)
	p4=models.CharField(max_length=200,blank=True,null=True)
	p5=models.CharField(max_length=200,blank=True,null=True)
	p6=models.CharField(max_length=200,blank=True,null=True)
	p7=models.CharField(max_length=200,blank=True,null=True)
	p8=models.CharField(max_length=200,blank=True,null=True)
	p9=models.CharField(max_length=200,blank=True,null=True)
	p10=models.CharField(max_length=200,blank=True,null=True)
	realizado=models.CharField(max_length=100,blank=True,null=True)




	

	

	
