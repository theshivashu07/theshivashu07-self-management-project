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
		'Tagged':{
			'TaggedProblemTitle' : _importantdatasets.TaggedProblemTitle,
			'TaggedPlateforms' : _importantdatasets.TaggedPlateforms,
			'TaggedDataStructures' : _importantdatasets.TaggedDataStructures,
			'TaggedDetails' : _importantdatasets.TaggedDetails,
			'TaggedTimeComplexity' : _importantdatasets.TaggedTimeComplexity,
			'TaggedAuxiliarySpace' : _importantdatasets.TaggedAuxiliarySpace,
		}
	}


def index(request):
	return render(request,"otherapps/codecollections/index.html");


def codesubmissions(request):
	return render(request,"otherapps/codecollections/codesubmissions.html", SenderDatasets);

def problemsubmissions(request):
	if request.method=="POST":
		comingFrom=request.POST["comingFrom"]
		if(comingFrom=='problem_head'):
			comingProblemTitle=request.POST["comingProblemTitle"]
			comingPlateforms=request.POST.getlist("comingPlateforms")
			comingDataStructures=request.POST.getlist("comingDataStructures")
			# print('comingProblemTitle:',comingProblemTitle,'  |  ','comingPlateforms:',comingPlateforms,'  |  ','comingDataStructures:',comingDataStructures)
			if(comingProblemTitle):
				SenderDatasets['Tagged']['TaggedProblemTitle']=comingProblemTitle
			if(comingPlateforms):
				SenderDatasets['Tagged']['TaggedPlateforms']=comingPlateforms
			if(comingDataStructures):
				SenderDatasets['Tagged']['TaggedDataStructures']=comingDataStructures
		elif(comingFrom=='problem_mid'):
			comingDetails=request.POST["comingDetails"]
			comingTimeComplexity=request.POST["comingTimeComplexity"]
			comingAuxiliarySpace=request.POST["comingAuxiliarySpace"]
			# print('comingDetails:',comingDetails,'  |  ','comingTimeComplexity:',comingTimeComplexity,'  |  ','comingAuxiliarySpace:',comingAuxiliarySpace)
			if(comingDetails):
				SenderDatasets['Tagged']['TaggedDetails'].append(comingDetails)
			if(comingTimeComplexity):
				SenderDatasets['Tagged']['TaggedTimeComplexity']=comingTimeComplexity
			if(comingAuxiliarySpace):
				SenderDatasets['Tagged']['TaggedAuxiliarySpace']=comingAuxiliarySpace
		else:
			print("Choosen Else!!!")
		return redirect("/codecollections/problemsubmissions/")
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
