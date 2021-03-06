# Generated by Django 3.1.2 on 2020-10-16 23:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0011_auto_20201006_1138'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderitem',
            name='note',
            field=models.CharField(max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='status',
            field=models.CharField(choices=[('Pending', 'Pending'), ('Out for delivery', 'Out for delivery'), ('Delivered', 'Delivered'), ('Cancelled', 'Cancelled')], default='Pending', max_length=200, null=True),
        ),
    ]
