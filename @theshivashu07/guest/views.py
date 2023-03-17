from django.shortcuts import render,redirect
from django.http import HttpResponse




# def index(request):
	# return HttpResponse("Hey <b>Shivam Shukla</b>, <b style='font-size:10px'>N your url '@theshivashu07'</b> !!!");


def index(request):
	return render(request,"guest/index.html");

def services(request):
	return render(request,"guest/services.html");

def projects2(request):
	return render(request,"guest/projects-2.html");

def projects3(request):
	return render(request,"guest/projects-3.html");

def projectdetails(request):
	return render(request,"guest/project-details.html");

def blog(request):
	return render(request,"guest/blog.html");

def blogsingle(request):
	return render(request,"guest/blog-single.html");

def ourteam(request):
	return render(request,"guest/our-team.html");

def archives(request):
	return render(request,"guest/archives.html");

def grids(request):
	return render(request,"guest/grids.html");

def error404(request):
	return render(request,"guest/404.html");

def contact(request):
	return render(request,"guest/contact.html");



#########################################################################################



def index(request):
	return render(request,"guest/_index.html");

# def index(request):
# 	return render(request,"guest/index.html");

# def index(request):
# 	return render(request,"guest/index.html");

# def index(request):
# 	return render(request,"guest/index.html");







