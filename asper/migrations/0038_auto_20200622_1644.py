# Generated by Django 3.0 on 2020-06-22 11:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('asper', '0037_auto_20200622_1641'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='firsttask',
            name='FirstTS',
        ),
        migrations.RemoveField(
            model_name='firsttask',
            name='ud',
        ),
        migrations.RemoveField(
            model_name='firsttask',
            name='usr',
        ),
    ]