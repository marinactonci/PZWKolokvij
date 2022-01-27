from django.urls import path
from . import views

urlpatterns = [
    path('', views.hoomepage),
    path('sladoledi', views.SladoledList.as_view()),
    path('napitci', views.NapitakList.as_view()),
    path('drugiSlad', views.filerSladoledi),
    path('drugiNap', views.filerNapitci)
]
