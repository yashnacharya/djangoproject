from django.urls import path, include, re_path
from django.conf.urls.static import static
from django.conf import settings
from . import views
urlpatterns = [

    path("", views.Indexpage, name="index"),
    path("signup/", views.SignupPage, name="signup"),
    path("register/", views.RegisterUser, name="register"),
    path("otppage/", views.OtpPage, name="otppage"),
    path("otp/", views.Otpverify, name="otp"),
    path("loginpage/", views.LoginPage, name="loginpage"),
    path("loginuser/", views.LoginUser, name="login"),    
    path("profile/<int:pk>", views.ProfilePage, name="profile"),
    path("updateprofile/<int:pk>", views.UpdateProfile, name="updateprofile"),
    path("joblist/",views.CandidateJobListPage, name="joblist"),
    path("apply/<int:pk>", views.ApplyPage, name="apply"),
    path("applyjob/<int:pk>", views.ApplyJob, name="applyjob"),


    ### Company Side ####ProfilePage
    # path("companyindex/", views.CompanyIndexPage, name="companyindex"),
    path("companyprofile/<int:pk>", views.CompanyProfilePage, name="companyprofile"),
    path("updatecompanyprofile/<int:pk>", views.UpdateCompanyProfile, name="updatecompanyprofile"), 
    path("jobpostpage/", views.JobPostPage, name="jobpostpage"), 
    path("jobpost/<int:pk>", views.JobDetailSubmit, name="jobpost"), 
    path("jobpostlistpage/<int:pk>", views.JobListPage, name="joblistpage"), 
    path("companylogout/", views.CompanyLogout,name="companylogout"), 
    path("applyjoblist/", views.JobApplyList,name="applylist"),
    
    

    ##### ADMIN SIDE #######
    
    path("adminloginpage/",views.AdminLoginPage,name="adminloginpage"),
    path("adminindex/", views.AdminIndexPage,name="adminindex"), 
    path("adminlogin/", views.AdminLogin, name="adminlogin"),
    path("adminuserlist/", views.AdminUserList,name="userlist"), 
    path("admincompanylist/", views.AdminCompanyList, name="companylist"),
    path("deleteuser/<int:pk>", views.UserDelete, name="userdelete"),
    path("verifycompanypage/<int:pk>", views.VerifyCompanyPage, name="verifypage"), 
    path("verifycompany/<int:pk>", views.VerifyComapny, name="verify"),
    path("deletecompany/<int:pk>", views.CompanyDelete, name="companydelete"),
]  
if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)