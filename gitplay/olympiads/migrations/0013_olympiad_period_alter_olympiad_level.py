# Generated by Django 4.1.7 on 2023-03-27 20:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_alter_period_options_period_unique period'),
        ('olympiads', '0012_level'),
    ]

    operations = [
        migrations.AddField(
            model_name='olympiad',
            name='period',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, related_name='olympiads', to='core.period'),
        ),
        migrations.AlterField(
            model_name='olympiad',
            name='level',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='olympiads', to='olympiads.level'),
        ),
    ]
