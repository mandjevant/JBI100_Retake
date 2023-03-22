from jbi100_app.main import app
from jbi100_app.views.menu import make_menu_layout
from jbi100_app.views.PCPlot import PCPlot
from jbi100_app.views.Heatmap import Heatmap
from jbi100_app.views.HistogramFrequencySingleAttr import HistogramFrequencySingleAttr
from jbi100_app.views.HistogramFrequencyGroup import HistogramFrequencyGroupAttr
from jbi100_app.data import get_data

from dash import html, dcc
import plotly.express as px
from dash.dependencies import Input, Output, State


if __name__ == '__main__':
    # Create data
    df = get_data()
    train_df = df[df["ORIGIN"] == "train"]
    test_df = df[df["ORIGIN"] == "test"]

    # Instantiate custom views
    pcp_plot = PCPlot("Parallel coordinate plot (PCP)", train_df)
    heatmap_plot = Heatmap(train_df)
    hist_single_plot = HistogramFrequencySingleAttr("HistogramFrequencySingleAttr", train_df)
    hist_group_plot = HistogramFrequencyGroupAttr("HistogramFrequencyGroupAttr", train_df)

    app.layout = html.Div(
        id="app-container",
        children=[
            # Left column
            html.Div(
                id="left-column",
                className="three columns",
                children=make_menu_layout()
            ),

            # Right column
            html.Div(
                id="right-column",
                className="nine columns",
                children=[
                    pcp_plot,
                    html.Div(
                        className="graph_card",
                        children=[
                            html.H6("Correlation between features"),
                            dcc.Graph(id="heatmapplot", figure=heatmap_plot.fig),
                        ]),
                    hist_single_plot,
                    hist_group_plot
                ],
                # Custom styling to allow right column to scroll
                # style={"flex": "1 1 auto",
                #        "overflow": "auto"},
            ),
        ],
        # style={"display": "flex", "height": "100vh"},
    )

    # Define interactions
    @app.callback(
        Output(pcp_plot.html_id, "figure"),
        [Input("select-columns-pcp", "value")]
    )
    def update_pcp_1(selected_columns):
        return pcp_plot.update(selected_columns)


    @app.callback(
        [Output(hist_single_plot.html_id, "figure"),
         Output("HistogramFrequencySingleAttr_HistogramFrequencySingleAttr", "children")],
        Input("select-single-attr", "value")
    )
    def update_single_attr_hist(attr1):
        return \
            hist_single_plot.update(attr1), \
            f"Histogram distribution plot attribute {attr1}"

    @app.callback(
        [Output(hist_group_plot.html_id, "figure"),
         Output("HistogramFrequencyGroupAttr_HistogramFrequencyGroupAttr", "children")],
        Input("select-group-attr", "value")
    )
    def update_grouped_dist_hist(group_attr1):
        return \
            hist_group_plot.update(group_attr1), \
            f"Histogram distribution plot attribute group {group_attr1}"

    # Data description popup
    # https://dash-bootstrap-components.opensource.faculty.ai/docs/components/modal/
    @app.callback(
        Output("modal", "is_open"),
        Input("open", "n_clicks"),
        State("modal", "is_open"),
    )
    def dataset_description_popup(n1, is_open):
        if n1:
            return not is_open
        return is_open

    app.run_server(debug=True, dev_tools_ui=True,)
