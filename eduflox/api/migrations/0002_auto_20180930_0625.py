# Generated by Django 2.1.1 on 2018-09-30 06:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agent',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='agent', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='invitation',
            name='inviter',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='invitations', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='school',
            name='code',
            field=models.CharField(blank=True, max_length=10, null=True, unique=True, verbose_name='School Code'),
        ),
        migrations.AlterField(
            model_name='school',
            name='created_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='schools', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='school',
            name='status',
            field=models.CharField(choices=[('pending', 'Pending'), ('approved', 'Approved'), ('rejected', 'Rejected')], default='pending', max_length=20, verbose_name='Status'),
        ),
        migrations.AlterField(
            model_name='service',
            name='requested_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='services', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='service',
            name='school',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='services', to='api.School'),
        ),
    ]
