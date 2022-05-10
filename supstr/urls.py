from django.urls import path
from .views import home, sing_up_view

urlpatterns = [
    path('', home, name='home-view'),
    path('sing-up', sing_up_view, name='sing-up-view'),
]
