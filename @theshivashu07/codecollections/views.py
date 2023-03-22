from django.shortcuts import render,redirect
from django.http import HttpResponse

import codecollections._importantdatasets as _importantdatasets
# Create your views here.



# def index(request):
	# return HttpResponse("Hey <b>Shivam Shukla</b>, <b style='font-size:10px'>N your url '@theshivashu07'</b> !!!");


def index(request):
	return render(request,"otherapps/codecollections/index.html");

def codesubmissions(request):
	SenderDatasets={
		'DataStructures':_importantdatasets.DataStructures,
		'Plateforms':_importantdatasets.Plateforms,
		'ProgrammingLanguages':_importantdatasets.ProgrammingLanguages,
	}
	return render(request,"otherapps/codecollections/codesubmissions.html", SenderDatasets);

