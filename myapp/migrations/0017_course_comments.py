# Generated by Django 3.0.7 on 2020-08-13 22:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0016_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='comments',
            field=models.TextField(blank=True, max_length=1000, null=True),
        ),
    ]
