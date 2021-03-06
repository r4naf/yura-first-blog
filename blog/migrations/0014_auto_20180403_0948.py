# Generated by Django 2.0.3 on 2018-04-03 06:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0013_auto_20180403_0946'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='myEmailField1',
            field=models.EmailField(blank=True, default='', max_length=254),
        ),
        migrations.AlterField(
            model_name='post',
            name='myIPAddressField',
            field=models.GenericIPAddressField(blank=True, default='', null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='myImageField',
            field=models.ImageField(blank=True, default='pic_folder/no-img.jpg', null=True, upload_to='pic_folder/'),
        ),
        migrations.AlterField(
            model_name='post',
            name='myURLField',
            field=models.URLField(blank=True, default='', null=True),
        ),
    ]
