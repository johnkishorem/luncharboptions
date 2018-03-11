# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import logout

# Create your views here.

def index(request):
	if request.user.is_authenticated:
		logout(request)
		return HttpResponse("Hello " + request.user.username)
	else:
		return HttpResponseRedirect('login/')
