import pandas as pd
import pickle
from joblib import load
# from collections import OrderedDict
from json2html import *


# Update file path to app specific path
test_df = pd.read_csv("app/home/model/test_df.csv")


def pred_function(x):
    """
    NOTE: Files required for correct functionality!

    Take in string input and feed it into model for cannabis predictions

    :param x: 'qualities to match'
    :type x: string
    :return: predictions
    :rtype: dict
    """

    # Load mode file and perform prediction
    model = load("app/home/model/mvp_product.joblib")
    tfidf = pickle.load(open("app/home/model/vectorizer.pickle", "rb"))
    review = [x]
    trans = tfidf.transform(review)
    pred = model.kneighbors(trans.todense())[1][0]
    # create empty dictionary
    pred_dict = {}
    # summary statistics of 5 closest neighbors
    for x in pred:
        # add new dictionary to pred_dict containing predictions
        preds_dict = OrderedDict({f"#{(1 + len(pred_dict))}": {"Strain": test_df["Strain"][x],
                                                         "Dosage Size": test_df["Dosage Size"][x],
                                                         "Rating Category": test_df["Rating Category"][x],
                                                         "Rating": test_df["Rating"][x],
                                                         "Type": test_df["Type"][x],
                                                         "Description": test_df["Description"][x],
                                                         "Flavor": test_df["Flavor"][x],
                                                         "Effects": test_df["Effects"][x],
                                                         "Ailments": test_df["Ailments"][x]}})
        pred_dict.update(preds_dict)
    html_data = json2html.convert(json=pred_dict,
                                  table_attributes="class=\"table tablesorter\"")

    return html_data
