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
        userAddress = userAddress.replace(" ", "+")

        url = 'https://maps.googleapis.com/maps/api/geocode/json?address=' + userAddress + '&key=AIzaSyDGnMTSopj_ZzyiNWEEM_pdb6tBCHYxEc8'
        #url = 'https://maps.googleapis.com/maps/api/geocode/json?address=1600+Amphitheatre+Parkway,+Mountain+View,+CA&key=AIzaSyDGnMTSopj_ZzyiNWEEM_pdb6tBCHYxEc8'

        location_response = urlfetch.fetch(url).content
        location_response_json = json.loads(location_response)

        latitude = location_response_json['results'][0]['geometry']['location']['lat']
        longitude = location_response_json['results'][0]['geometry']['location']['lng']

        #cuisines = self.request.params.getall('cuisine')
        cuisine = self.request.get('cuisine')
        cuisine = cuisine.lower()
        user_miles = self.request.get("miles")
        miles = str(int(user_miles)*1609.34)

        api_url = 'https://maps.googleapis.com/maps/api/place/nearbysearch/json?location=' + str(latitude) + ',' + str(longitude) + '&radius=' + miles + '&type=restaurant&keyword=' + str(cuisine) + '&key=AIzaSyDGnMTSopj_ZzyiNWEEM_pdb6tBCHYxEc8'
        #print api_url
        rest_response = urlfetch.fetch(api_url).content
        rest_response_json = json.loads(rest_response)
        #print rest_response_json

        restaurants = []
        ratings = []
        photos = []
        for restaurant in rest_response_json['results'][0:10]:
            restaurants.append(restaurant['name'])
            ratings.append(restaurant['rating'])
            photo_url = 'https://maps.googleapis.com/maps/api/place/photo?maxwidth=400&photoreference=' + str(restaurant['photos'][0]['photo_reference']) + '&key=AIzaSyDGnMTSopj_ZzyiNWEEM_pdb6tBCHYxEc8'
            photos.append(photo_url)

        dict = {
            "restaurant_names" : restaurants,
            "rating_keys" : ratings,
            "photo_keys" : photos
        }

        restaurants_nearby_template = jinja_env.get_template('restaurants_nearby/restaurants_nearby.html')
        self.response.write(restaurants_nearby_template.render(dict))

class Summary(webapp2.RequestHandler):
    def get(self):
        summary_template = jinja_env.get_template('summary.html')

class Restaurant(webapp2.RequestHandler):
    def get(self):
        restaurant_template = jinja_env.get_template('restaurant.html')

    # def changespacesintopluses:
    #     text = 'Team Foodie Rocks'
    #     print(re.sub("[ ]", "+", text))

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
