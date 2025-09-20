from django.shortcuts import render
from urllib3 import request
# from .models import EstimarePret
# from .forms import EstimarePretForm

# Create your views here.

def plans_view(request):

    context = {
    }
    return render(request, "plans/estimare.html", context)


# def estimeaza_pret(suprafata, include_tva=True):
#     TVA = 0.21 

#     if suprafata <= 37:
#         cost_mp = 13.43
#         plan = "Plan Compact"
#     elif suprafata <= 186:
#         cost_mp = 3.75
#         plan = "Plan Mediu"
#     elif suprafata <= 372:
#         cost_mp = 2.41
#         plan = "Plan Mare"
#     else:
#         raise ValueError("Suprafața depășește limitele planurilor definite (maxim 372 m²).")

#     cost_total = suprafata * cost_mp
#     if include_tva:
#         cost_total *= (1 + TVA)

#     return round(cost_total, 2), plan

# def estimare_view(request):
#     rezultat = None
#     plan = None
#     if request.method == "POST":
#         form = EstimarePretForm(request.POST)
#         if form.is_valid():
#             suprafata = form.cleaned_data["suprafata"]
#             rezultat, plan = estimeaza_pret(suprafata)
#             EstimarePret.objects.create(
#                 suprafata=suprafata,
#                 rezultat=rezultat,
#                 plan=plan
#             )
#     else:
#         form = EstimarePretForm()
    
#     context = {
#         "form": form,
#         "rezultat": rezultat,
#         "plan": plan
#     }
#     return render(request, "plans/estimare.html", context)

# def estimare_view(request):
#     rezultat = None
#     if request.method == "POST":
#         form = EstimarePretForm(request.POST)
#         if form.is_valid():
#             suprafata = form.cleaned_data["suprafata"]
#             rezultat = estimeaza_pret(suprafata)
#     else:
#         form = EstimarePretForm()
    
#     return render(request, "estimare.html", {"form": form, "rezultat": rezultat})