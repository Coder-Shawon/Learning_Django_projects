from django.shortcuts import render

from .models import Myalbum 

# Create your views here.


def myalbum(request):

    Myalbums = Myalbum.objects.all()

    context = {
        'Myalbums': Myalbums


    }

    return render(request, 'album/index.html', context)

