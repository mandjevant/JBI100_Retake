from dash import dcc, html
import plotly.express as px


class FeatureImportances(html.Div):
    def __init__(self, name):
        """
        FeatureImportances class for the feature importance plot of a model.
        param df: dataframe for the feature importances plot
        """
        self.html_id = name.lower().replace(" ", "-")

        # Equivalent to `html.Div([...])`
        super().__init__(
            className="graph_card",
            children=[
                html.H6(name, id=f"FeatureImportances_{name}"),
                dcc.Graph(id=self.html_id)
            ],
        )

    def update(self, importances, cols):
        self.fig = px.bar(x=importances,
                          y=cols,
                          orientation="h",
                          height=1400,
                          labels={
                              "x": "Importance",
                              "y": "Feature"
                          })

        return self.fig
