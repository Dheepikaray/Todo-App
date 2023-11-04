from django.urls import path

from new_app import views

urlpatterns = [
   path("new",views.new,name='new'),
   path('create',views.create,name='create'),
   path('view',views.view,name='view'),



   path("delts/<int:id>/",views.delete,name='delts'),
   path("update/<int:id>/",views.update,name='update')
]
