#!/usr/bin/env python3
"""
Crunch numbers from speedtest output.
"""

import matplotlib.pyplot as plt
import pandas as pd
import requests

pd.options.display.float_format = "{:,.2f}".format


def list_versions():
    """
    List library versions.
    """
    print(f"pandas: {pd.__version__}")
    print(f"requests: {requests.__version__}")


if __name__ == "__main__":
    list_versions()

    df = pd.read_csv("speedtest/speedtest.csv", parse_dates=["time stamp"])
    sample_time = df["time stamp"]
    download_speed = df["download"]
    upload_speed = df["upload"]

    plt.style.use("dark_background")
    plt.figure(figsize=(16, 9))
    plt.title("Internet Speed")
    plt.xlabel("time")
    plt.gcf().axes[0].yaxis.get_major_formatter().set_scientific(False)
    plt.ylabel("speed")
    plt.scatter(sample_time, download_speed, label="download")
    plt.scatter(sample_time, upload_speed, label="upload")
    plt.legend()
    plt.show()
