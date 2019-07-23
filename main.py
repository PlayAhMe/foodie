import webapp2
import jinja2
import os
from google.appengine.api import urlfetch
import json


jinja_env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

class Home(webapp2.RequestHandler):
    def get(self):
        home_template = jinja_env.get_template('home/home.html')
        self.response.write(home_template.render())
class Filters(webapp2.RequestHandler):
    def get(self):
        filters_template = jinja_env.get_template('filters/filters.html')
        self.response.write(filters_template.render())
class RestaurantsNearby(webapp2.RequestHandler):
    def post(self):
        api_url = "https://maps.googleapis.com/maps/api/place/nearbysearch/json?location=-33.8670522,151.1957362&radius=5&type=restaurant&keyword=Mexican&key=AIzaSyDGnMTSopj_ZzyiNWEEM_pdb6tBCHYxEc8"
        response = urlfetch.fetch(api_url).content
        #print response
        latitude = self.request.get("lat")
        longitude = self.request.get("lng")
        name = self.request.get("name")
        icon = self.request.get("icon")
        photos = self.request.get("photos")
        rating = self.request.get("rating")
        restaurant_dict = {
            "latitude": latitude,
            "longitude": longitude,
            "name": name,
            "icon": icon,
            "photos": photos,
            "rating": rating,
        }
        restaurants_nearby_template = jinja_env.get_template('restaurants_nearby/restaurants_nearby.html')
        self.response.write(restaurants_nearby_template.render())
class Summary(webapp2.RequestHandler):
    def get(self):
        summary_template = jinja_env.get_template('summary.html')

class Restaurant(webapp2.RequestHandler):
    def get(self):
        restaurant_template = jinja_env.get_template('restaurant.html')

app = webapp2.WSGIApplication(
    [
        ('/', Home),
        ('/filters', Filters),
        ('/restaurants_nearby', RestaurantsNearby),
        ('/summary', Summary),
        ('/restaurant', Restaurant),
    ],
    debug = True
)
