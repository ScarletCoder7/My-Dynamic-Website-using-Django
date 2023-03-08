from django.urls import path
from. import views

urlpatterns = [
    path('', views.index, name='index'),
    path('education', views.education, name = 'education'),
    path('contact', views.contact, name = 'contact'),
]
