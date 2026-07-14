from flask import Blueprint, jsonify
from analysis.data_loader import load_data

prices_bp = Blueprint("prices", __name__)


@prices_bp.route("/prices", methods=["GET"])
def get_prices():

    df = load_data("data/BrentOilPrices.csv")

    df["Date"] = df["Date"].astype(str)

    return jsonify(df.to_dict(orient="records"))