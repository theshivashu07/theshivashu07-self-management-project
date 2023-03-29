from django.urls import path
from . import views

urlpatterns=[

		path('',views.index,name='index'),
		path('edittables/',views.edittables,name='edittables'),
		path('codesubmissions/',views.codesubmissions,name='codesubmissions'),
		path('problemsubmissions/',views.problemsubmissions,name='problemsubmissions'),
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







