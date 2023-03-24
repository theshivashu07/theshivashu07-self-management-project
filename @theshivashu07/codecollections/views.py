from django.shortcuts import render,redirect
from django.http import HttpResponse

import codecollections._importantdatasets as _importantdatasets
# Create your views here.



# def index(request):
	# return HttpResponse("Hey <b>Shivam Shukla</b>, <b style='font-size:10px'>N your url '@theshivashu07'</b> !!!");


SenderDatasets={
		'DataStructures':_importantdatasets.DataStructures,
		'Plateforms':_importantdatasets.Plateforms,
		'ProgrammingLanguages':_importantdatasets.ProgrammingLanguages,
	}

def index(request):
	return render(request,"otherapps/codecollections/index.html");

def codesubmissions(request):
	return render(request,"otherapps/codecollections/codesubmissions.html", SenderDatasets);

def problemsubmissions(request):
	return render(request,"otherapps/codecollections/problemsubmissions.html", SenderDatasets);

def edittables(request):
	print(request)
	if request.method=="POST":
		comingFrom=request.POST["comingFrom"]
		comingData=request.POST["comingData"]
		# print("comingFrom",comingFrom,"     ","comingData",comingData)
		hold=SenderDatasets[comingFrom+'s']
		hold[comingData]=None
		SenderDatasets[comingFrom+'s']=hold
		# return redirect("/codecollections/edittables/")
	return render(request,"otherapps/codecollections/edittables.html", SenderDatasets);


'''
	if request.method=="POST":
		values=ProjectInfo(
						Client=request.POST["clientID"],
'''
