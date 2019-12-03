from django.urls import path

from . import views

app_name = 'helloworld'

urlpatterns = [
    path('index1/', views.http_index, name="index1"),
    path('index2/', views.HelloWorldView.as_view(), name="index2"),
    path('index3/', views.render_index, name="index3"),
]