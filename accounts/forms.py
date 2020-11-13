from django.contrib.auth import get_user_model  #will give the currently activer user model
from django.contrib.auth.forms import UserCreationForm


class UserCreateForm(UserCreationForm):

    class Meta:
        fields = ('username','first_name','password1','password2','email')
        model = get_user_model()

    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.fields['username'].label = 'Display Name'
        self.fields['email'].label = 'Email'
        self.fields['first_name'].label = 'First Name'
        self.fields['password1'].label = 'Password'
        self.fields['password2'].label = 'Confirm Password'
