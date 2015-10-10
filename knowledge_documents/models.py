from django.db import models
from django.db.models import permalink

class Market_Research(models.Model):
    title = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    posted = models.DateField(db_index=True, auto_now_add=True)
    picture = models.ImageField(upload_to = "static/images/blog" )
    body = models.TextField()
    short_body = models.TextField(max_length=300)
    posted_by = models.CharField(max_length=100)
    published = models.BooleanField(default=True)

    def __unicode__(self):
        return '%s' % self.title


class Published_Post(models.Model):
    title = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    posted = models.DateField(db_index=True, auto_now_add=True)
    picture = models.ImageField(upload_to = "static/images/blog" )
    body = models.TextField()
    short_body = models.TextField(max_length=300)
    posted_by = models.CharField(max_length=100)
    published = models.BooleanField(default=True)

    def __unicode__(self):
        return '%s' % self.title

class Essential_Format(models.Model):
    title = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    posted = models.DateField(db_index=True, auto_now_add=True)
    picture = models.ImageField(upload_to = "static/images/blog" )
    body = models.TextField()
    short_body = models.TextField(max_length=300)
    posted_by = models.CharField(max_length=100)
    published = models.BooleanField(default=True)

    def __unicode__(self):
        return '%s' % self.title

    @permalink
    def get_absolute_url(self):
        return ('blog.views.post', None, {'slug': self.slug})