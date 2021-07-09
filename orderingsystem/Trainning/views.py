from django.shortcuts import render, redirect
from django.contrib import messages
from datetime import datetime
from django.http import HttpResponse
from .models import Trainning, Detail, Feedback

from django.conf import settings




# Create your views here.
def showIndex(request):
    if request.method == 'POST':
        
        name = request.POST['name']
        email = request.POST['email']
        contact = request.POST['contact']
        location = request.POST['location']
        error_message = None
       
        if(not name):
            
            messages.warning(request, 'Name required')
            return render(request, 'index.html',{'error_message':error_message})
        if(not contact):
            
            messages.warning(request, 'Contact required')
            return render(request, 'index.html',{'error_message':error_message})
        
        if(not location):
            
            messages.warning(request, 'Location required')
            return render(request, 'index.html',{'error_message':error_message})

        if not error_message:
        
            train = Trainning(name=name, email=email, contact=contact, location=location)
            train.save()
            messages.warning(request, 'Details submitted..Wait for verificaion Call')
            det = Detail.objects.all()
            return render(request, 'index.html',{'det':det})
       
    else:
        
        det = Detail.objects.all()

        return render(request, 'index.html', {'det':det})
       

   

def showTrainningDetails(request):
    train = Trainning.objects.all()
    return render(request, 'trainningdetails.html',{'train':train})



def delete(request, id):
    train = Trainning.objects.get(id=id)
    train.delete()
    return redirect('/trainningdetails')



def contactus(request):
    if request.method == 'POST':
        
        name = request.POST['name']
        phone = request.POST['phone']
        message = request.POST['message']
        feedbacks = Feedback(name=name, phone=phone, message=message)
        feedbacks.save()
        messages.warning(request, 'Feedback Submitted')
        return render(request, 'index.html')
   

    else:
        
        

        return render(request, 'contactus.html')
       

def feedback(request):
        feedbacks = Feedback.objects.all()
    
        return render(request, 'feedback.html',{'feedbacks':feedbacks})
   

  
