from django import forms
from .models import UserProfileInfo

class UserProfileInfoForm(forms.ModelForm):
    class Meta():
        model=UserProfileInfo
        fields=['COMPANY_NAME','FRONT_INSIDE_PICTURE','BUSINESS_CARD_IMAGE']
