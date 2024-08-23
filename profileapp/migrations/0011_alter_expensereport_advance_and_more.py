# Generated by Django 5.0.7 on 2024-08-13 07:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profileapp', '0010_rename_advance_drawn_expensereport_advance_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expensereport',
            name='advance',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='I.O.U/Advance Drawn (Tk.)'),
        ),
        migrations.AlterField(
            model_name='expensereport',
            name='amount_due',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=10, null=True, verbose_name='Amount due to Company/Employees'),
        ),
        migrations.AlterField(
            model_name='expensereport',
            name='battery',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=10, null=True, verbose_name='Battery'),
        ),
        migrations.AlterField(
            model_name='expensereport',
            name='battery_remarks',
            field=models.CharField(blank=True, default=0, max_length=200, null=True, verbose_name='Battery Remarks'),
        ),
        migrations.AlterField(
            model_name='expensereport',
            name='car_decorations',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=10, null=True, verbose_name='Car Decorations'),
        ),
        migrations.AlterField(
            model_name='expensereport',
            name='car_decorations_remarks',
            field=models.CharField(blank=True, default=0, max_length=200, null=True, verbose_name='Car Decorations Remarks'),
        ),
        migrations.AlterField(
            model_name='expensereport',
            name='car_denting_painting',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=10, null=True, verbose_name='Car Denting & Painting'),
        ),
        migrations.AlterField(
            model_name='expensereport',
            name='car_denting_painting_remarks',
            field=models.CharField(blank=True, default=0, max_length=200, null=True, verbose_name='Car Denting & Painting Remarks'),
        ),
        migrations.AlterField(
            model_name='expensereport',
            name='department',
            field=models.CharField(default=0, max_length=100, verbose_name='Department'),
        ),
        migrations.AlterField(
            model_name='expensereport',
            name='designation',
            field=models.CharField(default=0, max_length=100, verbose_name='Designation'),
        ),
        migrations.AlterField(
            model_name='expensereport',
            name='driver_wages',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=10, null=True, verbose_name='Driver Wages'),
        ),
        migrations.AlterField(
            model_name='expensereport',
            name='driver_wages_remarks',
            field=models.CharField(blank=True, default=0, max_length=200, null=True, verbose_name='Driver Wages Remarks'),
        ),
        migrations.AlterField(
            model_name='expensereport',
            name='expenses_as_above',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=10, null=True, verbose_name='Expenses as Above (Tk.)'),
        ),
        migrations.AlterField(
            model_name='expensereport',
            name='fuel_cost',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=10, null=True, verbose_name='Fuel Cost'),
        ),
        migrations.AlterField(
            model_name='expensereport',
            name='fuel_cost_remarks',
            field=models.CharField(blank=True, default=0, max_length=200, null=True, verbose_name='Fuel Cost Remarks'),
        ),
        migrations.AlterField(
            model_name='expensereport',
            name='gas_cost',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=10, null=True, verbose_name='Gas Cost'),
        ),
        migrations.AlterField(
            model_name='expensereport',
            name='gas_cost_remarks',
            field=models.CharField(blank=True, default=0, max_length=200, null=True, verbose_name='Gas Cost Remarks'),
        ),
        migrations.AlterField(
            model_name='expensereport',
            name='id_no',
            field=models.CharField(default=0, max_length=50, verbose_name='ID #'),
        ),
        migrations.AlterField(
            model_name='expensereport',
            name='leave_fare_assistance',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=10, null=True, verbose_name='Leave Fare Assistance-LFA'),
        ),
        migrations.AlterField(
            model_name='expensereport',
            name='leave_fare_assistance_remarks',
            field=models.CharField(blank=True, default=0, max_length=200, null=True, verbose_name='Leave Fare Assistance Remarks'),
        ),
        migrations.AlterField(
            model_name='expensereport',
            name='location',
            field=models.CharField(default=0, max_length=100, verbose_name='Location'),
        ),
        migrations.AlterField(
            model_name='expensereport',
            name='medical_expense',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=10, null=True, verbose_name='Medical Expense'),
        ),
        migrations.AlterField(
            model_name='expensereport',
            name='medical_expense_remarks',
            field=models.CharField(blank=True, default=0, max_length=200, null=True, verbose_name='Medical Expense Remarks'),
        ),
        migrations.AlterField(
            model_name='expensereport',
            name='medical_expense_surgery',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=10, null=True, verbose_name='Medical Expense-Surgery cost relating to Heart, Kidney, Eye, Liver and Cancer'),
        ),
        migrations.AlterField(
            model_name='expensereport',
            name='medical_expense_surgery_remarks',
            field=models.CharField(blank=True, default=0, max_length=200, null=True, verbose_name='Medical Expense Surgery Remarks'),
        ),
        migrations.AlterField(
            model_name='expensereport',
            name='mobile_set',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=10, null=True, verbose_name='Mobile Set'),
        ),
        migrations.AlterField(
            model_name='expensereport',
            name='mobile_set_remarks',
            field=models.CharField(blank=True, default=0, max_length=200, null=True, verbose_name='Mobile Set Remarks'),
        ),
        migrations.AlterField(
            model_name='expensereport',
            name='month',
            field=models.CharField(default=0, max_length=20, verbose_name='Month'),
        ),
        migrations.AlterField(
            model_name='expensereport',
            name='name',
            field=models.CharField(default=0, max_length=100, verbose_name='Name'),
        ),
        migrations.AlterField(
            model_name='expensereport',
            name='others',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=10, null=True, verbose_name='Others'),
        ),
        migrations.AlterField(
            model_name='expensereport',
            name='others_remarks',
            field=models.CharField(blank=True, default=0, max_length=200, null=True, verbose_name='Others Remarks'),
        ),
        migrations.AlterField(
            model_name='expensereport',
            name='purpose',
            field=models.CharField(default=0, max_length=200, verbose_name='Purpose'),
        ),
        migrations.AlterField(
            model_name='expensereport',
            name='repair_maintenance',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=10, null=True, verbose_name='Repair & Maintenance Allowance'),
        ),
        migrations.AlterField(
            model_name='expensereport',
            name='repair_maintenance_remarks',
            field=models.CharField(blank=True, default=0, max_length=200, null=True, verbose_name='Repair & Maintenance Allowance Remarks'),
        ),
        migrations.AlterField(
            model_name='expensereport',
            name='security_staff_wages',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=10, null=True, verbose_name='Security Staff Wages'),
        ),
        migrations.AlterField(
            model_name='expensereport',
            name='security_staff_wages_remarks',
            field=models.CharField(blank=True, default=0, max_length=200, null=True, verbose_name='Security Staff Wages Remarks'),
        ),
        migrations.AlterField(
            model_name='expensereport',
            name='service_staff_wages',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=10, null=True, verbose_name='Service Staff Wages'),
        ),
        migrations.AlterField(
            model_name='expensereport',
            name='service_staff_wages_remarks',
            field=models.CharField(blank=True, default=0, max_length=200, null=True, verbose_name='Service Staff Wages Remarks'),
        ),
        migrations.AlterField(
            model_name='expensereport',
            name='telephone',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=10, null=True, verbose_name='Telephone'),
        ),
        migrations.AlterField(
            model_name='expensereport',
            name='telephone_remarks',
            field=models.CharField(blank=True, default=0, max_length=200, null=True, verbose_name='Telephone Remarks'),
        ),
        migrations.AlterField(
            model_name='expensereport',
            name='toll',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=10, null=True, verbose_name='Toll'),
        ),
        migrations.AlterField(
            model_name='expensereport',
            name='toll_remarks',
            field=models.CharField(blank=True, default=0, max_length=200, null=True, verbose_name='Toll Remarks'),
        ),
        migrations.AlterField(
            model_name='expensereport',
            name='total_taka',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='Total Taka'),
        ),
        migrations.AlterField(
            model_name='expensereport',
            name='tyres',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=10, null=True, verbose_name='Tyre(s)'),
        ),
        migrations.AlterField(
            model_name='expensereport',
            name='tyres_remarks',
            field=models.CharField(blank=True, default=0, max_length=200, null=True, verbose_name='Tyre(s) Remarks'),
        ),
        migrations.AlterField(
            model_name='expensereport',
            name='unit',
            field=models.CharField(default=0, max_length=100, verbose_name='Unit'),
        ),
        migrations.AlterField(
            model_name='expensereport',
            name='utility',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=10, null=True, verbose_name='Utility-Water Gas Electricity'),
        ),
        migrations.AlterField(
            model_name='expensereport',
            name='utility_remarks',
            field=models.CharField(blank=True, default=0, max_length=200, null=True, verbose_name='Utility Remarks'),
        ),
    ]
