from django.urls import path
from contact.views import registration, send
urlpatterns = [
    path('', registration), 
    path('success', send)
]