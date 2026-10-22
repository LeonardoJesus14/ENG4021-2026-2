from django.shortcuts import render

# Create your views here.

def home(request):
    response = requests.get("https://omdbapi.com/?apikey=38b4b85b&s=Batman&y=2022&type=movie")
    response_json = response.json()
    movies = response_json["Search"]
    context = {
        "movies": movies
    }

    return render(request, "index.html", context)
