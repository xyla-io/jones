import unittest
import code

from ..api import FixerAPI
from ..reporting import FixerReporter
from datetime import datetime, timedelta

class Test_FixerReporter(unittest.TestCase):
    def setUp(self):
      api = FixerAPI(api_key='API_KEY')
      self.reporter = FixerReporter(api=api)
      self.reporter.verbose = True

    def test_exchange_rate_reporting(self):

      df = self.reporter.get_exchange_rate_report(from_currency='USD', to_currencies=['USD', 'CAD'], date=datetime(2018, 7, 1))

      print(df)
      self.assertIsNotNone(df)

    def test_exchange_rate_symmetry(self):
      date = datetime.utcnow() - timedelta(days=1)
      df1 = self.reporter.get_exchange_rate_report(from_currency='USD', to_currencies=['CAD'], date=date)
      print(df1)
      df2 = self.reporter.get_exchange_rate_report(from_currency='CAD', to_currencies=['USD'], date=date)
      print(df1)
      self.assertAlmostEqual(df1.rate[0], 1.0 / df2.rate[0], places=6)

