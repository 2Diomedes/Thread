# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Page

# Les pages

class PageAdmin(admin.ModelAdmin):
    list_display = ("title", "date")

    fieldsets = (
        ("Nouvelle page:", {
            'fields': ('title', 'slug', 'text', 'date'),
        }),
    )

    prepopulated_fields = {"slug": ("title",)}

admin.site.register(Page, PageAdmin)

# Les pages