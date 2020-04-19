# Generated by Django 2.1.9 on 2020-04-18 17:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('printapp', '0004_userdata_user_gender'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductDesignData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Product_ID', models.CharField(max_length=100)),
                ('Design_Image', models.ImageField(upload_to='productdesignes/')),
            ],
            options={
                'db_table': 'PropertyDesignData',
            },
        ),
    ]
