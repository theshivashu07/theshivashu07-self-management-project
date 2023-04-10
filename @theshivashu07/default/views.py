from django.shortcuts import render,redirect
from django.http import HttpResponse




# def index(request):
	# return HttpResponse("Hey <b>Shivam Shukla</b>, <b style='font-size:10px'>N your url '@theshivashu07'</b> !!!");


def index(request):
	return render(request,"default/index.html");

def services(request):
	return render(request,"default/services.html");

def projects2(request):
	return render(request,"default/projects-2.html");

def projects3(request):
	return render(request,"default/projects-3.html");

def projectdetails(request):
	return render(request,"default/project-details.html");

def blog(request):
	return render(request,"default/blog.html");

def blogsingle(request):
	return render(request,"default/blog-single.html");

def ourteam(request):
	return render(request,"default/our-team.html");

def archives(request):
	return render(request,"default/archives.html");

def grids(request):
	return render(request,"default/grids.html");

def error404(request):
	return render(request,"default/404.html");

def contact(request):
	return render(request,"default/contact.html");



#########################################################################################



# def index(request):
#	 return render(request,"default/index.html");

# def index(request):
# 	return render(request,"default/index.html");

# def index(request):
# 	return render(request,"default/index.html");

# def index(request):
# 	return render(request,"default/index.html");







