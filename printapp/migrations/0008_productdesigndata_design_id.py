# Generated by Django 2.1.9 on 2020-04-22 08:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('printapp', '0007_productdata_product_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='productdesigndata',
            name='Design_ID',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
