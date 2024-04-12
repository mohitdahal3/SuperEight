from django.shortcuts import render, redirect, HttpResponse
from webapp.models import Row, ContactMessage
from django.contrib import messages
import re

# Create your views here.
def home(request):
    allColumns = Row._meta.get_fields()
    allRows = Row.objects.all()

    numColsToShow = 0 #The number of columns to show in the page
    for row in allRows:
        colIndex = 0 #This value tracks how many columns in the particular row can be shown
        counter = 1 #This is the counter to track which column of the particular row we are at.
        for col in allColumns[1:]:
            value = getattr(row , col.name)
            if value is not None and value.strip() != '': #If the value exists, all columns upto and including that column can be shown
                colIndex = counter
            counter += 1
        if colIndex > numColsToShow: #If the showable columns in this particular row is greater than previous columns, this is the number of columns to show in the page
            numColsToShow = colIndex
    


    myRows = []
    for row in allRows:
        myRow = []
        for column in allColumns[1:numColsToShow+1]:
            myRow.append(getattr(row , column.name))
        myRows.append(myRow)

        

    dictionary = {
        'myRows' : myRows
    }

        
    return render(request , 'webapp/home.html' , dictionary)


def sendMessage(request):
    if request.method == "POST":
        _name = request.POST.get('name' , "")
        _email = request.POST.get('email' , "")
        _message = request.POST.get('message' , "")

        if(_name.strip() == ""):
            messages.error(request , "Name can not be blank.")
            return redirect("/")
        elif(validate_email_canbeempty(_email) == False):
            messages.error(request , "Enter a valid email.")
            return redirect("/")
        else:
            try:
                newMessage = ContactMessage(name = _name , email = _email , message = _message)
                newMessage.save()
                messages.success(request , "Message sent Successfully.")
                return redirect("/")
            except:
                messages.error(request , "An unexpected error has occurred.")
                return redirect("/")

    return HttpResponse("404 Not Found!")





def validate_email_canbeempty(email):
    if (email.strip() == "" or email is None):
        return True
    else:
        pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        return re.match(pattern, email) is not None