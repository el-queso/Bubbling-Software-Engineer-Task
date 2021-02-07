from django.shortcuts import render
from .models import Profile
# Create your views here.

def profile_create_view(request):
	form = ProfileForm(request.POST or None)
	if form.is_valid():
		form.save()
	context = {
		'form' : form

	}
	return render(request, "profiles/profile_create.html", context)



def profile_detail_view(request):
	obj = Profile.objects.get(id=1)
	# context = {
	# 	'title' : obj.title,
	# 	'description' : obj.description
	# }
	context = {
		'object' : obj

	}
	return render(request, "profiles/detail.html", context)