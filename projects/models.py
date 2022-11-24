from django.db import models


class Technology(models.Model):
    name = models.CharField(max_length=100)
    time_of_experience = models.CharField(max_length=50)

    base_tech = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.name


def validate_is_image(file):
    import os
    from django.core.exceptions import ValidationError
    valid_file_extensions = ['.jpg', '.gif', '.png', '.jpeg', '.svg']
    ext = os.path.splitext(file.name)[1]
    if ext.lower() not in valid_file_extensions:
        raise ValidationError('The file must be an image.')


class MediaFile(models.Model):
    file = models.FileField(upload_to='mediafiles', validators=[validate_is_image])

    project = models.ForeignKey('Project', on_delete=models.CASCADE, related_name='media_files')


class Project(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    year_of_realization = models.IntegerField()
    time_invested = models.CharField(max_length=50)
    project_link = models.CharField(max_length=100)
    github_link = models.CharField(max_length=100)

    technologies = models.ManyToManyField(Technology, related_name='projects')


    def __str__(self):
        return self.name
