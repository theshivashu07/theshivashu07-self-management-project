from django.shortcuts import render,redirect
from django.http import HttpResponse
# Create your views here.




# def index(request):
	# return HttpResponse("Hey <b>Shivam Shukla</b>, <b style='font-size:10px'>N your url '@theshivashu07'</b> !!!");


def index(request):
	return render(request,"backend/index.html");



#########################################################################################



# def index(request):
#	 return render(request,"backend/index.html");

# def index(request):
# 	return render(request,"backend/index.html");

# def index(request):
# 	return render(request,"backend/index.html");

# def index(request):
# 	return render(request,"backend/index.html");







