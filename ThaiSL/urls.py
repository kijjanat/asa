from django.urls import path
from . import views

urlpatterns = [
    path('animation/',views.animation_view,name='animation'),
    path('',views.home_view,name='home'),
    path('image/', views.image_view, name='image'),
	path('pronoun/', views.pronoun_view, name='pronoun'),
	path('place/', views.place_view, name='place'),
]
