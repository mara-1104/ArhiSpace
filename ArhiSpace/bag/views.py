from django.shortcuts import render, redirect
from .models import BagEntry

def bag_view(request):
    if request.method == "POST":
        if "plan" in request.POST and "email" not in request.POST:
            # Step 1: User selected a plan
            plan = request.POST.get("plan")
            request.session["selected_plan"] = plan
            return render(request, "bag/index.html", {"plan": plan})
        else:
            # Step 2: User submits email & phone
            email = request.POST.get("email")
            phone = request.POST.get("phone")
            plan = request.session.get("selected_plan")

            if plan and email and phone:
                # Save data to DB
                BagEntry.objects.create(plan=plan, email=email, phone=phone)

                # Clear session
                request.session.pop("selected_plan", None)

                # Redirect to homepage after submission
                return redirect("/")  # Homepage

            else:
                # Missing data
                return render(request, "bag/index.html", {
                    "plan": plan,
                    "error": "Completați toate câmpurile."
                })
    else:
        # Prevent direct access
        return redirect("/")
