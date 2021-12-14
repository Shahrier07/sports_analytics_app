from django import forms
from django.forms import widgets
from .models import User
from .models import School
from .models import Player
from .models import Team
from .models import Match
from .models import MatchView

 
class User(forms.ModelForm):
  class Meta:
    model = User
    fields = ["name", "mobile_number",]
    labels = {'name': "Name", "mobile_number": "Mobile Number",}

## School
class School(forms.ModelForm):
  class Meta:
    model = School
    fields = ["schoolID", "schoolName", "schoolAddress","schoolThana","postCode","subDistrict","district","phoneNo","email","contPerName","schlUname","password","schoolType","studentType",]
    labels = {"schoolID":"EIIN", "schoolName":"School Name", "schoolAddress":"School Address","schoolThana":"Thana","postCode":"Post Code","subDistrict":"Sub District","district":"District","phoneNo":"Phone No.","email":"Email","contPerName":"Contact Person Name","schlUname":"Username","password":"Password","schoolType":"School Type","studentType":"Student Type",}
    widgets={
        "schoolID": forms.TextInput(attrs={'class':'form-control'}),
        "schoolName": forms.TextInput(attrs={'class':'form-control'}),
        "schoolAddress":forms.TextInput(attrs={'class':'form-control'}),
        "schoolThana":forms.TextInput(attrs={'class':'form-control'}),
        "postCode":forms.TextInput(attrs={'class':'form-control'}),
        "subDistrict":forms.TextInput(attrs={'class':'form-control'}),
        "district":forms.TextInput(attrs={'class':'form-control'}),
        "phoneNo":forms.TextInput(attrs={'class':'form-control'}),
        "email":forms.TextInput(attrs={'class':'form-control'}),
        "contPerName":forms.TextInput(attrs={'class':'form-control'}),
        "schlUname":forms.TextInput(attrs={'class':'form-control'}),
        "password":forms.TextInput(attrs={'class':'form-control'}),
        "schoolType":forms.Select(attrs={'class':'form-control'}),
        "studentType":forms.Select(attrs={'class':'form-control'}),
    }

## Player

#date
class DateInput(forms.DateInput):
  input_type = "date"

class Player(forms.ModelForm):
  class Meta:
    model = Player
    fields = ["playerID", "schoolID","fName", "lName","birthDate","ageGroup","gender","playerAddress","city","province","postCode","parentName","parentPhoneNo","parentWorkPlace","size",]

    labels = {"playerID":"Player ID","schoolID":"EIIN","fName":"First Name", "lName":"Last Name","birthDate":"Date of Birth","ageGroup":"Age","gender":"Gender","playerAddress":"Adress","city":"City","province":"Province","postCode":"Post Code","parentName":"Parent Name","parentPhoneNo":"Parent Phone No.","parentWorkPlace":"Place of Work","size":"Size",}
    widgets={
        "playerID": forms.TextInput(attrs={'class':'form-control'}),
        "schoolID": forms.TextInput(attrs={'class':'form-control'}),
        "fName": forms.TextInput(attrs={'class':'form-control'}),
        "lName":forms.TextInput(attrs={'class':'form-control'}),
        "birthDate":forms.DateInput(attrs={'class':'form-control', 'placeholder': 'Select a date', 'type': 'date'}),
        "ageGroup":forms.TextInput(attrs={'class':'form-control'}),
        "gender":forms.Select(attrs={'class':'form-control'}),
        "playerAddress":forms.TextInput(attrs={'class':'form-control'}),
        "city":forms.TextInput(attrs={'class':'form-control'}),
        "province":forms.TextInput(attrs={'class':'form-control'}),
        "postCode":forms.TextInput(attrs={'class':'form-control'}),
        "parentName":forms.TextInput(attrs={'class':'form-control'}),
        "parentPhoneNo":forms.TextInput(attrs={'class':'form-control'}),
        "parentWorkPlace":forms.TextInput(attrs={'class':'form-control'}),
        "size":forms.Select(attrs={'class':'form-control'}),
    }


## Team
class Team(forms.ModelForm):
  class Meta:
    model = Team
    fields = ["teamID", "teamName", "schoolID", "sportsType","numOfPlayer","player1","player2","player3","player4","player5","player6","player7","player8","player9","player10","player11",]
    labels = {"teamID":"Team ID", "teamName":"Team Name","schoolID":"EIIN","sportsType":"Sports Type","numOfPlayer":"Number of Player","player1":"Player1 ID","player2":"Player2 ID","player3":"Player3 ID","player4":"Player4 ID","player5":"Player5 ID","player6":"Player6 ID","player7":"Player7 ID","player8":"Player8 ID","player9":"Player9 ID","player10":"Player10 ID","player11":"Player11 ID",}
    widgets={
        "teamID": forms.TextInput(attrs={'class':'form-control'}),
        "teamName":forms.TextInput(attrs={'class':'form-control'}),
        "schoolID": forms.TextInput(attrs={'class':'form-control'}),
        "sportsType":forms.Select(attrs={'class':'form-control'}),
        "numOfPlayer":forms.TextInput(attrs={'class':'form-control'}),
        "player1":forms.TextInput(attrs={'class':'form-control'}),
        "player2":forms.TextInput(attrs={'class':'form-control'}),
        "player3":forms.TextInput(attrs={'class':'form-control'}),
        "player4":forms.TextInput(attrs={'class':'form-control'}),
        "player5":forms.TextInput(attrs={'class':'form-control'}),
        "player6":forms.TextInput(attrs={'class':'form-control'}),
        "player7":forms.TextInput(attrs={'class':'form-control'}),
        "player8":forms.TextInput(attrs={'class':'form-control'}),
        "player9":forms.TextInput(attrs={'class':'form-control'}),
        "player10":forms.TextInput(attrs={'class':'form-control'}),
        "player11":forms.TextInput(attrs={'class':'form-control'}),
    }



## Match
class Match(forms.ModelForm):
  class Meta:
    model = Match
    fields = ["matchID", "matchDate","matchTime","venue","school","classes","team1","team2","trmtName","sportsType",]
    labels = {"matchID":"Match ID", "matchDate":"Match Date","matchTime":"Time","venue":"Venue","school":"School","classes":"Classes","team1":"Team 1 ID","team2":"Team 2 ID","trmtName":"Tournament name","sportsType":"Sports type",}
    widgets={
        "matchID": forms.TextInput(attrs={'class':'form-control'}),
        "matchDate":forms.DateInput(attrs={'class':'form-control', 'placeholder': 'Select a date',
               'type': 'date'}),
        "matchTime":forms.TimeInput(attrs={'class':'form-control', 'placeholder': 'Select a time',
               'type': 'time'}),
        "venue":forms.TextInput(attrs={'class':'form-control'}),
        "school":forms.TextInput(attrs={'class':'form-control'}),
        "classes":forms.TextInput(attrs={'class':'form-control'}),
        "team1":forms.TextInput(attrs={'class':'form-control'}),
        "team2":forms.TextInput(attrs={'class':'form-control'}),
        "trmtName":forms.TextInput(attrs={'class':'form-control'}),
        "sportsType":forms.Select(attrs={'class':'form-control'}),
        
    }    

  # # Match View
  # class MatchView(forms.ModelForm):
  #   class Meta:
  #       model = MatchView
  #       fields = ["batsman","bowler","run","wicket"]
  #       labels = {}
        