# Generated by Django 3.0.8 on 2020-07-26 17:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Menu_Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_name', models.TextField()),
                ('price', models.DecimalField(blank=True, decimal_places=2, max_digits=12, null=True)),
                ('large_price', models.DecimalField(blank=True, decimal_places=2, max_digits=12, null=True)),
                ('quantity', models.IntegerField(default=1)),
                ('active', models.BooleanField()),
                ('slug', models.SlugField(default='')),
                ('category_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='orders.Category')),
            ],
        ),
        migrations.CreateModel(
            name='Placed_Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('discount', models.DecimalField(blank=True, decimal_places=2, max_digits=12, null=True)),
                ('price', models.IntegerField(blank=True, null=True)),
                ('final_price', models.IntegerField(blank=True, null=True)),
                ('customer_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Order_Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ordered', models.BooleanField(default=False)),
                ('quantity', models.IntegerField(default=1)),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orders.Menu_Item')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateTimeField(auto_now_add=True)),
                ('ordered_date', models.DateTimeField()),
                ('ordered', models.BooleanField(default=False)),
                ('session_key', models.CharField(max_length=40)),
                ('items', models.ManyToManyField(to='orders.Order_Item')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('user', 'session_key')},
            },
        ),
    ]