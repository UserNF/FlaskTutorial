from flask import Blueprint

views = Blueprint('views', __name__)

# to define blueprint you define a function "hom" and put a decorator above it "views.route('/')"
@views.route('/')
def home(): 
    return "<h1>Test</h1>"
    
