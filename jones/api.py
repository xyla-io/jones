import requests

from typing import Optional, Dict
from furl import furl

class FixerAPI:
  api_key: str

  def __init__(self, api_key: str):
    self.api_key = api_key

  def _api_call(self, method, endpoint: str, parameters: Dict[str, any], verbose: bool=False):
    url = furl('https://data.fixer.io')
    url.path = '/api/{endpoint}'.format(
      endpoint=endpoint,
    )

    parameters['access_key'] = self.api_key
    url.args = parameters
    req = method(url.url)

    if verbose:
      print(url)
      print(req.text)

    return req.json()

  def get(self, endpoint: str, parameters: Dict[str, any], verbose: bool=False):
    return self._api_call(
      method=requests.get,
      endpoint=endpoint,
      parameters=parameters,
      verbose=verbose,
    )
