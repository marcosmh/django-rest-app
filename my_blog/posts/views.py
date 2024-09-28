from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.base import View

# Create your views here.
class HelloWorld(View):
    def get(self, request):
        data = {
            'name': 'Marcos Magaña',
            'years': '40',
            'codes': ['Python','Java','Node Js']
        }
        return render(request,'hello_world.html',context=data)
