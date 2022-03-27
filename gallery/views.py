from multiprocessing import context
# from unicodedata import category
from urllib import request
from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from gallery.models import Image, Category, Location
# from django.template import Template



# Create your views here.

def index(request):
    categories=Category.objects.all()  
    images = Image.objects.all()
    return render (request, 'all-gallery/index.html', {'images': images, 'categories': categories})


def image(request):  
    categories = Category.objects.all()
    context = {'categories': categories}
    return render(request,'all-gallery/image.html',context)


def imagedisplay(request):  
    resultsdisplay=Image.objects.all()
    return render(request,'all-gallery/image.html',{'image':resultsdisplay})

# def category(request):
    
#     return render(request, 'all-gallery/navbar.html')      

def search_results(request):  
    categories=Category.objects.all()  
    locations=Location.objects.all()  
    # print(request.GET.get("image_category"))

    if 'image_category' in request.GET and request.GET["image_category"]:
        search_term = request.GET.get("image_category")
        searched_images = Image.search_by_category(search_term)
       
        message = f"{search_term}"    

        return render(request, 'all-gallery/index.html',{"message":message,"images": searched_images, categories :categories, locations :locations})

    else:
        images = Image.objects.all()
        message = "You haven't searched for any term"
        return render(request, 'all-gallery/index.html',{"message":message, 'images': images})   







def image_upload(request):
    
    return render(request,'all-gallery/image.html',{'image'})


# def upload_image(request):
#     if request.method == "POST":
    
#         uploaded=ImageForm(data=request.POST, files=request.FILES,  request=request)
#         if uploaded.is_valid():
#             uploaded.save()
            
#             return redirect('show_all_images')  
#     else:
#         up=ImageForm()    
        
#         return render(request,"imagesapp/upload.html",{"up":up})    









