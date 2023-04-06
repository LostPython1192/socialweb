from django.contrib import admin
from groups import models

# Register your models here.

class GroupMemberInline(admin.TabularInline):
    '''Tabular Inline View for GroupMember'''

    model = models.GroupMember

admin.site.register(models.Group)