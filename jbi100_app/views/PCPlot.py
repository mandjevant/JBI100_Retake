from dash import dcc, html
import plotly.express as px


class PCPlot(html.Div):
    def __init__(self, name, df):
        """
        PCP plot class for the PCP plot graph
        :param df: dataframe for the PCP plot
        """
        self.html_id = name.lower().replace(" ", "-")
        self.df = df

        # Equivalent to `html.Div([...])`
        super().__init__(
            className="graph_card",
            children=[
                html.H6(name, id="PCPNAME"),
                dcc.Graph(id=self.html_id)
            ],
        )

    def update(self, col_list):
        """
        Update the multivariate plot based on the selection
         of columns in the checklist.
        :param: col_list list of columns
        :return: updated figure
        """
        # Create the figure
        self.fig = px.parallel_coordinates(self.df[col_list],
                                           color="CARAVAN",
                                           color_continuous_scale=px.colors.sequential.Bluered_r,
                                           height=600)

        return self.fig
