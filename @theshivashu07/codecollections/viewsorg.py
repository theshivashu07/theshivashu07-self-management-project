from django.shortcuts import render,redirect
from django.http import HttpResponse

import codecollections._BulkFunctions as _BulkFunctions
from BackEnd.models import *

# Create your views here.


# import codecollections._importantdatasets as _importantdatasets 
# problemID=Problems.objects.get(pk=2) 
# solutionID=Solutions.objects.get(pk=1) 

# default slug set!!!                                                                                                                             
defaultSlug='problem-number-0002' 





def index(request):
	if request.method=="POST":
		pass
	SenderDatasets={
		'ProblemsSlug':defaultSlug,
		'DataSet':None,
	}
	return render(request,"otherapps/codecollections/index.html",SenderDatasets);




def addproblems(request):
	# problemID=Problems.objects.get(slug=defaultSlug)
	if request.method=="POST":
		if( request.POST["ProblemsTitle"] and request.POST["ProblemsDetailSet"] ):
			_BulkFunctions.AddProblems(request)																			#wantchange___
			# _BulkFunctions.EditProblems(request,problemID)														#wantchange___
		else:
			print("This is not correct Input's... Reput again!!!")
		return redirect("/codecollections/problems/new/")

	SenderDatasets={
		'ProblemsSlug':defaultSlug,
		# 'ProblemDataSet':_BulkFunctions.ProblemDataSet(problemID),
		# 'SolutionDataSet':_BulkFunctions.SolutionDataSet(problemID,solutionID),
		'Plateforms':Plateforms.objects.all(),
		'DataStructures':DataStructures.objects.all(),
		'ProgrammingLanguages':ProgrammingLanguages.objects.all(),
	}
	return render(request,"otherapps/codecollections/new_addproblems.html",SenderDatasets);



def addsolutions(request,problemslug):
	problemID=Problems.objects.get(slug=defaultSlug)
	if request.method=="POST":
		if( request.POST["SolutionsCodeSubmissions"] ):
			_BulkFunctions.AddSolutions(request,problemID)
			# _BulkFunctions.EditSolutions(request,problemID)
		else:
			print("This is not correct Input's... Reput again!!!")
		return redirect("/codecollections/problemsandsolutions/"+defaultSlug+"/new/")

	SenderDatasets={
		'ProblemsSlug':defaultSlug,
		'ProblemDataSet':_BulkFunctions.ProblemDataSet(problemID),
		# 'SolutionDataSet':_BulkFunctions.SolutionDataSet(problemID,solutionID),
		'Plateforms':Plateforms.objects.all(),
		'DataStructures':DataStructures.objects.all(),
		'ProgrammingLanguages':ProgrammingLanguages.objects.all(),
	}
	return render(request,"otherapps/codecollections/new_addsolutions.html",SenderDatasets);




def addproblemsandsolutions(request):
	problemID=Problems.objects.get(slug=defaultSlug)
	if request.method=="POST":
		if( request.POST["ProblemsTitle"] and request.POST["ProblemsDetailSet"] ):
			_BulkFunctions.EditProblems(request,problemID)																			#wantchange___
			if( request.POST["SolutionsCodeSubmissions"] ):
				_BulkFunctions.EditSolutions(request,problemID)
			else:
				print("We're Discard only Solution... Reput again!!!")
		else:
			print("We're Discard both Problem and Solution... Reput again!!!")

	SenderDatasets={
		'ProblemsSlug':defaultSlug,
		# 'ProblemDataSet':_BulkFunctions.ProblemDataSet(problemID),
		# 'SolutionDataSet':_BulkFunctions.SolutionDataSet(problemID,solutionID),
		'Plateforms':Plateforms.objects.all(),
		'DataStructures':DataStructures.objects.all(),
		'ProgrammingLanguages':ProgrammingLanguages.objects.all(),
	}
	return render(request,"otherapps/codecollections/new_addproblemsandsolutions.html",SenderDatasets);





def editproblems(request,problemslug):
	problemID=Problems.objects.get(slug=defaultSlug)
	if request.method=="POST":
		if( request.POST["ProblemsTitle"] and request.POST["ProblemsDetailSet"] ):
			_BulkFunctions.EditProblems(request,problemID)																			#wantchange___
		else:
			print("This is not correct Input's... Reput again!!!")
		return redirect("/codecollections/problems/new/")

	SenderDatasets={
		'ProblemsSlug':defaultSlug,
		'ProblemDataSet':_BulkFunctions.ProblemDataSet(problemID),
		# 'SolutionDataSet':_BulkFunctions.SolutionDataSet(problemID,solutionID),
		'Plateforms':Plateforms.objects.all(),
		'DataStructures':DataStructures.objects.all(),
		'ProgrammingLanguages':ProgrammingLanguages.objects.all(),
	}
	return render(request,"otherapps/codecollections/new_editproblems.html",SenderDatasets);





def editsolutions(request,problemslug,solutionid='1'):
	problemID=Problems.objects.get(slug=defaultSlug)
	solutionID=Solutions.objects.get(slug=defaultSlug)
	if request.method=="POST":
		if( request.POST["SolutionsCodeSubmissions"] ):
			_BulkFunctions.EditSolutions(request,problemID)
		else:
			print("This is not correct Input's... Reput again!!!")
		return redirect("/codecollections/problemsandsolutions/"+defaultSlug+"/new/")

	SenderDatasets={
		'ProblemsSlug':defaultSlug,
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
		'ProblemsSlug':defaultSlug,
		# 'ProblemDataSet':_BulkFunctions.ProblemDataSet(problemID),
		# 'SolutionDataSet':_BulkFunctions.SolutionDataSet(problemID,solutionID),
		'Plateforms':Plateforms.objects.all(),
		'DataStructures':DataStructures.objects.all(),
		'ProgrammingLanguages':ProgrammingLanguages.objects.all(),
	}
	return render(request,"otherapps/codecollections/new_404.html");
	# return render(request,"otherapps/codecollections/new_problemswholelist.html",SenderDatasets);





def openproblemsandsolutions(request,problemslug,solutionid='1'):
	problemID=Problems.objects.get(slug=problemslug)
	solutionID=Solutions.objects.get(slug=problemslug)
	if request.method=="POST":
		pass
	SenderDatasets={
		'ProblemsSlug':defaultSlug,
		'ProblemDataSet':_BulkFunctions.ProblemDataSet(problemID),
		'SolutionDataSet':_BulkFunctions.SolutionDataSet(problemID,solutionID),
		'Plateforms':Plateforms.objects.all(),
		'DataStructures':DataStructures.objects.all(),
		'ProgrammingLanguages':ProgrammingLanguages.objects.all(),
	}
	return render(request,"otherapps/codecollections/new_openproblemsandsolutions.html",SenderDatasets);













