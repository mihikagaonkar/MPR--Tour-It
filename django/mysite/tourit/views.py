from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group

from django.contrib.auth import authenticate, login, logout

from django.contrib import messages
from django.contrib.auth import authenticate, login

from .models import *
from .forms import CreateUserForm, CustomerForm
from .decorators import unauthenticated_user, allowed_users

from django.views.generic import ListView, DetailView

from django.template.loader import render_to_string

from django.urls import reverse

def home(request):
    context = {}
    return render(request, 'tourit/home.html', context)


@unauthenticated_user
def loginPage(request):
    #if request.user.is_authenticated:
        #return render(request, 'tourit/dashboard.html')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        group = None
        if user is not None:
            login(request, user)
            if request.user.groups.exists():
                group= request.user.groups.all()[0].name
            if group== 'customer':
                return redirect('tourit:user')
            if group== 'admin':
                return redirect('tourit:dashboard')
        else:
            messages.info(request, 'Password or Username did not match')

    context = {}
    return render(request, 'tourit/login.html', context)


@unauthenticated_user
def registerPage(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user=form.save()
            username = form.cleaned_data.get('username')
             #to just get the username without all the attributes
            group = Group.objects.get(name= 'customer') #whichever user creates a page it is added to the customer group
            user.groups.add(group)
            Customer.objects.create(
                user = user,
                name = user.username,
                email = user.email
            )


            messages.success(request, 'account was created for ' + username)

            return redirect('tourit:login')
    context = {'form':form}
    return render(request, 'tourit/register.html', context)

def logoutUser(request):
    logout(request)
    return redirect('tourit:home')

@login_required(login_url='tourit:login')
@allowed_users(allowed_roles=['customer'])
def UserPage(request):
    placetypes= PlaceType.objects.all()
    context = {'placetypes':placetypes}
    return render(request, 'tourit/userpage.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['customer'])
def accountSettings(request):
    customer = request.user.customer
    form = CustomerForm(instance=customer)

    if request.method == 'POST':
        form= CustomerForm(request.POST, request.FILES, instance=customer)
        if form.is_valid():
            form.save()

    context={'form':form}
    return render(request,'tourit/account_settings.html', context)

@login_required(login_url='tourit:login')
@allowed_users(allowed_roles=['admin'])       #only admin access page
def dashboardPage(request):
    context = {}
    return render(request, 'tourit/dashboard.html', context)

#@login_required(login_url='tourit:login')
#def shopping(request):
    #places= Place.objects.filter(placetypes__name="shopping")
    #context = {'places':places}
    #return render(request, 'tourit/shopping.html', context)
@login_required(login_url='tourit:login')
def ListPage(request, pk):
    b = PlaceType.objects.get(id = pk)
    places = b.place_set.all()
    placetype = PlaceType.objects.all()
    current = pending(request)
    context = {'places':places , 'placetype':placetype, 'current':current}
    return render(request,'tourit/list.html', context)


class DetailPage(DetailView):
    model=Place
    template_name='tourit/detail.html'


@login_required(login_url='tourit:login')
def pending(request):
    user_profile = get_object_or_404(Customer, user=request.user)
    order = Itinerary.objects.filter(customer=user_profile, is_added=False)
    if order.exists():
        # get the only order in the list of filtered orders
        return order[0]
    return 0

def MyTrips(request, **kwargs):
    exsisting_order = pending(request)
    context = {'order':exsisting_order}
    return render(request, 'tourit/itinerary.html', context)



@login_required(login_url='tourit:login')
def add_to_trip(request, **kwargs):
    user_profile = get_object_or_404(Customer, user=request.user)
    product = Place.objects.filter(id=kwargs.get('item_id',"")).first()

    if product in request.user.customer.place.all():
        messages.info(request,'You have already added that to your Itinerary')
        return redirect(reverse('tourit:trip' ))

    itinerary_place,status = ItineraryPlace.objects.get_or_create(product=product)

    user_itinerary,status =Itinerary.objects.get_or_create(customer=user_profile, is_added=False)
    user_itinerary.place.add(itinerary_place)
    if status:
        user_itinerary.ref_code = generate_order_id()
        user_itinerary.save()

    messages.info(request,"place added to Itinerary")
    return redirect(reverse('tourit:trip'))

@login_required(login_url='tourit:login')
def delete_from_cart(request, item_id):
    item_to_delete = ItineraryPlace.objects.filter(pk=item_id)
    if item_to_delete.exists():
        item_to_delete[0].delete()
        messages.info(request, "place has been removed from itinerary")
    return redirect(reverse('tourit:trip'))






    #context = {'places':places}
    #def get_queryset(self):
        #qs = super().get_queryset()
        # filter by a variable captured from url, for example
        #return qs.filter(name__startswith=self.kwargs['placetypes'])





#to check     if email.has_changed():
              #try:
                # match = User.objects.get(email=email)
                # messages.info(request, 'email already exists ')
            #  except User.DoesNotExist:











# Create your views here.
