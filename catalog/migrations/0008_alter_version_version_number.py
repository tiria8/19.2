# Generated by Django 4.2.5 on 2023-10-25 17:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0007_alter_version_product'),
    ]

    operations = [
        migrations.AlterField(
            model_name='version',
            name='version_number',
            field=models.IntegerField(default=1, verbose_name='номер версии'),
        ),
    ]
