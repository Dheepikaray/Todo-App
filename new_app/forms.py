from datetime import date

from django import forms
from django.forms import DateInput
from django.utils import timezone

from new_app.models import Todo

class DateInput(forms.DateInput):
    input_type='date'
class TodoForm(forms.ModelForm):
    date = forms.DateField(widget=DateInput)
    class Meta:
        model=Todo
        fields=('title','name','date')

    # def check_date(self, data):
    #     if data > date.today():
    #         raise forms.ValidationError("'date' cannot be later than today.")
    #     return data

    def check_date(self):
        date1 = self.cleaned_data['date']
        today = date.today()

        if date1 < today:
            raise forms.ValidationError("Due date cannot be in the past")

        return date1


    def clean(self):
        cleaned_data = super().clean()
        self.check_date()


# from datetime import date


# class YourFormName(forms.Form):
#     date = forms.DateField()

# from datetime import date
# from django import forms

# class YourForm(forms.Form):
#     date = forms.DateField()
#
#     def check_date(self, data):
#         if data > date.today():
#             raise forms.ValidationError("'date' cannot be later than today.")
#         return data
#
#     def clean(self):
#         cleaned_data = super().clean()
#         date_value = cleaned_data.get('date')
#         if date_value:
#             self.check_date(date_value)




# from django import forms
#
# class DateInput(forms.DateInput):
#     input_type = 'date'
#
# class MyForm(forms.Form):
#     date = forms.DateField(widget=DateInput)