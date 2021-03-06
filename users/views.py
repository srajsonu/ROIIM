from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from users.forms import UserForm, CheckoutForm


def dashboard(request):
    if request.method == 'POST':
        checkout_form = CheckoutForm(request.POST)
        if checkout_form.is_valid():
            amount = checkout_form.cleaned_data['amount']
            print('amount....', amount)
            return render(request, 'checkout.html', {'amount': amount})
    return render(request, 'dashboard.html')


def register(request):
    registered = False
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        if user_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            registered = True
            return redirect('user:user_login')
        else:
            print(user_form.errors)
    else:
        user_form = UserForm()

    return render(request, 'register.html', {'user_form': user_form, 'registered': registered})

def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return redirect('checkout:checkout')
            else:
                return HttpResponse('Your account is not active')
        return render(request, 'signin.html')
    else:
        return render(request, 'signin.html')


@login_required
def signout(request):
    logout(request)
    return redirect('user:user_login')
