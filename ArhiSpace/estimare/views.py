from django.shortcuts import render
from .models import EstimarePret
from .forms import EstimarePretForm

def estimeaza_pret(suprafata, include_tva=True):
    TVA = 0.21
    plan = ""
    
    try:
        if suprafata <= 37:
            cost_mp = 13.43
            plan = "Plan Compact"
        elif suprafata <= 186:
            cost_mp = 3.75
            plan = "Plan Mediu"
        elif suprafata <= 372:
            cost_mp = 2.41
            plan = "Plan Mare"
        else:
            raise ValueError("Suprafața depășește limitele planurilor definite (maxim 372 m²).")
        
        cost_total = suprafata * cost_mp
        if include_tva:
            cost_total *= (1 + TVA)
        
        return round(cost_total, 2), plan
    except Exception as e:
        return None, str(e)

def estimare_view(request):
    rezultat = None
    plan = None
    error = None

    if request.method == "POST":
        form = EstimarePretForm(request.POST)
        if form.is_valid():
            suprafata = form.cleaned_data["suprafata"]
            rezultat, plan = estimeaza_pret(suprafata)
            
            if rezultat is not None:
                EstimarePret.objects.create(
                    suprafata=suprafata,
                    rezultat=rezultat,
                    plan=plan
                )
            else:
                error = plan
    else:
        form = EstimarePretForm()
    
    context = {
        "form": form,
        "rezultat": rezultat,
        "plan": plan,
        "error": error
    }
    return render(request, "estimare/index.html", context)
