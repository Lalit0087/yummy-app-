from django import forms  
from  blogs.models import Admin 
from  blogs.models import Blogs
from  blogs.models import Comments

class AdminForm(forms.ModelForm): 
    ename= forms.CharField(widget=forms.TextInput(attrs={'class':'un','placeholder':'Enter User Name'}))
    epassword= forms.CharField(widget=forms.PasswordInput(attrs={'class':'pass','required':'required','placeholder':'Enter Password'}))
    class Meta:  
        model = Admin  
        fields = "__all__"  

class BlogsForm(forms.ModelForm): 
    etitle=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Blog Title'}))
    edescription=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Blog Descreption'}))
    # eimagepath=forms.FileField()
    class Meta:  
        model = Blogs  
        fields = "__all__"  

class CommentsForm(forms.ModelForm): 
    ename=forms.CharField(widget=forms.TextInput(attrs={'class':'comment-form','placeholder':'Your name'}))
    eemail=forms.CharField(widget=forms.TextInput(attrs={'class':'comment-form','placeholder':'Your email'}))
    ecomments=forms.CharField(widget=forms.Textarea(attrs={'class':'comment-form','placeholder':'Comment'}))
    
    class Meta:  
        model = Comments  
        fields = "__all__"  