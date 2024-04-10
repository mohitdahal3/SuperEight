from django.shortcuts import render
from webapp.models import Row

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