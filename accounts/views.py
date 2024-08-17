from django.shortcuts import render, redirect

from accounts.models import User,UserProfile
from .forms import UserForm
from django.contrib import messages
from vendor.forms import VendorForm
# from .models import User

# Create your views here.


def register_user(request):
    """"""
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            password = form.cleaned_data.get('password')
            user = form.save(commit=False)
            user.set_password(password)
            user.role = user.CUSTOMER
            user.save()
            messages.success(request, 'Your account has been registered')
            # first_name = form.cleaned_data['first_name']
            # last_name = form.cleaned_data['last_name']
            # username = form.cleaned_data['username']
            # email = form.cleaned_data['email']
            # password = form.cleaned_data['password']
            # user = User.objects.create_user(first_name=first_name,last_name=last_name,username=username,email=email,password=password)
            # user.role = User.CUSTOMER
            # user.save()
            return redirect("home")
        else:
            return (form.errors)
    else:
        form = UserForm()
    context = {'form': form}
    return render(request, 'accounts/registerUser.html', context)


def register_vendor(request):
    """
    """
    if request.method == "POST":
        form = UserForm(request.POST)
        v_form = VendorForm(request.POST,request.FILES)
        if form.is_valid() and v_form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = User.objects.create_user(first_name=first_name, last_name=last_name, username=username, email=email, password=password)
            user.role = User.VENDOR
            user.save()
            vendor = v_form.save(commit=False)
            vendor.user = user
            user_profile = UserProfile.objects.get(user=user)
            vendor.user_profile = user_profile
            vendor.save()
            messages.success(request, 'Your vendor account has been registered, Please wait to approval')
            return redirect('home')
        else:
            return (form.errors)
    else:
        form = UserForm()
        v_form = VendorForm() 
    context = {
        'form': form,
        'vendor_form': v_form,
    }
    return render(request, 'accounts/registerVendor.html', context)
