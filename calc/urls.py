from django.urls import path,include

from . import views
urlpatterns = [
path('',views.home,name='home'),
path('selection',views.selection,name='selection'),
path('thanks/',views.thanks,name='thanks'),
path('bas',views.bas,name='bas'),
]