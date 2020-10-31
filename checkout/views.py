from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render


# Create your views here.

@login_required
def checkout(request):
    username = request.user.username
    user = User.objects.get(username=username)
    print(username, user.first_name, user.last_name, user.email)
    context = {
        'total_amount': 100,
        'first_name': user.first_name,
        'last_name': user.last_name,
        'email': user.email
    }
    return render(request, 'checkout.html', context)

@login_required
def payment_successful(request):
    return render(request, 'payment_successful.html')
