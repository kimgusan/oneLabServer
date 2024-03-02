# Generated by Django 5.0.2 on 2024-03-02 11:32

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('member', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Community',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('community_title', models.CharField(max_length=30)),
                ('community_content', models.CharField(max_length=2000)),
                ('community_status', models.SmallIntegerField(choices=[(-1, '기타'), (0, '자료유형'), (1, '질문')], default=0)),
                ('member', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='member.member')),
            ],
            options={
                'db_table': 'tbl_community',
                'ordering': ['-id'],
            },
        ),
    ]
