from django import forms
from ticket.models import Ticket


class AddTicketForm(forms.ModelForm):
    """Добавление тикетов
    """
    class Meta:
        model = Ticket
        fields = ("category", "title", "text")