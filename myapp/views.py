from urllib import request
from django.shortcuts import render, redirect
from .models import *
from random import randint


def Indexpage(request):
    return render(request, "index.html")
def SignupPage(request):        
    return render(request, "signup.html")
def LoginPage(request):
    return render(request, "login.html")
def ProfilePage(request):
    return render(request, "profile.html")   
def RegisterUser(request):
    role = request.POST['role']
    fname= request.POST['firstname']
    lname= request.POST['lastname']
    email = request.POST['email']
    password = request.POST['password']
    cpassword = request.POST['cpassword']
    user = UserMaster.objects.filter(email=email)
    if user:
        message = "User already Exist"
        return render(request, "signup.html", {'msg': message})
    else:
        if password == cpassword:
            otp = randint(100000,999999)
            newuser = UserMaster.objects.create(role=role, otp=otp, email=email, password=password)
            if role == "Candidate":
                newcand = Candidate.objects.create(user_id=newuser, firstname=fname, lastname=lname)
            elif role == "Company":
                newcom = Company.objects.create(user_id=newuser, firstname=fname, lastname=lname)
            return render(request, "otpverify.html", {'email':email})
def OtpPage(request):
    return render(request, "otpverify.html")

def Otpverify(request):
    email = request.POST['email']
    otp = int(request.POST['otp'])  
    user = UserMaster.objects.get(email=email)
    if user:
        if user.otp == otp:
            message = "Otp verify successfully"
            return render(request, "login.html", {'msg':message})
        else:
            message = "Otp is incorrect"
            return render(request, "otpverify.html", {'msg':message})
    else:
        return render(request, "signup.html")

def LoginUser(request):
    email = request.POST['email'] 
    lpassword = request.POST['pass']
    user = UserMaster.objects.get(email=email)
    if user:
        if user.password==lpassword and user.role=="Candidate":
            can = Candidate.objects.get(user_id=user)
            request.session['id'] = user.id
            request.session['role'] = user.role
            request.session['firstname'] = can.firstname
            request.session['lastname'] = can.lastname
            request.session['email'] = user.email
            return redirect('index')
        elif user.password==lpassword and user.role=="Company":
            comp = Company.objects.get(user_id=user)
            request.session['id'] = user.id
            request.session['role'] = user.role
            request.session['firstname'] = comp.firstname
            request.session['lastname'] = comp.lastname
            request.session['email'] = user.email
            return redirect('index')
        else:
            message = "Password does not match" 
            return render(request, "login.html", {'msg': message})
    else:
        message="User does not exist"
        return render(request, "login.html", {'msg' :message})

def ProfilePage(request, pk):
    user = UserMaster.objects.get(pk=pk)
    can = Candidate.objects.get(user_id=user)
    return render(request, "profile.html", {'user':user, 'can':can})

def UpdateProfile(request, pk):
    user = UserMaster.objects.get(pk=pk)
    if user.role == "Candidate":
        can = Candidate.objects.get(user_id=user)
        can.state = request.POST['state']
        can.city = request.POST['city']
        can.job_type = request.POST['jobtype']
        print(can.job_type)
        can.country = request.POST['country']
        can.jobcategory = request.POST['category']
        can.highestedu = request.POST['education']
        can.experience = request.POST['experience']
        can.website = request.POST['website'] 
        can.shift = request.POST['shift']
        can.jobdescription = request.POST['description']
        can.min_salary = request.POST['minsalary']
        can.max_salary = request.POST['maxsalary']
        can.contact = request.POST['contact']
        can.gender = request.POST['gender']
        can.profile_pic = request.FILES['image']
        can.save()
        url = f'/profile/{pk}' # formatting URL
        return redirect(url)
def ApplyPage(request, pk): 
    user = request.session['id'] 
    print(user)
    if user:
        cand = Candidate.objects.get(user_id=user)
        job = JobDetails.objects.get(id=pk) 
        return render(request, "apply.html",{'user':user, 'cand':cand, 'job':job})
def ApplyJob(request, pk):
    user = request.session['id']
    if user:
        can = Candidate.objects.get(user_id=user)
        job = JobDetails.objects.get(id=pk)
        edu = request.POST['education']
        exp = request.POST['experience'] 
        web = request.POST['website']
        gender = request.POST['gender']
        resume = request.FILES['resume']
        min_salary = request.POST['minsalary'] 
        max_salary = request.POST['maxsalary']
        newapply = ApplyList.objects.create(candidate=can, job=job, education=edu, experience=exp, website=web, min_salary=min_salary, max_salary=max_salary, gender=gender, resume=resume)
        message="job applied successfully"
        return render(request, "apply.html", {'msg': message})


