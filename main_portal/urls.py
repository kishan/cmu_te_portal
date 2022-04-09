from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('test_airtable/', views.test_airtable, name='test_airtable')
]