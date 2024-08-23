from django.db import models
from django.contrib.auth.models import User
from django.db import connection

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=True, blank=True)
    department = models.CharField(max_length=200, null=True, blank=True)
    designation = models.CharField(max_length=200, null=True, blank=True)
    profile_img = models.ImageField(default='media/profile.webp', upload_to='media', null=True, blank=True)

    # def save(self, *args, **kwargs):
    #     # Fetch the corresponding employee details from the Employee table
    #     employee_id = self.user.username  # Assuming employee_id is the same as the username
    #     with connection.cursor() as cursor:
    #         cursor.execute("SELECT name, department, designation FROM Employees WHERE employee_id = %s", [employee_id])
    #         row = cursor.fetchone()

    #     if row:
    #         self.name = row[0]
    #         self.department = row[1]
    #         self.designation = row[2]

    #     super(Profile, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.user.username}'s profile"

class RecruitmentForm(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    raised_by = models.CharField(max_length=255)
    date = models.DateField()
    department = models.CharField(max_length=255)
    unit_name = models.CharField(max_length=255)
    approved_by = models.CharField(max_length=255)
    designation = models.CharField(max_length=255)
    recruitment_type = models.CharField(max_length=50)
    vacant_position = models.PositiveIntegerField()
    location = models.CharField(max_length=50) 
    job_role = models.CharField(max_length=255, blank=True, null=True)  # Added job_role field

    def __str__(self):
        return f"Recruitment Form {self.id} by {self.raised_by}"

class VacancyDetail(models.Model):
    recruitment_form = models.ForeignKey(RecruitmentForm, related_name='vacancies', on_delete=models.CASCADE)
    vacancy_type = models.CharField(max_length=50)
    resigned_name = models.CharField(max_length=255, blank=True, null=True)
    employee_id = models.CharField(max_length=50, blank=True, null=True)
    designation = models.CharField(max_length=255, blank=True, null=True)
    resignation_date = models.DateField(blank=True, null=True)
    last_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return f"Vacancy Detail {self.id} for {self.recruitment_form}"

class Department(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    department_name = models.CharField(max_length=100)

    def __str__(self):
        return self.department_name
    

class Expense(models.Model):
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    id_no = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    designation = models.CharField(max_length=255)
    department = models.CharField(max_length=255)
    month = models.CharField(max_length=50)
    unit = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    
    utility = models.CharField(max_length=255, blank=True, null=True)
    utility_remarks = models.CharField(max_length=255, blank=True, null=True)
    driver_wages = models.CharField(max_length=255, blank=True, null=True)
    driver_wages_remarks = models.CharField(max_length=255, blank=True, null=True)
    service_staff_wages = models.CharField(max_length=255, blank=True, null=True)
    service_staff_wages_remarks = models.CharField(max_length=255, blank=True, null=True)
    security_staff_wages = models.CharField(max_length=255, blank=True, null=True)
    security_staff_wages_remarks = models.CharField(max_length=255, blank=True, null=True)
    leave_fare_assistance = models.CharField(max_length=255, blank=True, null=True)
    leave_fare_assistance_remarks = models.CharField(max_length=255, blank=True, null=True)
    
    fuel_cost = models.CharField(max_length=255, blank=True, null=True)
    fuel_cost_remarks = models.CharField(max_length=255, blank=True, null=True)
    gas_cost = models.CharField(max_length=255, blank=True, null=True)
    gas_cost_remarks = models.CharField(max_length=255, blank=True, null=True)
    repair_maintenance = models.CharField(max_length=255, blank=True, null=True)
    repair_maintenance_remarks = models.CharField(max_length=255, blank=True, null=True)
    
    tyres = models.CharField(max_length=255, blank=True, null=True)
    tyres_remarks = models.CharField(max_length=255, blank=True, null=True)
    battery = models.CharField(max_length=255, blank=True, null=True)
    battery_remarks = models.CharField(max_length=255, blank=True, null=True)
    car_denting_painting = models.CharField(max_length=255, blank=True, null=True)
    car_denting_painting_remarks = models.CharField(max_length=255, blank=True, null=True)
    car_decorations = models.CharField(max_length=255, blank=True, null=True)
    car_decorations_remarks = models.CharField(max_length=255, blank=True, null=True)
    toll = models.CharField(max_length=255, blank=True, null=True)
    toll_remarks = models.CharField(max_length=255, blank=True, null=True)
    
    others = models.CharField(max_length=255, blank=True, null=True)
    others_remarks = models.CharField(max_length=255, blank=True, null=True)
    telephone = models.CharField(max_length=255, blank=True, null=True)
    telephone_remarks = models.CharField(max_length=255, blank=True, null=True)
    mobile_set = models.CharField(max_length=255, blank=True, null=True)
    mobile_set_remarks = models.CharField(max_length=255, blank=True, null=True)
    medical_expense = models.CharField(max_length=255, blank=True, null=True)
    medical_expense_remarks = models.CharField(max_length=255, blank=True, null=True)
    medical_expense_surgery = models.CharField(max_length=255, blank=True, null=True)
    medical_expense_surgery_remarks = models.CharField(max_length=255, blank=True, null=True)
    
    total_taka = models.CharField(max_length=255)
    advance = models.CharField(max_length=255, blank=True, null=True)
    expenses_as_above = models.CharField(max_length=255, blank=True, null=True)
    amount_due = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f"Expense {self.id} for {self.name} ({self.id_no})"