from django.http import HttpResponse
from django.shortcuts import render

from ecommerceDb.utils import *



def index(request):
    return HttpResponse("Hello, world. You're at the polls index. hello ji ")

def query1(request):
    temp = get_products_by_given_names(["Tab"])
    return HttpResponse(str(temp))

def query2(request):
    temp = get_orders_in_date_range()
    return HttpResponse(temp)

def query3(request):
    temp = get_customers_who_ordered_laptop()
    print(temp)
    return HttpResponse(temp)

def add(request):
    add_element_to_db()
    return "Done"