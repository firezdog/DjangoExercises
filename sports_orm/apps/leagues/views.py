from django.shortcuts import render, redirect
from .models import League, Team, Player
from django.db.models import Count

from . import team_maker

def index(request):
	context = {
		"leagues": League.objects.all(),
		"teams": Team.objects.annotate(num_players = Count('all_players')).filter(num_players__gt = 12),
		"players": Player.objects.annotate(num_teams = Count('all_teams')).order_by('num_teams')
	}

	return render(request, "leagues/index.html", context)

def make_data(request):
	team_maker.gen_leagues(10)
	team_maker.gen_teams(50)
	team_maker.gen_players(200)

	return redirect("index")