import unittest

from ..api import FixerAPI

class Test_FixerAPI(unittest.TestCase):
    def setUp(self):
      self.api = FixerAPI(api_key='API_KEY')

    def test_api_connection(self):
      """
      Test that the AppsFlyer class connects to the Apple Search Ads API
      """
      report_parameters = {
        'base': 'USD',
        'symbols': 'USD,CAD',
      }
      response = self.api.get(endpoint='latest', parameters=report_parameters, verbose=True)

      self.assertIsNotNone(response)
    
