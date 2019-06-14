# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.contrib import auth
from django.utils import timezone


class User(auth.models.User, auth.models.PermissionsMixin):
	# upload to folder in media folder
	picture = models.ImageField(upload_to='images')
	
	def __str__(self):
		return "@{}".format(self.username)