from django.forms import ModelForm
from django import forms
from dash.models import PasswordEntry


class AddForm(ModelForm):
    class Meta:
        model = PasswordEntry
        fields = ['site_name', 'site_url', 'username', 'encrypted_password','remarks', 'category']
        labels = { 
            'site_name': 'NAME',
            'site_url': 'URL',
            'username': 'USERNAME',
            'encrypted_password': 'PASSWORD',
            'remarks': 'REMARKS',
            'category':'CATEGORY'
        }
        widgets = {  
            'site_name': forms.TextInput(attrs={'class': "bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"}),
            'site_url': forms.TextInput(attrs={'class': "bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"}),
            'username': forms.TextInput(attrs={'class': "bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"}),
            'encrypted_password': forms.TextInput(attrs={'class': "bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"}),
            'remarks': forms.Textarea(attrs={'class':  "bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500", 'rows': 3}),  
            'category': forms.Select()
        }


 