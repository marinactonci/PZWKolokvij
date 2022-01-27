from django.contrib import admin
from main.models import *
model_list = [Sladoled, Sladoledni_kup, Napitak]

admin.site.register(model_list)
