

from BackEnd.models import *






def ProblemDataSet(problemID):
	object=Problems.objects.get(id=problemID.id)
	holds=problems_plateforms.objects.filter(problem_id=problemID.id)
	object.plateforms=[ Plateforms.objects.get(pk=object.plateform_id) for object in holds ]
	holds=problems_datastructures.objects.filter(problem_id=problemID.id)
	object.datastructures=[ DataStructures.objects.get(pk=object.datastructure_id) for object in holds ]
	# object.detailsset=problems_detailssets.objects.filter(problem_id=problemID.id) 		#current_hidden_data 
	return object


def SolutionDataSet(problemID,solutionID):
	object=Solutions.objects.filter(problem_id=problemID.id)[0]
	object.programminglanguages=ProgrammingLanguages.objects.get(pk=object.programminglanguages)
	object.plateforms=Plateforms.objects.get(pk=object.plateforms)
	holds=solutions_datastructures.objects.filter(solution_id=solutionID.id)
	object.datastructures=[ DataStructures.objects.get(pk=object.datastructure_id) for object in holds ]     
	return object





def AddProblems(request):
	comingProblemTitle=request.POST["comingProblemTitle"]
	comingPlateforms=request.POST.getlist("comingPlateforms")
	comingDataStructures=request.POST.getlist("comingDataStructures")
	comingDetails=request.POST["comingDetails"]
	comingTimeComplexity=request.POST["comingTimeComplexity"]
	comingAuxiliarySpace=request.POST["comingAuxiliarySpace"]

	# object = Problems.objects.get(pk=problemID.id)  
	object = Problems()

	if(comingProblemTitle):
		object.title=comingProblemTitle
		object.save()

	if(comingPlateforms):
		object.plateforms=len(comingPlateforms)
		holds = [  str(object.plateform_id) for object in problems_plateforms.objects.filter(problem_id=object.id) ]
		for id in comingPlateforms:
			if(id in holds):
				holds.remove(id)
			else:
				miniobject=problems_plateforms()
				miniobject.problem_id=object
				miniobject.plateform_id=id
				miniobject.save()
		else:
			for id in holds:
				miniobject = problems_plateforms.objects.get(plateform_id=id, problem_id=object.id)
				miniobject.delete()
		object.save()

	if(comingDataStructures):
		object.datastructures=len(comingDataStructures)
		holds = [ str(object.datastructure_id) for object in problems_datastructures.objects.filter(problem_id=object.id) ]
		for id in comingDataStructures:
			if(id in holds):
				holds.remove(id)
			else:
				miniobject=problems_datastructures()
				miniobject.problem_id=object
				miniobject.datastructure_id=id
				miniobject.save()
		else:
			for id in holds:
				miniobject = problems_datastructures.objects.get(datastructure_id=id, problem_id=object.id)
				miniobject.delete()
		object.save()

	if(comingDetails):
		object.detailsset=comingDetails		 		#current_show_data 
		# object.detailsset+=1 								#current_hidden_data 
		# miniobject=problems_detailssets() 		#current_hidden_data 
		# miniobject.problem_id=problemID 		#current_hidden_data 
		# miniobject.detailsset=comingDetails 	#current_hidden_data 
		# miniobject.save() 									#current_hidden_data 
		object.save()

	if(comingTimeComplexity):
		object.timecomplexity=comingTimeComplexity
		object.save()

	if(comingAuxiliarySpace):
		object.auxiliaryspace=comingAuxiliarySpace
		object.save()

	return None
	# return object



