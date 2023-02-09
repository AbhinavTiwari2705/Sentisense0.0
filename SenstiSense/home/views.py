from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib.auth import login,logout
from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
import random
from datetime import datetime

import ktrain

# Create your views here.



def index(request):
    return render(request,'index.html')


def custom_404(request, exception=None):
    return render(request, "404.html", status=404)



def text(request):
    if User.is_authenticated: 
        predictor = ktrain.load_predictor('bert_model')
        model = ktrain.get_predictor(predictor.model, predictor.preproc)

        if request.method == 'POST':
            name = request.POST.get("text")

            predictions = model.predict(name)
            messages.info(request, "Your query is succesfully submitted")
            print(predictions)
            
            is_joy = predictions == "joy"
            is_anger = predictions == "anger"
            is_fear = predictions == "fear"
            is_neutral = predictions == "neutral"
            is_sadness = predictions == "sadness"
            is_surprise = predictions == "sadness"


            facts = [
            "Fact 1",
            "Fact 2",
            "Fact 3",
            "Fact 4",
            # ... add more facts as needed ...
        ]
            
            random_fact=random.choice(facts)

            context = {
                "is_joy": is_joy,
                "is_anger": is_anger,
                "is_fear": is_fear,
                "is_neutral": is_neutral,
                "is_sadness": is_sadness,
                "is_surprise": is_surprise,
                "random_fact": random_fact,
            }

            return render(request, 'text.html', {"predictions": predictions, **context})
    else:
        messages.error(request, 'Please log in first')

    return render(request, 'index.html')




def signup(request):

    try:
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
                    user=User.objects.create_user(username=User_name,password=User_pass1,email=User_email)
                    user.save()

            else:
                # message confirmation password not matching
                messages.info(request,'Password not matching with confirmed password')
                return redirect('/')

            return render(request,'index.html')


        else:
            return redirect('/')


    except Exception as e:
        print(e)

 

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
