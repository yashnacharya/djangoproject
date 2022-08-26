from email.policy import default
from django.db import models

class UserMaster(models.Model):
    email = models. EmailField(max_length=50) 
    password = models.CharField(max_length=50)
    otp = models.IntegerField()
    role = models.CharField(max_length=50)
    is_active = models.BooleanField(default=True)
    is_verified = models.BooleanField(default=False)
    is_created = models.DateTimeField (auto_now_add=True)
    is_updated = models.DateTimeField (auto_now_add=True)
    def __str__(self):
         return self.email

class Candidate(models.Model):
    user_id = models.ForeignKey(UserMaster,on_delete=models.CASCADE)
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    contact = models.CharField(max_length=50, )
    state = models.CharField(max_length=50, )
    city= models.CharField(max_length=50, )
    address = models.CharField(max_length=150, )
    dob = models.CharField(max_length=50, )
    gender = models.CharField(max_length=50, )
    min_salary = models.BigIntegerField(null=True)
    max_salary = models.BigIntegerField(null=True)
    job_type = models.CharField(max_length=150, )
    jobcategory = models.CharField(max_length=150, )
    country = models.CharField(max_length=150, )
    highestedu = models.CharField(max_length=150, )
    experience = models.CharField(max_length=150, )
    website = models.CharField(max_length=150, )
    shift = models.CharField(max_length=150, )
    jobdescription = models.CharField(max_length=500, )
    profile_pic = models.ImageField(upload_to="img/candidate", )
    def __str__(self):
        return self.firstname

class Company(models.Model):
    user_id = models.ForeignKey(UserMaster,on_delete=models.CASCADE)
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    company_name = models.CharField(max_length=150, )
    state = models.CharField(max_length=50, )
    city = models.CharField(max_length=50, ) 
    contact = models.CharField(max_length=50, )
    address = models.CharField(max_length=150, )
    website = models.CharField(max_length=250, )
    description = models.CharField(max_length=500, )
    logo_pic = models.ImageField(upload_to="img/company", )

    def __str__(self):
         return self.firstname

class JobDetails(models.Model):
    company = models.ForeignKey(Company,on_delete=models.CASCADE)
    jobname = models.CharField(max_length=250) 
    companyname = models.CharField(max_length=250)
    companyaddress = models.CharField(max_length=250) 
    jobdescription= models.TextField(max_length=500) 
    qualification= models.CharField(max_length=250) 
    resposibilties = models.CharField(max_length=250) 
    location = models.CharField(max_length=250)
    companywebiste = models.CharField(max_length=250) 
    companyemail = models.CharField(max_length=250) 
    companycontact = models.CharField(max_length=20) 
    salarypackage = models.CharField(max_length=250)
    experience = models.IntegerField()
    logo = models.ImageField(upload_to="img/jobpost",)

class ApplyList(models.Model):
    candidate = models.ForeignKey(Candidate,on_delete=models.CASCADE) 
    job = models.ForeignKey(JobDetails, on_delete=models.CASCADE) 
    education = models.CharField(max_length=200)
    experience = models.CharField(max_length=200)
    website = models.CharField(max_length=200)
    min_salary = models.CharField(max_length=200)
    max_salary = models.CharField(max_length=200)
    gender = models.CharField(max_length=200)
    resume = models.FileField(upload_to="resume")


