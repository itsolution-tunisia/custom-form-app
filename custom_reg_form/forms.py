from .models import ExtraInfo
from django.forms import ModelForm
from django.utils.translation import ugettext_lazy as _
from django.utils.translation import ugettext_noop

class ExtraInfoForm(ModelForm):
    """
    The fields on this form are derived from the ExtraInfo model in models.py.
    """
    def __init__(self, *args, **kwargs):
        super(ExtraInfoForm, self).__init__(*args, **kwargs)

        self.fields['tel'].error_messages = {
            "required": _("Please tell us your telephone number."),
            "invalid": _("Invalid telephone number."),
        }

    class Meta(object):
        model = ExtraInfo
        fields = ('tel', 'org_inst')
