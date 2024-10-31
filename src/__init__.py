from flask import Flask

app = Flask(__name__)


# This import statement is at the bottom of the file to avoid circular imports
import src.routes
