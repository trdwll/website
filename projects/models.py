from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=100, help_text='The title of the project')
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.title


channel = (
    ('Stable', 'Stable'),
    ('Beta', 'Beta'),
    ('Alpha', 'Alpha'),
    ('Development', 'Development'),
)

class ProjectVersion(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    version = models.CharField(max_length=32, help_text='The version via 0.0.0.0 format.')
    version_label = models.CharField(max_length=32, help_text='The version label such as alpha, beta, or rc.1.', blank=True)
    is_critical_update = models.BooleanField(default=False, help_text='Is this update a critical update?')
    is_active = models.BooleanField(default=True, help_text='Is this update live?')
    channel = models.CharField(max_length=32, default='Stable', choices=channel, help_text='What update channel is this version on?')
    download_url = models.URLField(help_text='Where can someone download this version?', blank=True)
    date = models.DateTimeField()

    def __str__(self):
        return str(self.project.title) + ' - ' + str(self.version)


category = (
    ('Added', 'Added'),
    ('Updated', 'Updated'),
    ('Fixed', 'Fixed'),
    ('Removed', 'Removed'),
    ('Deprecated', 'Deprecated'),
    ('Security', 'Security'),
)

class ProjectPatchNote(models.Model):
    project_version = models.ForeignKey(ProjectVersion, on_delete=models.CASCADE)
    category = models.CharField(max_length=20, choices=category)
    description = models.CharField(max_length=200, help_text='A brief description.')

    def __str__(self):
        return str(self.project_version.project.title) + ' ' + str(self.project_version.version)