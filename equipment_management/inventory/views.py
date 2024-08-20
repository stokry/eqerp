from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Equipment, Employee  # Ensure Employee is imported

def home(request):
    return render(request, 'home.html')

@login_required
def employee_dashboard(request):
    # Ensure the user is an employee
    try:
        employee = request.user.employee
    except Employee.DoesNotExist:
        return render(request, 'error.html', {'message': 'No employee profile found.'})

    # Get equipment assigned to this employee
    equipment_list = Equipment.objects.filter(assigned_to=employee)
    context = {
        'username': request.user.username,  # Use request.user.username
        'equipment_list': equipment_list
    }

    return render(request, 'employee_dashboard.html', context)

@login_required
def admin_dashboard(request):
    if not request.user.is_superuser:
        return redirect('employee_dashboard')

    employees = Employee.objects.all()
    equipment_list = Equipment.objects.all()

    return render(request, 'admin_dashboard.html', {'employees': employees, 'equipment_list': equipment_list})