from django.shortcuts import render
from server.models import *
# Create your views here.
def index(request):
	artigos = Artigo.artigo.all()
	ps = P.p.filter(artigo = artigos[0])
	return render(request,'index.html',{'artigos':artigos,'artigo':artigos[0],'ps': ps})                        
