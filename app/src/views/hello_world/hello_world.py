
from flask import Blueprint, render_template


hello_world_bp = Blueprint('hello_world', __name__, url_prefix='/hello_world')

@hello_world_bp.route('/', methods= ('GET',))
def hello_world():
    """
    Hello World View
    """
    return render_template('base.html')