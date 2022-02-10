from django.shortcuts import render, redirect
from . models import Product
from . forms import ProductForm
from urllib.request import urlopen
import json
import pandas as pd

# Create your views here.

def index(request):
    products = Product.objects.all()

    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = ProductForm()        

    context = {
        "products": products,
        "form": form
    }
    url = "https://api.etherscan.io/api?module=account&startblock=0&endblock=99999999&sort=asc&apikey=ZDGWTTZ8NFEFYFEN5KPM157MUDR9QAQDSR"
    response = urlopen(url)
    data_json = json.loads(response.read())
    df = pd.read_json(data_json)
    df.to_csv(r'info.csv', index=None)

    return render(request, 'chartapp/index.html', context)


def pie(request):
    products = Product.objects.all()

    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('pie')
    else:
        form = ProductForm()

    context = {
        "products": products,
        "form": form
    }
    url = "https://api.etherscan.io/api?module=account&startblock=0&endblock=99999999&sort=asc&apikey=ZDGWTTZ8NFEFYFEN5KPM157MUDR9QAQDSR"
    response = urlopen(url)
    data_json = json.loads(response.read())
    df = pd.read_json(data_json)
    df.to_csv(r'info.csv', index=None)
    return render(request, 'chartapp/pie.html', context)


def line(request):
    products = Product.objects.all()

    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('line')
    else:
        form = ProductForm()

    context = {
        "products": products,
        "form": form
    }
    url = "https://api.etherscan.io/api?module=account&startblock=0&endblock=99999999&sort=asc&apikey=ZDGWTTZ8NFEFYFEN5KPM157MUDR9QAQDSR"
    response = urlopen(url)
    data_json = json.loads(response.read())
    df = pd.read_json(data_json)
    df.to_csv(r'info.csv', index=None)

    return render(request, 'chartapp/line.html', context)
