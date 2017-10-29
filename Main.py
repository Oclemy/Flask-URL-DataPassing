# Our main.py file.
# First import falsk,render_template, redirect and url_for
# We initialize flask passing in the name of the current source file.
# We will ur render_template to render our jinja template.
# Redirect will help us redirect to specific urls.
# url_for will build us a url from a function

# import flask
from flask import Flask, render_template, redirect, url_for

# initialize flask
app = Flask(__name__)


# homepage
@app.route('/')
def index():
    return render_template('index.html', site_title="Camposha.info", header="Dynamic URLS",
                           sub_header="Passing Variables Via URLS ",
                           description="Camposha.info is a programming portal site with hundreds of example projects.")


@app.route('/404')
def page_not_found():
    return render_template('index.html', site_title="Camposha.info", header="404 Error", sub_header="Page Not Found",
                           description="We cannot find the requested page on this server")


# build and redirect
@app.route('/user/<name>')
def login(name):
    # check for admin
    if name == 'admin':
        return render_template('index.html', site_title="Camposha.info", header="Welcome " + name,
                               sub_header="Get Started Below",
                               description="Hello " + name + " how do you do?")
        # check for guest
    elif name == 'guest':
        return render_template('index.html', site_title="Camposha.info", header="Welcome " + name,
                               sub_header="You are Guest.",
                               description="Hello " + name + " how do you do?")
        # check for others
    else:
        return redirect(url_for('page_not_found'))

# run flask
if __name__ == '__main__':
    app.run(debug=True)
