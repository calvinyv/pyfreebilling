# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-04-13 16:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Acc',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('method', models.CharField(default=b'', help_text='A method is the primary function that a request is meant to invoke on a server.', max_length=16)),
                ('from_tag', models.CharField(default=b'', help_text='The tag parameter serves as a general mechanism to identify a dialog, which is the combination of the Call-ID along with two tags, one from participant in the dialog.', max_length=64)),
                ('to_tag', models.CharField(default=b'', help_text='The tag parameter serves as a general mechanism to identify a dialog, which is the combination of the Call-ID along with two tags, one from participant in the dialog.', max_length=64)),
                ('callid', models.CharField(db_index=True, default=b'', help_text='Call-ID header field uniquely identifies a particular invitation or all registrations of a particular client.', max_length=255)),
                ('sip_code', models.CharField(default=b'', help_text='SIP reply code.', max_length=3)),
                ('sip_reason', models.CharField(default=b'', help_text='SIP reply reason', max_length=128)),
                ('time', models.DateTimeField(help_text='Date and time when this record was written.')),
            ],
            options={
                'ordering': ('-pk',),
                'db_table': 'acc',
            },
        ),
        migrations.CreateModel(
            name='MissedCall',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('method', models.CharField(default=b'', help_text='A method is the primary function that a request is meant to invoke on a server.', max_length=16)),
                ('from_tag', models.CharField(default=b'', help_text='The tag parameter serves as a general mechanism to identify a dialog, which is the combination of the Call-ID along with two tags, one from participant in the dialog.', max_length=64)),
                ('to_tag', models.CharField(default=b'', help_text='The tag parameter serves as a general mechanism to identify a dialog, which is the combination of the Call-ID along with two tags, one from participant in the dialog.', max_length=64)),
                ('callid', models.CharField(db_index=True, default=b'', help_text='Call-ID header field uniquely identifies a particular invitation or all registrations of a particular client.', max_length=255)),
                ('sip_code', models.CharField(default=b'', help_text='SIP reply code.', max_length=3)),
                ('sip_reason', models.CharField(default=b'', help_text='SIP reply reason', max_length=128)),
                ('time', models.DateTimeField(help_text='Date and time when this record was written.')),
            ],
            options={
                'ordering': ('-pk',),
                'db_table': 'missed_calls',
            },
        ),
    ]
