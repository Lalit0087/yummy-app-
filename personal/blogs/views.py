from django.shortcuts import render,redirect
from blogs.forms import AdminForm,BlogsForm,CommentsForm
from blogs.models import Admin,Blogs,Comments

#from django.contrib.auth.models import User
#from django.contrib.auth import authenticate, login
from datetime import date,datetime,time
# Create your views here.

def show(request):
    return render(request, 'index.html', {})

def blog(request):
    cmnts = CommentsForm(request.POST)
    commentsform=CommentsForm(request.POST)

    #for showing comments 
    data =  Comments.objects.all()
    print(data)

    if request.method == "POST":
          
        username= request.POST.get('ename')
        useremail= request.POST.get('eemail')
        usercomments= request.POST.get('ecomments')
         
        print(username)
        print(useremail)
        cmnts.save()
        return redirect("/cmntstable")
        
    return render(request, 'blog.html', {'cmnts':cmnts,'commentsform':commentsform, 'data':data})

def login(request):
    if request.method == "POST":  
        form = AdminForm(request.POST)  
        textename= request.POST.get('ename')
        textepassword= request.POST.get('epassword') 
        admincheck=Admin.objects.all()
        admincheck=Admin.objects.raw("SELECT * from admin where ename=%s and epassword=%s",[textename,textepassword])
        
        print("admin check starts")
        print(admincheck)
        if not admincheck:
            print("Not login") 
            return redirect("/adminlogin")
        else:
        # Do that...
            print(" login successfuly")
            return redirect("/dashboard")

        #try:  
                     
         #   return redirect('/')  
        #except:  
         #   pass  
    else:  
        form = AdminForm()  
    return render(request, 'login.html', {'form':form})

def dashoard(request):
    return render(request, 'dashboard.html', {})

def blogtable(request):

    blogsdata=Blogs.objects.raw("SELECT * from blogs ")
        
    return render(request, 'blog_table.html', {'blogsdata':blogsdata})

def addblog(request):
    #
    forms = BlogsForm(request.POST)    
    if request.method == "POST":
          
        blogname= request.POST.get('etitle')
        blogdescription= request.POST.get('edescription')
        print(blogname)
        print(blogdescription)
        forms.save()
        return redirect("/blogtable") 
      # date=datetime.datetime.now()
    
    return render(request, 'add_blog.html', {'forms':forms})

def cmntstable(request):

    cmntsdata=Comments.objects.raw("SELECT * from comments ")
    print(cmntsdata)
    return render(request, 'comments_table.html', {'cmntssdata':cmntsdata})

#def blogs(request):
    #return render(request, 'blogs.html', {})

#def contact(request):
    #return render(request, 'contact.html', {})        

#def recipe(request):
    #return render(request, 'recipe.html', {})