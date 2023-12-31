# Generated by Django 4.2.2 on 2023-06-23 07:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=250)),
                ('createBy', models.CharField(max_length=250)),
                ('updateBy', models.CharField(max_length=250)),
                ('createDate', models.DateTimeField(blank=True, null=True)),
                ('updateDate', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'note',
                'ordering': ['-id'],
            },
        ),
    ]
