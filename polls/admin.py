# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from models import hotel_option, time_option, arb_option

# Register your models here.
admin.site.register(hotel_option)
admin.site.register(time_option)
admin.site.register(arb_option)