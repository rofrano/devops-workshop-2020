from service import app

counter = 0

############################################################
# R O U T E S
############################################################
@app.route("/")
def index():
    return "Hello Flask"

@app.route("/counter")
def get_counter():
    global counter
    counter += 1
    return dict(counter=counter)

############################################################
# Utility for testing
############################################################
def reset_counter():
    global counter
    if app.testing:
        counter = 0 