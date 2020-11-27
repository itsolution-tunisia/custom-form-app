from .models import ExtraInfo
from django.forms import ModelForm

class ExtraInfoForm(ModelForm):
    """
    The fields on this form are derived from the ExtraInfo model in models.py.
    """
    def __init__(self, *args, **kwargs):
        super(ExtraInfoForm, self).__init__(*args, **kwargs)
        self.fields['member_org_inst'].error_messages = {
            "required": u"Please tell us if your are a member of an organization/institution.",
            "invalid": u"Please enter the membership information.",
        }
        
        self.fields['org_inst'].error_messages = {
            "required": u"Please tell us the organization/institution you are a member of.",
            "invalid": u"Invalid entrie.",
        }

        self.fields['tel'].error_messages = {
            "required": u"Please tell us your telephone number.",
            "invalid": u"Invalid telephone number.",
        }

    class Meta(object):
        model = ExtraInfo
        fields = ('tel', 'member_org_inst', 'org_inst')
