# Generated by Django 3.0.5 on 2020-04-28 18:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_auto_20200422_1244'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='language',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalog.Language'),
        ),
    ]
