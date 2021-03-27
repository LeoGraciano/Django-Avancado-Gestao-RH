from apps.employees.models import Employee
from django.forms import ModelForm
from .models import OverTime
from apps.employees.models import Employee


class OverTimeForm(ModelForm):
    def __init__(self, employee, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['employee'].queryset = Employee.objects.filter(
            company=employee.company)

    class Meta:
        model = OverTime
        fields = ['reason', 'employee', 'hours']
