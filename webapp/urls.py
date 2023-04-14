from django.urls import path

from webapp.views import *


urlpatterns = [
     path('', index_view, name='index_list'),

]