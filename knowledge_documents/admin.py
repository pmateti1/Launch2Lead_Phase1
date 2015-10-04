from django.contrib import admin
from .models import Market_Research
from django_markdown.admin import MarkdownModelAdmin
from django_markdown.widgets import AdminMarkdownWidget
from django.db.models import TextField


class MarketResearchAdmin(MarkdownModelAdmin):
    list_display = ('title', 'posted', 'posted_by')
    exclude = ['posted']
    prepopulated_fields = {'slug': ('title',)}
    formfield_overrides = {TextField: {'widget': AdminMarkdownWidget}}

admin.site.register(Market_Research, MarketResearchAdmin)
