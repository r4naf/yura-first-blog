# Generated by Django 2.0.3 on 2018-04-03 11:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0017_delete_post2'),
    ]

    operations = [
        migrations.CreateModel(
            name='Keyword',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, unique=True)),
                ('slug', models.SlugField(max_length=200, unique=True)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.AddField(
            model_name='post',
            name='keywords',
            field=models.ManyToManyField(blank=True, to='blog.Keyword'),
        ),
    ]