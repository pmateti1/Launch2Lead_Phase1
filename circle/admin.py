from django.contrib import admin
from circle.models import Comment

class CommentedBy(admin.ModelAdmin):
    list_display = ('posted_by', 'posted')

admin.site.register(Comment,CommentedBy)
