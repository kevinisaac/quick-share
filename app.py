import falcon

# Resources
class Home:
    """The alpha resource."""
    def on_get(self, req, res):
        """Handles GET requests."""
        res.status = falcon.HTTP_200
        res.body = 'Ready to share?'

# Instantiating resources

app = falcon.API()

home = Home()

# Routes
app.add_route('/home', home)
