# Generated by Django 2.0.3 on 2018-04-03 06:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20180403_0836'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='mySelectCharField',
            field=models.CharField(choices=[('FR', 'Freshman'), ('SO', 'Sophomore'), ('JR', 'Junior'), ('SR', 'Senior')], default='FR', max_length=2),
        ),
    ]