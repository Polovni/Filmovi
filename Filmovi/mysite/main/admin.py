from django.contrib import admin
from .models import Film, Recenzija


model_list = [Film, Recenzija]
## Register your models here.
admin.site.register(model_list)