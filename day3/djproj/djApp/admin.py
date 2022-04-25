from django.contrib import admin
from .models import Student, Track
# Register your models here.


class CutomStudent(admin.ModelAdmin):
    fieldsets = (
        [
            ['Student Information', {'fields': ['fname', 'lname', 'age']}],
            ['Scholarship Info', {'fields': ['std_track']}]
        ])
    list_display = (['fname', 'lname', 'age', 'std_track', 'is_adult'])
    search_fields = (
        ['fname', 'lname', 'age', 'std_track__track_name'])
    list_filter = (
        ['age', 'std_track__track_name'])


class InlineStudent(admin.StackedInline):
    model = Student
    extra = 1


class CustomTrack(admin.ModelAdmin):
    inlines = [InlineStudent]


admin.site.register(Student, CutomStudent)
admin.site.register(Track, CustomTrack)
