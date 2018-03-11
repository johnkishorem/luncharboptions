# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import datetime

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import logout
from django.urls import reverse
from django.contrib.auth.models import User
from polls.models import hotel_option, time_option, arb_option

# Create your views here.

def index(request):
	if request.user.is_authenticated:
		logged_user = User.objects.get(username=request.user.username)
		selected_option = logged_user.arb_option_set.filter(arb_pub_date=datetime.date.today())
		if selected_option.count() == 1:
			selected_hotel = selected_option.get().arb_hotel_option.hotel_name
			selected_time = selected_option.get().arb_time_option.time_slot
		else:
			selected_hotel = None
			selected_time = None

		hotels = hotel_option.objects.all()
		time_slots = time_option.objects.all()
		context = {'username' : request.user.username, 
			'hotels' : hotels, 
			'time_slots' : time_slots,
			'selected_hotel' : selected_hotel,
			'selected_time': selected_time}
		return render(request, 'polls/index.html', context)
	else:
		return HttpResponseRedirect(reverse('login'))


def logout_view(request):
	logout(request)
	return HttpResponseRedirect(reverse('login'))