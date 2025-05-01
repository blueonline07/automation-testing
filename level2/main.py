import unittest

import pandas as pd
from custom import CustomTest
import argparse

def loadsuite(test_cls, data_source: str, fields: str):
    suite = unittest.TestSuite()
    fields = pd.read_csv(fields, dtype=str).fillna("")
    datas= pd.read_csv(data_source, dtype=str).fillna("")
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
        suite.addTest(test_cls(steps, output))
    return suite

if __name__ == "__main__":
    suites = [
        loadsuite(CustomTest, 'https://docs.google.com/spreadsheets/d/e/2PACX-1vQMlrtlEly7hMK1eLYPMp-vHPAond1KIeAtTIWwp6mu4Z9hWdCaix_SITrQfzI5xnMvpbru9DnGSwD9/pub?gid=0&single=true&output=csv', 'https://docs.google.com/spreadsheets/d/e/2PACX-1vQMlrtlEly7hMK1eLYPMp-vHPAond1KIeAtTIWwp6mu4Z9hWdCaix_SITrQfzI5xnMvpbru9DnGSwD9/pub?gid=1736309277&single=true&output=csv'),
        loadsuite(CustomTest, 'https://docs.google.com/spreadsheets/d/e/2PACX-1vQMlrtlEly7hMK1eLYPMp-vHPAond1KIeAtTIWwp6mu4Z9hWdCaix_SITrQfzI5xnMvpbru9DnGSwD9/pub?gid=271412661&single=true&output=csv', 'https://docs.google.com/spreadsheets/d/e/2PACX-1vQMlrtlEly7hMK1eLYPMp-vHPAond1KIeAtTIWwp6mu4Z9hWdCaix_SITrQfzI5xnMvpbru9DnGSwD9/pub?gid=1295565285&single=true&output=csv'),
        loadsuite(CustomTest, 'https://docs.google.com/spreadsheets/d/e/2PACX-1vQMlrtlEly7hMK1eLYPMp-vHPAond1KIeAtTIWwp6mu4Z9hWdCaix_SITrQfzI5xnMvpbru9DnGSwD9/pub?gid=1971721181&single=true&output=csv', 'https://docs.google.com/spreadsheets/d/e/2PACX-1vQMlrtlEly7hMK1eLYPMp-vHPAond1KIeAtTIWwp6mu4Z9hWdCaix_SITrQfzI5xnMvpbru9DnGSwD9/pub?gid=1615296235&single=true&output=csv'),
        loadsuite(CustomTest, 'https://docs.google.com/spreadsheets/d/e/2PACX-1vQMlrtlEly7hMK1eLYPMp-vHPAond1KIeAtTIWwp6mu4Z9hWdCaix_SITrQfzI5xnMvpbru9DnGSwD9/pub?gid=2008912901&single=true&output=csv', 'https://docs.google.com/spreadsheets/d/e/2PACX-1vQMlrtlEly7hMK1eLYPMp-vHPAond1KIeAtTIWwp6mu4Z9hWdCaix_SITrQfzI5xnMvpbru9DnGSwD9/pub?gid=1158241216&single=true&output=csv')
    ]

    parser = argparse.ArgumentParser()
    parser.add_argument('--suite', type=int, choices=[0, 1, 2, 3], required=True)
    args = parser.parse_args()
    runner = unittest.TextTestRunner()
    runner.run(suites[args.suite])
