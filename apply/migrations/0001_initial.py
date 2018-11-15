# Generated by Django 2.0.9 on 2018-11-13 11:24

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Candidate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60, unique=True)),
                ('project_name', models.CharField(max_length=60, unique=True)),
                ('project_objective', models.TextField()),
                ('target_audience', models.TextField()),
                ('revenue_model', models.TextField()),
                ('project_age', models.CharField(max_length=60, unique=True)),
                ('contact_details', models.TextField()),
                ('submission_date', models.DateField(default=django.utils.timezone.now)),
                ('status', models.CharField(choices=[('REJECTED', 'rejected'), ('APPROVED', 'approved'), ('PENDING', 'pending')], default='PENDING', max_length=50)),
            ],
        ),
    ]
