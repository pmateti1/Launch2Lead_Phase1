from django.contrib import admin
from .models import Market_Research, Published_Post,  Essential_Format


class MarketResearchAdmin(admin.ModelAdmin):
    list_display = ('title', 'posted', 'posted_by')
    exclude = ['posted']
    prepopulated_fields = {'slug': ('title',)}



class PublishedPostsAdmin(admin.ModelAdmin):
    list_display = ('title', 'posted', 'posted_by')
    exclude = ['posted']
    prepopulated_fields = {'slug': ('title',)}


class EssentialFormatsAdmin(admin.ModelAdmin):
    list_display = ('title', 'posted', 'posted_by')
    exclude = ['posted']
    prepopulated_fields = {'slug': ('title',)}



admin.site.register(Market_Research, MarketResearchAdmin)
admin.site.register(Published_Post, PublishedPostsAdmin)
admin.site.register(Essential_Format, EssentialFormatsAdmin)
