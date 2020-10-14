import pandas as pd

from . import api
from datetime import datetime
from typing import Optional, List, Dict

class FixerReporter:
  api: api.FixerAPI
  verbose: bool = False

  def __init__(self, api: api.FixerAPI, verbose: bool=False):
    self.api = api
    self.verbose = verbose
    self._date_format = '%Y-%m-%d'

  def _convert_response_to_data_frame(self, response: str, columns: Optional[List[str]]) -> pd.DataFrame:
    records = [{'target': k, 'rate': response['rates'][k]} for k in response['rates']]
    df = pd.DataFrame.from_records(records)
    df['base'] = response['base']
    df['date'] = datetime.strptime(response['date'], self._date_format)

    if columns is not None:
      df = df[columns]

    return df

  def get_exchange_rate_report(self, from_currency: str, to_currencies: List[str], date: datetime, columns: Optional[List[str]]=None) -> pd.DataFrame:
    report_parameters = {
      'base': from_currency,
      'symbols': ','.join(to_currencies),
    }

    report = self.get_report(
      report_endpoint=date.strftime(self._date_format), 
      report_parameters=report_parameters, 
      columns=columns
    )
    return report

  def get_report(self, report_endpoint: str, report_parameters: Dict[str, any]={}, columns: Optional[List[str]]=None) -> pd.DataFrame:
    response = self.api.get(
      endpoint=report_endpoint, 
      parameters=report_parameters, 
      verbose=self.verbose
    )
    data_frame = self._convert_response_to_data_frame(response=response, columns=columns)
    return data_frame
