from dash import dcc, html
import plotly.express as px


class Heatmap(html.Div):
    def __init__(self, name, df):
        """
        Heatmap class for the heatmap graph.
        :param df: dataframe for the heat map plot
        """
        self.html_id = name.lower().replace(" ", "-")
        self.df = df

        # Equivalent to `html.Div([...])`
        super().__init__(
            className="graph_card",
            children=[
                html.H6("Heat map of selected attributes", id=f"heatmap_{name}"),
                dcc.Graph(id=self.html_id)
            ],
        )

    def update(self, col_list):
        # Update the heat map to display only the selected attributes.
        df = self.df[col_list]
        corr_df = df.corr(numeric_only=True)
        self.fig = px.imshow(corr_df,
                             x=corr_df.columns,
                             y=corr_df.index,
                             height=800,
                             width=800)
        return self.fig
