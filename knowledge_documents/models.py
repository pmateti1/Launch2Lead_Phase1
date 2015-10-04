from django.db import models
from django.db.models import permalink

My_CAT = (
    ('1','Market Research'),
    ('2','Published Post'),
    ('3','Essential Formats'),
)
class Market_Research(models.Model):
    title = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    posted = models.DateField(db_index=True, auto_now_add=True)
    picture = models.ImageField(upload_to = "static/images/blog" )
    body = models.TextField()
    short_body = models.TextField(max_length=300)
    posted_by = models.CharField(max_length=100)

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

    def __unicode__(self):
        return '%s' % self.title

    @permalink
    def get_absolute_url(self):
        return ('view_blog_post', None, {'slug': self.slug})
