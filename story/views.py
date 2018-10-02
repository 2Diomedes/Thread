# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.shortcuts import render
from .models import Page
# Les views des mobs

class IndexView(ListView):
    model = Page

