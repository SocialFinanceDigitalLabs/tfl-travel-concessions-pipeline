import pytest

from tfl_travel_concessions_pipeline.tfl import pipeline


def test_pipeline():
    assert pipeline("") == True
