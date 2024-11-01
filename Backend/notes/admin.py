from django.contrib import admin
from notes.models import Note, Text, Pic
# Register your models here.

admin.site.register(Note)
admin.site.register(Text)
admin.site.register(Pic)