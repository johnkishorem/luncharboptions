from django import forms
from polls.models import hotel_option


class VoteTodayForm(forms.Form):
	vote_hotel = forms.ChoiceField(label = 'Select a hotel')
	vote_time = forms.ChoiceField(label = 'Select a time slot')