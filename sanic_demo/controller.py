# this is our 'controller.py' file
from sanic import response
from sanic import Blueprint

my_bp = Blueprint('my_blueprint')

@my_bp.route('/my_bp')
async def my_bp_func(request):
	return response.text('My First Blueprint')
