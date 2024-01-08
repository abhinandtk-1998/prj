from django.urls import path, include
from .import views

urlpatterns = [
    path('',views.hellofirst,name='hellofirst'),
    path('hellosecond',views.hellosecond,name='hellosecond'),
]
