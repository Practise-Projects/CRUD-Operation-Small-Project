from django.urls import path
from . import views


#app_name='employee_register'

urlpatterns = [
    path('',views.employee_form ,name='employee_insert'),  #This is for get and Post request for Insert Opertion
    path('<int:id>/',views.employee_form ,name ='employee_update'), # this is for Update Operation
    path('list/',views.employee_list,name='employee_list'), # this is for displaying the information 
    path('delete/<int:id>/',views.employee_delete ,name='employee_delete')
]

# Note
'''
this Insert and Update Operition uses the same page . We can update in form also as we do in django admin.
'''