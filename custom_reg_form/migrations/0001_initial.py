# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ExtraInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('org_inst', models.CharField(max_length=100, verbose_name=b'Organization/Institution name')),
                ('tel', models.CharField(max_length=100, verbose_name=b'Phone number', error_messages={b'required': 'Please tell us your telephone number.', b'invalid': "Invalid telephone number."})),
                ('user', models.OneToOneField(null=True, to=settings.AUTH_USER_MODEL, on_delete=models.PROTECT)),
            ],
        ),
    ]
