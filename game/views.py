from django.http import  HttpResponse

# Create your views here.
def index(request):
    line1 = '<h1 style= "text-align: center">Warlock_Brawl</h1>'
    line2 = '<img src="https://assets.dicebreaker.com/0-dungeons-and-dragons-warlock-5e-guide.png/BROK/resize/1920x1920%3E/format/jpg/quality/80/0-dungeons-and-dragons-warlock-5e-guide.png">'
    return HttpResponse(line1 + line2);

