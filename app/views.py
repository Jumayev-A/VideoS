from django.shortcuts import render, redirect
from .models import Videos
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout

# Create your views here.
@login_required
def home(request):
	videos = Videos.objects.all()
	context = {'videos': videos}
	return render(request, 'home.html', context)

@login_required
def view_video(request, id):
	video = Videos.objects.get(id=id)
	context = {'video': video}
	return render(request, 'detail.html', context)

def login_func(request):
	if request.method == 'POST':
		username = request.POST.get('username')
		password = request.POST.get('password')
		user = authenticate(request, username=username, password=password)
		if user is not None:
			login(request, user)
			return redirect('/')
		else:
			pass
	context = {}
	return render(request, 'login.html', context)

def logout_func(request):
	logout(request)
	return redirect('/')