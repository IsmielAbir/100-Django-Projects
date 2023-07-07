from django.urls import path
from wordCount.views import countWord

urlpatterns = [
    path('wc/', countWord),

]
