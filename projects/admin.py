from django.contrib import admin

from .models import Project, Technology, MediaFile, DevelopmentMethodology, ProjectField


class FilesInline(admin.TabularInline):
    model = MediaFile
    min_num = 1
    extra = 0
    max_num = 3


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'get_technologies_names', 'year_of_realization', 'is_active') # Fields to display in the list view
    list_filter = ['year_of_realization', 'is_active'] # Add a filter sidebar
    search_fields = ['name', 'year_of_realization'] # Add a search box
    inlines = [FilesInline]

    @admin.display(description='Technologies')
    def get_technologies_names(self, obj):
        return [tech.name for tech in obj.technologies.all()]


@admin.register(Technology)
class TechnologyAdmin(admin.ModelAdmin):
    list_display = ('name', 'time_of_experience', 'tech_domain', 'get_parent_tech') # Fields to display in the list view
    search_fields = ['name'] # Add a search box

    @admin.display(description='Parent technology')
    def get_parent_tech(self, obj):
        if obj.base_tech:
            return obj.base_tech.name
        return ''

    @admin.display(description='Time of experience')
    def time_of_experience(self, obj):
        return obj.time_of_experience()


@admin.register(DevelopmentMethodology)
class DevelopmentMethodologyAdmin(admin.ModelAdmin):
    list_display = ('name',) # Fields to display in the list view
    search_fields = ['name'] # Add a search box


@admin.register(ProjectField)
class ProjectFieldAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ['name']