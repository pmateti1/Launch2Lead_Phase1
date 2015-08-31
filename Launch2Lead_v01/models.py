from django.db import models
from django.utils.text import slugify

# Create your models here.
class Service(models.Model):
    Title = models.CharField(max_length=128, unique=True)
    Description = models.TextField()
    slug = models.SlugField(unique=True, blank=True, null=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Service, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.name


