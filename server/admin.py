from django.contrib import admin
from server.models import *
# Register your models here.

class ArtigoAdmin(admin.ModelAdmin):	
	search_fields = ['titulo']
	list_display = ['foto','titulo']	
	list_filter = ['titulo']
	save_on_top = True	

class PAdmin(admin.ModelAdmin):	
	search_fields = ['titulo']
	list_display = ['foto','titulo']	
	list_filter = ['titulo']
	save_on_top = True	
admin.site.register(Artigo,ArtigoAdmin)	
admin.site.register(P,PAdmin)