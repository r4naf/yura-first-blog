# Generated by Django 2.0.3 on 2018-04-03 06:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_post_myselectcharfield'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='myEmailField1',
            field=models.EmailField(max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='myEmailField2',
            field=models.EmailField(default='mail@mail.ru', max_length=254),
        ),
    ]
