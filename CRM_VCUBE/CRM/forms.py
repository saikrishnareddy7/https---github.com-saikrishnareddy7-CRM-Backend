from django import forms


class Enrollform(forms.Form):

    first_name = forms.CharField(max_length=20)
    last_name = forms.CharField(max_length=20)
    email_id = forms.EmailField(max_length=30)
    phone_no = forms.IntegerField(required=True)