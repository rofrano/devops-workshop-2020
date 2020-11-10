import logging
from flask import Flask

app = Flask(__name__)

from service import routes, log_handler