def EditProblems(request,problemID):
	comingProblemTitle=request.POST["comingProblemTitle"]
	comingPlateforms=request.POST.getlist("comingPlateforms")
	comingDataStructures=request.POST.getlist("comingDataStructures")
	comingDetails=request.POST["comingDetails"]
	comingTimeComplexity=request.POST["comingTimeComplexity"]
	comingAuxiliarySpace=request.POST["comingAuxiliarySpace"]

	object = Problems.objects.get(pk=problemID.id)  
	# object = Problems()

	if(comingProblemTitle):
		object.title=comingProblemTitle
		object.save()

	if(comingPlateforms):
		object.plateforms=len(comingPlateforms)
		holds = [  str(object.plateform_id) for object in problems_plateforms.objects.filter(problem_id=object.id) ]
		for id in comingPlateforms:
			if(id in holds):
				holds.remove(id)
			else:
				miniobject=problems_plateforms()
				print(object)
				miniobject.problem_id=object
				miniobject.plateform_id=id
				miniobject.save()
		else:
			for id in holds:
				miniobject = problems_plateforms.objects.get(plateform_id=id, problem_id=object.id)
				miniobject.delete()
		object.save()
				
	if(comingDataStructures):
		object.datastructures=len(comingDataStructures)
		holds = [ str(object.datastructure_id) for object in problems_datastructures.objects.filter(problem_id=object.id) ]
		for id in comingDataStructures:
			if(id in holds):
				holds.remove(id)
			else:
				miniobject=problems_datastructures()
				print(object)
				miniobject.problem_id=object
				miniobject.datastructure_id=id
				miniobject.save()
		else:
			for id in holds:
				miniobject = problems_datastructures.objects.get(datastructure_id=id, problem_id=object.id)
				miniobject.delete()
		object.save()

	if(comingDetails):
		object.detailsset=comingDetails		 		#current_show_data 
		# object.detailsset+=1 								#current_hidden_data 
		# miniobject=problems_detailssets() 		#current_hidden_data 
		# miniobject.problem_id=problemID 		#current_hidden_data 
		# miniobject.detailsset=comingDetails 	#current_hidden_data 
		# miniobject.save() 									#current_hidden_data 
		object.save()

	if(comingTimeComplexity):
		object.timecomplexity=comingTimeComplexity
		object.save()

	if(comingAuxiliarySpace):
		object.auxiliaryspace=comingAuxiliarySpace
		object.save()

	return None
	# return object


def AddSolutions(request):
	comingProblemID= problemID.id; #request.POST["comingProblemID"]
	comingDataStructures=request.POST.getlist("comingDataStructures")
	comingProgrammingLanguage=request.POST["comingProgrammingLanguage"]
	comingPlateforms=request.POST["comingPlateforms"]
	comingTimeComplexity=request.POST["comingTimeComplexity"]
	comingAuxiliarySpace=request.POST["comingAuxiliarySpace"]
	comingCodeSubmissions=request.POST["comingCodeSubmissions"]

	object=Solutions()
	# object=Solutions.objects.get(pk=1) 

	object.problem_id=problemID
	object.codesubmissions=comingCodeSubmissions
	object.save()

	if(comingProgrammingLanguage):
		object.programminglanguages=comingProgrammingLanguage
		object.save()

	if(comingPlateforms):
		object.plateforms=comingPlateforms
		object.save()

	if(comingTimeComplexity):
		object.timecomplexity=comingTimeComplexity
		object.save()

	if(comingAuxiliarySpace):
		object.auxiliaryspace=comingAuxiliarySpace
		object.save()

	# must that you putted any one data-structure...
	if(comingDataStructures):
		object.datastructures=len(comingDataStructures)
		holds = [ str(object.datastructure_id) for object in solutions_datastructures.objects.filter(solution_id=object.id) ]
		for id in comingDataStructures:
			if(id in holds):
				holds.remove(id)
			else:
				miniobject=solutions_datastructures()
				miniobject.solution_id=object
				miniobject.datastructure_id=id
				miniobject.save()
		else:
			for id in holds:
				miniobject = solutions_datastructures.objects.get(datastructure_id=id, solution_id=object.id)
				miniobject.delete()
		object.save()

	return None
	# return object


