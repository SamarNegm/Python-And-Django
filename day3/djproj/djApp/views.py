
from django.http import HttpResponse
from django.shortcuts import redirect, render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import StudentSerializer
from .forms import StudentForm, UserForm
from .models import Student, Track
# Create your views here.


def home(request):
    all_students = Student.objects.all()
    context = {'student_list': all_students}
    return render(request, 'djapp/home.html', context)


def show(request, st_id):
    st = Student.objects.get(id=st_id)
    context = {'st': st}
    return render(request, 'djApp/show.html', context)


def del_St(request, st_id):
    st = Student.objects.get(id=st_id)
    st.delete()
    return redirect('home')


def addStudent(request):
    if request.method == 'POST':
        st_form = StudentForm(request.POST)
        if st_form.is_valid():
            st_form.save()
            return redirect('home')
    st_form = StudentForm()
    context = {'form': st_form}
    return render(request, 'djApp/add-student.html', context)


def editStudent(request, st_id):
    student = Student.objects.get(id=st_id)
    st_form = StudentForm(instance=student)

    if request.method == 'POST':
        st_form = StudentForm(request.POST, instance=student)
        if st_form.is_valid():
            st_form.save()
            return redirect('home')
    context = {'form': st_form}
    return render(request, 'djApp/add-student.html', context)


def ListStudentDetails(request, st_id):
    st = Student.objects.get(id=st_id)
    context = {'st': st}
    return render(request, 'djApp/st-details.html', context)


# rest_framework views.
@api_view(['GET'])
def api_all_students(request):
    all_st = Student.objects.all()
    sr_serializer = StudentSerializer(all_st, many=True)
    return Response(sr_serializer.data)


@api_view(['GET'])
def api_student_details(request, st_id):
    all_st = Student.objects.get(id=st_id)
    sr_serializer = StudentSerializer(all_st, many=False)
    return Response(sr_serializer.data)


@api_view(['POST'])
def api_student_create(request):
    print(",,,,,,,,,,,,,,", request.data)
    sr_serializer = StudentSerializer(data=request.data)
    if sr_serializer.is_valid():
        sr_serializer.save()
    return redirect('api-list')


@api_view(['POST'])
def api_student_edit(request, st_id):
    st = Student.objects.get(id=st_id)
    sr_serializer = StudentSerializer(instance=st, data=request.data)
    if sr_serializer.is_valid():
        sr_serializer.save()
    return redirect('api-list')


@api_view(['DELETE'])
def api_student_delete(request, st_id):
    print(",,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,")
    st = Student.objects.get(id=st_id)
    print(st)
    st.delete()
    return Response('User Deleted')
