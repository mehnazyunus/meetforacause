from django.urls import path, include
from . import views
from django.contrib import admin

admin.site.site_header = 'Meet For a Cause Admin'

urlpatterns = [
    path('', views.home, name='home'),
    path('add',views.add, name='add'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/signup', views.signup, name='signup'),
    path('accounts/login_user', views.login_user, name='login_user'),
    path('search_by_location', views.search_by_location, name='search_by_location'),
    path('events/<int:pk>', views.event_details, name="event_details"),
    path('events/<int:pk>/attend', views.attend, name="attend"),
    path('events/<int:pk>/organise', views.organise, name="organise"),
    path('events/<int:pk>/sponsor', views.sponsor, name="sponsor"),
    path('events/<int:pk>/paid_services', views.paid_services, name='paid_services'),
    path('profile/', views.view_profile, name='view_profile'),
]