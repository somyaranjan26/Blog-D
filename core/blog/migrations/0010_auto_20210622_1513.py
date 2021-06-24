# Generated by Django 3.0.5 on 2021-06-22 15:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='status',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, related_name='blog_category', to='blog.Category'),
        ),
    ]