def EditSolutions(request,problemID):
	comingProblemID= problemID.id; #request.POST["comingProblemID"]
	comingDataStructures=request.POST.getlist("comingDataStructures")
	comingProgrammingLanguage=request.POST["comingProgrammingLanguage"]
	comingPlateforms=request.POST["comingPlateforms"]
	comingTimeComplexity=request.POST["comingTimeComplexity"]
	comingAuxiliarySpace=request.POST["comingAuxiliarySpace"]
	comingCodeSubmissions=request.POST["comingCodeSubmissions"]

	# object=Solutions()
	object=Solutions.objects.get(pk=1) 

	object.problem_id=problemID
	object.codesubmissions=comingCodeSubmissions
	object.save()

	if(comingProgrammingLanguage):
		object.programminglanguages=comingProgrammingLanguage
		object.save()

	if(comingPlateforms):
		object.plateforms=comingPlateforms
		object.save()

	if(comingTimeComplexity):
		object.timecomplexity=comingTimeComplexity
		object.save()

	if(comingAuxiliarySpace):
		object.auxiliaryspace=comingAuxiliarySpace
		object.save()

	# must that you putted any one data-structure...
	if(comingDataStructures):
		object.datastructures=len(comingDataStructures)
		holds = [ str(object.datastructure_id) for object in solutions_datastructures.objects.filter(solution_id=object.id) ]
		for id in comingDataStructures:
			if(id in holds):
				holds.remove(id)
			else:
				miniobject=solutions_datastructures()
				miniobject.solution_id=object
				miniobject.datastructure_id=id
				miniobject.save()
		else:
			for id in holds:
				miniobject = solutions_datastructures.objects.get(datastructure_id=id, solution_id=object.id)
				miniobject.delete()
		object.save()

	return None
	# return object














# def index(request):
	# return HttpResponse("Hey <b>Shivam Shukla</b>, <b style='font-size:10px'>N your url '@theshivashu07'</b> !!!");

