from django import forms
status=(('Open',"open"),("Close","close"))
class Task_Form(forms.Form):
    task=forms.CharField(max_length=30,label="Task Title",required=True)
    desc=forms.CharField(max_length=10, label="Description", required=True)
    end_date=forms.CharField(label="EndDate", help_text="Date must be DD-MM-YYYY format")
    status=forms.ChoiceField(choices=status, label="Status")


