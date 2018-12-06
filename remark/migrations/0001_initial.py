# Generated by Django 2.1.3 on 2018-12-06 09:08

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Remark',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='评论人')),
                ('text', models.TextField(blank=True, default='', verbose_name='评论内容')),
                ('create_time', models.DateTimeField(default=django.utils.timezone.now, verbose_name='创建时间')),
                ('aid', models.IntegerField(default=0)),
            ],
            options={
                'verbose_name': '评论内容',
                'db_table': 'remark',
                'ordering': ['-create_time'],
            },
        ),
    ]
