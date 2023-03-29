from django.shortcuts import render,redirect
from django.http import HttpResponse

from BackEnd.models import *

import codecollections._importantdatasets as _importantdatasets
# Create your views here.


problemID=Problems.objects.get(pk=1)
solutionID=Solutions.objects.get(pk=1)




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
	if request.method=="POST":
		comingProblemID= problemID.id; #request.POST["comingProblemID"]
		comingDataStructures=request.POST.getlist("comingDataStructures")
		comingProgrammingLanguage=request.POST["comingProgrammingLanguage"]
		comingPlateforms=request.POST["comingPlateforms"]
		comingTimeComplexity=request.POST["comingTimeComplexity"]
		comingAuxiliarySpace=request.POST["comingAuxiliarySpace"]
		comingCodeSubmissions=request.POST["comingCodeSubmissions"]
		# print(comingDataStructures, comingProgrammingLanguage, comingPlateforms, comingTimeComplexity, comingAuxiliarySpace, comingCodeSubmissions)
		if(comingCodeSubmissions):
			# locks=Solutions()
			locks=Solutions.objects.get(pk=1) 
			locks.problem_id=problemID
			locks.codesubmissions=comingCodeSubmissions
			locks.save()
			if(comingProgrammingLanguage):
				locks.programminglanguages=comingProgrammingLanguage
			if(comingPlateforms):
				locks.plateforms=comingPlateforms
			if(comingTimeComplexity):
				locks.timecomplexity=comingTimeComplexity
			if(comingAuxiliarySpace):
				locks.auxiliaryspace=comingAuxiliarySpace
			locks.save()
			# must that you putted any one data-structure...
			if(comingDataStructures):
				locks.datastructures=len(comingDataStructures)
				holds = [ str(object.datastructure_id) for object in solutions_datastructures.objects.filter(solution_id=locks.id) ]
				for id in comingDataStructures:
					if(id in holds):
						holds.remove(id)
					else:
						lock=solutions_datastructures()
						lock.solution_id=locks
						lock.datastructure_id=id
						lock.save()
				else:
					for id in holds:
						object = solutions_datastructures.objects.get(datastructure_id=id, solution_id=locks.id)
						object.delete()
				locks.save()
		return redirect("/codecollections/codesubmissions/")

	locks=Problems.objects.get(id=problemID.id)
	holds=problems_plateforms.objects.filter(problem_id=problemID.id)
	locks.plateforms=[ Plateforms.objects.get(pk=object.plateform_id) for object in holds ]
	holds=problems_datastructures.objects.filter(problem_id=problemID.id)
	locks.datastructures=[ DataStructures.objects.get(pk=object.datastructure_id) for object in holds ]
	locks.detailsset=problems_detailssets.objects.filter(problem_id=problemID.id)
	SenderDatasets={
		'DataSet':locks,
		'Plateforms':Plateforms.objects.all(),
		'DataStructures':DataStructures.objects.all(),
		'ProgrammingLanguages':ProgrammingLanguages.objects.all(),
	}
	return render(request,"otherapps/codecollections/codesubmissions.html", SenderDatasets);


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
					holds = [  str(object.plateform_id) for object in problems_plateforms.objects.filter(problem_id=problemID.id) ]
					for id in comingPlateforms:
						if(id in holds):
							holds.remove(id)
						else:
							lock=problems_plateforms()
							lock.problem_id=problemID
							lock.plateform_id=id
							lock.save()
					else:
						for id in holds:
							object = problems_plateforms.objects.get(plateform_id=id, problem_id=problemID.id)
							object.delete()
				if(comingDataStructures):
					locks.datastructures=len(comingDataStructures)
					holds = [ str(object.datastructure_id) for object in problems_datastructures.objects.filter(problem_id=problemID.id) ]
					for id in comingDataStructures:
						if(id in holds):
							holds.remove(id)
						else:
							lock=problems_datastructures()
							lock.problem_id=problemID
							lock.datastructure_id=id
							lock.save()
					else:
						for id in holds:
							object = problems_datastructures.objects.get(datastructure_id=id, problem_id=problemID.id)
							object.delete()

				locks.save()

		elif(comingFrom=='problem_mid'):
			comingDetails=request.POST["comingDetails"]
			comingTimeComplexity=request.POST["comingTimeComplexity"]
			comingAuxiliarySpace=request.POST["comingAuxiliarySpace"]
			if(comingDetails or comingTimeComplexity or comingAuxiliarySpace):
				locks = Problems.objects.get(pk=problemID.id)  #Problems()
				# locks = Problems()
				if(comingDetails):
					locks.detailsset+=1
					lock=problems_detailssets()
					lock.problem_id=problemID
					lock.detailsset=comingDetails
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
	holds=problems_plateforms.objects.filter(problem_id=problemID.id)
	locks.plateforms=[ Plateforms.objects.get(pk=object.plateform_id) for object in holds ]
	holds=problems_datastructures.objects.filter(problem_id=problemID.id)
	locks.datastructures=[ DataStructures.objects.get(pk=object.datastructure_id) for object in holds ]
	locks.detailsset=problems_detailssets.objects.filter(problem_id=problemID.id)
	SenderDatasets={
		'DataSet':locks,
		'Plateforms':Plateforms.objects.all(),
		'DataStructures':DataStructures.objects.all(),
		'ProgrammingLanguages':ProgrammingLanguages.objects.all(),
	}
	return render(request,"otherapps/codecollections/problemsubmissions.html", SenderDatasets);


def edittables(request):
	if request.method=="POST":
		comingFrom=request.POST["comingFrom"]
		comingData=request.POST["comingData"]
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




