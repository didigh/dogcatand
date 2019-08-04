from django.contrib import admin

# Register your models here.
from .models import Blog,Comment,Re

admin.site.register(Blog)
admin.site.register(Comment)
admin.site.register(Re)