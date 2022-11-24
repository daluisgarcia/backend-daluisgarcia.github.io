from django.contrib import admin

from .models import Project, Technology, MediaFile


class FilesInline(admin.TabularInline):
    model = MediaFile
    min_num = 1
    extra = 0
    max_num = 3


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'year_of_realization', 'get_technologies_names') # Fields to display in the list view
    list_filter = ['year_of_realization'] # Add a filter sidebar
    search_fields = ['name', 'year_of_realization'] # Add a search box
    inlines = [FilesInline]

    @admin.display(description='Technologies')
    def get_technologies_names(self, obj):
        return [tech.name for tech in obj.technologies.all()]


@admin.register(Technology)
class TechnologyAdmin(admin.ModelAdmin):
    list_display = ('name', 'time_of_experience', 'get_parent_tech') # Fields to display in the list view
    list_filter = ['time_of_experience'] # Add a filter sidebar
    search_fields = ['name', 'time_of_experience'] # Add a search box

    @admin.display(description='Parent technology')
    def get_parent_tech(self, obj):
        if obj.base_tech:
            return obj.base_tech.name
        return ''