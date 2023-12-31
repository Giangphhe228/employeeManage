# Generated by Django 4.2.2 on 2023-06-23 07:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('OKRs', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Log',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('note', models.CharField(max_length=250)),
                ('createBy', models.CharField(max_length=250)),
                ('updateBy', models.CharField(max_length=250)),
                ('createAt', models.DateTimeField(blank=True, null=True)),
                ('updateAt', models.DateTimeField(blank=True, null=True)),
                ('okrs_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='okr_log', to='OKRs.okr')),
            ],
            options={
                'db_table': 'log',
                'ordering': ['-id'],
            },
        ),
    ]
