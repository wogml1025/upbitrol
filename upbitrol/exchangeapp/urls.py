from django.urls import path

from exchangeapp.views import exchange

app_name = 'exchangeapp'

urlpatterns = [
    path('', exchange, name='exchange')
]