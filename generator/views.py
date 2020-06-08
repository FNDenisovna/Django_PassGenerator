from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.

"""def home(request):
	///return HttpResponse('Hello there friend!')"""

def home(request):
	return render(request,'generator/home.html')

def about(request):
	return render(request,'generator/about.html')

def password(request):
	thepassword = ''
	characters = list('abcdefghijklmnopqrstuvwxyz')
	length = int(request.GET.get('length', 12))

	if request.GET.get('uppercase') and request.GET.get('uppercase') is not None:
		characters.extend(('abcdefghijklmnopqrstuvwxyz').upper())
	if request.GET.get('numbers') and request.GET.get('numbers') is not None:
		characters.extend(('1234567890').upper())
	if request.GET.get('special') and request.GET.get('special') is not None:
		characters.extend(('!@#$%^&*№?').upper())

	for i in range(length):
		thepassword += random.choice(characters)

	return render(request,'generator/password.html', {'password':thepassword})