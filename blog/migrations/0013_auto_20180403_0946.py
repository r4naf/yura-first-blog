# Generated by Django 2.0.3 on 2018-04-03 06:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0012_auto_20180403_0946'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='myEmailField1',
            field=models.EmailField(default='', max_length=254),
        ),
    ]
