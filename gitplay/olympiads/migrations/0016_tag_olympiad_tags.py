# Generated by Django 4.1.7 on 2023-03-27 21:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('olympiads', '0015_alter_olympiad_level_alter_olympiad_period'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag', models.CharField(max_length=256, unique=True)),
            ],
        ),
        migrations.AddField(
            model_name='olympiad',
            name='tags',
            field=models.ManyToManyField(related_name='olympiads', to='olympiads.tag'),
        ),
    ]
