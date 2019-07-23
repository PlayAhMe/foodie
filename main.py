import webapp2

class Home(webapp2.RequestHandler):
    def get(self):
        home_template = jinja_env.get_template('home.html')

class Filters(webapp2.RequestHandler):
    def get(self):
        filters_template = jinja_env.get_template('filters.html')

class RestaurantsNearby(webapp2.RequestHandler):
    def get(self):
        userCusine = self.request.get("top-line")
        restaurants_nearby_template = jinja_env.get_template('restaurants_nearby.html')

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
