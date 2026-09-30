from django.urls import path, include  # keep BOTH path AND include!
from . import views

urlpatterns = [
    
    path('dynamic-form/', views.dynamic_form, name='dynamic-form'),

   
    path('accounts/', include('django.contrib.auth.urls')),

   
    path('api/', include('registration.api_urls')),

    
    path('', include('registration.urls')),
]