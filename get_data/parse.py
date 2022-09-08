import requests
import json

from support.imports import *


async def retrieve_source(URL, session):
    async with session.get(URL) as response:
        json_data = await response.json()
        return json_data
