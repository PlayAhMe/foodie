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
        userAddress = self.request.get("user_address")
        #cuisines = self.request.params.getall('cuisine')
        cuisine = self.request.get('cuisine')
        print "cuisine" + cuisine

        api_url = 'https://maps.googleapis.com/maps/api/place/nearbysearch/json?location=42.339500,-83.056160&radius=10000&type=restaurant&keyword=mexican&key=AIzaSyDGnMTSopj_ZzyiNWEEM_pdb6tBCHYxEc8'
        rest_response = urlfetch.fetch(api_url).content
        rest_response_json = json.loads(rest_response)

        restaurants = []
        for restaurant in rest_response_json['results'][0:10]:
            restaurants.append(restaurant["name"])
        rest_dict = {
            "restaurant" : restaurant
        }
        print "rest_dict" + str(rest_dict)

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
