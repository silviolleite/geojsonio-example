from shapely.geometry import Point, Polygon
import geopandas as gpd
import geojsonio

p1 = Point(-45.85959434509277, -23.218788635003936)

polygon = Polygon([(
              -45.86620330810547,
              -23.19244047577093
),
                  (
              -45.887489318847656,
              -23.20979613466111
                  ),
(
              -45.87787628173828,
              -23.2315664097847
),
(
              -45.85075378417969,
              -23.228096024018107
),
(
              -45.86620330810547,
              -23.19244047577093
)])
#arregando as coordenadas com as variáveis
states = gpd.GeoDataFrame(geometry=[p1, polygon])

#Carregando as coordenadas com arquivo .geojon
#states = gpd.read_file('sjcinpe.geojson')

states.loc[0, 'name'] = 'INPE'
states.loc[0, 'marker-color'] = '#48ff00'

print(states.head())
states = states.to_json()

geojsonio.display(states)
