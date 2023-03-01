from django.urls import path
from . import views

urlpatterns = [
    path('services/', views.services, name='services'), 
    path('search_services/', views.search_services, name='search_services'),
    path('services/<str:service_provider_services>/', views.view_service_category, name='view_service_category'),
    path('services/<str:service_provider>/<str:service_name>/', views.view_service, name='view_service'),
    path('services/<str:service_provider>/<str:service_name>/contact-provider/', views.contactProvider, name='contactProvider'),
    path('contact-admin/', views.contactAdmin, name='contactAdmin'),
    path('all-services/',views.all_services, name='all_services'),
   
    
    # Create 2 url in for <str: sp_name>
    
]