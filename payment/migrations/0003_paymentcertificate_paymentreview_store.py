# Generated by Django 5.1.6 on 2025-02-11 00:06

import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0002_payment_description'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='PaymentCertificate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('certificate_number', models.CharField(max_length=100)),
                ('issued_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('valid_until', models.DateTimeField()),
                ('payment', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='certificate', to='payment.payment')),
            ],
        ),
        migrations.CreateModel(
            name='PaymentReview',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.IntegerField()),
                ('comment', models.TextField()),
                ('date_added', models.DateTimeField(default=django.utils.timezone.now)),
                ('payment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='payment.payment')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Store',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=100)),
                ('payment_options', models.ManyToManyField(related_name='stores', to='payment.payment')),
            ],
        ),
    ]
