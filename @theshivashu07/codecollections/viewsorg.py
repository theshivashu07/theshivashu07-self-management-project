from django.shortcuts import render,redirect
from django.http import HttpResponse

import codecollections._BulkFunctions as _BulkFunctions
from BackEnd.models import *

# Create your views here.


# import codecollections._importantdatasets as _importantdatasets
problemID=Problems.objects.get(pk=1)
solutionID=Solutions.objects.get(pk=1)






def index(request):
	if request.method=="POST":
		pass
	SenderDatasets={
		'DataSet':None,
	}
	return render(request,"otherapps/codecollections/index.html",SenderDatasets);




def addproblems(request):
	if request.method=="POST":
		if( request.POST["comingProblemTitle"] and request.POST["comingDetails"] ):
			comingProblemTitle=request.POST["comingProblemTitle"]
			comingPlateforms=request.POST.getlist("comingPlateforms")
			comingDataStructures=request.POST.getlist("comingDataStructures")
			if(comingProblemTitle or comingPlateforms or comingDataStructures):
				locks = Problems.objects.get(pk=problemID.id)  #Problems()
				locks = Problems()
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
			print("This is not correct Input's... Reput again!!!")
		return redirect("/codecollections/problems/new/")

	SenderDatasets={
		# 'ProblemDataSet':_BulkFunctions.ProblemDataSet(problemID),
		# 'SolutionDataSet':_BulkFunctions.SolutionDataSet(problemID,solutionID),
		'Plateforms':Plateforms.objects.all(),
		'DataStructures':DataStructures.objects.all(),
		'ProgrammingLanguages':ProgrammingLanguages.objects.all(),
	}
	return render(request,"otherapps/codecollections/new_addproblems.html",SenderDatasets);



def addsolutions(request,problemslug='problem-number-0001'):
	if request.method=="POST":
		comingProblemID= problemID.id; #request.POST["comingProblemID"]
		comingDataStructures=request.POST.getlist("comingDataStructures")
		comingProgrammingLanguage=request.POST["comingProgrammingLanguage"]
		comingPlateforms=request.POST["comingPlateforms"]
		comingTimeComplexity=request.POST["comingTimeComplexity"]
		comingAuxiliarySpace=request.POST["comingAuxiliarySpace"]
		comingCodeSubmissions=request.POST["comingCodeSubmissions"]
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
		return redirect("/codecollections/problemsandsolutions/problem-number-001/new/")

	SenderDatasets={
		'ProblemDataSet':_BulkFunctions.ProblemDataSet(problemID),
		'SolutionDataSet':_BulkFunctions.SolutionDataSet(problemID,solutionID),
		'Plateforms':Plateforms.objects.all(),
		'DataStructures':DataStructures.objects.all(),
		'ProgrammingLanguages':ProgrammingLanguages.objects.all(),
	}
	return render(request,"otherapps/codecollections/new_addsolutions.html",SenderDatasets);




def addproblemsandsolutions(request,problemslug='problem-number-0001'):
	if request.method=="POST":
		pass

	SenderDatasets={
		'ProblemDataSet':_BulkFunctions.ProblemDataSet(problemID),
		'SolutionDataSet':_BulkFunctions.SolutionDataSet(problemID,solutionID),
		'Plateforms':Plateforms.objects.all(),
		'DataStructures':DataStructures.objects.all(),
		'ProgrammingLanguages':ProgrammingLanguages.objects.all(),
	}
	return render(request,"otherapps/codecollections/new_addproblemsandsolutions.html",SenderDatasets);





def editproblems(request,problemslug='problem-number-0001'):
	if request.method=="POST":
		pass

	SenderDatasets={
		'ProblemDataSet':_BulkFunctions.ProblemDataSet(problemID),
		'SolutionDataSet':_BulkFunctions.SolutionDataSet(problemID,solutionID),
		'Plateforms':Plateforms.objects.all(),
		'DataStructures':DataStructures.objects.all(),
		'ProgrammingLanguages':ProgrammingLanguages.objects.all(),
	}
	return render(request,"otherapps/codecollections/new_editproblems.html",SenderDatasets);





def editsolutions(request,problemslug='problem-number-0001',solutionid='1'):
	if request.method=="POST":
		pass

	SenderDatasets={
		'ProblemDataSet':_BulkFunctions.ProblemDataSet(problemID),
		'SolutionDataSet':_BulkFunctions.SolutionDataSet(problemID,solutionID),
		'Plateforms':Plateforms.objects.all(),
		'DataStructures':DataStructures.objects.all(),
		'ProgrammingLanguages':ProgrammingLanguages.objects.all(),
	}
	return render(request,"otherapps/codecollections/new_editsolutions.html",SenderDatasets);





def problemswholelist(request):
	if request.method=="POST":
		pass

	SenderDatasets={
		'ProblemDataSet':_BulkFunctions.ProblemDataSet(problemID),
		'SolutionDataSet':_BulkFunctions.SolutionDataSet(problemID,solutionID),
		'Plateforms':Plateforms.objects.all(),
		'DataStructures':DataStructures.objects.all(),
		'ProgrammingLanguages':ProgrammingLanguages.objects.all(),
	}
	return render(request,"otherapps/codecollections/new_404.html",SenderDatasets);
	# return render(request,"otherapps/codecollections/new_problemswholelist.html",SenderDatasets);





# def openproblems(request,problemslug='problem-number-0001'):
# 	if request.method=="POST":
# 		pass

# 	SenderDatasets={
# 		'ProblemDataSet':_BulkFunctions.ProblemDataSet(problemID),
# 		'SolutionDataSet':_BulkFunctions.SolutionDataSet(problemID,solutionID),
# 		'Plateforms':Plateforms.objects.all(),
# 		'DataStructures':DataStructures.objects.all(),
# 		'ProgrammingLanguages':ProgrammingLanguages.objects.all(),
# 	}
# 	return render(request,"otherapps/codecollections/new_openproblems.html",SenderDatasets);





def openproblemsandsolutions(request,problemslug='problem-number-0001',solutionid='1'):
	if request.method=="POST":
		pass

	SenderDatasets={
		'ProblemDataSet':_BulkFunctions.ProblemDataSet(problemID),
		'SolutionDataSet':_BulkFunctions.SolutionDataSet(problemID,solutionID),
		'Plateforms':Plateforms.objects.all(),
		'DataStructures':DataStructures.objects.all(),
		'ProgrammingLanguages':ProgrammingLanguages.objects.all(),
	}
	return render(request,"otherapps/codecollections/new_openproblemsandsolutions.html",SenderDatasets);













