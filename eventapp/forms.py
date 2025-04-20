from django import forms
from . models import Booking
class DateInput(forms.DateInput):
    input_type='date'



class  BookingForm(forms.ModelForm):
    class Meta:
        model=Booking
        fields='__all__'

        widgets={
            'booking_date':DateInput(),
        }

        labels={
            'cus_name':"Customer Name:",
            'cus_ph':"Phone Number:",
            'name':"Event Name:",
            'booking_date':"Booking Date:",


        }