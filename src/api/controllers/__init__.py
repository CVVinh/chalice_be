from api.controllers.prefecture_controller import prefecture_bp
from api.controllers.base_controller import base_bp
from api.controllers.account_controller import account_bp
from api.controllers.rental_order_controller import rental_order_bp
from api.controllers.vehicles_controller import vehicles_bp
from api.controllers.makers_controller import makers_bp
from api.controllers.stores_controller import stores_bp
from api.controllers.insurance_controller import insurance_bp
from api.controllers.option_controller import option_bp
from api.controllers.payment_method_controller import payment_method_bp


def init_app(app):
    base_url = '/'
    app.register_blueprint(prefecture_bp, url_prefix=base_url)
    app.register_blueprint(base_bp, url_prefix=base_url)
    app.register_blueprint(account_bp, url_prefix=base_url)
    app.register_blueprint(rental_order_bp, url_prefix=base_url)
    app.register_blueprint(vehicles_bp, url_prefix=base_url)
    app.register_blueprint(makers_bp, url_prefix=base_url)
    app.register_blueprint(stores_bp, url_prefix=base_url)
    app.register_blueprint(insurance_bp, url_prefix=base_url)
    app.register_blueprint(option_bp, url_prefix=base_url)
    app.register_blueprint(payment_method_bp, url_prefix=base_url)
