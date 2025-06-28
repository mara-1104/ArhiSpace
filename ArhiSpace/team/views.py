from django.shortcuts import render

# Create your views here.

def team_view(request):
	context = {}
	return render(request, 'team/index.html', context)
