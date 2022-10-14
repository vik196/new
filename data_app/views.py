from django.shortcuts import render,redirect
from data_app.models import employs
from data_app.models import students
 
# Create your views here.
def new(request):
    new_data= employs.objects.all()
    return render(request,'data.html', {'new_data':new_data})

def form_data(request):
    if request.method=="POST":
        name = request.POST['name']
        field = request.POST['field']
        salary = request.POST['salary']
        assets = request.POST['assets']

        data = employs(name=name,field=field,salary=salary,assets=assets)
        data.save()
        return redirect('new')
    return render(request,'forms.html')

#2

def newdata(request):
    newd= students.objects.all()
    return render(request,'calssdata.html', {'newd':newd})

def studens_data(request):
    if request.method=='POST':
        Name = request.POST['Name']
        Standard = request.POST['Standard']
        Subject = request.POST['Subject']
        Marks = request.POST['Marks']
        sports = request.POST['sports']

        stu = students(Name=Name,Standard=Standard,Subject=Subject,Marks=Marks,sports=sports)
        stu.save()
        return redirect('newdata')
    return render(request,'class10.htlm')  




    

