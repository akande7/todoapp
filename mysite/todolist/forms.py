from django import forms

class TodoListForm(forms.form):
    text = forms.CharField(max_length = 45,
        Widget = forms.TextInput(
            attrs = {'class': 'form-control', 'placeholder':'Enter todo e.g Grocery Shopping', 'aria-label':'Todo', 'aria-describeby':'add-btn'}
        )
        )