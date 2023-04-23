from django.shortcuts import render

from .models import Post

# Create your views here.



# Create your views here.
def index(request):
        posts = Post.objects.all()
        return render(request,'index.html', {'posts':posts})


def post(request, pk):
        posts = Post.objects.get(id=pk)
        
        return render(request,'post.html', {'posts':posts})


def usage(request):
    
    return render(request,'terms_of_use.html')

def privacy(request):
    
    return render(request,'PrivacyNotice.html')

def contact(request):
    
    return render(request,'contactus.html')