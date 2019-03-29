from django import forms


class CommentForm(forms.Form):
    message = forms.CharField(max_length=200, widget=forms.Textarea(attrs={
        'name': "message", 'id': "message", 'cols': "30", 'rows': "10", 'class': "form-control"}))


