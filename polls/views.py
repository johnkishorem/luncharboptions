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
		context_hotels = []
		for hotel in hotels:
			votes = arb_option.objects.filter(arb_hotel_option=hotel, 
				arb_pub_date=datetime.date.today()).count()
			context_hotel = {'context_hotel_name' : hotel.hotel_name, 
				'context_hotel_location' : hotel.hotel_location,
				'context_hotel_budget' : hotel.hotel_avg_budget,
				'context_hotel_votes' : votes}
			context_hotels.append(context_hotel)

		time_slots = time_option.objects.all()
		context_time_slots = []
		for each_time_slot in time_slots:
			votes = arb_option.objects.filter(arb_time_option=each_time_slot, 
				arb_pub_date=datetime.date.today()).count()
			context_time = {'context_time_slot' : each_time_slot.time_slot, 
				'context_time_slot_votes' : votes}
			context_time_slots.append(context_time)

		context = {'username' : request.user.username, 
			'context_hotels' : context_hotels, 
			'context_time_slots' : context_time_slots,
			'selected_hotel' : selected_hotel,
			'selected_time': selected_time}
		return render(request, 'polls/index.html', context)
	else:
		return HttpResponseRedirect(reverse('login'))


def logout_view(request):
	logout(request)
	return HttpResponseRedirect(reverse('login'))