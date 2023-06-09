

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
	# when you want to ADD Problems...
	ProblemsTitle=request.POST["ProblemsTitle"]
	ProblemsPlateforms=request.POST.getlist("ProblemsPlateforms")
	ProblemsDataStructures=request.POST.getlist("ProblemsDataStructures")
	ProblemsDetailSet=request.POST["ProblemsDetailSet"]
	ProblemsTimeComplexity=request.POST["ProblemsTimeComplexity"]
	ProblemsAuxiliarySpace=request.POST["ProblemsAuxiliarySpace"]

	# object = Problems.objects.get(pk=problemID.id)  
	object = Problems()

	if(ProblemsTitle):
		object.title=ProblemsTitle
		object.save()

	if(ProblemsPlateforms):
		object.plateforms=len(ProblemsPlateforms)
		holds = [  str(object.plateform_id) for object in problems_plateforms.objects.filter(problem_id=object.id) ]
		for id in ProblemsPlateforms:
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

	if(ProblemsDataStructures):
		object.datastructures=len(ProblemsDataStructures)
		holds = [ str(object.datastructure_id) for object in problems_datastructures.objects.filter(problem_id=object.id) ]
		for id in ProblemsDataStructures:
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

	if(ProblemsDetailSet):
		object.detailsset=ProblemsDetailSet
		object.save()

	if(ProblemsTimeComplexity):
		object.timecomplexity=ProblemsTimeComplexity
		object.save()

	if(ProblemsAuxiliarySpace):
		object.auxiliaryspace=ProblemsAuxiliarySpace
		object.save()

	return None
	# return object



def EditProblems(request,problemID):
	# when you want to EDIT Problems...
	ProblemsTitle=request.POST["ProblemsTitle"]
	ProblemsPlateforms=request.POST.getlist("ProblemsPlateforms")
	ProblemsDataStructures=request.POST.getlist("ProblemsDataStructures")
	ProblemsDetailSet=request.POST["ProblemsDetailSet"]
	ProblemsTimeComplexity=request.POST["ProblemsTimeComplexity"]
	ProblemsAuxiliarySpace=request.POST["ProblemsAuxiliarySpace"]

	object = Problems.objects.get(pk=problemID.id)  
	# object = Problems()

	if(ProblemsTitle):
		object.title=ProblemsTitle
		object.save()

	if(ProblemsPlateforms):
		object.plateforms=len(ProblemsPlateforms)
		holds = [  str(object.plateform_id) for object in problems_plateforms.objects.filter(problem_id=object.id) ]
		for id in ProblemsPlateforms:
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
				
	if(ProblemsDataStructures):
		object.datastructures=len(ProblemsDataStructures)
		holds = [ str(object.datastructure_id) for object in problems_datastructures.objects.filter(problem_id=object.id) ]
		for id in ProblemsDataStructures:
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

	if(ProblemsDetailSet):
		object.detailsset=ProblemsDetailSet
		object.save()

	if(ProblemsTimeComplexity):
		object.timecomplexity=ProblemsTimeComplexity
		object.save()

	if(ProblemsAuxiliarySpace):
		object.auxiliaryspace=ProblemsAuxiliarySpace
		object.save()

	return None
	# return object


def AddSolutions(request,problemID):
	# when you want to ADD Solution...
	SolutionsDataStructures=request.POST.getlist("SolutionsDataStructures")
	SolutionsProgrammingLanguage=request.POST["SolutionsProgrammingLanguage"]
	SolutionsPlateforms=request.POST["SolutionsPlateforms"]
	SolutionsTimeComplexity=request.POST["SolutionsTimeComplexity"]
	SolutionsAuxiliarySpace=request.POST["SolutionsAuxiliarySpace"]
	SolutionsCodeSubmissions=request.POST["SolutionsCodeSubmissions"]

	object=Solutions()
	# object=Solutions.objects.get(pk=1) 

	object.problem_id=problemID
	object.codesubmissions=SolutionsCodeSubmissions
	object.save()

	if(SolutionsProgrammingLanguage):
		object.programminglanguages=SolutionsProgrammingLanguage
		object.save()

	if(SolutionsPlateforms):
		object.plateforms=SolutionsPlateforms
		object.save()

	if(SolutionsTimeComplexity):
		object.timecomplexity=SolutionsTimeComplexity
		object.save()

	if(SolutionsAuxiliarySpace):
		object.auxiliaryspace=SolutionsAuxiliarySpace
		object.save()

	# must that you putted any one data-structure...
	if(SolutionsDataStructures):
		object.datastructures=len(SolutionsDataStructures)
		holds = [ str(object.datastructure_id) for object in solutions_datastructures.objects.filter(solution_id=object.id) ]
		for id in SolutionsDataStructures:
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
	# when you want to EDIT Solution...
	SolutionsDataStructures=request.POST.getlist("SolutionsDataStructures")
	SolutionsProgrammingLanguage=request.POST["SolutionsProgrammingLanguage"]
	SolutionsPlateforms=request.POST["SolutionsPlateforms"]
	SolutionsTimeComplexity=request.POST["SolutionsTimeComplexity"]
	SolutionsAuxiliarySpace=request.POST["SolutionsAuxiliarySpace"]
	SolutionsCodeSubmissions=request.POST["SolutionsCodeSubmissions"]

	# object=Solutions()
	object=Solutions.objects.get(pk=1) 

	object.problem_id=problemID
	object.codesubmissions=SolutionsCodeSubmissions
	object.save()

	if(SolutionsProgrammingLanguage):
		object.programminglanguages=SolutionsProgrammingLanguage
		object.save()

	if(SolutionsPlateforms):
		object.plateforms=SolutionsPlateforms
		object.save()

	if(SolutionsTimeComplexity):
		object.timecomplexity=SolutionsTimeComplexity
		object.save()

	if(SolutionsAuxiliarySpace):
		object.auxiliaryspace=SolutionsAuxiliarySpace
		object.save()

	# must that you putted any one data-structure...
	if(SolutionsDataStructures):
		object.datastructures=len(SolutionsDataStructures)
		holds = [ str(object.datastructure_id) for object in solutions_datastructures.objects.filter(solution_id=object.id) ]
		for id in SolutionsDataStructures:
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


















