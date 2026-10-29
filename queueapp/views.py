

from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Max
from .models import Service, QueueToken


def home(request):
    services = Service.objects.filter(is_active=True)
    return render(request, 'queueapp/home.html', {
        'services': services
    })


@login_required
def book_token(request, service_id):
    if request.method != 'POST':
        return redirect('home')

    service = Service.objects.filter(
        id=service_id,
        is_active=True
    ).first()

    if service is None:
        messages.error(request, 'Service not available.')
        return redirect('home')

    last_token = QueueToken.objects.filter(
        service=service
    ).aggregate(Max('token_number'))['token_number__max']

    next_number = (last_token or 0) + 1

    token = QueueToken.objects.create(
        user=request.user,
        service=service,
        token_number=next_number
    )

    return render(request, 'queueapp/token_success.html', {
        'token': token
    })
