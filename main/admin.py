from django.contrib import admin

from main.models import *

models_list = [Film]

## Register your models here.
admin.site.register(models_list)