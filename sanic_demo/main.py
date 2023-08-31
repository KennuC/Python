# this is our 'main.py' file
from sanic import Sanic
from sanic import response
from sanic.log import logger
from controller import my_bp # type: ignore
from sanic.exceptions import ServerError, NotFound

app = Sanic("Sanic")

app.blueprint(my_bp)

app.static('/flower', 'C:/Users/kennu/OneDrive/Documents/programming/Python/sanic_demo/flower.jpeg')

# raise Exception
@app.route('/timeout')
async def terminate(request):
    return response.text("Gateway Timeout error", status=504)
 
 
@app.exception(NotFound)
async def ignore_5xx(request, exception):
    return response.text(f"Gateway is always up: {request.url}")

@app.route("/")
async def run(request):
	return response.text("Hello World !")


@app.route("/post", methods =['POST'])
async def on_post(request):
	try:
		return response.json({"content": request.json})
	except Exception as ex:
		import traceback
		logger.error(f"{traceback.format_exc()}")

@app.route("/display")
def display(request):
    return response.file('C:/Users/kennu/OneDrive/Documents/programming/Python/sanic_demo/index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)