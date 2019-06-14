# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from felineapp.forms import UserCreateForm 
from django.views.generic import (
	TemplateView, 
	CreateView,
)
from django.core.urlresolvers import reverse_lazy


class Register(CreateView):
    form_class = UserCreateForm
    success_url = reverse_lazy("index")
    template_name = "felineapp/register.html"

class IndexView(TemplateView):
	template_name = "felineapp/index.html"

