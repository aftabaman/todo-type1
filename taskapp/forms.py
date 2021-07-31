# this is form representation of the models in the project

from django import forms
from django.forms import ModelForm

from .models import *


class TaskForm(forms.ModelForm):

    class Meta:

        model  = Task # here we are selecting the model of that we want to
                        # create the form


        fields = '__all__' # here we are selecting the fields that we want
                            # in the form

