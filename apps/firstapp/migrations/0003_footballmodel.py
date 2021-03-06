# Generated by Django 3.2.7 on 2021-11-28 03:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0002_auto_20211116_1001'),
    ]

    operations = [
        migrations.CreateModel(
            name='FootBallModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('playerID', models.CharField(max_length=100)),
                ('timestamp', models.CharField(max_length=100)),
                ('match_ref_id', models.CharField(default='temporary', max_length=100)),
                ('team1Score', models.CharField(default='temporary', max_length=100)),
                ('team2Score', models.CharField(default='temporary', max_length=100)),
                ('action', models.CharField(default='temporary', max_length=100)),
            ],
        ),
    ]
