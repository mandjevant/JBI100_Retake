from dash import dcc, html
import plotly.express as px


class StackedBarChart(html.Div):
    def __init__(self, name, df):
        """
        StackedBarChart class for the stacked bar chart.
        param df: dataframe for the stacked bar chart plot
        """
        self.html_id = name.lower().replace(" ", "-")
        self.df = df

        # Equivalent to `html.Div([...])`
        super().__init__(
            className="graph_card",
            children=[
                html.H6(name, id=f"StackedBar_{name}"),
                dcc.Graph(id=self.html_id)
            ],
        )

    def update(self, col_name):
        self.fig = px.bar(self.df,
                          x=col_name,
                          color="CARAVAN")

        return self.fig
