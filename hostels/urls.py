from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from . import views

urlpatterns=[
    path('', views.home, name='hostels'),
    path('register/', views.register, name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='registration/logout.html'), name='logout'),
    path('hostel/<int:id>',views.hostels,name = 'hostel'),
    path('profile/',views.profile,name = 'profile'),
    path('editprofile/',views.edit_Profile,name = 'editprofile'),
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)