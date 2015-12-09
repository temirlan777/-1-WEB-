# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0003_auto_20151208_1920'),
    ]

    operations = [
        migrations.AddField(
            model_name='answer',
            name='counts',
            field=models.IntegerField(default=0),
        ),
    ]
