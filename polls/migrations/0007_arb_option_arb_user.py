# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-03-11 04:40
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('polls', '0006_arb_option_arb_time_option'),
    ]

    operations = [
        migrations.AddField(
            model_name='arb_option',
            name='arb_user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]