from django.shortcuts import render

# Create your views here.

def team_view(request):
	context = {'team_members' : team_members}
	return render(request, 'team/index.html', context)

team_members = [
	{
		'name' : 'Cosmin Florin Brezeanu',
		'role' : 'Director General',
		'photo' : 'images/male.png'
	},

	{
		'name' : 'Andrei Ștefan Gagiu',
		'role' : 'Director Marketing',
		'photo' : 'images/male.png'
	},

	{
		'name' : 'Vlad Cristian Mogîlă',
		'role' : 'Director Tehnic',
		'photo' : 'images/male.png'
	},

	{
		'name' : 'Valentina Maria Pătrașcu',
		'role' : 'Director Vânzări',
		'photo' : 'images/female.png'
	},

	{
		'name' : 'Tudor Brătucu',
		'role' : 'Contabil Șef',
		'photo' : 'images/male.png'
	},

	{
		'name' : 'Sebastian Ștefan Sîrboiu',
		'role' : 'Administrator',
		'photo' : 'images/male.png'
	},

	{
		'name' : 'Sergiu Alexis Adamov',
		'role' : 'Contabil',
		'photo' : 'images/male.png'
	}
]