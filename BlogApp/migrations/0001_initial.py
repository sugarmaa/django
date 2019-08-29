# Generated by Django 2.2.3 on 2019-07-28 18:59

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='GARCHIG', max_length=30)),
                ('shortNews', models.CharField(max_length=80)),
                ('news', models.TextField()),
                ('createdDate', models.DateTimeField(blank=True, default=django.utils.timezone.now)),
                ('author', models.CharField(max_length=30)),
                ('image', models.URLField()),
            ],
            options={
                'db_table': 'news',
            },
        ),
    ]