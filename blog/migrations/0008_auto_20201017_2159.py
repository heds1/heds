# Generated by Django 3.1.2 on 2020-10-17 08:59

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_remove_blogpost_published_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blogpost',
            name='published_date2',
        ),
        migrations.AddField(
            model_name='blogpost',
            name='published_date',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
