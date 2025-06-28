from django.shortcuts import render

# Create your views here.

def about_view(request):
	context = {}
	return render(request, 'about/index.html', context)
