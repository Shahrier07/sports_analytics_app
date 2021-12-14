from django.db import models

# Create your models here.
 
class User(models.Model):
    name = models.CharField(max_length=200)
    mobile_number = models.IntegerField()

## School
class School(models.Model):
    schoolID= models.CharField(max_length=100, primary_key=True)  
    schoolName= models.CharField(max_length=100)  
    schoolAddress= models.CharField(max_length=100)
    schoolThana= models.CharField(max_length=100)
    postCode= models.CharField(max_length=100)
    subDistrict= models.CharField(max_length=100)
    district= models.CharField(max_length=100)
    phoneNo= models.CharField(max_length=100)
    email= models.EmailField(max_length=100)
    contPerName= models.CharField(max_length=100)
    schlUname= models.CharField(max_length=100)
    password= models.CharField(max_length=100)
    schoolType=(
        ('Primary','Primary'),
        ('Secondary','Secondary'),
        ('Madrassa','Madrassa'),
        )
    schoolType= models.CharField(max_length=100,choices=schoolType)
    studentType=(
        ('Boys','Boys'),
        ('Girls','Girls'),
        ('Coed','Coed'),
        )
    studentType= models.CharField(max_length=100,choices=studentType)

    def __str__(self):
        return "%s %s" % (self.schoolID, self.schoolName)

## Player Reg DB
class Player(models.Model):
    playerID= models.CharField(max_length=100,default="p",primary_key=True) 
    schoolID= models.ForeignKey(School, on_delete=models.CASCADE, null=True)
    fName= models.CharField(max_length=100)
    lName= models.CharField(max_length=100)  
    birthDate= models.DateTimeField()
    ageGroup= models.CharField(max_length=100)
    gender=(
        ('Male','Male'),
        ('Female','Female'),
        )
    gender= models.CharField(max_length=100,choices=gender)
    playerAddress= models.CharField(max_length=100)
    city= models.CharField(max_length=100)
    province= models.CharField(max_length=100)
    postCode= models.CharField(max_length=100)
    parentName= models.CharField(max_length=100)
    parentPhoneNo= models.CharField(max_length=100)
    parentWorkPlace= models.CharField(max_length=100)
    size=(
        ('XS','XS'),
        ('S','S'),
        ('M','M'),
        ('L','L'),
        ('XL','XL'),
        ('XXL','XXL'),
        )
    size= models.CharField(max_length=100, choices=size)

    def __str__(self):
        return "%s %s  %s" % (self.playerID, self.schoolID,self.fName)
    
## Team
class Team(models.Model):
    teamID= models.CharField(max_length=100, primary_key=True)
    schoolID= models.ForeignKey(School, on_delete=models.CASCADE, null=True)  
    teamName= models.CharField(max_length=100)

    sportsType=(
        ('cricket','Cricket'),
        ('football','Football'),
        ('volleyball','Volleyball')
        )
    sportsType= models.CharField(max_length=100,choices=sportsType)
    numOfPlayer= models.CharField(max_length=100)
    player1= models.CharField(max_length=100)
    player2= models.CharField(max_length=100)
    player3= models.CharField(max_length=100)
    player4= models.CharField(max_length=100)
    player5= models.CharField(max_length=100) 
    player6= models.CharField(max_length=100)
    player7= models.CharField(max_length=100)
    player8= models.CharField(max_length=100)   
    player9= models.CharField(max_length=100)
    player10= models.CharField(max_length=100)   
    player11= models.CharField(max_length=100)

    def __str__(self):
        return "%s  %s %s" % (self.teamID, self.schoolID,self.teamName)

## Match
class Match(models.Model):
    matchID= models.CharField(max_length=100,primary_key=True)  
    matchDate= models.DateField()
    matchTime= models.TimeField()
    venue= models.CharField(max_length=100)
    school= models.CharField(max_length=100)
    classes= models.CharField(max_length=100)
    team1= models.CharField(max_length=100)
    team2= models.CharField(max_length=100)
    trmtName= models.CharField(max_length=100) 
    sportsType=(
            ('cricket','Cricket'),
            ('football','Football'),
            ('volleyball','Volleyball')
            )
    sportsType= models.CharField(max_length=100,choices=sportsType)

class MatchExtra(models.Model):
    matchID = models.ForeignKey(Match, on_delete=models.CASCADE, null=True)
    toss = models.CharField(max_length=100)
    over = models.IntegerField()
    result = models.CharField(max_length=100)
    batting = models.CharField(max_length=100, default="temporary")
    bowling = models.CharField(max_length=100, default="temporary")
    
## Match View
class MatchView(models.Model):
    #match_ref_id = models.OneToOneField(Match, on_delete=models.CASCADE, null=True) 
    batsman= models.CharField(max_length=100)
    bowler= models.CharField(max_length=100)
    run= models.CharField(max_length=100)
    wicket= models.CharField(max_length=100)
    match_ref_id = models.CharField(max_length=100) 
    bowlerType= models.CharField(max_length=100, default="temporary") 
    extraRunType= models.CharField(max_length=100, default="temporary")
    extraRun= models.CharField(max_length=100, default="temporary")
    ballNo= models.CharField(max_length=100, default="temporary") 
    outBatsman = models.CharField(max_length=100, default="temporary") 
    
##volleyball
class VolleyBallModel(models.Model): 
    playerID= models.CharField(max_length=100)
    #playerName= models.CharField(max_length=100)
    timestamp= models.CharField(max_length=100)
    match_ref_id = models.CharField(max_length=100, default="temporary") 
    setNo = models.CharField(max_length=100, default="temporary")
    team1Point = models.CharField(max_length=100, default="temporary")
    team2Point = models.CharField(max_length=100, default="temporary")
    action =  models.CharField(max_length=100, default="temporary")
    

## Football
class FootBallModel(models.Model): 
    playerID= models.CharField(max_length=100)
    #playerName= models.CharField(max_length=100)
    timestamp= models.CharField(max_length=100)
    match_ref_id = models.CharField(max_length=100, default="temporary") 
    attack =  models.CharField(max_length=100, default="temporary")
    defence = models.CharField(max_length=100, default="temporary")
    passing = models.CharField(max_length=100, default="temporary")
    running = models.CharField(max_length=100, default="temporary")
    

