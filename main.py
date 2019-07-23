import webapp2
import jinja2
import os


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
    def get(self):
        restaurants_nearby_template = jinja_env.get_template('restaurants_nearby.html')
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
