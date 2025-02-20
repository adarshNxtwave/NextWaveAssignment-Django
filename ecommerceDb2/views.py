from django.http import HttpResponse
from django.shortcuts import render

from ecommerceDb.utils import *
# Create your views here.

def index(request):
    return HttpResponse("Hello, world. You're at the Db2 Project. hello ji ")

def query1(request):
    temp = get_products_by_given_names(["Tab"])
    return HttpResponse(str(temp))