from django.urls import path
from . import views

urlpatterns = [
    path('services/', views.services, name='services'), 
    path('search_services/', views.search_services, name='search_services'),
    path('services/<int:service_provide_id>/', views.view_service_category, name='view_service_category'),
    path('services/product/<int:service_id>/', views.view_service, name='view_service'),
    path('contact-admin/', views.contactAdmin, name='contactAdmin'),
    path('all-services/',views.all_services, name='all_services'),

    # path('services/sp_messages/', views.view_messages_service_provider, name='sp_messages'),
    # path('services/<str:service_provider>/<str:service_name>/contact-provider/', views.contactProvider, name='contactProvider'), 
]