from django.urls import path
from api.views import *


urlpatterns = [
    path('echo/', json_echo_view),
    path('csrf/', get_token_view),
    path('add/', add_view),
    path('subsrtact/', subsrtact_view),
    path('divide/', divide_view),
    path('multiply/', multiply_view),
]