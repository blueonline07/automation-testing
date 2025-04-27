import unittest

import pandas as pd

from eatest import EATest
from natest import NATest


def loadsuite(test_cls, data_source: str):
    df = pd.read_csv(data_source, dtype=str)
    df = df.fillna("")
    suite = unittest.TestSuite()
    for row in df.itertuples():
        data = {
            "email":row[1],
            "password":row[2],
            "firstname":row[3],
            "lastname":row[4],
            "address":row[5],
            "city":row[6],
            "postcode": row[7],
            "country":row[8],
            "zone":row[9],
        }
        output = {
            "class_":row[10],
            "text_":row[11]
        }
        suite.addTest(test_cls("test_case", data, output))

    return suite

if __name__ == "__main__":
    NASuite = loadsuite(NATest, 'https://docs.google.com/spreadsheets/d/e/2PACX-1vQMlrtlEly7hMK1eLYPMp-vHPAond1KIeAtTIWwp6mu4Z9hWdCaix_SITrQfzI5xnMvpbru9DnGSwD9/pub?gid=0&single=true&output=csv')
    EASuite = loadsuite(EATest, 'https://docs.google.com/spreadsheets/d/e/2PACX-1vQMlrtlEly7hMK1eLYPMp-vHPAond1KIeAtTIWwp6mu4Z9hWdCaix_SITrQfzI5xnMvpbru9DnGSwD9/pub?gid=271412661&single=true&output=csv')
    runner = unittest.TextTestRunner()

    runner.run(NASuite)
    runner.run(EASuite)