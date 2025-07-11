# Generated by Django 4.2.5 on 2025-07-12 08:50

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('details', models.TextField(max_length=300)),
                ('priority', models.IntegerField(default=1, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)])),
                ('status', models.CharField(max_length=100)),
                ('project', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='projects.project')),
            ],
        ),
    ]
