"""Form class"""
from django import forms

from api.models import Report


class ReportForm(forms.ModelForm):
    """Form class for Report model"""

    class Meta:
        model = Report
        fields = ("definition", "status", "attachment")
