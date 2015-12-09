# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0004_answer_counts'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='answer',
            name='counts',
        ),
        migrations.AddField(
            model_name='question',
            name='counts',
            field=models.IntegerField(default=0),
        ),
    ]
