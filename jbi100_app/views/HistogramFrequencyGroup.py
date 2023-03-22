from dash import dcc, html
import plotly.express as px


class HistogramFrequencyGroupAttr(html.Div):
    def __init__(self, name, df):
        """
        HistogramFrequencyGroupAttr class for the histogram plot of grouped attributes.
        param df: dataframe for the histogram plot
        """
        self.html_id = name.lower().replace(" ", "-")
        self.df = df

        # Equivalent to `html.Div([...])`
        super().__init__(
            className="graph_card",
            children=[
                html.H6(name, id=f"HistogramFrequencyGroupAttr_{name}"),
                dcc.Graph(id=self.html_id)
            ],
        )

    def update(self, group_name):
        self.fig = px.histogram(self.df[[group_name, "CARAVAN"]],
                                x=group_name,
                                color="CARAVAN",
                                hover_data=[group_name, "CARAVAN"],
                                barmode="overlay")

        return self.fig
