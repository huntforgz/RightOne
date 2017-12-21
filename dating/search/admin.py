
# Register your models here.
from django.contrib import admin
from .models import music, movie, hobbies, health, spend, userfeature

# Register your models here.
class musicAdmin(admin.ModelAdmin):
    list_display = ('genre',) # list
class movieAdmin(admin.ModelAdmin):
	list_display = ('genre',)
class hobbiesAdmin(admin.ModelAdmin):
	list_display = ('hobby_name',)
admin.site.register(music,musicAdmin)
admin.site.register(movie,movieAdmin)
admin.site.register(hobbies,hobbiesAdmin)
admin.site.register(health)
admin.site.register(spend)
admin.site.register(userfeature)
