from django import forms
from django.core import validators
# def starts_with_d(value):
#     if value.isalpha()!= True:
#         raise forms.ValidationError('Name should contains only alphabet ')
# def gmail_verification(value):
#      if value[len(value)-9:]!='gmail.com':
#          raise forms.ValidationError('Must be gmail')
class FeedBackForm(forms.Form):
    name=forms.CharField()
    rollno=forms.IntegerField()
    email=forms.EmailField()
    password=forms.CharField(widget=forms.PasswordInput)
    rpassword=forms.CharField(label='Password(Again)',widget=forms.PasswordInput)
    feedback=forms.CharField(widget=forms.Textarea)
    bot_handler=forms.CharField(required=False,widget=forms.HiddenInput)

    def clean(self):
        print("Bot Validation...")
        cleaned_data = super().clean()
        # inputpwd=cleaned_data['password']
        # inputrpwd=cleaned_data['rpassword']
        # if inputpwd!=inputrpwd:
        bot_handler_value=cleaned_data['bot_handler']
        if len(bot_handler_value)>0:
            raise forms.ValidationError('Thanks Bot!!!!')
        # inputrollno = cleaned_data['rollno']
        # if len(str(inputrollno))!=3:
        #     raise forms.ValidationError('Roll number should contains exactly 3 characters ')




    # def clean_gmail(self):
    #     inputemail=self.cleaned_data['email']
    #     print('email validation')
    #     return inputemail

# def clean_name(self):
#     inputname=self.cleaned_data['name']
#     if len(input_name)<4:
#         raise forms.ValidationError('The Lenght of Name Should be >=4')
#     return inputname
