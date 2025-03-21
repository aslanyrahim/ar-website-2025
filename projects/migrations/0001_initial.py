# Generated by Django 5.1.6 on 2025-03-05 05:04

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('slug', models.SlugField(max_length=200, unique=True)),
                ('short_description', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('icon', models.CharField(blank=True, help_text='Font Awesome icon name', max_length=50)),
                ('image', models.ImageField(blank=True, null=True, upload_to='projects/')),
                ('is_featured', models.BooleanField(default=False)),
                ('order', models.PositiveIntegerField(default=0)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('client', models.CharField(max_length=200)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField(blank=True, null=True)),
                ('technologies', models.CharField(max_length=255)),
                ('status', models.CharField(choices=[('planning', 'Planning'), ('in_progress', 'In Progress'), ('completed', 'Completed'), ('on_hold', 'On Hold')], default='in_progress', max_length=20)),
                ('outcomes', models.TextField()),
            ],
            options={
                'ordering': ['order'],
            },
        ),
        migrations.CreateModel(
            name='ProjectChallenge',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('solution', models.TextField()),
                ('order', models.PositiveIntegerField(default=0)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='challenges', to='projects.project')),
            ],
            options={
                'ordering': ['order'],
            },
        ),
        migrations.CreateModel(
            name='ProjectFeature',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('order', models.PositiveIntegerField(default=0)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='features', to='projects.project')),
            ],
            options={
                'ordering': ['order'],
            },
        ),
        migrations.CreateModel(
            name='TeamMember',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('role', models.CharField(max_length=200)),
                ('avatar', models.ImageField(blank=True, null=True, upload_to='team_members/')),
                ('projects', models.ManyToManyField(related_name='team_members', to='projects.project')),
            ],
        ),
    ]
