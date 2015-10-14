from django.db import models

My_CAT = (
    ('1', 'Jobs Posting'),
    ('2', 'Buy/Sell Products'),
    ('3', "Networking"),
)

class Comment(models.Model):
    text = models.TextField()
    picture = models.ImageField(upload_to="static/images/customer-pic")
    posted_by = models.CharField(max_length=100)
    posted = models.DateField(db_index=True, auto_now_add=True)
    category = models.IntegerField(choices = My_CAT)

    def __unicode__(self):
        return self.text