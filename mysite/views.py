from multiprocessing.pool import rebuild_exc

from django.http import HttpResponse
from django.shortcuts import render

def homepage(request):
    data = {"header": "Homepage", "message":"Welcome to my site!"}
    return render(request, 'homepage.html', data)

def about(request):
    header = "About us"
    staff = ['John1', 'John2', 'John3']
    director = {"name": "David", "img": '/director.jpg'}
    address = ('20 W 34th St.', 'New York', 'NY10001', 'USA')
    data = {"header": header, "staff": staff, "director": director, "address": address}
    return render(request, 'about.html', data)
