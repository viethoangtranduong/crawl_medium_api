from flask import Flask, jsonify
from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with
# from flask_sqlalchemy import SQLAlchemy
from crawl_year_summary import scraper

application = Flask(__name__)
api = Api(application)


medium_read_args = reqparse.RequestParser()
medium_read_args.add_argument("publication_url", type = str, help = "publications_url needed", required = True)
medium_read_args.add_argument("year_query", type = str, help = "year_query required", required = True)


class read_publication(Resource):
    @application.route('/')
    def index():
        return "<h1>Welcome to our medium read_publication !!</h1>"

    def put(self, running):
        if running != "running":
            return {"outcome": "method not exist", 'val': running}, 405

        args = medium_read_args.parse_args()

        name = scraper(args['publication_url'], args['year_query'])
        output = {"url": args["publication_url"], "year": args['year_query'], "text": f"File ready at {name}"}

        # try:
        #     name = scraper(args['publication_url'], args['year_query'])
        #     output = {"url": args["publications_url"], "year": args['year_query'], "text": f"File ready at {name}"}

        # except:
        #     output = {"url": args["publications_url"], "year": args['year_query'], "text": "Error"}
        # print(output)
        resp = jsonify(output)
        resp.status_code = 200
        return resp

        # return output, 200


# registering resources
api.add_resource(read_publication, "/<string:running>")

if __name__ == "__main__":
    # app.run(host='0.0.0.0', port = 3000, debug=True)
    application.debug = True
    application.run()