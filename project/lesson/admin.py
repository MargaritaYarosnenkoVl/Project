from django.contrib import admin


from .models import *


class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'owner')

class LessonAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'name', 'video', 'duration_video', 'product')


admin.site.register(Product, ProductAdmin)
admin.site.register(Lesson, LessonAdmin)

