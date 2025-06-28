from django.shortcuts import render

# Create your views here.

def contact_view(request):
	context = {}
	return render(request, 'contact/index.html', context)
