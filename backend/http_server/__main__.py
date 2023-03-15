import os
import argparse


def create_app():
    from flask import Flask
    from .page.default import welcome_page
    app = Flask(__name__)
    app.secret_key = os.urandom(12)
    app.add_url_rule('/', view_func=welcome_page)
    return app


def run_develop(app):
    app.run(port=5000, host='0.0.0.0', debug=True)


def run_production(app):
    from waitress import serve
    serve(app, host='0.0.0.0', port=5000)



if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        formatter_class=argparse.RawTextHelpFormatter,
        description='Running the application.'
    )

    parser.add_argument('-c', '--config-name', dest='config_name', type=str, required=True,
                        help='An example:\npython main.py --config-name development|production')
    args = parser.parse_args()
    application = create_app()
    if args.config_name == "development":
        run_develop(application)

    if args.config_name == "production":
        run_production(application)