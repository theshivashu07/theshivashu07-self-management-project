

kal = {
    "name":"Shivam Shukla",
    "number":78985650729,
    "password":"78985650729",
    "email":"sks1@gmail.com"
}



    path('registration/', views.user_registration, name='user_registration'),
    path('profile/', views.user_profile, name='user_profile'),
    path('mark-spam/', views.mark_spam, name='mark_spam'),
    path('search/name/', views.searching_by_name, name='searching_by_name'),
    path('search/number/', views.searching_by_number, name='searching_by_number'),