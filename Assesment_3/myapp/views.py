from django.shortcuts import render,redirect
from .models import signup_model,members_model,events_model
from django.contrib.auth import logout
from .forms import members_form,editmembers_form,signup_update_form,events_form,editevent_form
from django.core.mail import send_mail
from Assesment_3 import settings
from django.contrib import messages

# Create your views here.

def index (request):

    if request.method == 'POST':
        unm = request.POST['username']
        pas = request.POST['password']

        user = signup_model.objects.get(username=unm)
        var = signup_model.objects.filter(username=unm,password=pas)
        if var :
            print ('LogIn Successfully!')
            request.session['username']=unm
            request.session['userid']=user.id

            return redirect('home')
        else :
            print('Error! Login Failed')

    return render (request, 'index.html')

def forget (request):

    if request.method == 'POST':
        unm = request.POST['username']
        userdata = signup_model.objects.get(username=unm)
        
        # send mail to user :-

        subject = 'Forget Password'
        message = f'Dear user, \n\nYour password is {userdata.password} \n\nNever Share Your password to any one.'
        mail = settings.EMAIL_HOST_USER
        maillist = [userdata.mail]

        # send_mail(subject=subject,message=message,from_email=mail,recipient_list=maillist)

        messages.success(request,'Your Password has been Sent in Your registered E-Mail')

    return render (request, 'forget.html')

def profile (request):

    uid = request.session.get('userid')
    userdata = signup_model.objects.get(id=uid)
    usersignupdata =  signup_model.objects.get(id=uid)

    if request.method == 'POST':
        updatedata = signup_update_form(request.POST)
        if updatedata.is_valid():
            updatedata = signup_update_form(request.POST,instance=usersignupdata)
            updatedata.save()
            print('Your Data has been updated.')
        else:
            print (updatedata.errors)

    return render (request, 'profile.html',{'userdata':userdata})

def home (request):

    username = request.session.get('username')

    return render (request, 'home.html',{'user':username})

def userlogout (request):

    logout(request)
    print ('Logout! Successfully.')

    return redirect ('/')

# Society Member :-

def societymember (request):

    if request.method == 'POST':
        mem = members_form(request.POST)
        if mem.is_valid():
            mem.save()
            print ('Society Member data has been added successfully.')

        else :
            print (mem.errors)

    return render (request,'societymember.html')

def editsocietymember (request):

    memberdata = members_model.objects.all()

    if request.method == 'POST':

        Member_id = request.POST.get('id')
        Member_data = members_model.objects.get(id=Member_id)

        memedit = editmembers_form(request.POST)
        if memedit.is_valid():
            memedit = editmembers_form(request.POST,instance=Member_data)
            memedit.save()
            print('Your data has been updated successfully')

        else:
            print(memedit.errors)


    return render (request,'editsocietymenber.html',{'memberdata':memberdata})

def deletemember (request,id):

    member_id = members_model.objects.get(id=id)
    member_id.delete()

    messages.error(request,'Your member has been successfully.')

    return redirect ('editsocietymember')

# Society Watchmen :- 

def watchmen (request):

    return render (request,'watchmen.html')

def editwatchmen (request):

    return render (request,'editwatchmen.html')

# Events :-

def events (request):

    if request.method == 'POST':
        eve = events_form(request.POST,request.FILES)
        if eve.is_valid():
            eve.save()
            print('event is updated successfully.')
            messages.success(request,'event is updated successfully.')
        else :
            print (eve.errors)

    return render (request,'Events.html')

def editevent (request):
    
    eventdata = events_model.objects.all()

    if request.method == 'POST':

        event_id = request.POST.get('id')
        event_data = events_model.objects.get(id=event_id)

        eveedit = editevent_form(request.POST,request.FILES)
        if eveedit.is_valid():
            eveedit = editevent_form(request.POST,request.FILES,instance=event_data)
            eveedit.save()
            print('Your data has been updated successfully')

        else:
            print(eveedit.errors)


    return render (request,'editevent.html',{'eventdata':eventdata})

def deleteevent (request,id):

    event_id = events_model.objects.get(id=id)
    event_id.delete()

    messages.error(request,'Your Event has been deleted successfully.')

    return redirect ('editevent')

# Notices :- 

def notices (request):

    return render (request,'notices.html')

def notice_view (request):

    return render (request,'notice_view.html')
