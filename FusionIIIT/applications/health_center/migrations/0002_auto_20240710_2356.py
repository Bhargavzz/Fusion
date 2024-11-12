# Generated by Django 3.1.5 on 2024-07-10 23:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('health_center', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='All_Medicine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('medicine_name', models.CharField(default='NOT_SET', max_length=50)),
                ('brand_name', models.CharField(default='NOT_SET', max_length=50)),
                ('constituents', models.TextField(default='NOT_SET')),
                ('manufacturer_name', models.CharField(default='NOT_SET', max_length=50)),
                ('pack_size_label', models.CharField(default='NOT_SET', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='All_Prescribed_medicine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=0)),
                ('days', models.IntegerField(default=0)),
                ('times', models.IntegerField(default=0)),
                ('revoked', models.BooleanField(default=False)),
                ('revoked_date', models.DateField(null=True)),
                ('medicine_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='health_center.all_medicine')),
            ],
        ),
        migrations.CreateModel(
            name='All_Prescription',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.CharField(max_length=15)),
                ('details', models.TextField(null=True)),
                ('date', models.DateField()),
                ('suggestions', models.TextField(null=True)),
                ('test', models.CharField(blank=True, max_length=200, null=True)),
                ('file_id', models.IntegerField(default=0)),
                ('is_dependent', models.BooleanField(default=False)),
                ('dependent_name', models.CharField(default='SELF', max_length=30)),
                ('dependent_relation', models.CharField(default='SELF', max_length=20)),
                ('doctor_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='health_center.doctor')),
            ],
        ),
        migrations.CreateModel(
            name='Prescription_followup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('details', models.TextField(null=True)),
                ('date', models.DateField()),
                ('test', models.CharField(blank=True, max_length=200, null=True)),
                ('suggestions', models.TextField(null=True)),
                ('file_id', models.IntegerField(default=0)),
                ('Doctor_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='health_center.doctor')),
                ('prescription_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='health_center.all_prescription')),
            ],
        ),
        migrations.CreateModel(
            name='Present_Stock',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Stock_entry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=0)),
                ('supplier', models.CharField(default='NOT_SET', max_length=50)),
                ('Expiry_date', models.DateField()),
                ('date', models.DateField(auto_now=True)),
                ('medicine_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='health_center.all_medicine')),
            ],
        ),
        migrations.RemoveField(
            model_name='ambulance_request',
            name='user_id',
        ),
        migrations.RemoveField(
            model_name='announcements',
            name='anno_id',
        ),
        migrations.RemoveField(
            model_name='appointment',
            name='doctor_id',
        ),
        migrations.RemoveField(
            model_name='appointment',
            name='schedule',
        ),
        migrations.RemoveField(
            model_name='appointment',
            name='user_id',
        ),
        migrations.RemoveField(
            model_name='complaint',
            name='user_id',
        ),
        migrations.DeleteModel(
            name='Counter',
        ),
        migrations.RemoveField(
            model_name='expiry',
            name='medicine_id',
        ),
        migrations.RemoveField(
            model_name='hospital_admit',
            name='doctor_id',
        ),
        migrations.RemoveField(
            model_name='hospital_admit',
            name='hospital_name',
        ),
        migrations.RemoveField(
            model_name='hospital_admit',
            name='user_id',
        ),
        migrations.RemoveField(
            model_name='medicine',
            name='medicine_id',
        ),
        migrations.RemoveField(
            model_name='medicine',
            name='patient',
        ),
        migrations.RemoveField(
            model_name='prescribed_medicine',
            name='medicine_id',
        ),
        migrations.RemoveField(
            model_name='prescribed_medicine',
            name='prescription_id',
        ),
        migrations.RemoveField(
            model_name='prescription',
            name='doctor_id',
        ),
        migrations.RemoveField(
            model_name='prescription',
            name='user_id',
        ),
        migrations.RemoveField(
            model_name='specialrequest',
            name='request_ann_maker',
        ),
        migrations.DeleteModel(
            name='Ambulance_request',
        ),
        migrations.DeleteModel(
            name='Announcements',
        ),
        migrations.DeleteModel(
            name='Appointment',
        ),
        migrations.DeleteModel(
            name='Complaint',
        ),
        migrations.DeleteModel(
            name='Expiry',
        ),
        migrations.DeleteModel(
            name='Hospital',
        ),
        migrations.DeleteModel(
            name='Hospital_admit',
        ),
        migrations.DeleteModel(
            name='Medicine',
        ),
        migrations.DeleteModel(
            name='Prescribed_medicine',
        ),
        migrations.DeleteModel(
            name='Prescription',
        ),
        migrations.DeleteModel(
            name='SpecialRequest',
        ),
        migrations.DeleteModel(
            name='Stock',
        ),
        migrations.AddField(
            model_name='present_stock',
            name='stock_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='health_center.stock_entry'),
        ),
        migrations.AddField(
            model_name='all_prescribed_medicine',
            name='prescription_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='health_center.all_prescription'),
        ),
    ]
