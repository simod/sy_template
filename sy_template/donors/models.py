from django.db import models


class DonorsMapping(models.Model):
    keyword = models.SlugField()
    name = models.CharField(max_length=128)
    thumbnail = models.ImageField(upload_to='donors_mapping')
    type = models.CharField(max_length=10, choices=[['mapping', 'Mapping'], ['meeting', 'Meeting']])

    def __unicode__(self):
        return self.name