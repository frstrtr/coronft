from flask import Flask

import folium

app = Flask(__name__)


@app.route('/')
def index():
    start_coords = (46.9540700, 142.7360300)
    folium_map = folium.Map(width=1000, height=700, zoom_start=5.5,
              location=[52.5, 19], tiles='http://tile.stamen.com/toner/{z}/{x}/{y}.png', 
    attr="toner-bcgs")
    return folium_map._repr_html_()


if __name__ == '__main__':
    app.run(debug=True)