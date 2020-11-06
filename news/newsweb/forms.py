from django import forms


class SearchFunction(forms.Form):
    search_keywords = forms.CharField(help_text="Please enter any keywords to search for specific articles.")
