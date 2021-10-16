from django import forms
class StudentRegisration(forms.Form):
    name=forms.CharField()
    marks=forms.IntegerField()
