
from django import forms
from django.http.response import HttpResponse,JsonResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from .forms import User
from .forms import School
from .forms import Player
from .forms import Team
from .forms import Match
# from .forms import MatchView
# importing model
from .models import MatchView as MV
from .models import Match, MatchExtra
from .models import VolleyBallModel, FootBallModel
# Create your views here.
##
import pandas as pd


##School Register
def school_register(request):
    if request.method == 'POST':
      fm = School(request.POST)
      if fm.is_valid():
          fm.save()
          fm = School()
          #return HttpResponseRedirect('/thanks/')
    else:
        fm = School()

    return render(request,'firstapp/school_register.html', {'form1':fm})

##Player Register
def player_register(request):
    #playerID = request.POST.get('playerID')
    #forms.fields['playerID'].choices = [(playerID, playerID)]
   
    if request.method == 'POST':
      fm = Player(request.POST)
      if fm.is_valid():
          fm.save()
          fm = Player()
          #return HttpResponseRedirect('/thanks/')
    else:
        fm = Player()

    return render(request,'firstapp/player_register.html', {'form2':fm})


## Team Formation
def team_form(request):
    if request.method == 'POST':
      fm = Team(request.POST)
      if fm.is_valid():
          fm.save()
          fm = Team()
          #return HttpResponseRedirect('/thanks/')
    else:
        fm = Team()

    return render(request,'firstapp/team_form.html', {'form3':fm})

## Match Formation
def match_form(request):
    from .forms import Match
    if request.method == 'POST':
      fm = Match(request.POST)
      if fm.is_valid():
          fm.save()
          fm = Match()
          #return HttpResponseRedirect('/thanks/')
    else:
        fm = Match()

    return render(request,'firstapp/match_form.html', {'form4':fm})

##toss
@csrf_exempt
def match_toss(request):
    if request.is_ajax and request.method == 'POST':
        flag = request.POST.get('flag')
        print(flag)
        if flag == '0':
            matchID = request.POST.get('matchId')
            match = Match.objects.get(matchID=matchID)
            if match:
                return JsonResponse({"instance": 'data', 'matchId': matchID, 'team1': match.team1, 'team2': match.team2}, status=200)
            else:
                return JsonResponse({"error": "No Match With This ID."},status=404)
        if flag == '1':
            matchID = request.POST.get('matchId')
            toss = request.POST.get('toss')
            batting = request.POST.get('batting')
            bowling = request.POST.get('bowling')
            over = request.POST.get('over')

            print(matchID)
            match = Match.objects.get(matchID=matchID)
            matchExtra = MatchExtra.objects.create(matchID=match, toss=toss,batting=batting, bowling=bowling, over=over)
            if match:
                return JsonResponse({"instance": 'data', 'matchId': matchID, 'toss': matchExtra.toss,'batting': matchExtra.batting,'bowling': matchExtra.bowling, 'over': matchExtra.over}, status=200)
            else:
                return JsonResponse({"error": "No Match With This ID."}, status=404)
    return render(request, 'firstapp/match_toss.html')

## Match View
@csrf_exempt
def match_view(request):
    from .models import Team
    objectlist = Team.objects.all()
    from .models import Match
    match =Match.objects.all()
    #print(objectlist)

    if request.is_ajax and request.method == 'POST':
    
        data = request.POST.getlist('tmp[]') # to get a list 
        matchID = request.POST.get('matchId')
        print(data)
        if data:
            batsman = data[0]
            runMate = data[1]
            bowler = data[2]
            fielder = data[3]
            run = data[4]
            wicket = data[5]
            outBatsman = data[6]+","+data[7]
            bowlerType =data[8]
            extraRunType =data[9]
            extraRun = data[10]
            ballNo= data[12]
            #print(batsman, run, bowler)
            
            foo = MV.objects.create(batsman = batsman, bowler = bowler, run = run, wicket = wicket, outBatsman=outBatsman, match_ref_id = matchID,  bowlerType= bowlerType, extraRunType=extraRunType, extraRun= extraRun, ballNo=ballNo)
            #print(foo)
            return JsonResponse({"instance": data, 'matchId': matchID}, status=200)
        else:
            return JsonResponse({"error": ""}, status=400)
    # else:
    #     fm = MatchView()
    return render(request,'firstapp/match_view.html', {'objectlist':objectlist,'form5':'fm','match': match })


