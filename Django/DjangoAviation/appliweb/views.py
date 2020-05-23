from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from appliweb.models import airports, accidents_events, aircrafts, fatalities_report, flight_info, departure_airport, destination_airport

from django.http import HttpResponseRedirect
from .forms import SearchForm, SearchFormPerDate, SearchFormBetweenTwoDates


# Page d'acceuil : vue index déclenchant le template home.tmpl
def index(request) :
    #return HttpResponse("Cette page d'accueil est à définir.... \n")
    return render(request, 'home.tmpl')


#############################################################################################

from .views2 import worldmap, template2

#############################################################################################


#vue pour la table airports
def aeroport(request) :
    return render(request, 'airports.tmpl', 
        {                                          
            'airports': airports.objects.all(),
            'nb': airports.objects.count(),
            'rien': airports.objects.count()==0
        })

#vue pour la table accidents_events
def accident(request) :
    return render(request, 'accidents.tmpl', 
        {                                          
            'accidents': accidents_events.objects.all(),
            'nb': accidents_events.objects.count(),
            'rien': accidents_events.objects.count()==0
        })


############# Recherches dans la table accidents ############

#### Recherche par année #########

#vue associée au formulaire de recherche pour récupérer les paramètres de recherche par année
def get_search_parameters(request):
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            year=form.cleaned_data['year']

            # redirection vers la vue utilisant les paramètres :
            return HttpResponseRedirect(f"/appliweb/accident/{year}/")

    else:
        form = SearchForm()

    return render(request, 'search.tmpl', {'form': form})

#vue pour la table accidents_events avec paramètres de recherche
def accidentSearch(request,year) :
    queryset = accidents_events.objects.filter(identifiant__startswith=year).order_by('identifiant')
    #queryset = accidents_events.objects.filter(identifiant[:4]=year).order_by('identifiant')
    return render(request, 'accidents.tmpl', 
        {                                          
            'accidents': queryset,
            'nb': queryset.count(),
            'rien': queryset.count()==0
        })


#### Recherche pour une date précise #########

#vue associée au formulaire de recherche pour récupérer les paramètres de recherche pour une date précise
def get_search_parameters_per_date(request):
    if request.method == 'POST':
        form = SearchFormPerDate(request.POST)
        if form.is_valid():
            year=form.cleaned_data['year']
            month=form.cleaned_data['month']
            day=form.cleaned_data['day']

            # redirection vers la vue utilisant les paramètres :
            return HttpResponseRedirect(f"/appliweb/accident/date/{year}{month}{day}/")

    else:
        form = SearchFormPerDate()

    return render(request, 'search.tmpl', {'form': form})

#vue pour la table accidents_events avec paramètres de recherche par date
def accidentSearchPerDate(request,date) :
    queryset = accidents_events.objects.filter(identifiant__startswith=date).order_by('identifiant')
    #queryset = accidents_events.objects.filter(identifiant[:4]=year).order_by('identifiant')
    return render(request, 'accidents.tmpl', 
        {                                          
            'accidents': queryset,
            'nb': queryset.count(),
            'rien': queryset.count()==0
        })


#### Recherche entre deux dates #########

#vue associée au formulaire de recherche pour récupérer les paramètres de recherche pour une date précise
def get_search_parameters_per_dates(request):
    if request.method == 'POST':
        form = SearchFormBetweenTwoDates(request.POST)
        if form.is_valid():
            year_1=form.cleaned_data['year_1']
            month_1=form.cleaned_data['month_1']
            day_1=form.cleaned_data['day_1']

            year_2=form.cleaned_data['year_2']
            month_2=form.cleaned_data['month_2']
            day_2=form.cleaned_data['day_2']

            # redirection vers la vue utilisant les paramètres :
            return HttpResponseRedirect(f"/appliweb/accident/{year_1}{month_1}{day_1}/{year_2}{month_2}{day_2}/")

    else:
        form = SearchFormBetweenTwoDates()

    return render(request, 'search.tmpl', {'form': form})

#vue pour la table accidents_events avec paramètres de recherche par date
def accidentSearchPerDates(request,dateDebut,dateFin) :
    queryset = accidents_events.objects.filter(identifiant__gte=dateDebut,identifiant__lte=dateFin).order_by('identifiant')
    #queryset = accidents_events.objects.filter(identifiant[:4]=year).order_by('identifiant')
    return render(request, 'accidents.tmpl', 
        {                                          
            'accidents': queryset,
            'nb': queryset.count(),
            'rien': queryset.count()==0
        })


### vue pour lien de rédirection vers les filtres pour accidents

def tableAccidents(request) :
    return render(request, 'tableAccidents.tmpl')