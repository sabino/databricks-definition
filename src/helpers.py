from databricks_api import DatabricksAPI
import json


def dictfilt(x, y):
    return dict([(i, x[i]) for i in x if i in set(y)])


def get_db():
    with open("../config.json", "r") as config:
        return DatabricksAPI(**json.load(config))
