from django.db import models
# Create your models here.
from autoslug import AutoSlugField


class DataStructures(models.Model):
	name = models.CharField(max_length=25);
	slug = AutoSlugField(populate_from='name');
	def __str__(self):
		return "Added a new Data Structure : "+self.name+".";

class Plateforms(models.Model):
	name = models.CharField(max_length=25);
	slug = AutoSlugField(populate_from='name');
	color = models.CharField(max_length=25, default=None, null=True);
	bgcolor = models.CharField(max_length=25, default=None, null=True);	
	def __str__(self):
		return "Added a new Plateform : "+self.name+".";

class ProgrammingLanguages(models.Model):
	name = models.CharField(max_length=25);
	slug = AutoSlugField(populate_from='name');
	def __str__(self):
		return "Added a new Programming Language : "+self.name+".";




class Problems(models.Model):
	title = models.CharField(max_length=100);
	slug = AutoSlugField(populate_from='title');
	plateforms = models.IntegerField(default=0, null=True);
	datastructures = models.IntegerField(default=0, null=True);
	detailsset = models.IntegerField(default=0, null=True);
	timecomplexity = models.CharField(max_length=35, default=None, null=True);
	auxiliaryspace = models.CharField(max_length=35, default=None, null=True);
	JoiningDate = models.DateTimeField(auto_now_add=True);
	UpdationDate = models.DateTimeField(auto_now=True);

class problems_plateforms(models.Model):
	problem_id = models.ForeignKey(Problems, null=True, on_delete=models.CASCADE)
	plateform_id = models.IntegerField(default=None, null=True);

class problems_datastructures(models.Model):
	problem_id = models.ForeignKey(Problems, null=True, on_delete=models.CASCADE)
	datastructure_id = models.IntegerField(default=None, null=True);

class problems_detailssets(models.Model):
	problem_id = models.ForeignKey(Problems, null=True, on_delete=models.CASCADE)
	detailsset = models.CharField(max_length=500, default=None, null=True);





class Solutions(models.Model):
	problem_id = models.ForeignKey(Problems, null=True, on_delete=models.CASCADE) 
	plateforms = models.IntegerField(default=0, null=True); 
	programminglanguages = models.IntegerField(default=0, null=True);	
	datastructures = models.IntegerField(default=0, null=True); 
	codesubmissions =models.CharField(max_length=1000, default=None, null=True); 
	timecomplexity = models.CharField(max_length=35, default=None, null=True); 
	auxiliaryspace = models.CharField(max_length=35, default=None, null=True); 
	explainlevel = models.IntegerField(default=1, null=True); 
	JoiningDate = models.DateTimeField(auto_now_add=True); 
	UpdationDate = models.DateTimeField(auto_now=True); 

class solutions_datastructures(models.Model):
	solution_id = models.ForeignKey(Solutions, null=True, on_delete=models.CASCADE)
	datastructure_id = models.IntegerField(default=None, null=True);











