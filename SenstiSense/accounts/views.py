from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib.auth import login,logout
from django.contrib import messages

# Create your views here.



def signup(request):
    if request.method=='POST':
        User_name=request.POST.get("newusername")
        User_email=request.POST.get("newusername_email")
        User_pass1=request.POST.get("newusername_password1")
        User_pass2=request.POST.get("newusername_password2")

        if User_pass1==User_pass2:

            # message daal ki username taken
            if User.objects.filter(username=User_name).exists():

                messages.info(request,'Username already Taken')
                # messege daal user exists
                return redirect('/')

            elif User.objects.filter(email=User_email).exists():
                messages.info(request,'Email exits already')
                return redirect('/')
            else:
                user=User.objects.create_user(username=User_name,password=User_pass1)
                user.save()

        else:
            # message confirmation password not matching
            messages.info(request,'Password not matching with confirmed password')
            return redirect('/')

        return (request,'index.html')


    else:
        return redirect('/')

 

def login_user(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        # Redirect to a success page.
        messages.info(request,'user logged in')
        return redirect('/')
        
    else:
        # Return an 'invalid login' error message.

        messages.info(request,'Invalid credentials')

        return redirect('/')
        
        
def logout_user(request):
    logout(request)
    messages.info(request,'You have been succesfully logged out!')
    return redirect('/')
