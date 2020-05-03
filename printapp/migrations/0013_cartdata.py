# Generated by Django 2.1.1 on 2020-04-30 11:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('printapp', '0012_auto_20200430_1553'),
    ]

    operations = [
        migrations.CreateModel(
            name='CartData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Cart_ID', models.CharField(max_length=100)),
                ('Order_ID', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'CartData',
            },
        ),
    ]