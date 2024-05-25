from django.shortcuts import render,redirect
from django.views.generic import View
from work.forms import Register,Loginform,Taskform
from work.models import User,Taskmodel
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.utils.decorators import method_decorator

def singin_required(fn):

    def wrapper(request,**kwargs):

        if not request.user.is_authenticated:

            return redirect('login')
        else:
            return fn(request,**kwargs)
    return wrapper

def mylogin(fn):

    def wrapper(request,**kwargs):

        id=kwargs.get('pk')
        obj=Taskmodel.objects.get(id=id)

        if obj.user!=request.user:
            return redirect('login')
        
        else:
            return fn(request,kwargs)
    return wrapper

class Registration(View):

    def get(self,request,**kwargs):

        form=Register()

        return render (request,'Registration.html',{'form':form})
    
    def post(self,request,**kwargs):

        form=Register(request.POST)

        if form.is_valid():

            User.objects.create_user(**form.cleaned_data)


        return redirect ('login')


class Signin(View):

    def get(self,request,**kwargs):

        form=Loginform()

        return render(request,"login.html",{'form':form})
    
    def post(self,request,**kwargs):

        form=Loginform(request.POST)

        if form.is_valid():

            u_name=form.cleaned_data.get('username')
            pwd=form.cleaned_data.get('password')

            user_obj=authenticate(username=u_name,password=pwd)

            if user_obj:

                login(request,user_obj)
                return redirect('index')
            
            else:
                return render(request,"login.html")
            

@method_decorator(singin_required,name='dispatch')            
class Add_task(View):

    def get(self,request,**kwargs):
        
        form=Taskform()
        data=Taskmodel.objects.filter(user=request.user).order_by('completed')

        return render(request,'index.html',{'form':form,'data':data})
    
    def post(self,request,**kwargs):

        form=Taskform(request.POST)

        if form.is_valid:   
            form.instance.user=request.user
            form.save()
            messages.success(request,'added sucessfully')
            
            form=Taskform()
            data=Taskmodel.objects.filter(user=request.user).order_by('completed')

        return render(request,'index.html',{'form':form,'data':data})
    
@method_decorator(singin_required,name='dispatch')  
@method_decorator(mylogin,name='dispatch')  
class Delete_task(View):

    def get(self,request,**kwargs):

        id=kwargs.get('pk')
        Taskmodel.objects.get(id=id).delete()

        return redirect('index')
    
@method_decorator(singin_required,name='dispatch')  
@method_decorator(mylogin,name='dispatch')      
class Taskedit(View):
     def get(self,request,**kwargs):

        id=kwargs.get('pk')
        data=Taskmodel.objects.get(id=id)

        if data.completed==False:
            data.completed=True
            data.save()
            return redirect('index')
        else:
            data.completed=False
            data.save()
            return redirect('index')
        
class Signout(View):

    def get(self,request):

        logout(request)

        return redirect('login')


class Del_user(View):

    def get(self,request,**kwargs):

        id=kwargs.get('pk')
        User.objects.get(id=id).delete()

        return redirect('regis')
        
class Update_user(View):

    def get(self,request,**kwargs):

        id=kwargs.get("pk")
        data=User.objects.get(id=id)
        form=Register(instance=data)

        return render(request,'Registration.html',{'form':form})
    

    def post(self,request,**kwargs):
        id=kwargs.get("pk")
        data=User.objects.get(id=id)
        form=Register(request.POST,instance=data)

        if form.is_valid():
            form.save()

        return redirect('login')









