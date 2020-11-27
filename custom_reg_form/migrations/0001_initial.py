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
                ('member_org_inst', models.CharField(blank=True, max_length=5, verbose_name=b'Are you a member of an organization/institution', error_messages={b'required': 'Please tell us if your are a member of an organization/institution..', b'invalid': "Please enter the membership information."}, choices=[(b'0', b'No'), (b'1', b'Yes')])),
                ('org_inst', models.CharField(max_length=100, verbose_name=b'Organization/Institution name', error_messages={b'required': 'Please tell us the organization/institution you are a member of.', b'invalid': "Invalid entrie."})),
                ('tel', models.CharField(max_length=100, verbose_name=b'Tel', error_messages={b'required': 'Please tell us your telephone number.', b'invalid': "Invalid telephone number."})),
                ('user', models.OneToOneField(null=True, to=settings.AUTH_USER_MODEL, on_delete=models.PROTECT)),
            ],
        ),
    ]
