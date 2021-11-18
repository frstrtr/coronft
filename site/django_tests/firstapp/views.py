from django.shortcuts import render
from django.http import HttpResponse, response
import folium

# Create your views here.
def index(request):
    return HttpResponse("Hello world!")

def about(request):
    return HttpResponse("<h2> О сайте </h2>")
    
def contact(request):
    return HttpResponse("<h2>Контакты</h2>")

def tile(request, x, y, z):
    return HttpResponse("<h2> ({0}, {1}, {2}) </h2>".format(x, y, z))

def map(request):
    start_coords = (-1000, 1000)
    folium_map = folium.Map(location=start_coords, width=1500, height=900, min_zoom = 0, max_zoom = 7, zoom_start=0, crs='Simple', tiles='http://127.0.0.1:8000/map2/{z}/{x}/{y}.png',  #tiles='http://tile.stamen.com/toner/{z}/{x}/{y}.png', 
    attr="covid")
    
    tooltip = "Click me!"

    folium.CircleMarker(
    location=[-1000, 1000],
    radius=1,
    popup="Laurelhurst Park",
    color="#3186cc",
    # fill=False,
    # fill_color="#3186cc",
    ).add_to(folium_map)

    # folium.Marker(
    #     [-1000, 1000], popup="<i>Mt. Hood Meadows</i>", tooltip=tooltip
    # ).add_to(folium_map)
    folium.Marker(
        [45.3311, -121.7113], popup="<b>Timberline Lodge</b>", tooltip=tooltip
    ).add_to(folium_map)
    return HttpResponse(folium_map._repr_html_())

def map2(request, x, y, z):
    img = open('static/images/{0}/1.png'.format(z%2), 'rb')
    return response.FileResponse(img)
    # return render(request, "tile.html")