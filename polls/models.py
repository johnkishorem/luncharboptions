# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Models for represent hotel options
class hotel_option(models.Model):
	hotel_name = models.CharField(max_length=200)
	hotel_location = models.CharField(max_length=200)
	hotel_avg_budget = models.CharField(max_length=100)

	def __str__(self):
		return self.hotel_name

class time_option(models.Model):
	time_slot = models.CharField(max_length=50)

	def __str__(self):
		return self.time_slot


class arb_option(models.Model):
	arb_user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
	arb_hotel_option = models.ForeignKey(hotel_option, on_delete=models.CASCADE, null=True)
	arb_time_option = models.ForeignKey(time_option, on_delete=models.CASCADE, null=True)
	arb_pub_date = models.DateField(auto_now=False, auto_now_add=True)

	def __str__(self):
		user = str(self.arb_user.username)
		hotel_name = str(self.arb_hotel_option.hotel_name)
		time_slot = str(self.arb_time_option.time_slot)
		date = str(self.arb_pub_date)
		return "%s recommended %s at %s on %s" % (user, hotel_name, time_slot, date)