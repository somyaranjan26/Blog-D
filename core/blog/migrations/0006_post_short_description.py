# Generated by Django 3.0.5 on 2021-02-22 09:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20210222_0729'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='short_description',
            field=models.TextField(null=True),
        ),
    ]