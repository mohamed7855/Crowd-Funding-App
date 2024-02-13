from django.shortcuts import render,HttpResponse

# Create your views here.

def mainPage(request):
     # images = ['iot.jpg', 'os.jpg', 'php.jpg'] 
     return  render(request,'index.html')

    # return HttpResponse("Hello omara World")

# views.py


# def slider_view(request):
#     # List your image filenames here
#     return render(request, 'your_app/slider.html')
