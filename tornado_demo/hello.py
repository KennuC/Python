import tornado.ioloop # importing main event loop

import tornado.web #map requests to request handlers

class HelloHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, Sir!")

class PostHandler (tornado.web.RequestHandler):
    def get(self):
        self.write("<h1> This is Post 1 </h1>")

class HomeHandler (tornado.web.RequestHandler):
    def get(self):
        self.render("home.html")

class WeatherHandler(tornado.web.RequestHandler):
    def get(self):
        degree = int(self.get_argument("degree"))
        output = "Hot!" if degree > 20 else "Cold"
        drink = "Have some beer" if degree > 20 else "Hot choco"
        self.render("weather.html", output = output, drink = drink)

def make_app():
    return tornado.web.Application([
        (r"/", HelloHandler),
        (r"/post", PostHandler),
        (r"/home", HomeHandler),
        (r"/weather", WeatherHandler)
    ],
    debug = True,
    autoreload = True)


if __name__ == "__main__":
    app = make_app()
    port = 8888
    app.listen(port)
    print(f"Server is listeninig on port {8888}")
    tornado.ioloop.IOLoop.current().start()