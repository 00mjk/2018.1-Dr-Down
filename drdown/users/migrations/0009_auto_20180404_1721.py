# Generated by Django 2.0.3 on 2018-04-04 17:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_auto_20180404_1643'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='patient',
            name='Urgency',
        ),
        migrations.AddField(
            model_name='patient',
            name='Priority',
            field=models.IntegerField(choices=[(5, 'Not urgent'), (4, 'Not very urgent'), (3, 'Urgent'), (2, 'Very urgent'), (1, 'Emerging')], default=5, help_text='Please, insert the degree of priority of the patient'),
        ),
    ]
