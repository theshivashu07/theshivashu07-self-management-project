from django.shortcuts import render,redirect
from django.http import HttpResponse

from BackEnd.models import *

import codecollections._importantdatasets as _importantdatasets
# Create your views here.


problemID=Problems.objects.get(pk=1)




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


def problemsubmissions(request):
	if request.method=="POST":
		comingFrom=request.POST["comingFrom"]
		if(comingFrom=='problem_head'):
			comingProblemTitle=request.POST["comingProblemTitle"]
			comingPlateforms=request.POST.getlist("comingPlateforms")
			comingDataStructures=request.POST.getlist("comingDataStructures")
			if(comingProblemTitle or comingPlateforms or comingDataStructures):
				locks = Problems.objects.get(pk=problemID.id)  #Problems()
				# locks = Problems()
				if(comingProblemTitle):
					locks.title=comingProblemTitle
				if(comingPlateforms):
					locks.plateforms=len(comingPlateforms)
					for id in comingPlateforms:
						lock=problems_plateforms()
						lock.problem_id=problemID
						lock.plateform_id=id
						lock.save()
				if(comingDataStructures):
					locks.datastructures=len(comingDataStructures)
					for id in comingDataStructures:
						lock=problems_datastructures()
						lock.problem_id=problemID
						lock.datastructure_id=id
						lock.save()
				locks.save()
		elif(comingFrom=='problem_mid'):
			comingDetails=request.POST["comingDetails"]
			comingTimeComplexity=request.POST["comingTimeComplexity"]
			comingAuxiliarySpace=request.POST["comingAuxiliarySpace"]
			if(comingDetails or comingTimeComplexity or comingAuxiliarySpace):
				locks = Problems.objects.get(pk=problemID)  #Problems()
				# locks = Problems()
				if(comingDetails):
					locks.detailsset+=1
					lock=problems_detailssets()
					lock.problem_id=problemID
					lock.detailsset=detailsset
					lock.save()
				if(comingTimeComplexity):
					locks.timecomplexity=comingTimeComplexity
				if(comingAuxiliarySpace):
					locks.auxiliaryspace=comingAuxiliarySpace
				locks.save()
		else:
			print("Choosen Else!!!")
		return redirect("/codecollections/problemsubmissions/")
	locks=Problems.objects.get(id=problemID.id)
	locks.plateforms=problems_plateforms.objects.filter(problem_id=problemID.id)
	for object in locks.plateforms:
		object.plateform_id=Plateforms.objects.get(pk=object.plateform_id).name
		print(object,object.plateform_id,end=' | ')
	print()
	locks.datastructures=problems_datastructures.objects.filter(problem_id=problemID.id)
	for object in locks.datastructures:
		object.datastructure_id=DataStructures.objects.get(pk=object.datastructure_id).name
		print(object,object.datastructure_id,end=' | ')
	print()
	locks.detailsset=problems_detailssets.objects.filter(problem_id=problemID.id)
	print(locks.plateforms, locks.datastructures, locks.detailsset)
	SenderDatasets={
		'DataSet':locks,
		'Plateforms':Plateforms.objects.all(),
		'DataStructures':DataStructures.objects.all(),
		'ProgrammingLanguages':ProgrammingLanguages.objects.all(),
	}
	# print(SenderDatasets)
	return render(request,"otherapps/codecollections/problemsubmissions.html", SenderDatasets);


def edittables(request):
	if request.method=="POST":
		comingFrom=request.POST["comingFrom"]
		comingData=request.POST["comingData"]
		print(comingFrom,comingData)
		if(comingFrom=='Plateform'):
			lock=Plateforms()
			lock.name=comingData;
			lock.save()
		elif(comingFrom=='DataStructure'):
			lock=DataStructures()
			lock.name=comingData;
			lock.save()
		elif(comingFrom=='ProgrammingLanguage'):
			lock=ProgrammingLanguages()
			lock.name=comingData;
			lock.save()
		else:
			print("Go to somewhere else.....")
		return redirect("/codecollections/edittables/")
	SenderDatasets={
		'Plateforms':Plateforms.objects.all(),
		'DataStructures':DataStructures.objects.all(),
		'ProgrammingLanguages':ProgrammingLanguages.objects.all(),
	}
	return render(request,"otherapps/codecollections/edittables.html", SenderDatasets);


'''

BULK - DATA - ASSIGNMENT

	if request.method=="POST":
		for key in _importantdatasets.Plateforms:
			locks=Plateforms()
			locks.name=key
			locks.save()
		count=0
		for key in _importantdatasets.DataStructures:
			count+=1
			if(count==15):
				break;
			locks=DataStructures()
			locks.name=key
			locks.save()
		for key in _importantdatasets.ProgrammingLanguages:
			locks=ProgrammingLanguages()
			locks.name=key
			locks.save()
		return redirect("/codecollections/edittables/")
'''




