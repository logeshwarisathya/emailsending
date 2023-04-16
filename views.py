from django.shortcuts import render,redirect
from django.http import HttpResponse
from cbvapp.form import MarksForm
from cbvapp.models import Marks
from django.views import View
from django.conf import settings
from django.core.mail import send_mail
from django.views.generic import CreateView
# Create your views here.

# --------------fbv---------
def MarksFbv(request):
    form=MarksForm()
    if request.method=='POST':
        form=MarksForm(request.POST)
        if form.is_valid():
            form.save()
            name=form.cleaned_data['name']
            email=form.cleaned_data['email']
            tamil=form.cleaned_data['tamil']
            english=form.cleaned_data['english']
            maths=form.cleaned_data['maths']
            science=form.cleaned_data['science']
            social=form.cleaned_data['social']
            subject = f'HI {name} your report card'
            message = f'''tamil:-{tamil},
                           english:-{english},
                           maths:-{maths},
                            science:-{science},
                            social:-{social},
            '''
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [email,]
            send_mail( subject, message, email_from, recipient_list )


            return HttpResponse(f'data is stored and email is sent to {email}')
    return render(request,'markscbv.html',{'form':form})

def Readfbv(request):
    data=Marks.objects.all()
    return render(request,'marksread',{'data':data})

def Updatefbv(request,pk):
    data=Marks.objects.get(id=pk)
    form=MarksForm(instance=data)
    if request.method=='POST':
        form=MarksForm(request.POST,instance=data)
        if form.is_valid():
            form.save()
            return redirect('cbv/readcbv/')
    return render(request,'markscbv.html',{'form':form})

# ----------------------------user defined cbv-------
class MarksCbv(View):
    def get(self,request):
        form=MarksForm()
        return render(request,'markscbv.html',{'form':form})
    
    def post(self,request):
        form =MarksForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('data is stored')
        
class ReadCbv(View):
    def get(self,request):
        data=Marks.objects.all()
        return render(request,'marksread.html',{'data':data})


class UpdateCbv(View):
    def get(self,request,pk):
        data=Marks.objects.get(id=pk)
        form=MarksForm(instance=data)
        return render(request,'marksupdate.html',{'form':form})
    
    def post(self,request,pk):
        data=Marks.objects.get(id=pk)
        form=MarksForm(request.POST,instance=data)
        if form.is_valid():
            form.save()
            return redirect('/cbv/readcbv/')
    

# ...........................PREDEFINED CLASS BASE VIEWS...........................

# class Marks_PCEV()