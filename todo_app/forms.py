from django import forms

class Todoform(forms.Form):
    text =forms.CharField(max_length=400
    , widget=forms.TextInput(
        attrs={'class':'form-control', 'placeholder':'Enter todo e.g. Delete junk files','aria-label':'Todo', 'aria-describedby':'add-btn'}
     )
    )       