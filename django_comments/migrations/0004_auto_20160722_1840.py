# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_comments', '0003_add_submit_date_index'),
    ]

    operations = [
        migrations.RunSQL('ALTER TABLE "django_comments" ALTER COLUMN "object_pk" TYPE integer USING "object_pk"::integer, ALTER COLUMN "object_pk" SET NOT NULL, ALTER COLUMN "object_pk" DROP DEFAULT;')
    ]
