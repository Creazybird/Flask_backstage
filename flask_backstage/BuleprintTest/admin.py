from flask import Blueprint

admin = Blueprint('admin', __name__ ,static_folder='static')
@admin.route('/')
def admin_hone():
    return 'admin_home'

@admin.route('/new')
def new():
    return 'new'

@admin.route('/edit')
def edit():
    return 'edit'

@admin.route('/publish')
def publish():
    return 'publish'
