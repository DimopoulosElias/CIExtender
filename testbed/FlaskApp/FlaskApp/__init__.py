#From: https://0day.work/jinja2-template-injection-filter-bypasses/

from flask import *

app = Flask(__name__)

@app.route("/")
def home():
        output = request.args.get('name')
        #exec(output)
        blacklist = ["__class__", "request[request."]
        blacklist += ["__"]
    # Level 1
        for bad_string in blacklist:
                if  bad_string in output:
                        return "HACK ATTEMPT {}".format(bad_string), 400
    # Level 2
        for bad_string in blacklist:
                for param in request.args:
                        if bad_string in request.args[param]:
                                return "HACK ATTEMPT {}".format(bad_string), 400
                                
        output = render_template_string(output)
        #return output
        if output:
                pass
        else:
                output = "Test"
        return output

if __name__ == "__main__":
        app.run(debug=True)
