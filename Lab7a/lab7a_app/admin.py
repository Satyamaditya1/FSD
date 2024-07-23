from django.contrib import admin
from lab7a_app.models import student,course

admin.site.site_header = 'FDP ON Django'
admin.site.site_title = 'FDP ON Django'

@admin.register(student)
class studentAdmin(admin.Model.Admin):
    list_display=('usn','name')
    ordering=('usn',)
    search_fields=('name',)

@admin.register(course)
class courseAdmin(admin.Model.Admin):
    list_display=('courseCode', 'courseName')
    ordering=('courseCode',)
    search_fields=('courseName',)