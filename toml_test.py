import toml
from pprint import pprint

with open(".streamlit/secrets.toml", "rt") as f:
    secrets = toml.load(f)

pprint(secrets)
