from django.shortcuts import render
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from .models import BagEntry


def bag_view(request):
    context = {}

    if request.GET.get("clear_bag"):
        request.session.pop("selected_plan", None)

    if request.method == "POST":
        plan = request.POST.get("plan") or request.session.get("selected_plan")
        email = request.POST.get("email")
        phone = request.POST.get("phone")

        if plan and not email and not phone:
            request.session["selected_plan"] = plan
            context["plan"] = plan
            return render(request, "bag/index.html", context)
        
        if email and phone:
            context["plan"] = plan
            context["email"] = email
            context["phone"] = phone

            if not plan:
                context["error"] = "Selectați un plan înainte de a trimite formularul."
                return render(request, "bag/index.html", context)

            try:
                validate_email(email)
            except ValidationError:
                context["error"] = "Email invalid."
                return render(request, "bag/index.html", context)

            if len(phone.replace(" ", "")) < 9:
                context["error"] = "Număr de telefon invalid."
                return render(request, "bag/index.html", context)

            BagEntry.objects.create(plan=plan, email=email, phone=phone)

            request.session.pop("selected_plan", None)
            context.clear()
            context["success"] = True
            return render(request, "bag/index.html", context)

        context["error"] = "Completați toate câmpurile."
        context["plan"] = plan
        context["email"] = email
        context["phone"] = phone
        return render(request, "bag/index.html", context)

    else:
        context["plan"] = request.session.get("selected_plan")
        return render(request, "bag/index.html", context)
