from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('trends/', views.trends, name='trends'), 
    path('login/',views.login,name='login'),
    path('landing_page/',views.landing_page,name='landing_page'),
    path('calculate_score/',views.calculate_score,name='calculate_score'),
    
]
