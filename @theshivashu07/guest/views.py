from django.shortcuts import render,redirect
from django.http import HttpResponse
# Create your views here.




# def index(request):
	# return HttpResponse("Hey <b>Shivam Shukla</b>, <b style='font-size:10px'>N your url '@theshivashu07'</b> !!!");


def index(request):
	return render(request,"guest/index.html");

def profile_metaverse(request):
	return render(request,"guest/404.html");

def study_center(request):
	return render(request,"guest/404.html");

#def code_collections(request):
#	return render(request,"guest/404.html");

def daily_routines(request):
	return render(request,"guest/404.html");

def enjoy_sections(request):
	return render(request,"guest/404.html");




#########################################################################################



# def index(request):
#	 return render(request,"guest/index.html");

# def index(request):
# 	return render(request,"guest/index.html");

# def index(request):
# 	return render(request,"guest/index.html");

# def index(request):
# 	return render(request,"guest/index.html");







