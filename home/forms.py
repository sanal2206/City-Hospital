from django import forms
from django.utils import timezone

from.models import Booking
class DateInput(forms.DateInput):
        input_type='date'
        def __init__(self, **kwargs):
          
          kwargs['attrs'] = {'min': timezone.now().date().isoformat()}
          super().__init__(**kwargs)

class BookingForm(forms.ModelForm):
   
    class Meta:
        model=Booking
        fields='__all__'
         

        widgets= {
            'booking_date':DateInput(),
        }

        labels={
             'p_name':'Patient Name',
             'p_email':'Patient Email',
             'p_phone':'Patient Phone',
             'doc_name':"Doctor Name",
             'booking_date':'Booking Date',
        }

 
 
 
 

    