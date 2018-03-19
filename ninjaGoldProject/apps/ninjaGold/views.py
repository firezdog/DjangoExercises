# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect
import random

# Create your views here.
def index(request):
    gold = request.session.get('gold', 0)
    request.session['gold'] = gold
    results = request.session.get('results', [])
    request.session['results'] = results
    context = {'gold': gold, 'results': results}
    return render(request, "index.html", context)

def process_money(request, building):
    earned = "earned"
    winnings = 0
    if building == 'farm':
        winnings += random.randint(10,20)
    elif building == 'cave':
        winnings += random.randint(5,10)
    elif building == 'house':
        winnings += random.randint(2,5)
    elif building == 'casino':
        winnings = random.randint(0,50)
        if random.randint(0,1) == 0:
            winnings *= -1
            earned = "lost"
    request.session['gold'] += winnings
    if earned == "lost":
        winnings *= -1
    request.session['results'].insert(0, "You went to the {} and {} {} gold".format(building, earned, winnings))
    return redirect('/')

def reset(request):
    request.session['gold'] = 0
    request.session['results'] = []
    return redirect('/')