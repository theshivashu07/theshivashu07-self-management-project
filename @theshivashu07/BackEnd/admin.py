from django.contrib import admin
# Register your models here.
from .models import DataStructures,Plateforms,ProgrammingLanguages,Problems,problems_plateforms,problems_datastructures,problems_detailssets,Solutions,solutions_datastructures

admin.site.register(DataStructures)
admin.site.register(Plateforms)
admin.site.register(ProgrammingLanguages)

admin.site.register(Problems)
admin.site.register(problems_plateforms)
admin.site.register(problems_datastructures)
admin.site.register(problems_detailssets)

admin.site.register(Solutions)
admin.site.register(solutions_datastructures)


