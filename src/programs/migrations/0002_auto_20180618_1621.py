# Generated by Django 2.0.1 on 2018-06-18 16:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('programs', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='name',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='program',
            name='age_group',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='program',
            name='cost',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='program',
            name='date',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='program',
            name='location',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='program',
            name='nomination',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='program',
            name='nomination_deadline',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='program',
            name='scholarship_app',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='program',
            name='scholarship_app_deadline',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='program',
            name='student_app',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='program',
            name='student_app_deadline',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='program',
            name='time',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='program',
            name='topic',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='program',
            name='volunteer_app',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='program',
            name='volunteer_app_deadline',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]