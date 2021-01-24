#!/usr/bin/env python3
"""
Crunch numbers from speedtest output.
"""
import pandas as pd
import requests

pd.options.display.float_format = "{:,.2f}".format


def list_versions():
    """
    List library versions.
    """
    print("pandas: {}".format(pd.__version__))
    print("requests: {}".format(requests.__version__))


if __name__ == "__main__":
    list_versions()

    df = pd.read_csv(
        "speedtest/speedtest.csv", index_col="Timestamp", parse_dates=["Timestamp"]
    )

    df = df.drop(["Share"], axis=1)
    print("=" * 16)
    print(df)

    print("=" * 16)
    print(df.columns)

    print("=" * 16)
    print(df["Download"])

    print("=" * 16)
    print(df.head(4))

    print("=" * 16)
    print(df.tail(4))

    print("=" * 16)
    print(df.describe())
