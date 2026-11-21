import pandas as pd

from analiza import podstawowe_statystyki

def test_pusty_dataframe(capsys):
    df = pd.DataFrame()
    podstawowe_statystyki(df)
    captured = capsys.readouterr().out
    assert captured == "Najpierw wczytaj dane z pliku CSV.\n"