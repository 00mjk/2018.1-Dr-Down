# Generated by Django 2.0.3 on 2018-05-07 17:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appointments', '0003_request'),
    ]

    operations = [
        migrations.AddField(
            model_name='request',
            name='day',
            field=models.CharField(choices=[('Sunday', 'Sunday'), ('Monday', 'Monday'), ('Tuesday', 'Tuesday'), ('Wednesday', 'Wednesday'), ('Thursday', 'Thursday'), ('Friday', 'Friday'), ('Saturday', 'Saturday')], default=0, help_text='Day of the week', max_length=10, verbose_name='Day of the week'),
            preserve_default=False,
        ),
    ]
