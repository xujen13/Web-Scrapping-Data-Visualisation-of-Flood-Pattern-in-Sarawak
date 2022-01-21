from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.shortcuts import redirect, render
from plotly.offline import plot
import plotly.graph_objects as go
import pandas as pd
from django.urls import reverse
from home.forms import CustomUserCreationForm # Changed user to home, as we wanted this to import the CustomUserCreationForm from home

# Create your views here3

#@login_required(login_url='/accounts/login/')

def dashboard(request):
    return render(request, "home/dashboard.html")

def test(request):
    return render(request, "home/test.html")

def register(request):
    if request.method == "GET":
        return render(
            request, "home/register.html",
            {"form": CustomUserCreationForm}
        )
    elif request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect(reverse("home"))

#@login_required(login_url='/accounts/login/')
def home(request):
    def scatter():
        
        df =  pd.read_csv(r"C:\Users\User\Documents\SideHustles\FSProjOne\ADS.csv")

        data = [go.Histogram(x=df['Branch'],marker=dict(color='green'))] #histogram only needs one set of data

        layout = go.Layout(
        hovermode='closest',
         xaxis = {'title':'Language Branch'},
         yaxis = {'title': 'Number of Language Included'},
        title = 'Language Branch vs Language Variation'
        )


        fig = go.Figure(data=data,layout=layout)
        plot_div = plot(fig, output_type='div', include_plotlyjs=False)
        return plot_div

    def saza():
        
        df =  pd.read_csv(r"C:\Users\User\Documents\SideHustles\FSProjOne\ADS.csv")

        data = [go.Histogram(x=df['Branch'],marker=dict(color='green'))] #histogram only needs one set of data

        layout = go.Layout(
        hovermode='closest',
         xaxis = {'title':'Ohoho Branch'},
         yaxis = {'title': 'Number of Language Included'},
        title = 'I am just testing things out'
        )


        fig = go.Figure(data=data,layout=layout)
        plot_div = plot(fig, output_type='div', include_plotlyjs=False)
        return plot_div

    context ={
        'plot1': scatter(),
        'plot2': saza()
    }

    return render(request, 'home/dashboard.html', context)

def infobanjir(request):
    def uno():
        
        df =  pd.read_csv(r"C:\Users\User\Documents\SideHustles\FSProjOne\ADS.csv")

        data = [go.Histogram(x=df['Branch'],marker=dict(color='green'))] #histogram only needs one set of data

        layout = go.Layout(
        hovermode='closest',
         xaxis = {'title':'Language Branch'},
         yaxis = {'title': 'Number of Language Included'},
        title = 'Language Branch vs Language Variation'
        )


        fig = go.Figure(data=data,layout=layout)
        plot_div = plot(fig, output_type='div', include_plotlyjs=False)
        return plot_div

    context ={
        'plot1': uno()
    }

    return render(request, 'home/infobanjir.html', context)    

class page2PageView(TemplateView): #was planning to add another page, this could be handy once i wanted to designate the login page
    template_name ="home/Page2.html"

