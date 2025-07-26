from django.urls import path
from .views import SumNumber
from .views import FirstLastName
from .views import average
from .views import exponent
from .views import even
urlpatterns=[
    path("sum/",SumNumber),
    path("name/",FirstLastName),
    path("average/",average),
    path("exponent/",exponent),
    path("even/",even),
]