from django.contrib import admin
from . import models
# Register your models here.

class MembershipInline(admin.StackedInline):
    """
    to hold the records of the many to many relation
    """
    model = models.Membership
    extra = 1

class UserAdmin(admin.ModelAdmin):
    """
    The model admin to use to manage objects of the User model
    """
    model = models.User
    inlines = (MembershipInline,)

class GroupAdmin(admin.ModelAdmin):
    """
    The model admin to use to manage objects of the Group model
    """
    model = models.Group
    inlines = (MembershipInline,)

admin.site.register(models.Group, GroupAdmin)
admin.site.unregister(models.User)
admin.site.register(models.User, UserAdmin)