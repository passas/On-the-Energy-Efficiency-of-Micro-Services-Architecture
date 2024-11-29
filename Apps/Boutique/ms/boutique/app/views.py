from django.shortcuts import render

from django.http import HttpResponseRedirect
from django.urls import reverse

from . import requests


def index (request):
    
    context = {}

    context["man_categories"] = requests.all_man_categories()
    context["woman_categories"] = requests.all_woman_categories()

    return render (request, 'app/index.html', context=context)



def man (request):
    
    context = {}

    context["title"] = "Man"
    context["sub_title"] = "All"

    context["man_categories"] = requests.all_man_categories()
    context["woman_categories"] = requests.all_woman_categories()

    context ["products"] = requests.all_man() # Man products

    return render (request, 'app/catalog.html', context=context)



def woman (request):
    
    context = {}

    context["title"] = "Woman"
    context["sub_title"] = "All"

    context["man_categories"] = requests.all_man_categories()
    context["woman_categories"] = requests.all_woman_categories()

    context ["products"] = requests.all_woman() # Woman products

    return render (request, 'app/catalog.html', context=context)



def man_category (request, category):
    
    context = {}

    context["title"] = "Man"
    context["sub_title"] = category

    context["man_categories"] = requests.all_man_categories()
    context["woman_categories"] = requests.all_woman_categories()

    (status, products) = requests.man_category( category ) # Man products

    context ["products"] = products

    if status == 404:

        return render (request, 'app/404.html', context=context)

    return render (request, 'app/catalog.html', context=context)



def woman_category (request, category):
    
    context = {}

    context["title"] = "Woman"
    context["sub_title"] = category

    context["man_categories"] = requests.all_man_categories()
    context["woman_categories"] = requests.all_woman_categories()

    (status, products) = requests.woman_category( category ) # Woman products

    context ["products"] = products

    if status == 404:

        return render (request, 'app/404.html', context=context)

    return render (request, 'app/catalog.html', context=context)



def product (request, id):
    
    context = {}

    context["title"] = "Product"
    context["sub_title"] = id

    context["man_categories"] = requests.all_man_categories()
    context["woman_categories"] = requests.all_woman_categories()

    (status, product) = requests.product ( id )
    
    context["product"] = product

    if status == 404:

        return render (request, 'app/404.html', context=context)

    if "message" in request.session: # Reservation details

        context["message"] = request.session["message"]

        del request.session["message"]

        request.session.modified = True

    return render (request, 'app/product.html', context=context)



#login_required
def cart (request):
    
    #login_required
    if "JWT" in request.session:

        (status, data) = requests.authenticate ( request.session["JWT"] )

        if status == 403: # Expired session
            
            request.session.flush() # Get out of the session

            request.session.modified = True

            request.session["message"] = "Expired session, please login."

            return HttpResponseRedirect ( reverse("login") )

    else: # Not in a session
        
        return HttpResponseRedirect ( reverse("login") )
    
    context = {}

    if request.method == 'GET':
        
        context["title"] = "Cart"

        context["sub_title"] = "Products"

        (status, data) = requests.get_cart ( request.session["JWT"] )

        if status == 403: # Expired session
            
            request.session.flush() # Get out of the session

            request.session.modified = True

            request.session["message"] = "Expired session, please login."

            return HttpResponseRedirect ( reverse("login") )
        
        elif status == 404: # Empty cart
            
            context["products"] = []

            return render (request, 'app/cart.html', context=context)

        elif status == 406: # Wrong protocol

            return HttpResponseRedirect ( reverse("index") )
        
        elif status == 200:

            context["count"] = data['count']

            context["total"] = data['total']

            context["products"] = data['products']

            return render (request, 'app/cart.html', context=context)

    if request.method == 'POST':

        if 'id' in request.POST and 'size' in request.POST: # Protocol
            
            (status, data) = requests.post_cart (request.session['JWT'], request.POST['id'], request.POST['size'])
            
            if status == 403: # Expired session
            
                request.session.flush() # Get out of the session

                request.session.modified = True

                request.session["message"] = "Expired session, please login."

                return HttpResponseRedirect ( reverse("login") )

            elif status == 404: # Product not found

                return render (request, 'app/404.html', context=context)

            elif status == 409: # Out of stock
                
                request.session["message"] = "The product went out of stock, we're sorry."

                kwargs = {
                    "id": request.POST['id']
                }

                return HttpResponseRedirect ( reverse("product", kwargs=kwargs) )
            
            elif status == 200:
                
                request.session["message"] = "Product added to cart."

                kwargs = {
                    "id": request.POST['id']
                }

                return HttpResponseRedirect ( reverse("product", kwargs=kwargs) )

        else: # Failed protocol

            return HttpResponseRedirect ( reverse("index") )
            


