# -*- encoding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Artigo(models.Model):	
	class Meta:		
		verbose_name = 'Artigo'
		verbose_name_plural = 'Artigos'
	foto = models.ImageField(upload_to = 'fotos/', default = 'fotos/sem.png')
	titulo = models.CharField(max_length=250,verbose_name='título')    
	subtitulo = models.CharField(max_length=250,verbose_name='subtítulo')    
	artigo = models.Manager()
class P(models.Model):	
	class Meta:		
		verbose_name = 'Paragrafo'
		verbose_name_plural = 'Paragrafos'
	artigo = models.ForeignKey(Artigo)
	foto = models.ImageField(upload_to = 'fotos/', default = 'fotos/sem.png')
	titulo = models.CharField(max_length=250,verbose_name='título',default='vizio**')    
	texto = models.CharField(max_length=250,verbose_name='texto',default=' ')    
	p = models.Manager()