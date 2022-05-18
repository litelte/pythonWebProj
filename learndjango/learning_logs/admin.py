from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Entry, Topic
admin.site.register(Topic)
admin.site.register(Entry)