# Generated by Django 2.1.1 on 2018-09-02 12:17

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import eduflox.api.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Agent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=25, verbose_name='First Name')),
                ('middle_name', models.CharField(max_length=25, null=True, verbose_name='Middle Name')),
                ('last_name', models.CharField(max_length=25, verbose_name='Last Name')),
                ('mobile_no', models.CharField(max_length=11, validators=[django.core.validators.RegexValidator(message='Invalid mobile number.', regex='^\\d{11}$')], verbose_name='Mobile No')),
                ('email', models.EmailField(max_length=254, verbose_name='Email')),
                ('address', models.CharField(max_length=200, verbose_name='Street')),
                ('city', models.CharField(max_length=25, verbose_name='City')),
                ('state', models.CharField(max_length=25, verbose_name='State')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-created_at', 'first_name', 'last_name'],
            },
        ),
        migrations.CreateModel(
            name='Invitation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('invitee_email', models.EmailField(max_length=254, verbose_name='Invitee Email')),
                ('token', models.CharField(default=eduflox.api.models.create_token, max_length=75, unique=True, verbose_name='Token')),
                ('invitation_date', models.DateTimeField(auto_now_add=True)),
                ('accepted_date', models.DateTimeField(null=True)),
                ('inviter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-invitation_date', 'inviter'],
            },
        ),
        migrations.CreateModel(
            name='Invoice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cpe', models.CharField(max_length=75, verbose_name='Add CPE')),
                ('cpe_amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='School',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='School')),
                ('location', models.CharField(max_length=25, verbose_name='Location')),
                ('district', models.CharField(max_length=25, verbose_name='District')),
                ('code', models.CharField(max_length=10, unique=True, verbose_name='School Code')),
                ('status', models.CharField(choices=[('pending', 'Pending'), ('approved', 'Approved'), ('rejected', 'Rejected')], max_length=20, verbose_name='Status')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-created_at', 'name'],
            },
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service_description', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('requested_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('school', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.School')),
            ],
            options={
                'ordering': ['-created_at', 'school'],
            },
        ),
        migrations.AddField(
            model_name='invoice',
            name='request_code',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Service'),
        ),
    ]
