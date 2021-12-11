from django.shortcuts import render, redirect
from .models import Videos
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.db.models import Q
from django.core.paginator import Paginator

# Create your views here.


     # Show 25 contacts per page.

    
    
# @login_required
def home(request):
	videos = Videos.objects.all()
	paginator = Paginator(videos, 5)
	page_number = request.GET.get('page')
	page_obj = paginator.get_page(page_number)
	context = {'videos': page_obj}
	return render(request, 'home.html', context)

# @login_required
def view_video(request, id):
	video = Videos.objects.get(video_id=id)
	context = {'video': video}
	return render(request, 'detail.html', context)


# @login_required
def search(request):
	context = {}
	if request.method == 'POST':
		search = request.POST.get('search')
		data = Videos.objects.filter(Q(name__startswith=search))
	
		context = {'videos': data}
	return render(request, 'home.html', context)

# def login_func(request):
# 	if request.method == 'POST':
# 		username = request.POST.get('username')
# 		password = request.POST.get('password')
# 		user = authenticate(request, username=username, password=password)
# 		if user is not None:
# 			login(request, user)
# 			return redirect('/')
# 		else:
# 			pass
# 	context = {}
# 	return render(request, 'login.html', context)

# def logout_func(request):
# 	logout(request)
# 	return redirect('/')