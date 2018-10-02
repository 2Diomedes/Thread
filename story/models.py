# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models

# Les models des pages

class Page(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField()
    text = models.TextField()
    date =  models.DateField()

# Les models des pages