'''
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
			# object=Solutions()
			object=Solutions.objects.get(pk=1) 
			object.problem_id=problemID
			object.codesubmissions=comingCodeSubmissions
			object.save()
			if(comingProgrammingLanguage):
				object.programminglanguages=comingProgrammingLanguage
			if(comingPlateforms):
				object.plateforms=comingPlateforms
			if(comingTimeComplexity):
				object.timecomplexity=comingTimeComplexity
			if(comingAuxiliarySpace):
				object.auxiliaryspace=comingAuxiliarySpace
			object.save()
			# must that you putted any one data-structure...
			if(comingDataStructures):
				object.datastructures=len(comingDataStructures)
				holds = [ str(object.datastructure_id) for object in solutions_datastructures.objects.filter(solution_id=object.id) ]
				for id in comingDataStructures:
					if(id in holds):
						holds.remove(id)
					else:
						miniobject=solutions_datastructures()
						miniobject.solution_id=object
						miniobject.datastructure_id=id
						miniobject.save()
				else:
					for id in holds:
						object = solutions_datastructures.objects.get(datastructure_id=id, solution_id=object.id)
						object.delete()
				object.save()
		return redirect("/codecollections/codesubmissions/")

	object=Problems.objects.get(id=problemID.id)
	holds=problems_plateforms.objects.filter(problem_id=problemID.id)
	object.plateforms=[ Plateforms.objects.get(pk=object.plateform_id) for object in holds ]
	holds=problems_datastructures.objects.filter(problem_id=problemID.id)
	object.datastructures=[ DataStructures.objects.get(pk=object.datastructure_id) for object in holds ]
	object.detailsset=problems_detailssets.objects.filter(problem_id=problemID.id)
	SenderDatasets={
		'DataSet':object,
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
				object = Problems.objects.get(pk=problemID.id)  #Problems()
				# object = Problems()
				if(comingProblemTitle):
					object.title=comingProblemTitle
				if(comingPlateforms):
					object.plateforms=len(comingPlateforms)
					holds = [  str(object.plateform_id) for object in problems_plateforms.objects.filter(problem_id=problemID.id) ]
					for id in comingPlateforms:
						if(id in holds):
							holds.remove(id)
						else:
							miniobject=problems_plateforms()
							miniobject.problem_id=problemID
							miniobject.plateform_id=id
							miniobject.save()
					else:
						for id in holds:
							object = problems_plateforms.objects.get(plateform_id=id, problem_id=problemID.id)
							object.delete()
				if(comingDataStructures):
					object.datastructures=len(comingDataStructures)
					holds = [ str(object.datastructure_id) for object in problems_datastructures.objects.filter(problem_id=problemID.id) ]
					for id in comingDataStructures:
						if(id in holds):
							holds.remove(id)
						else:
							miniobject=problems_datastructures()
							miniobject.problem_id=problemID
							miniobject.datastructure_id=id
							miniobject.save()
					else:
						for id in holds:
							object = problems_datastructures.objects.get(datastructure_id=id, problem_id=problemID.id)
							object.delete()

				object.save()

		elif(comingFrom=='problem_mid'):
			comingDetails=request.POST["comingDetails"]
			comingTimeComplexity=request.POST["comingTimeComplexity"]
			comingAuxiliarySpace=request.POST["comingAuxiliarySpace"]
			if(comingDetails or comingTimeComplexity or comingAuxiliarySpace):
				object = Problems.objects.get(pk=problemID.id)  #Problems()
				# object = Problems()
				if(comingDetails):
					object.detailsset+=1
					miniobject=problems_detailssets()
					miniobject.problem_id=problemID
					miniobject.detailsset=comingDetails
					miniobject.save()
				if(comingTimeComplexity):
					object.timecomplexity=comingTimeComplexity
				if(comingAuxiliarySpace):
					object.auxiliaryspace=comingAuxiliarySpace
				object.save()
		else:
			print("Choosen Else!!!")
		return redirect("/codecollections/problemsubmissions/")
	object=Problems.objects.get(id=problemID.id)
	holds=problems_plateforms.objects.filter(problem_id=problemID.id)
	object.plateforms=[ Plateforms.objects.get(pk=object.plateform_id) for object in holds ]
	holds=problems_datastructures.objects.filter(problem_id=problemID.id)
	object.datastructures=[ DataStructures.objects.get(pk=object.datastructure_id) for object in holds ]
	object.detailsset=problems_detailssets.objects.filter(problem_id=problemID.id)
	SenderDatasets={
		'DataSet':object,
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
			miniobject=Plateforms()
			miniobject.name=comingData;
			miniobject.save()
		elif(comingFrom=='DataStructure'):
			miniobject=DataStructures()
			miniobject.name=comingData;
			miniobject.save()
		elif(comingFrom=='ProgrammingLanguage'):
			miniobject=ProgrammingLanguages()
			miniobject.name=comingData;
			miniobject.save()
		else:
			print("Go to somewhere else.....")
		return redirect("/codecollections/edittables/")
	SenderDatasets={
		'Plateforms':Plateforms.objects.all(),
		'DataStructures':DataStructures.objects.all(),
		'ProgrammingLanguages':ProgrammingLanguages.objects.all(),
	}
	return render(request,"otherapps/codecollections/edittables.html", SenderDatasets);'''


'''

BULK - DATA - ASSIGNMENT

	if request.method=="POST":
		for key in _importantdatasets.Plateforms:
			object=Plateforms()
			object.name=key
			object.save()
		count=0
		for key in _importantdatasets.DataStructures:
			count+=1
			if(count==15):
				break;
			object=DataStructures()
			object.name=key
			object.save()
		for key in _importantdatasets.ProgrammingLanguages:
			object=ProgrammingLanguages()
			object.name=key
			object.save()
		return redirect("/codecollections/edittables/")
'''







