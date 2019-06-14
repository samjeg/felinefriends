from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django import forms


class UserCreateForm(UserCreationForm):
	picture = forms.ImageField(required=False)

	class Meta:
		fields = ("username", "picture", "password1", "password2")
		model = get_user_model()

	def __init__(self, *args, **kwargs):
		super(UserCreateForm, self).__init__(*args, **kwargs)
		self.fields["username"].label = "Username:"
		self.fields["picture"].label = "Add Picture"
		self.fields["username"].help_text = None
		self.fields["password1"].help_text = None
		self.fields["password2"].help_text = None
