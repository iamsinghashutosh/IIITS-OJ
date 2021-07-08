from django.contrib import admin
from .models import program	
from .models import author
# Register your models here.
admin.site.register(program)
admin.site.register(author)