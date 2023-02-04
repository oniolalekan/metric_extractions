# test metric_extraction
import pandas as pd
import metric_extraction as me
import pytest


def test_metric_extraction():
    dataset = pd.read_excel('test_data.xlsx')

    assert me.metrics_extract(dataset) == (124, 8)
