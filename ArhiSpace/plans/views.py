from django.shortcuts import render

# Create your views here.

def plans_view(request):
	context = {}
	return render(request, 'plans/index.html', context)
