# Generated by Django 3.0.8 on 2020-07-26 19:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='cart',
            unique_together=set(),
        ),
        migrations.RemoveField(
            model_name='cart',
            name='session_key',
        ),
    ]