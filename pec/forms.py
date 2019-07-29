from django import forms
from .models import Carpenter,Plumber,Mason,Driver,User, Server

class cform(forms.ModelForm):
#Carpenter
    class Meta:
        model=Carpenter
        fields=[
        "name",
        "image",
        "contact",
        "address"
        ]

class dform(forms.ModelForm):
#Driver
    class Meta:
        model=Driver
        fields=[
        "name",
        "image",
        "contact",
        "address"
        ]

class pform(forms.ModelForm):
#Plumber
    class Meta:
        model=Plumber
        fields=[
        "name",
        "image",
        "contact",
        "address"
        ]

class mform(forms.ModelForm):
#Mason
    class Meta:
        model=Mason
        fields=[
        "name",
        "image",
        "contact",
        "address"
        ]


class userform(forms.ModelForm):
    class Meta:
        model=User
        fields=[
        "address",
        ]