#volleyball view
@csrf_exempt
def volleyball_view(request):
    #return render(request,'volleyball_view.html', {'name':'Shahrier'})
    from .models import Team
    objectlist = Team.objects.all()
    from .models import Match
    match = Match.objects.all()
   #print(objectlist)

    if request.is_ajax and request.method == 'POST':
    
        data = request.POST.getlist('tmp[]') # to get a list 
        matchID = request.POST.get('matchId')
        print(data)
        if data:
            playerID = data[0]
            setNo = data[1]
            team1Point = data[2]
            team2Point = data[3]
            timestamp = data[4]
            action = data[5]
           
            
            #return HttpResponseRedirect('/thanks/')
            #print(playerID)
            
            foo = VolleyBallModel.objects.create(playerID=playerID,setNo=setNo,team1Point=team1Point,team2Point=team2Point, timestamp=timestamp, match_ref_id = matchID, action=action)
            #print(foo)
            return JsonResponse({"instance": data, 'matchId': matchID}, status=200)
        else:
            return JsonResponse({"error": ""}, status=400)
    # else:
    #     fm = MatchView()
    return render(request,'firstapp/volleyball_view.html', {'objectlist':objectlist,'form6':'fm','match': match })

#Football view
@csrf_exempt
def football_view(request):
    from .models import Team
    objectlist = Team.objects.all()
    from .models import Match
    match = Match.objects.all()
    #print(objectlist)

    if request.is_ajax and request.method == 'POST': 
        data = request.POST.getlist('tmp[]') # to get a list 
        matchID = request.POST.get('matchId')
        print(data)
        if data:
            playerID = data[0]
            attack = data[1]
            defence = data[2]
            passing = data[3]
            running = data[4]
            timestamp = "time"
           
            
            #return HttpResponseRedirect('/thanks/')
            #print(playerID)
            
            foo = FootBallModel.objects.create(playerID=playerID, attack = attack, defence=defence,passing=passing,running=running, timestamp=timestamp, match_ref_id = matchID,)
            #print(foo)
            return JsonResponse({"instance": data, 'matchId': matchID}, status=200)
        else:
            return JsonResponse({"error": ""}, status=400)
    # else:
    #     fm = MatchView()
    return render(request,'firstapp/football_view.html', {'objectlist':objectlist,'match': match })








##====== Dashboard ==============

