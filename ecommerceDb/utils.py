import datetime
from ecommerceDb.models import Customer,Product,Order,Review

def get_products_by_given_names(product_names):
    products = Product.objects.filter(name__in = product_names)



    products_list = list(products.values())
    result = {}

    for i in range(0,len(products_list)):
        nameOfProduct = products_list[i]['name']
        if nameOfProduct in result.keys():
            result[nameOfProduct].append(products_list[i])
        else:
            result[nameOfProduct] = [products_list[i]]

    return result

def get_orders_in_date_range():

    orders = Order.objects.select_related("customer","product").filter(order_date__gte=datetime.date(2023, 1, 1), order_date__lte=datetime.date(2023, 12, 31))

    #using range 
    # orders = Order.objects.select_related("customer","product").filter(order_date__range=(datetime.date(2023, 1, 1), datetime.date(2023, 12, 31)))

    # trying using filter and exclude both
    # orders = Order.objects.filter(order_date__gte=datetime.date(2023, 1, 1))
    # orders = orders.exclude(order_date__gt= datetime.date(2023,12,31))

    return list(orders.values())

def get_customers_who_ordered_laptop():
    queryset = Customer.objects.filter(order__product__name='Laptop')
    # print(queryset.query)
    names = list(queryset.distinct().values_list('name',flat = True))
    return names

def add_element_to_db():
    c = Customer.objects.create(name = "Adarsh12344", email = "adarsh1111112@gmail.com")
    p = Product.objects.create(name = "Laptop", category = "Electronics",price = 50000,stock_quantity = 5)
    o = Order.objects.create(customer = c,product = p,quantity = 1,order_date = datetime.date(2025, 2, 10))
    pass