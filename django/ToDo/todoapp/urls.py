from django.urls import path
from todoapp import views




urlpatterns = [
    path('',views.Home),
    path('about/',views.About),
    path('contact/',views.Contact)
]