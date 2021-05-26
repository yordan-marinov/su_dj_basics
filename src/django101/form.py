from django import forms


class ContactForm(forms.Form):
    full_name = forms.CharField(max_length=50)
    email = forms.EmailField()
    content = forms.CharField(widget=forms.Textarea)

    def clean_email(self, *args, **kwargs):
        """This is a validation func which validates the email if they ends with .bg extension
        and if they do it raises ValidatonError to the client."""

        email = self.cleaned_data.get("email") # => email=form.cleaned_data.get('email')
        # In this case self refers to the form object.
        print(f"== email ==> {email}")
        if email.endswith(".bg"):
            raise forms.ValidationError("This is not a valid email!")
        return email
