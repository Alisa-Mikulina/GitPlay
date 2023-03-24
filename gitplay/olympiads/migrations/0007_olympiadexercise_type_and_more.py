# Generated by Django 4.1.7 on 2023-03-24 09:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_alter_period_options_period_unique period'),
        ('olympiads', '0006_alter_exercisetype_options_alter_exercisetype_type_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='olympiadexercise',
            name='type',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.PROTECT, related_name='olympic_exercises', to='olympiads.exercisetype'),
        ),
        migrations.AlterField(
            model_name='olympiadexercise',
            name='olympiad',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='olympic_exercises', to='olympiads.olympiad'),
        ),
        migrations.AlterField(
            model_name='olympiadexercise',
            name='period',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='olympic_exercises', to='core.period'),
        ),
    ]
