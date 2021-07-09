from django.contrib import admin
from .models import Trainning, Detail, Feedback

# Register your models here.

class Trainningadmin(admin.ModelAdmin):
    list_display = ('id','name','email', 'contact','location')


class Detailadmin(admin.ModelAdmin):
    list_display = ('id','size','img', 'colour','price')

class Feedbackadmin(admin.ModelAdmin):
    list_display = ('name','phone','message')


admin.site.register(Trainning,Trainningadmin)
admin.site.register(Detail,Detailadmin)
admin.site.register(Feedback,Feedbackadmin)