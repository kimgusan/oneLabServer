# Generated by Django 5.0.2 on 2024-03-02 11:46

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exhibition', '0001_initial'),
        ('file', '0001_initial'),
        ('like', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExhibitionFile',
            fields=[
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('file', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, primary_key=True, serialize=False, to='file.file')),
                ('path', models.ImageField(upload_to='exhibition/%Y/%m/%d')),
            ],
            options={
                'db_table': 'tbl_exhibition_file',
            },
        ),
        migrations.CreateModel(
            name='ExhibitionLike',
            fields=[
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('like', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, primary_key=True, serialize=False, to='like.like')),
            ],
            options={
                'db_table': 'tbl_exhibition_like',
            },
        ),
    ]
