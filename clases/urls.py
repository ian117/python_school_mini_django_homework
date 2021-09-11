
from django.urls import path

from clases.views import clases_all, clases_by_id

app_name = 'clases'
urlpatterns = [
    path('', clases_all, name='general'),
    path('<id>/', clases_by_id, name='details')
]