#### company side #####



# def CompanyIndexPage(request): 
#     return render(request, "company/index.html")

def CompanyProfilePage(request, pk):
    user = UserMaster.objects.get(pk=pk)
    comp = Company.objects.get(user_id=user)
    # print(comp.address)
    print(comp.firstname)
    return render(request, "companyprofile.html",{'user':user, 'comp':comp})
    

def UpdateCompanyProfile(request, pk):
    user = UserMaster.objects.get(pk=pk)
    if user.role == "Company":
        comp = Company.objects.get(user_id=user)
        comp.firstname = request.POST['firstname']
        comp.lastname = request.POST['lastname']
        comp.company_name = request.POST['companyname']
        comp.state = request.POST['state']
        comp.city = request.POST['city']
        comp.website = request.POST['website']
        comp.address = request.POST['address']
        comp.description = request.POST['description']
        comp.logo_pic = request.FILES['image']
        comp.save()
        url = f"/companyprofile/{pk}"
        return redirect(url)

def JobPostPage(request):   
    return render(request, "jobpost.html")

def JobDetailSubmit(request, pk):
    user = UserMaster.objects.get(id=pk)
    if user.role =="Company": 
        comp = Company.objects.get(user_id=user.id)
        # print(comp.id)
        companyemail = request.POST['companyemail']
        companycontact = request.POST['companycontact']
        jobname = request.POST['jobname'] 
        companyname = request.POST['companyname']
        address = request.POST['companyaddress']
        jobdescription = request.POST['jobdescription']
        qualification = request.POST['qualification']
        responsebility = request.POST['responbility'] 
        location = request.POST['location']
        salary = request.POST['salary']
        experience = request.POST['experience'] 
        website = request.POST['website']
        logo = request.FILES['image']
        newjob = JobDetails.objects.create(company_id=comp.id, jobname=jobname, companyname=companyname, companyaddress=address,jobdescription=jobdescription, qualification=qualification, resposibilties=responsebility, location=location, companywebiste=website, companyemail=companyemail, companycontact=companycontact, salarypackage=salary, experience=experience, logo=logo)

        message = "Job Post SuccessFully" 
        return render(request, "jobpost.html", {'msg':message})
def JobListPage(request, pk):
    user = request.session['id'] 
    i = Company.objects.get(user_id=user)
    all_job = JobDetails.objects.filter(company_id=i.id)
    return render(request, "jobpostlist.html",{'alljob' :all_job})

def CandidateJobListPage(request):
    all_job = JobDetails.objects.all()
    return render(request, "job-list.html", {'alljob' :all_job})
def CompanyLogout(request): 
    # del request.session['email'] 
    del request.session
    return redirect('loginpage')

def JobApplyList(request):
    all_jobapply = ApplyList.objects.all()
    return render(request, "applyjoblist.html", {'all_job': all_jobapply})

##### ADMIN SIDE #######


def AdminLoginPage(request):
    return render(request, "admin1/login.html")

def AdminIndexPage(request):
    if 'username' in request.session and 'password' in request.session: 
        return render (request, "admin1/index.html")
    else:
        return redirect('adminloginpage')
def AdminLogin(request):
    username = request.POST['username'] 
    password = request.POST['password']
    if username == "admin" and password=="admin":
        request.session['username'] = username
        request.session['password'] = password
        return redirect('adminindex')
    else:
        message = "Username and Password not Match"
        return render(request, "admin1/login.html", {'msg':message})

def AdminCompanyList(request):
    all_company = UserMaster.objects.filter(role="Company")
    return render(request, "admin1/companylist.html", {'allcompany': all_company})

def AdminUserList(request):
    all_user = UserMaster.objects.filter(role="Candidate")
    return render(request, "admin1/userlist.html", {'alluser': all_user})

def UserDelete(request, pk): 
    user = UserMaster.objects.get(pk=pk) 
    user.delete() 
    print(user)
    return redirect('userlist')

def VerifyCompanyPage(request, pk): 
    company = UserMaster.objects.get(pk=pk)
    if company:
        return render(request, "admin1/verify.html", {'company': company})

def VerifyComapny (request,pk):
    company = UserMaster.objects.get(pk=pk)
    if company:
        company.is_verified = request.POST['verify']
        company.save()
        return redirect('companylist')

def CompanyDelete(request, pk): 
    company = UserMaster.objects.get(pk=pk)
    company.delete()
    return redirect('companylist')


# This is my online job seaker project