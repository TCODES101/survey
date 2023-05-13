from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages
import re
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.core.mail import send_mail
from django.conf import settings

#pdf
from django.http import HttpResponse
from io import BytesIO
from django.template.loader import get_template
from xhtml2pdf import pisa


def graduatesPdf(request):
    graduates=outrunsGraduates.objects.all()
    template_path='gpdf.html'
    context= {'graduates':graduates}
    response=HttpResponse(content_type='application/pdf')
    response['content-disposition']='attachment; filename="graduatereport.pdf"'

    template=get_template(template_path)
    html=template.render(context)

    pisa_status=pisa.CreatePDF(
        html, dest=response)
    if pisa_status.err:
        return HttpResponse('we had some errore<pre>'+html+'</pre>')
    return response
def intakePdf(request):
    intake=studentIntake.objects.all()
    
    template_path='ipdf.html'
    context= {'intake':intake}
    response=HttpResponse(content_type='application/pdf')
    response['content-disposition']='attachment; filename="intakereport.pdf"'

    template=get_template(template_path)
    html=template.render(context)

    pisa_status=pisa.CreatePDF(
        html, dest=response)
    if pisa_status.err:
        return HttpResponse('we had some errore<pre>'+html+'</pre>')
    return response
def staffPdf(request):
    staff=staffTotal.objects.all()
    template_path='staffPdf.html'
    context= {'staff':staff}
    response=HttpResponse(content_type='application/pdf')
    response['content-disposition']='attachment; filename="staffreport.pdf"'

    template=get_template(template_path)
    html=template.render(context)

    pisa_status=pisa.CreatePDF(
        html, dest=response)
    if pisa_status.err:
        return HttpResponse('we had some errore<pre>'+html+'</pre>')
    return response
def ssPdf(request):
    shortage=skillShortage.objects.all()
    template_path='ssPdf.html'
    context= {'shortage':shortage}
    response=HttpResponse(content_type='application/pdf')
    response['content-disposition']='attachment; filename="shortagereport.pdf"'

    template=get_template(template_path)
    html=template.render(context)

    pisa_status=pisa.CreatePDF(
        html, dest=response)
    if pisa_status.err:
        return HttpResponse('we had some errore<pre>'+html+'</pre>')
    return response
def cPdf(request):
    challenge=challenges.objects.all()
    template_path='cPdf.html'
    context= {'challenge':challenge}
    response=HttpResponse(content_type='application/pdf')
    response['content-disposition']='attachment; filename="challengesreport.pdf"'

    template=get_template(template_path)
    html=template.render(context)

    pisa_status=pisa.CreatePDF(
        html, dest=response)
    if pisa_status.err:
        return HttpResponse('we had some errore<pre>'+html+'</pre>')
    return response

def challenge(request):
    context={'challenge':challenges.objects.all()}
    return render(request, 'challenges.html',context)


def staff(request):
    context={'staff':staffTotal.objects.all()}
    return render(request, 'staffnumber.html',context)
def skill(request):
    context={'skill':skillShortage.objects.all()}
    return render(request, 'skillshortage.html',context)
def graduates(request):
    context={'graduates':outrunsGraduates.objects.all()}
    return render(request, 'graduate.html', context)
def intake(request):
    context={'intake':studentIntake.objects.all()}
    return render(request,'intake.html',context)

def admin2(request):
    context={'number':str(generalParticulars.objects.all().count()),
                 'privateInstitution':str(generalParticulars.objects.filter(InstitutionType='Private').count()),
                 'publicInstitution':str(generalParticulars.objects.filter(InstitutionType='Public').count()),
                 'allSchools':generalParticulars.objects.values('Institution', 'InstitutionType').order_by('-id')[:5]
                 }
    return render(request, 'admin2.html',context)
def index(request):
    return render(request, 'index.html')


