from django.shortcuts import render

def fruit_students(request):
    fruitList = ['Mango', 'Kiwi', 'Banana', 'Apple']
    studentList = ['Rama', 'Chetan', 'Kumar', 'Harish']
    return render(request, 'fruit_student.html', {'fruitList':fruitList , 'studentList':sorted(studentList)})
