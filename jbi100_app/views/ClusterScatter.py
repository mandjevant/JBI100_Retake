from dash import dcc, html
import plotly.express as px


class ClusterScatterPlot(html.Div):
    def __init__(self, name):
        """
        Cluster scatter plot class for the cluster scatter plot
        """
        self.html_id = name.lower().replace(" ", "-")

        # Equivalent to `html.Div([...])`
        super().__init__(
            className="graph_card",
            children=[
                html.H6(name, id=f"clusterScatter_{name}"),
                dcc.Graph(id=self.html_id)
            ],
        )

    def update(self, x, y, color):
        # Update the scatter plot by the selected embedded x, y attributes.
        #  update the color based on attribute
        fig_scatter = px.scatter(
            x=x,
            y=y,
            color=color
        )
        return fig_scatter
