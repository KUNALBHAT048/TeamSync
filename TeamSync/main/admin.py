from django.contrib import admin
from .models import ProjectList,Project_History,Chat
# Register your models here.
admin.site.register(ProjectList)
admin.site.register(Project_History)
admin.site.register(Chat)