from django.urls import URLPattern

from django.urls import path
from .views import mysecondview, myfirtsview

urlpatterns = [
    path('uno/', myfirtsview),
    path('dos/', mysecondview)
]