#login_required
def cart_purchase (request):

    #login_required
    if "JWT" in request.session:

        (status, data) = requests.authenticate ( request.session["JWT"] )

        if status == 403: # Expired session
            
            request.session.flush() # Get out of the session

            request.session.modified = True

            request.session["message"] = "Expired session, please login."

            return HttpResponseRedirect ( reverse("login") )

    else: # Not in a session
        
        return HttpResponseRedirect ( reverse("login") )
    
    context = {}

    if request.method == 'POST':

        (status, data) = requests.purchase_cart (request.session['JWT'])

        if status == 400:

            context["messages"] = []
            context["messages"].append ("Something went wrong with your purchase.")
            context["messages"].append ("Check your cart.")
            context["messages"].append ("If necessery contact the support team.")

            return render (request, 'app/purchased.html', context=context)

        elif status == 200:

            context["messages"] = []
            context["messages"].append ("Thank you for purchasing with us.")
            context["messages"].append ("We will sent you an email with your invoice.")
            context["messages"].append ("The Boutique team.")

            return render (request, 'app/purchased.html', context=context)



def login (request):

    if 'JWT' in request.session: # Already in a session

        return HttpResponseRedirect ( reverse("index") )

    context = {}

    if request.method == 'GET':

        if "message" in request.session: # Session expired

            context["message"] = request.session["message"]

            del request.session["message"]

            request.session.modified = True

        return render (request, 'app/login.html', context=context)
    
    elif request.method == 'POST':

        if 'email' in request.POST and 'password' in request.POST: # Protocol

            email = request.POST['email']
            password = request.POST['password']

            (status, data) = requests.login (email, password)

            if status == 200:

                request.session["JWT"] = data['token'] # Session

                return HttpResponseRedirect ( reverse("index") ) # 302

            elif status == 404:
                
                context["message"] = data["detail"]

                return render (request, 'app/login.html', context=context)

            elif status == 403:

                context["message"] = data["detail"]

                return render (request, 'app/login.html', context=context)

        else: # Protocol Failure

            return render (request, 'app/login.html', context=context) # {}



def logout (request):

    context = {}

    request.session.flush() # Delete session

    return HttpResponseRedirect ( reverse("index") )



def register (request):

    if 'JWT' in request.session: # Already in a session

        return HttpResponseRedirect ( reverse("index") )

    context = {}

    if request.method == 'GET':

        return render (request, 'app/register.html', context=context) # {}
    
    elif request.method == 'POST':

        if 'first' in request.POST and 'email' in request.POST and 'password' in request.POST: # Protocol
            
            first = request.POST['first']
            if 'last' in request.POST: # Protocol
                last = request.POST['last']
            else:
                last = ""
            email = request.POST['email']
            password = request.POST['password']

            (status, data) = requests.register (email, password, first, last)

            if status == 200:

                request.session["JWT"] = data['token'] # Session

                return HttpResponseRedirect ( reverse("index") )

            elif status == 400:
                
                context["message"] = data["detail"]

                return render (request, 'app/register.html', context=context)

        else: # Protocol Failure

            return render (request, 'app/register.html', context=context) # {}