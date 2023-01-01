from rest_framework import serializers

from projects.models import Project, MediaFile, Technology, DevelopmentMethodology, ProjectField


class MediaFileSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = MediaFile
        fields = ('file',)


class BaseTechnologySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Technology
        fields = ('id', 'name',)


class TechnologySerializer(serializers.HyperlinkedModelSerializer):
    base_tech = BaseTechnologySerializer(many=False, read_only=True)

    class Meta:
        model = Technology
        fields = ('id', 'name', 'time_of_experience', 'icon_name', 'base_tech')


class ProjectFieldSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ProjectField
        fields = ('id', 'name', 'icon_name',)


class ProjectSerializer(serializers.HyperlinkedModelSerializer):
    media_files = MediaFileSerializer(many=True, read_only=True)
    technologies = TechnologySerializer(many=True, read_only=True)
    tech_fields = ProjectFieldSerializer(many=True, read_only=True)
    class Meta:
        model = Project
        fields = ('id', 'name', 'description', 'year_of_realization', 'purpose', 'time_invested', 'project_link', 'github_link', 'media_files', 'technologies', 'methodology', 'tech_fields')


class DevelopmentMethodologySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = DevelopmentMethodology
        fields = ('id', 'name',)
