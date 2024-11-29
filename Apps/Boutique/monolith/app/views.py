from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

from . import utils

def index (request):
    
    context = {}

    context ["man_categories"] = utils.all_man_categories() # Man categories
    context ["woman_categories"] = utils.all_woman_categories() # Woman categories

    return render (request, 'app/index.html', context=context)

def man (request):

    context = {}

    context["title"] = "Man"
    context["sub_title"] = "All"

    context ["man_categories"] = utils.all_man_categories() # Man categories
    context ["woman_categories"] = utils.all_woman_categories() # Woman categories

    context ["products"] = utils.all_man() # Man products

    return render (request, 'app/catalog.html', context=context)

def woman (request):

    context = {}

    context["title"] = "Woman"
    context["sub_title"] = "All"

    context ["man_categories"] = utils.all_man_categories() # Man categories
    context ["woman_categories"] = utils.all_woman_categories() # Woman categories

    context ["products"] = utils.all_woman() # Woman products

    return render (request, 'app/catalog.html', context=context)

def man_category (request, category):

    context = {}

    context["title"] = "Man"
    context["sub_title"] = category

    context ["man_categories"] = utils.all_man_categories() # Man categories
    context ["woman_categories"] = utils.all_woman_categories() # Woman categories

    context ["products"] = utils.all_man_category( category ) # Category man products

    return render (request, 'app/catalog.html', context=context)

def woman_category (request, category):

    context = {}

    context["title"] = "Woman"
    context["sub_title"] = category

    context ["man_categories"] = utils.all_man_categories() # Man categories
    context ["woman_categories"] = utils.all_woman_categories() # Woman categories

    context ["products"] = utils.all_woman_category( category ) # Category man products

    return render (request, 'app/catalog.html', context=context)


def product_id (request, id):

    context = {}

    context["title"] = "Product"
    context["sub_title"] = id

    context ["man_categories"] = utils.all_man_categories() # Man categories
    context ["woman_categories"] = utils.all_woman_categories() # Woman categories

    context ["product"] = utils.product_id ( id ) 

    if "message" in request.session:
        context["message"] = request.session["message"]
        del request.session["message"]

    return render (request, 'app/product.html', context=context)


@login_required(login_url='/login')
def add_to_cart (request):
   
    context = {}

    if request.method == "POST":
        
        if "product_id" in request.POST and 'size' in request.POST: # Protocol
            
            product_id = request.POST["product_id"]
            size = request.POST["size"]

            order_confirm = utils.get_from_stock (product_id, size)
            
            if order_confirm["product_id"] == False:
                
                return render (request, 'app/404.html', context=context)
            
            elif order_confirm["size"] == False:

                request.session["message"] = "The size isn't available, we're sorry."

                kwargs = {
                    "id": product_id
                }
                return HttpResponseRedirect(reverse("product_id", kwargs=kwargs)) 
            
            utils.add_to_cart (request.user, product_id, size)

            kwargs = {
                "id": product_id
            }
            return HttpResponseRedirect(reverse("product_id", kwargs=kwargs))
        
    return render (request, 'app/404.html', context=context)


@login_required(login_url='/login')
def cart (request):

    context = {}

    context["title"] = "Cart"

    context["sub_title"] = "Products"

    cart = utils.my_cart ( request.user )

    if cart:

        context["cart"] = cart
    
        context["total"] = cart.total

    return render (request, 'app/cart.html', context=context)


@login_required(login_url='/login')
def purchase (request):

    context = {}

    if request.method == "POST":

        context["title"] = "Purchase"

        context["sub_title"] = "Purchase"

        cart = utils.my_cart ( request.user )
        
        if utils.payAPI ( request.user, cart.total ):

            order = utils.create_order ( request.user, cart )

            utils.create_payment ( order )

            utils.send_order_invoice ( order, request.user )
            
            cart.delete ()

            context["messages"] = []
            context["messages"].append ("Thank you for purchasing with us.")
            context["messages"].append ("We will sent you an email with your invoice.")
            context["messages"].append ("The Boutique team.")

            return render (request, 'app/cart-purchase.html', context=context)
        
        else: 
            context["messages"] = []
            context["messages"].append ("Something went wrong with your purchase.")
            context["messages"].append ("Check your cart.")
            context["messages"].append ("If necessery contact the support team.")

            return render (request, 'app/cart-purchase.html', context=context)

    return HttpResponseRedirect( reverse("cart") )



@login_required(login_url='/login')
def orders (request):

    context = {}

    if request.method == "GET":

        context["title"] = "Orders"

        context["sub_title"] = "Orders"

        orders = utils.my_orders ( request.user )

        context["orders"] = orders

        print (orders)

        return render (request, 'app/orders.html', context=context)

    return HttpResponseRedirect ( reverse ("index") )


def login_view (request):

    context = {}

    if request.method == "POST":

        if "email" in request.POST and "password" in request.POST: # Protocol
            
            email = request.POST["email"]
            password = request.POST["password"]

            user = authenticate(request, username=email, password=password)
            
            if user is not None:

                login(request, user)
                
                return HttpResponseRedirect ( reverse("index") )
            
            else:
                
                context = {
                    "message": "Invalid email and/or password."
                }

                return render(request, 'app/login.html', context=context)
        else:

            context["status"] = 400

    return render (request, 'app/login.html', context=context)
    

def logout_view (request):

    logout(request)

    return HttpResponseRedirect ( reverse("index") )


def register (request):

    context = {}

    if request.user.is_authenticated:

        return HttpResponseRedirect ( reverse("index") )        

    if request.method == "POST":

        if "first" in request.POST and "email" in request.POST and "password" in request.POST: # Protocol
            
            first = request.POST["first"]
            if "last" in request.POST: # Protocol
                last = request.POST["last"]
            else:
                last = ""
            email = request.POST["email"]
            password = request.POST["password"]

            try:
                user = User.objects.create_user(username=email, password=password, first_name=first, last_name=last)
                user.save()
            except IntegrityError:
                return render(request, 'app/register.html', {
                    "message": "Email already taken."
                })
            
            login(request, user)
            
            return HttpResponseRedirect ( reverse("index") )
        
        else:

            context["status"] = 400

    return render (request, 'app/register.html', context=context)