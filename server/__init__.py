from flask import Flask, send_from_directory

def create_app(test_config=None):
    # set up app config
    app = Flask(__name__, static_url_path='', static_folder='../client')
    app.url_map.strict_slashes = False
    app.config.from_mapping(
        SECRET_KEY='super_secret_key'
    )

    @app.route('/', defaults={'path':''})
    def serve(path):
        return send_from_directory(app.static_folder, 'index.html')

    @app.route('/hello')
    def hello():
        return 'hello world'

    return app