# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('readerApp', '0004_auto_20150705_0943'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='imageMain',
            field=models.ImageField(upload_to=b'images'),
        ),
    ]
