from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout


def home(request) :
	if request.user.is_authenticated():
		logged_in = true
	else:
		logged_in = false

	return render(request, 'home.html', {'logged_in' : logged_in})

def login(request) :
	username = request.POST['username']
	password = request.POST['password']
	user = authenticate(username=username, password=password)

	if user is not None :
		if user.is_active:
			login(request, user)
			# redirect to a success page
		else:
			# return "disabled account"
	else:
		# return "invalid login"

def logout_view(request):
    logout(request)