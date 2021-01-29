from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home_view(request, *args, **kwargs): # *args, **kwargs
	print (args, kwargs)
	print (request.user)
	#return HttpResponse("<h1>Home Page</h1>") # string of HTML code not HTML CODE
	return render(request, "home.html", {})

def contact_view(request, *args, **kwargs):
	return render(request, "contact.html", {})

def about_view(request, *args, **kwargs):
 	my_context = {
 		"my_text" : "This is a text",
 		"my_number" : 123,
 		"my_list" : [1, 2, 3 ,4]

 	}
 	return render(request, "about.html", my_context)

def social_view(request, *args, **kwargs):
	return render(request, "social.html", {})
