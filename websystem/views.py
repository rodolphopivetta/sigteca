from django.shortcuts import render

def index(request):
	return render(request, 'index.html')

def register_hq(request):
	return render(request, 'register_hq.html')

def register_member(request):
	return render(request, 'register_member.html')
