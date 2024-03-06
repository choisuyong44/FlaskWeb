from flask import Blueprint

bp = Blueprint('main',__name__,url_prefix='/')


@bp.route("/hello")
def hello():
    return "Hello world"
    
@bp.route('/')
def index():
    return "Hello index"