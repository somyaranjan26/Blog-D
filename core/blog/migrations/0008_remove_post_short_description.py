# Generated by Django 3.0.5 on 2021-06-16 08:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_comment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='short_description',
        ),
    ]
