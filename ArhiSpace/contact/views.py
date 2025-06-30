from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.



def contact_view(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        message = request.POST['message']

        full_message = f"Mesaj de la {name} ({email}):\n\n{message}"

        send_mail(
            subject="Formular Contact - Arhispace",
            message=full_message,
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[settings.DEFAULT_FROM_EMAIL],
        )

        return render(request, 'contact/index.html', {'success': True})

    return render(request, 'contact/index.html')