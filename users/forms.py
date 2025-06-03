from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from profiles.models import Profile

User = get_user_model()

class UserRegistrationForm(UserCreationForm):
    role = forms.ChoiceField(
        choices=Profile.Role.choices,
        # widget=forms.RadioSelect, 
        # label="Account Type"
    )
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'role']
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Customize field labels if needed
        self.fields['password1'].label = 'Password'
        self.fields['password2'].label = 'Confirm Password'
        self.fields['email'].required = True  # Make email required
    
    def save(self, commit=True):
        user = super().save(commit=False)
        if commit:
            user.save()
            # Create profile with selected role
            Profile.objects.create(user=user, role=self.cleaned_data['role'])
        return user