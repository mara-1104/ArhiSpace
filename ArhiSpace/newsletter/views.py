from django.shortcuts import render
from .models import Subscriber

def newsletter_view(request):
    message = ""
    if request.method == "POST":
        email = request.POST.get("email")
        if email:
            subscriber, created = Subscriber.objects.get_or_create(email=email)
            if created:
                message = "Mulțumim pentru abonare!"
            else:
                message = "Acest email este deja abonat."
        else:
            message = "Te rugăm să introduci un email valid."

    return render(request, "newsletter/index.html", {"message": message})
