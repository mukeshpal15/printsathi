# Generated by Django 2.1.1 on 2020-04-26 09:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('printapp', '0009_orderdata'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderdata',
            name='Payment_ID',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
