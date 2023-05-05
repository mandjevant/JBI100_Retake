from dash import dcc, html
import plotly.express as px
import pandas as pd


class ErrorBar(html.Div):
    def __init__(self, name):
        """
        ErrorBar class for the error bar plot graph.
        """
        self.html_id = name.lower().replace(" ", "-").replace(".", "")

        # Equivalent to `html.Div([...])`
        super().__init__(
            className="graph_card",
            children=[
                html.H6(name, id=f"ErrorBar_{name}"),
                dcc.Graph(id=self.html_id)
            ],
        )

    def update(self, scores: list, model_name: str):
        """
        :param scores: list of errors for chosen model
        :param model_name: name of chosen model
        """
        # create dictionary with the error measures
        df_dict = {
            "Accuracy": [scores[0]],
            "Precision": [scores[1]],
            "Recall": [scores[2]]
        }
        # turn dictionary into dataframe
        err_df = pd.DataFrame.from_dict(df_dict,
                                        orient="index",
                                        columns=[model_name])

        # Update the distribution plots with the error measures
        self.fig = px.bar(err_df,
                          x=err_df.index,
                          y=err_df.columns,
                          barmode="group",
                          labels={"index": "Error measure",
                                  "value": "Error score"})

        return self.fig
