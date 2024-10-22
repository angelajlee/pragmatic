from django.forms import ModelForm

from commentapp.migrations.models import Comment


class CommentCreationForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['content']