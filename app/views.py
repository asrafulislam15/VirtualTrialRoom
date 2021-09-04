from django.shortcuts import render
from django.views import View
from .models import Cart,Customer,Product,OrderPlaced
from .forms import CustomarRegistrationForm,CustomerProfileForm
from django.contrib import messages


class ProductView(View):
  def get(self,request):
   topwearsmale=Product.objects.filter(category='Top Wear Male')
   topwearsfemale=Product.objects.filter(category='Top Wear Female')
   return render(request,'app/home.html',{'topwearsmale':topwearsmale,'topwearsfemale':topwearsfemale})

class ProductDetailView(View):
 def get(self,request,pk):
  product=Product.objects.get(pk=pk)
  return render(request, 'app/productdetail.html',{'product':product})

def add_to_cart(request):
 return render(request, 'app/addtocart.html')

def buy_now(request):
 return render(request, 'app/buynow.html')

def profile(request):
 return render(request, 'app/profile.html')

def address(request):
 add = Customer.objects.filter(user=request.user)
 return render(request, 'app/address.html',{'add':add,'active':'btn-primary'})

def orders(request):
 return render(request, 'app/orders.html')


def mobile(request):
 return render(request, 'app/mobile.html')


class CustomerRegistrationView(View):
 def get(self,request):
  form =CustomarRegistrationForm()
  return render(request,'app/customerregistration.html', {'form':form})

 def post(self,request):
  form=CustomarRegistrationForm(request.POST)
  if form.is_valid():
   messages.success(request, 'Congratulation!! Registered Successfully')
   form.save()
  return render(request, 'app/customerregistration.html', {'form':form})

def checkout(request):
 return render(request, 'app/checkout.html')

class ProfileView(View):
 def get(self,request):
  form =CustomerProfileForm()
  return render(request,'app/profile.html',{'form':form, 'active':'btn-primary'})

def post(self,request):
  form= CustomerProfileForm(request.POST)
  if form.is_valid():
   user=request.user
   name = form.cleaned_date['name']
   locality = form.cleaned_date['locality']
   city = form.cleaned_date['city']
   state = form.cleaned_date['state']
   zipcode = form.cleaned_date['zipcode']
   reg = Customer(user=user, name=name, locality=locality, city=city, state=state, zipcode=zipcode)
   reg.save()
   messages.success(request,'Congratulations! Profile Update Successfully ')
  return render(request, 'app/profile.html',{'form':form,'active':'btn-primary'})