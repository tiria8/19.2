# Generated by Django 4.2.5 on 2023-10-24 17:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0006_alter_version_product'),
    ]

    operations = [
        migrations.AlterField(
            model_name='version',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.product', verbose_name='продукт'),
        ),
    ]
