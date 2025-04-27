import unittest

import pandas as pd
from custom import CustomTest


def loadsuite(test_cls, data_source: str, fields: str):
    datas= pd.read_csv(data_source, dtype=str)
    fields = pd.read_csv(fields, dtype=str)
    suite = unittest.TestSuite()
    for t in datas.itertuples():
        t = t._asdict()
        steps = []
        for f in fields.itertuples():
            step = {
                'field': f[1],
                'xpath': f[2],
                'type': f[3],
                'data': t[f[1]] if f[1] in t else None,
            }
            steps.append(step)
        output = {
            'xpath': t['out_xpath'],
            'value': t['out_value']
        }
        suite.addTest(test_cls('https://ecommerce-playground.lambdatest.io/index.php?route=account/login', steps, output))

    return suite

if __name__ == "__main__":
    data = 'https://docs.google.com/spreadsheets/d/e/2PACX-1vQMlrtlEly7hMK1eLYPMp-vHPAond1KIeAtTIWwp6mu4Z9hWdCaix_SITrQfzI5xnMvpbru9DnGSwD9/pub?gid=913268719&single=true&output=csv'
    fields = 'https://docs.google.com/spreadsheets/d/e/2PACX-1vQMlrtlEly7hMK1eLYPMp-vHPAond1KIeAtTIWwp6mu4Z9hWdCaix_SITrQfzI5xnMvpbru9DnGSwD9/pub?gid=1303266692&single=true&output=csv'
    suite = loadsuite(CustomTest, data, fields)
    runner = unittest.TextTestRunner()
    runner.run(suite)
