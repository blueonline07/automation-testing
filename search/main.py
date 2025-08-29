import unittest
import argparse
import pandas as pd

from search import SearchTest


def loadsuite(data_source: str, browser: str):
    df = pd.read_csv(data_source, dtype=str)
    df = df.fillna("")
    suite = unittest.TestSuite()
    for row in df.itertuples():
        data = {
            "value":row[1],
            "output":row[2]
        }
        suite.addTest(SearchTest("test_case", data, browser))

    return suite

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Run tests with different browsers')
    parser.add_argument('--browser', type=str, default='chrome', choices=['chrome', 'firefox', 'edge', 'safari'], help='Browser to use for testing')
    args = parser.parse_args()
    suite = loadsuite('data.csv', args.browser)

    runner = unittest.TextTestRunner()
    runner.run(suite)