def dashboard_demo(request):
    innings_1 = pd.read_csv('data/1_innings_1.csv') # use pandas to read the csv
    innings_2 = pd.read_csv('data/1_innings_2.csv')
    #match_ref_id = innings_1.iloc[0, 6] ##df.iloc[<row>, <column>]
    match_ref_id = 1 
    run_inn_1 = innings_1['run'].sum()
    six_innings_1 =  innings_1['run'].value_counts()[6] 
    four_innings_1 =  innings_1['run'].value_counts()[4]
    three_innings_1 =  innings_1['run'].value_counts()[3]
    two_innings_1 =  innings_1['run'].value_counts()[2] 
    one_innings_1 =  innings_1['run'].value_counts()[1] 
    dot_innings_1 = innings_1['run'].value_counts()[0] 
    wicket_innings_1 = innings_1['wicket'].value_counts()['run_out'] + innings_1['wicket'].value_counts()['catch_out'] + innings_1['wicket'].value_counts()['bowled_out'] 
    ##innings 2
    run_inn_2 = innings_2['run'].sum()
    six_innings_2 =  innings_2['run'].value_counts()[6] 
    four_innings_2 =  innings_2['run'].value_counts()[4]
    three_innings_2 =  innings_2['run'].value_counts()[3]
    two_innings_2 =  innings_2['run'].value_counts()[2] 
    one_innings_2 =  innings_2['run'].value_counts()[1] 
    dot_innings_2 = innings_2['run'].value_counts()[0] 
    wicket_innings_2 = innings_2['wicket'].value_counts()['run_out'] + innings_2['wicket'].value_counts()['catch_out'] + innings_2['wicket'].value_counts()['bowled_out'] 
    ##result
    result =  (run_inn_1 -  run_inn_2)

    #individual player report
    df= pd.DataFrame(innings_1)
    df2 = pd.DataFrame(innings_2)
    playerName = 'p7'
    ##--batting
    batsmanRun = df.loc[df['batsman'] ==  playerName, 'run'].sum()
    ballFaced = df.loc[df['batsman'] ==  playerName, 'run'].count()
    batRunSix = df.loc[(df['batsman'] ==  playerName)& (df['run'] == 6), 'run'].count()
    batRunFour = df.loc[(df['batsman'] ==  playerName)& (df['run'] == 4), 'run'].count()
    strikerate = float("{:.2f}".format(batsmanRun/ballFaced))*100
    ## --bowling
    checkBowler = df2[df2['bowler']==playerName] #check if bowler is existed
    checkBowler = len( checkBowler)
    bowlerBall=bowlerWicket=bowlerRun=bowlerAvg=bowlerEco=0 #initialize
    if( checkBowler!=0):
        bowlerBall = df2['bowler'].value_counts()[playerName]
        bowlerRun = df2.loc[df2['bowler'] == playerName, 'run'].sum()
        bowlerWicket = df2.loc[(df2['bowler'] == playerName)& (df['wicket'] != 'N/A'), 'wicket'].count()
        bowlerAvg = float("{:.2f}".format(bowlerRun/bowlerWicket))
        bowlerOver = bowlerBall/6
        bowlerEco = float("{:.2f}".format(bowlerRun/bowlerOver))
    
    #VolleyBall
    volleyBallData = pd.read_csv('data/volleyBallData.csv') #pandas to read the csv  
    df= pd.DataFrame(volleyBallData)
    playerName = 'p17' #fixed player for testing purpose
    numOfReturned = df.loc[(df['playerID'] ==  playerName)& (df['action'] == 'returned'), 'action'].count()
    numOfFailed = df.loc[(df['playerID'] ==  playerName)& (df['action'] == 'failed'), 'action'].count()
    numOfSmashed = df.loc[(df['playerID'] ==  playerName)& (df['action'] == 'Smashed'), 'action'].count()
    numOfMissed = df.loc[(df['playerID'] ==  playerName)& (df['action'] == 'missed'), 'action'].count()
    numOfSentOut = df.loc[(df['playerID'] ==  playerName)& (df['action'] == 'sentOut'), 'action'].count()
    numOfSaved = df.loc[(df['playerID'] ==  playerName)& (df['action'] == 'saved'), 'action'].count()
    numOfServed = df.loc[(df['playerID'] ==  playerName)& (df['action'] == 'served'), 'action'].count()
    numOfBarred = df.loc[(df['playerID'] ==  playerName)& (df['action'] == 'barred'), 'action'].count()
    
    #point achieved 
    numofError = numOfFailed + numOfMissed + numOfSentOut
    numOfPoint = numOfSmashed + numOfBarred













    ##=========Render============
    return render(request,'firstapp/dashboard_demo.html',
     {'run_inn_1': run_inn_1, 'run_inn_2': run_inn_2, 'match_ref_id': match_ref_id, 
     #innings 1
     'six_innings_1':six_innings_1 ,'four_innings_1': four_innings_1, 'three_innings_1':three_innings_1,'two_innings_1':two_innings_1,'one_innings_1':one_innings_1,'dot_innings_1':dot_innings_1,
     'wicket_innings_1': wicket_innings_1,
     #innings 2
     'six_innings_2':six_innings_2 ,'four_innings_2': four_innings_2, 'three_innings_2':three_innings_2,'two_innings_2':two_innings_2,'one_innings_2':one_innings_2,'dot_innings_2':dot_innings_2, 'result':result,
     'wicket_innings_2': wicket_innings_2, 
     #Indivual 
     'playerName':playerName,'batsmanRun': batsmanRun, 'ballFaced':ballFaced, 'batRunSix':batRunSix,'batRunFour':batRunFour, 'strikerate':strikerate,
     'bowlerBall':bowlerBall,'bowlerRun':bowlerRun,'bowlerWicket':bowlerWicket, 
     'bowlerAvg':  bowlerAvg, 'bowlerEco':bowlerEco,
     #Volleyball
     'numOfSmashed':numOfSmashed, 'numOfBarred':numOfBarred, 'numofError':numofError,'numOfPoint':numOfPoint

     
     })





#########################################################################

def home(request):
    return render(request,'firstapp/home.html', {'name':'Shahrier'})

def contact(request):
    return HttpResponse('<h1>Contact</h1>')   
   
def school_reg(request):
    
    return render(request,'firstapp/school_reg.html', {'name':'School Registration'})

def player_reg(request):
    #return HttpResponse('<h1>Contact</h1>')   
    #if request.method == 'POST':
    #   firstname = request.POST['fName']
       
    return render(request,'firstapp/player_reg.html', {'name':'Player Registration'})
    #return HttpResponse(firstname) 

def player_data(request):
    #return HttpResponse('<h1>Contact</h1>')   
    return render(request,'firstapp/player_data.html', {'name':'Player Data'})

def team_formation(request):
      
    return render(request,'firstapp/team_formation.html', {'name':'Team Formation'})
