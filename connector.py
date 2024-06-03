
from fivetran_connector_sdk import Connector
from fivetran_connector_sdk import Operations as op
import requests as rq

def update(configuration: dict, state: dict):

    # Get pokemon data
    response = rq.get("https://pokeapi.co/api/v2/pokemon/")


if __name__ == "__main__":
    connector.debug()