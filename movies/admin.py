from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Person)
admin.site.register(Organization)
admin.site.register(Genre)
admin.site.register(Movie)
admin.site.register(Critic)
