from django.contrib import messages
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect

from django.shortcuts import render, get_object_or_404

from .models import Department, Course , Details

# Create your views here.


def allDept(request, d_slug=None):
    c_page = None
    # course_list = None
    if d_slug != None :
       c_page = get_object_or_404(Department, slug=d_slug)

    return render(request, 'index.html', {'department': c_page })


def deptDetail(request, d_slug):
    course_list = None
    try:
        dept = get_object_or_404(Department, slug=d_slug)
        course_list = Course.objects.all().filter(department__slug=d_slug, seat_available=True)
    except Exception as e:
        raise e
    return render(request, 'departments.html', {'department': dept,'course':course_list})


def student_Details(request):
    return render(request,'details.html')


def add_studDetails(request):
     if request.method == "POST":
         name = request.POST.get('name','')
         dob = request.POST.get('dob','')
         age = request.POST.get('age','')
         gender = request.POST.get('gender','')
         phn = request.POST.get('phn','')
         email = request.POST.get('email','')
         address = request.POST.get('address','')
         department = request.POST.get('department','')
         course = request.POST.get('course','')
         purpose = request.POST.get('purpose','')
         materials = request.POST.get('material1','')+request.POST.get('material2','')+request.POST.get('material3','')
         details = Details(name=name,dob=dob,age=age,gender=gender,phn=phn,email=email,address=address,
                           department=department,course=course,purpose=purpose,materials=materials)
         if details.save():
            messages.success(request, 'Details submission successful')
            return redirect('/')

         else:
            messages.error(request, 'Details submission wes not completed')
            return render(request, 'student_Details')


def course_list(request):
    dept = request.POST.get('deptName')
    # get instances
    course = Course.objects.filter(department=dept)
    return JsonResponse({"status_code": 200,"instances": course})