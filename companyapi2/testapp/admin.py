from django.contrib import admin
from testapp.models import User,UserManager

# Register your models here.
#class UserManagerAdmin(admin.ModelAdmin):
    #list_display=('email','password')

class UserAdmin(admin.ModelAdmin):
    list_display=('email','name')

admin.site.register(User,UserAdmin)
#admin.site.register(UserManager,UserManagerAdmin)
