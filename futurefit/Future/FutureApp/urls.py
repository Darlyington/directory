from django.urls import path
from . import views
from .views import contact_view

urlpatterns = [
    path('', views.home_view, name='home'),
    path('about/', views.about_us_view, name='about_us'),
    path('services/', views.our_service_view, name='our_service'),
    path('programs/', views.programs_view, name='programs'),
    path('study-abroad/', views.study_abroad_view, name='study_abroad'),
    path('energy-solution/', views.energy_solution_view, name='energy_solution'),
    path('store/', views.store_view, name='store'),
    path('news/', views.news_update_view, name='news_update'),
    path('contact/', contact_view.as_view(), name='contact'),
    path('subscribe/', views.newsletter_subscribe_view, name='newsletter_subscribe'),
  
    path('store/<int:pk>/', views.store_detail_view, name='store_detail'),
]