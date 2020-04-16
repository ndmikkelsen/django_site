from django.contrib import admin
from .models import Tutorial, Blog
from django.db import models
from tinymce.widgets import TinyMCE


# Register your models here.
class TutorialAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Title/date', {'fields': ['tutorial_title', 'tutorial_publish']}),
        ('Content', {'fields': ['tutorial_content']})
    ]

    formfield_overrides = {
        models.TextField: {'widget': TinyMCE()}
    }


class BlogAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Title/date', {'fields': ['blog_title', 'blog_publish']}),
        ('Content', {'fields': ['blog_content']})
    ]

    formfield_overrides = {
        models.TextField: {'widget': TinyMCE()}
    }


admin.site.register(Tutorial, TutorialAdmin)
admin.site.register(Blog, BlogAdmin)
