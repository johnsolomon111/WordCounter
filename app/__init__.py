from flask import Flask, request
import sqlite3
server = Flask(__name__)

from app.models import *

# createCountTable() #uncomment this if Db does not exist
from app.utilities import *
from app.app import *
