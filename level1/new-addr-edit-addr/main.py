import unittest

import pandas as pd

from eatest import EATest
from natest import NATest


def loadsuite(test_cls, data_source: str):
    df = pd.read_csv(data_source, dtype=str)
    df = df.fillna("")
    suite = unittest.TestSuite()
    for row in df.itertuples():
        suite.addTest(test_cls("test_case", row._asdict()))
    return suite

if __name__ == "__main__":
    NASuite = loadsuite(NATest, 'https://docs.google.com/spreadsheets/d/e/2PACX-1vQMlrtlEly7hMK1eLYPMp-vHPAond1KIeAtTIWwp6mu4Z9hWdCaix_SITrQfzI5xnMvpbru9DnGSwD9/pub?gid=0&single=true&output=csv')
    EASuite = loadsuite(EATest, 'https://docs.google.com/spreadsheets/d/e/2PACX-1vQMlrtlEly7hMK1eLYPMp-vHPAond1KIeAtTIWwp6mu4Z9hWdCaix_SITrQfzI5xnMvpbru9DnGSwD9/pub?gid=271412661&single=true&output=csv')
    runner = unittest.TextTestRunner()

    runner.run(NASuite)
    runner.run(EASuite)