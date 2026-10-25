"""
OPIM 3510 - Module 2 forecasting helpers
Dr. Dave Wanik - University of Connecticut

One scorecard for every forecast we make this module.

    from forecast_helpers import evaluate

    evaluate(actual, predicted)
    evaluate(actual, predicted, naive=naive_forecast)

Sign convention (same all module long):
    error = predicted - actual
    positive error -> we OVER-forecast
    negative error -> we UNDER-forecast
"""
import numpy as np
import pandas as pd


def evaluate(actual, predicted, naive=None):
    """Score a forecast. Returns a pandas Series you can stack into a leaderboard.

    actual    : the true values (Series, list, or numpy array)
    predicted : your forecast for the same time steps
    naive     : (optional) a baseline forecast for the same time steps.
                If you give one, you also get "skill vs naive (%)":
                how much smaller your MAE is than the baseline's MAE.
                Positive = you beat the baseline. Negative = the baseline wins.

    Rows where any of the forecasts is missing (NaN) are dropped first,
    so every model is scored on exactly the same time steps.
    """
    # put everything side by side so the rows line up
    scores = pd.DataFrame({"actual": actual, "predicted": predicted})
    if naive is not None:
        scores["naive"] = naive

    # only score time steps where we have every number
    scores = scores.dropna()

    # error = predicted - actual
    error = scores["predicted"] - scores["actual"]

    # the four forecast KPIs
    bias = error.mean()
    mae = error.abs().mean()
    rmse = np.sqrt((error ** 2).mean())
    mape = (error.abs() / scores["actual"].abs()).mean() * 100

    results = {
        "n": len(scores),
        "bias": bias,
        "MAE": mae,
        "RMSE": rmse,
        "MAPE (%)": mape,
    }

    # how much better than the baseline?
    if naive is not None:
        naive_error = scores["naive"] - scores["actual"]
        naive_mae = naive_error.abs().mean()
        results["skill vs naive (%)"] = (1 - mae / naive_mae) * 100

    return pd.Series(results).round(2)
