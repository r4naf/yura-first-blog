# Generated by Django 2.0.3 on 2018-04-02 13:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20180402_1618'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='field7',
            field=models.CharField(default='', max_length=210),
        ),
    ]