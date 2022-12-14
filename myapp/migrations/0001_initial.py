# Generated by Django 4.1 on 2022-08-26 05:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=50)),
                ('lastname', models.CharField(max_length=50)),
                ('company_name', models.CharField(max_length=150)),
                ('state', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=50)),
                ('contact', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=150)),
                ('website', models.CharField(max_length=250)),
                ('description', models.CharField(max_length=500)),
                ('logo_pic', models.ImageField(upload_to='img/company')),
            ],
        ),
        migrations.CreateModel(
            name='UserMaster',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=50)),
                ('password', models.CharField(max_length=50)),
                ('otp', models.IntegerField()),
                ('role', models.CharField(max_length=50)),
                ('is_active', models.BooleanField(default=True)),
                ('is_verified', models.BooleanField(default=False)),
                ('is_created', models.DateTimeField(auto_now_add=True)),
                ('is_updated', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='JobDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('jobname', models.CharField(max_length=250)),
                ('companyname', models.CharField(max_length=250)),
                ('companyaddress', models.CharField(max_length=250)),
                ('jobdescription', models.TextField(max_length=500)),
                ('qualification', models.CharField(max_length=250)),
                ('resposibilties', models.CharField(max_length=250)),
                ('location', models.CharField(max_length=250)),
                ('companywebiste', models.CharField(max_length=250)),
                ('companyemail', models.CharField(max_length=250)),
                ('companycontact', models.CharField(max_length=20)),
                ('salarypackage', models.CharField(max_length=250)),
                ('experience', models.IntegerField()),
                ('logo', models.ImageField(upload_to='img/jobpost')),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.company')),
            ],
        ),
        migrations.AddField(
            model_name='company',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.usermaster'),
        ),
        migrations.CreateModel(
            name='Candidate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=50)),
                ('lastname', models.CharField(max_length=50)),
                ('contact', models.CharField(max_length=50)),
                ('state', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=150)),
                ('dob', models.CharField(max_length=50)),
                ('gender', models.CharField(max_length=50)),
                ('min_salary', models.BigIntegerField()),
                ('max_salary', models.BigIntegerField()),
                ('job_type', models.CharField(max_length=150)),
                ('jobcategory', models.CharField(max_length=150)),
                ('country', models.CharField(max_length=150)),
                ('highestedu', models.CharField(max_length=150)),
                ('experience', models.CharField(max_length=150)),
                ('website', models.CharField(max_length=150)),
                ('shift', models.CharField(max_length=150)),
                ('jobdescription', models.CharField(max_length=500)),
                ('profile_pic', models.ImageField(upload_to='img/candidate')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.usermaster')),
            ],
        ),
        migrations.CreateModel(
            name='ApplyList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('education', models.CharField(max_length=200)),
                ('experience', models.CharField(max_length=200)),
                ('website', models.CharField(max_length=200)),
                ('min_salary', models.CharField(max_length=200)),
                ('max_salary', models.CharField(max_length=200)),
                ('gender', models.CharField(max_length=200)),
                ('resume', models.FileField(upload_to='resume')),
                ('candidate', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.candidate')),
                ('job', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.jobdetails')),
            ],
        ),
    ]
