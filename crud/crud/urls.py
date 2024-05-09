from django.contrib import admin
from django.urls import path
from mainApp import views
urlpatterns = [
    path("admin/", admin.site.urls),
    path('',views.homePage),
    path('add/',views.addPage),
    path('delete/<int:id>/',views.deleteRecord),
    path('edit/<int:id>/',views.editRecord),
    path('search/',views.searchPage)
 
    
]
