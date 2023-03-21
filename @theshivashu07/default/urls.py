from django.urls import path
from . import views

urlpatterns=[

		path('',views.index,name='index'),
		# path('index/',views.index,name='index'),
		
		path('services/',views.services,name='services'),
		path('projects2/',views.projects2,name='projects2'),
		path('projects3/',views.projects3,name='projects3'),
		path('projectdetails/',views.projectdetails,name='projectdetails'),
		path('blog/',views.blog,name='blog'),
		path('blogsingle/',views.blogsingle,name='blogsingle'),
		path('ourteam/',views.ourteam,name='ourteam'),
		path('archives/',views.archives,name='archives'),
		path('grids/',views.grids,name='grids'),
		path('error404/',views.error404,name='error404'),
		path('contact/',views.contact,name='contact'),

		
		# path('/index',views.index,name='index'),
		#path('/',views.,name=''),
		#path('/',views.,name=''),
		#path('/',views.,name=''),

]








