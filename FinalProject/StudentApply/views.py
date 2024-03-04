from django.shortcuts import render , redirect
from StudentApply.models import Student , Mentor ,Adminstration ,AbsentReason
from django.http import HttpResponse ,HttpResponseRedirect
from django.urls import reverse
from django.db.models import Q


# Create your views here.

def index(request):

    return render(request, 'index.html')
    
def adminlogin(request):
    if request.method == 'POST':
        AdminID = request.POST['AdminID']
        Password = request.POST['password']
        try:
            user = Adminstration.objects.get(AdminId = AdminID , Password=Password)
            request.session['Adminstration'] = user.AdminId
            return redirect('admin')
        except Adminstration.DoesNotExist:
            return render(request, 'adminlogin.html', {'error': 'Invalid credentials'})
    else:
        return render(request, 'adminlogin.html')
    
def admin(request):
    if 'Adminstration' in request.session:
        user=request.session['Adminstration']
        Record = AbsentReason.objects.all().values()
        admin = Adminstration.objects.all().first()
        dict={
            "Record":Record,
            "admin":admin
        }
        return render(request,'adminpage.html',dict)
    else:
        return redirect('adminlogin')
    
def update_status(request):
    if request.method == 'POST':
        record_id = request.POST.get('record_id')
        status = request.POST.get('status')
        record = AbsentReason.objects.get(id=record_id)
        record.Status = status
        record.save()
        return redirect('admin')

def mentorlogin(request):
    if request.method == 'POST':
        MentorID = request.POST['MentorID']
        Password = request.POST['password']
        try:
            user = Mentor.objects.get(MentorID=MentorID, Password=Password)
            request.session['Mentor'] = user.MentorID
            return redirect('StudentTable')
        except Mentor.DoesNotExist:
            return render(request, 'login.html', {'error': 'Invalid credentials'})
    else:
        return render(request, 'login.html')
        
def studentmentee(request):
    if 'Mentor' in request.session :
        MentorID = request.session['Mentor']
        Data = Student.objects.filter(MentorID_id = MentorID)

        dict = {
            'Data':Data
        }
        return render(request,'mentor.html',dict)
    else:
        return redirect("Login")
    
def view_absent_records(request, StudentID):
    absences = AbsentReason.objects.filter(StudentID_id=StudentID)
    student = Student.objects.get(StudentID=StudentID)
    dict = {
        'absences': absences,
        'student': student,
        'StudentID': StudentID,  # Pass student ID to the context
    }
    return render(request, 'absent_records.html', dict)

    
def studentlogin(request):
    if request.method == 'POST':
        StudentID = request.POST['StudentID']
        Password = request.POST['password']
        try:
            user = Student.objects.get(StudentID = StudentID , Password=Password)
            request.session['Student'] = user.StudentID
            return redirect('Studentpage')
        except Student.DoesNotExist:
            return render(request, 'studentlogin.html', {'error': 'Invalid credentials'})
    else:
        return render(request, 'studentlogin.html')
    
def studentpage(request):
    if 'Student' in request.session:
        StudentID=request.session['Student']
        myform = AbsentReason.objects.filter(StudentID_id= StudentID)
        student = Student.objects.get(StudentID=StudentID)
        dict={
            'student':student,
            'myform':myform
        }
        
    return render(request,"studentpage.html",dict)

def profilementor(request):
    if 'Mentor' in request.session:
        MentorID=request.session['Mentor']
        mentor = Mentor.objects.get(MentorID=MentorID)
        dict={
            'mentor':mentor
        }
        
    return render(request,"profilementor.html",dict)

def absent_form_history(request):
    # Fetch all absent forms for the logged-in student
    if 'Student' in request.session:
        StudentID = request.session['Student']
        student = Student.objects.get(pk=StudentID)  # Assuming Student is your model for students
        absent_forms = AbsentReason.objects.filter(StudentID_id=StudentID)
        return render(request, 'absent_form_history.html', {'student': student, 'absent_forms': absent_forms})
    else:
        # Handle case where student is not logged in
        return HttpResponse("You are not logged in.")


def absentpage(request,StudentID):
    mystudent = Student.objects.get(StudentID=StudentID)
    mymentor = Mentor.objects.all().values()

    dict={
        'mymentor':mymentor,
        'mystudent':mystudent
    }

    return render(request,'studentform.html',dict)

def absenttable(request,StudentID):
    if request.method == 'POST':
        menid = request.POST['menid']
        reason = request.POST['reason']
        date = request.POST['date']
        a = Mentor.objects.get(MentorID=menid)
        b = Student.objects.get(StudentID = StudentID)

        data1 = AbsentReason(MentorID = a , StudentID = b , Reason = reason , Date = date )
        data1.save()
        return HttpResponseRedirect(reverse("Studentpage"))
    
def updatestudent(request,StudentID):
    studname=request.POST['studname']
    studcourse=request.POST['studcourse']
    studclass = request.POST['studclass']
    studno = request.POST['studno']
    mystudent=Student.objects.get(StudentID=StudentID)
    mystudent.StudentName=studname
    mystudent.StudentCourse = studcourse
    mystudent.StudentClass=studclass
    mystudent.StudentPhoneNumber=studno    
    mystudent.save()
    return HttpResponseRedirect(reverse("StudentTable"))

def update(request,StudentID):
    mystudent=Student.objects.get(StudentID=StudentID)

    dict={
     "mystudent":mystudent,
    } 

    return render(request,'updatestudent.html',dict)

def delete(request,StudentID):
    student=Student.objects.get(StudentID=StudentID)

    dict={
        "student":student
    }
    return render(request,'delete.html',dict)

def delete_data(request,StudentID):
    student=Student.objects.get(StudentID=StudentID)
    student.delete()
    return HttpResponseRedirect(reverse("StudentTable"))

def deletestud(request,id):
    table=AbsentReason.objects.get(id=id)
    dict={
        "table":table
    }
    return render(request,'deleteabsent.html',dict)

def deletedata(request,id):
    table=AbsentReason.objects.get(id=id)
    table.delete()
    return HttpResponseRedirect(reverse("admin"))

def search(request):

    mystudent=AbsentReason.objects.filter(Q(StudentID_id=request.GET.get('search')))

    dict={
        'mystudent':mystudent,
    }

    return render(request,'search.html',dict)





