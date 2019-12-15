# Generated by Django 2.2.7 on 2019-12-05 09:09

from django.conf import settings
from django.db import migrations, models
import shortuuidfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('whursauth', '0003_auto_20191204_1623'),
    ]

    operations = [
        migrations.CreateModel(
            name='TagList',
            fields=[
                ('tag_name', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('link_count', models.IntegerField()),
            ],
        ),
        migrations.AlterField(
            model_name='user',
            name='download_history',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='user',
            name='upload_history',
            field=models.CharField(max_length=1000),
        ),
        migrations.CreateModel(
            name='Resource',
            fields=[
                ('uid', shortuuidfield.fields.ShortUUIDField(blank=True, editable=False, max_length=22, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=40)),
                ('abs_url', models.CharField(max_length=60, unique=True)),
                ('upload_time', models.DateTimeField(auto_now_add=True)),
                ('description', models.CharField(default='', max_length=140)),
                ('download_count', models.IntegerField()),
                ('is_valid', models.BooleanField(default=True)),
                ('tag', models.CharField(max_length=20)),
                ('upload_user', models.ForeignKey(on_delete='CASCADE', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='TagResourceLink',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('resource', models.ForeignKey(on_delete='CASCADE', to='whursauth.Resource')),
                ('tag_name', models.ForeignKey(on_delete='CASCADE', to='whursauth.TagList')),
            ],
            options={
                'unique_together': {('tag_name', 'resource')},
            },
        ),
    ]