# Generated by Django 4.2.5 on 2023-10-15 11:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0003_blog'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='description',
            field=models.TextField(blank=True, null=True, verbose_name='Содержание'),
        ),
    ]
