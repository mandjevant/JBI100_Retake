from dash import dcc, html
import plotly.express as px


class HistogramFrequencySingleAttr(html.Div):
    def __init__(self, name, df):
        """
        HistogramFrequencySingleAttr class for the histogram plot of a single attribute.
        param df: dataframe for the histogram plot
        """
        self.html_id = name.lower().replace(" ", "-")
        self.df = df

        # Equivalent to `html.Div([...])`
        super().__init__(
            className="graph_card",
            children=[
                html.H6(name, id=f"HistogramFrequencySingleAttr_{name}"),
                dcc.Graph(id=self.html_id)
            ],
        )

    def update(self, col_name):
        self.fig = px.histogram(self.df,
                                x=col_name,
                                color="CARAVAN",
                                marginal="violin",
                                hover_data=self.df.columns,
                                barmode="stack")

        return self.fig
