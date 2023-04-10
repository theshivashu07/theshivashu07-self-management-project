from django.urls import path
from . import views

urlpatterns=[

		path('',views.index,name='index'),
		path('edittables/',views.edittables,name='edittables'),
		path('codesubmissions/',views.codesubmissions,name='codesubmissions'),
		path('problemsubmissions/',views.problemsubmissions,name='problemsubmissions'),

		path('problems/new/',views.addproblems,name='addproblems'),
		path('problemsandsolutions/problem-number-001/new/',views.addsolutions,name='addsolutions'),
		path('problemsandsolutions/new/',views.addproblemsandsolutions,name='addproblemsandsolutions'),

		path('problems/edit/problem-number-001/',views.editproblems,name='editproblems'),
		path('problemsandsolutions/problem-number-001/edit/1/',views.editsolutions,name='editsolutions'),

		path('problems/wholelist/',views.problemswholelist,name='problemswholelist'),
		# path('problems/problem-number-001/',views.openproblems,name='openproblems'),
		path('problemsandsolutions/problem-number-001/1/',views.openproblemsandsolutions,name='openproblemsandsolutions'),

		# path('justtry/',views.justtry,name='justtry'),
		# path('/codecollections/',views.problemsubmissions,name='problemsubmissions'),


		# path('index/',views.index,name='index'),
		# path('index/',views.index,name='index'),
		# path('index/',views.index,name='index'),
		# path('index/',views.index,name='index'),
		# path('index/',views.index,name='index'),
		# path('index/',views.index,name='index'),
		#path('/',views.,name=''),
		#path('/',views.,name=''),
		#path('/',views.,name=''),

]






