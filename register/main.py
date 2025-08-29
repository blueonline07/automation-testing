import unittest
import argparse
import pandas as pd

from register import RegisterTest


def loadsuite(data_source: str, browser: str):
    df = pd.read_csv(data_source, dtype=str)
    df = df.fillna("")
    suite = unittest.TestSuite()
    for row in df.itertuples():
        data = {
            "firstname":row[1],
            "lastname":row[2],
            "address":row[3],
            "city":row[4],
            "state":row[5],
            "postcode":row[6],
            "country":row[7],
            "phone":row[8],
            "email":row[9],
            "dob":row[10],
            "password":row[11],
            "output":row[12]
        }
        suite.addTest(RegisterTest("test_case", data, browser))

    return suite

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Run tests with different browsers')
    parser.add_argument('--browser', type=str, default='chrome', choices=['chrome', 'firefox', 'edge', 'safari'], help='Browser to use for testing')
    args = parser.parse_args()
    suite = loadsuite('data.csv', args.browser)

    runner = unittest.TextTestRunner()
    runner.run(suite)