def collect(request):
    if request.method == 'POST':
        institution = request.POST['institution']
        county = request.POST['counties']
        subcounty = request.POST['subC']
        building = request.POST['building']
        floor = request.POST['floors']
        town = request.POST['town']
        postaladdress = request.POST['postalAddress']
        postalcode = request.POST['postalCode']
        telephone = request.POST['tNumber']
        phone = request.POST['pNumber']
        email = request.POST['email']
        institutioncategory = request.POST['institutionCategory']
        institutionType = request.POST['institutionType']


        #SECOND FORMSTEP
        course1 = request.POST['course']
        courselevel = request.POST['courseLevel']
        cost = request.POST['cost']
        intakeyear = request.POST['intakeYear']
        gender = request.POST['Gender']


        #THIRD FORM STEP
        course2 =request.POST['programmeCourse']
        courseLevel2 = request.POST['courseLevel2']
        courseDuration = request.POST['cDuration']
        examiningBody = request.POST['examiningBody']
        year = request.POST['year']
        gender2 = request.POST['gender2']


        #FOURTH FORMSTEP
        numberOfStaff = request.POST['numberOfStaff']
        numberOfStaffWithDissability = request.POST['pwd']
        skillArea = request.POST['skillArea']
        skillLevel = request.POST['skillLevel']
        gender3 = request.POST['gender3']


        #FIFTH FORMSTEP
        SkillArea2 = request.POST['sArea']
        skilllevelRequired = request.POST['skillLevelRequired']
        optimal = request.POST['optimal']
        inPostGender = request.POST['inPostGender']
        shortFall = request.POST['shortfall']
        reasonsForShortFall = request.POST['shortfallReasons']


        #SIXTH FORM STEP
        covidEffects = request.POST['covideEffects']
        otherChallenges = request.POST['otherChallenges']
        otherChallengesSelected = request.POST['challengeSelect']
        Name = request.POST['name']
        contactNumber = request.POST['contactNumber']
        emailAddress = request.POST['email']
        Date = request.POST['date']
        officer = request.POST['officer']

        #fetching and saving data
        if postalcode=='' or telephone=='' or phone=='' or cost=='' or numberOfStaff=='' or numberOfStaffWithDissability=='' or contactNumber=='' or Date=='':
            messages.info(request, 'All fields must be filled!')
            return render(request, 'index.html')

        else:
            GParticulars=generalParticulars( Institution=institution,County=county, Subcounty=subcounty,Building=building,Floor=floor,
                                            Town=town, Postaladdress=postaladdress,Postalcode=postalcode, Telephone=telephone, 
                                            Phone=phone, Email=email,Institutioncategory=institutioncategory, InstitutionType=institutionType)
            GParticulars.save()

            SIntake=studentIntake(Institution=institution,Course=course1,Courselevel=courselevel,Cost=cost,Intakeyear=intakeyear,Gender=gender)
            SIntake.save()

            OGraduates=outrunsGraduates(Institution=institution,Course=course2,CourseLevel=courseLevel2,CourseDuration=courseDuration,
                                        ExaminingBody=examiningBody,Year=year,Gender=gender2)
            OGraduates.save()

            STotal=staffTotal(Institution=institution,NumberOfStaff=numberOfStaff,NumberOfStaffWithDissability=numberOfStaffWithDissability,
                            SkillArea=skillArea,SkillLevel=skillLevel,Gender=gender3)
            STotal.save()

            SShortage=skillShortage(Institution=institution,SkillArea=SkillArea2,SkilllevelRequired=skilllevelRequired, Optimal=optimal, 
                                    InPostGender=inPostGender,ShortFall=shortFall, ReasonsForShortFall=reasonsForShortFall)
            SShortage.save()

            chhallenges=challenges(Institution=institution,CovidEffects=covidEffects, OtherChallenges=otherChallenges, OtherChallengesSelected=otherChallengesSelected,
                                    name=Name, ContactNumber=contactNumber, EmailAddress=emailAddress,date=Date,Officer=officer)
            chhallenges.save()



            
            return render(request, 'index.html')


def signup(request):
    return render(request, 'signup.html')
def loginf(request):
    return render(request, 'login.html')
def logoutUser(request):
    logout(request)
    return render(request,'login.html')
def loginProcess(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user =authenticate(request, username=username, password=password)

    if user is not None:
        login(request, user)
        
        return redirect('admin2')
    else:
        messages.info(request, 'Credentials invalid')
        return redirect('loginf')
  

    

def signupProcess(request):
    if request.method=='POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['repeatPassword']
        pl = len(password)
        subject = 'ADMIN'
        message = 'Welcome. You are the new admin'
        from_email = settings.EMAIL_HOST_USER
        recipient_list = [email]
        reg=re.compile('[@_!#$%^&*()~:/\|]')

        if password == password2:
            if User.objects.filter(email=email).exists():
                messages.info(request, 'Email already exists')
                return redirect('signupProcess')
            elif User.objects.filter(username=username).exists():
                messages.info(request, 'Username already used')
                return redirect('signupProcess')
            elif(pl < 8):
                messages.info(request, 'password must be 8 or more characters')
                return redirect('signupProcess')
            elif reg.search(password)==None:
                messages.info(request, 'password must contain special characters eg. @ # $')
                return redirect('signupProcess')

            else:
                user = User.objects.create_user(
                    username=username, email=email, password=password)
                user.save()
                #send_mail(subject, message, from_email,
                         # recipient_list, fail_silently=False)
                return render(request,'login.html')

        else:
            messages.info(request, 'Password not the same')
            return redirect('signup')

    else:
        return render(request, 'signUp.html')
