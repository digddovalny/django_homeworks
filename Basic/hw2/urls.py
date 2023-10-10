from django.urls import path
from .views import hw2, basket, sorted_basket

urlpatterns = [
    path('', hw2, name='hw2'),
    path('client/<int:client_id>/', basket, name='basket'),
    path('client/<int:client_id>/<int:days_ago>/', sorted_basket, name='sorted_basket'),
]