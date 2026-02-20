from config.wsgi import *
from django.test import TestCase
from core.erp.models import *

# Create your tests here.
for i in Category.objects.filter(id=1):
    print(i)