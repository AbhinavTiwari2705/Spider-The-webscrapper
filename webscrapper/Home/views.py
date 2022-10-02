from email import message
from turtle import clear
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import messages
from django.contrib import sessions

import requests
import bs4
import csv
value=[]
# values=[]




def index(request):
    return render(request,'index.html')

def Extension(request):
   


    
  
    if request.method =='POST':
    
        
        form = request.POST['your_url']
        if(len(form) == 0):
            messages.warning(request, "Please input Something")
            return render(request,'Extension.html')

        else:

            response= requests.get(form)
            scrapval= bs4.BeautifulSoup(response.text,"html.parser")
            messages.success(request, "Your file is ready to download!")
            for data in scrapval.find_all('img'):
                srcval =data.get('src')
                print(srcval)
                value.append(srcval)
                

            

        
            

    return render(request,'Extension.html',{'value':value})






 


def CSV(request):
    # Create the HttpResponse object with the appropriate CSV header.
    # response = HttpResponse(
    #     content_type='text/csv',
    #     headers={'Content-Disposition': 'attachment; filename="loo_Tumhari_CSV_File.csv"'},

    # )
    
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="csv_simple_write.csv"'

    writer = csv.writer(response)
    # writer.writerow(['First row', 'Foo', 'Bar', 'Baz'])
    
    writer.writerow(i for i in range(0,100))
    # for i in value:
    #     print('***')

    # print('***' for  in value)

    
    # for values in value:
    
    writer.writerow(value)

    return response







