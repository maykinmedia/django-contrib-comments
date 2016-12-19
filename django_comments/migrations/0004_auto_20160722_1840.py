# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_comments', '0003_add_submit_date_index'),
    ]

    operations = [
        migrations.operations.AlterField(
            model_name='comment',
            name='object_pk',
            field=models.PositiveIntegerField(verbose_name="object ID")
        )
    ]
