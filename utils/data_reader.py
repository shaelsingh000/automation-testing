import csv
import json
import yaml
import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

def read_csv(file_name):
    path = os.path.join(BASE_DIR, "data", file_name)
    with open(path, newline="", encoding="utf-8") as f:
        return [row["search_term"] for row in csv.DictReader(f)]

def read_json(file_name):
    path = os.path.join(BASE_DIR, "data", file_name)
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)
    return data["search_terms"]

def read_yaml(file_name):
    path = os.path.join(BASE_DIR, "data", file_name)
    with open(path, "r", encoding="utf-8") as f:
        data = yaml.safe_load(f)
    return data["search_terms"]
