from django.urls import path
from .views import *

urlpatterns = [
		path('', home, name='home'),
		path('view_video/<int:id>/', view_video, name='view_video'),
		path('login/', login_func, name='login'),
		path('logout/', logout_func, name='logout'),
]