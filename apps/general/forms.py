from django.forms import ModelForm
from . models import Message

class MessageForm(ModelForm):
    class Meta:
        model = Message
        fields = ["name", "email", "subject", "text"]

        def __init__(self, *args, **Kwargs):
            super(MessageForm, self).__init__(*args, **Kwargs)
            
            #Add bootstrap form control to each class
            for key in self.fields:
                self.fields[key].widget.attrs["class"] = "form-control"

            # Set placeholders for all fields
            self.fields["name"].widget.attrs["placeholder"] = "Full Name"
            self.fields["email"].widget.attrs["placeholder"] = "E-Mail Address"
            self.fields["subject"].widget.attrs["placeholder"] = "Subject"
            self.fields["text"].widget.attrs["placeholder"] = "Your Message"


