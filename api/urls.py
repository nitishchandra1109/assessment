
from django.urls import path
from .views import employee_list,EventNewsItems
urlpatterns = [
    path('',employee_list, name='employee-list'),
    path('list/',EventNewsItems.as_view(), name='employee-list-cbv'),
]