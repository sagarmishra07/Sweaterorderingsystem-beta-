from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth

# Create your views here.

def login(request):
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']

		user = auth.authenticate(username=username, password=password)
		if user is None:
			messages.warning(request, 'Invalid')
			return render(request, 'login.html')	
		
		
		elif user.is_authenticated and user.is_superuser == False:
			auth.login(request, user)
			return redirect("/order")
		
		elif user.is_authenticated and user.is_superuser == True:
			
			auth.login(request, user)
			return redirect("orderdetails")
		
		else:

		
			return render(request, 'login.html')	

			
	
	else:
			
		return render(request, 'login.html')



def register(request):
	if request.method == 'POST':
		phone = request.POST['first_name']
		location = request.POST['last_name']
		username = request.POST['username']
		password1 = request.POST['password1']
		password2 = request.POST['password2']
		email = request.POST['email']
		if password1 == password2:
			if User.objects.filter(username=username).exists():
				messages.info(request, 'Username taken')
				return render(request, 'register.html')	
			else:
				user = User.objects.create_user(username=username, password=password1, email=email, first_name=phone, last_name=location)
				user.save()
				messages.warning(request, 'Account created')		
				return redirect('/')
		else:
			messages.info(request, 'password not matching')
			return render(request, 'register.html')		
	else:
		return render(request, 'register.html')

def logout(request):
	auth.logout(request)
	return redirect('/')
	
