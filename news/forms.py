from django.forms import ModelForm
from .models import Comments

class CommentForm(ModelForm):
    """Форма комментариев к статье
    """
    class Meta:
        model = Comments
        fields = ('text',)