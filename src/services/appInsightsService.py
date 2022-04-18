from datetime import datetime, timedelta

import requests
import pandas as pd


class AppInsightsService:
    def __init__(self, base_url, application_id, api_key):
        self._api_key = api_key
        self._base_url = f"{base_url}/{application_id}/"
        self.session = requests.Session()
        self.session.headers['x-api-key'] = api_key

    @staticmethod
    def _result_to_df(data):
        # Convert the JSON into a dictionary of pandas dataframes
        result = {}
        for table in data['tables']:
            result[table['name']] = pd.DataFrame.from_records(table['rows'],
                                                              columns=[col['name'] for col in table['columns']])
        return result

    def _query_past_seconds(self, query, seconds: int):
        resp = self.session.get(self._base_url + "query", params={'query': query, 'timespan': f'PT{seconds}S'})
        resp.raise_for_status()
        return resp.json()

    def _query(self, query, start_date):
        date_now = datetime.utcnow().isoformat()
        start_date = start_date + timedelta(milliseconds=1)
        time_interval = f'{start_date.isoformat()}/{date_now}'

        resp = self.session.get(self._base_url + "query", params={'query': query, 'timespan': f'{time_interval}'})

        resp.raise_for_status()
        return resp.json()

    def query_as_df(self, query, start_date: datetime, primary_result=True):
        result = self._query(query, start_date)
        if primary_result:
            return self._result_to_df(result)['PrimaryResult']
        return self._result_to_df(result)
