# Generated by Django 2.0.3 on 2018-04-03 07:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0014_auto_20180403_0948'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('field1', models.CharField(default='', max_length=50)),
                ('field2', models.TextField(default='')),
            ],
        ),
    ]
