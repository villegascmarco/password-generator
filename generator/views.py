from django.shortcuts import render
import random
import string

# Create your views here.
def home(request):
    length = int(request.POST.get('length',0))
    if not length:
        return render(request,"home.html")
        
    options=''

    if request.POST.get('uppercase',''):
        options+= string.ascii_uppercase
    if request.POST.get('lowercase',''):
        options+= string.ascii_lowercase
    if request.POST.get('numbers',''):
        options+= string.digits
    if request.POST.get('symbols',''):
        options+= string.punctuation
  
    generated_password=''
    for i in range(length):
        generated_password+= random.choice(options)

    return render(request,"home.html",{'generated_password':generated_password, 'length':length})
