from jbi100_app.main import app
from jbi100_app.views.menu import make_menu_layout
from jbi100_app.views.PCPlot import PCPlot
from jbi100_app.views.Heatmap import Heatmap
from jbi100_app.views.HistogramFrequencySingleAttr import HistogramFrequencySingleAttr
from jbi100_app.views.HistogramFrequencyGroup import BarFrequencyGroupAttr
from jbi100_app.views.HorizontalBarFeatures import FeatureImportances
from jbi100_app.views.ErrorBar import ErrorBar
from jbi100_app.views.ClusterScatter import ClusterScatterPlot
from jbi100_app.data import get_data, get_models_errors
from sklearn.inspection import permutation_importance
from umap import UMAP
from sklearn.manifold import TSNE
from sklearn.cluster import DBSCAN
import pandas as pd
from sklearn.preprocessing import MinMaxScaler

from dash import html
from dash.dependencies import Input, Output, State


if __name__ == '__main__':
    # Create data
    df = get_data()

    # Get the fitted models and errors on the prediction
    copy_train_df = df[df["ORIGIN"] == "train"].drop("ORIGIN", axis=1)
    copy_test_df = df[df["ORIGIN"] == "test"].drop("ORIGIN", axis=1)
    train_df = df[df["ORIGIN"] == "train"]
    test_df = df[df["ORIGIN"] == "test"]
    nb_m, dt_m, nb_e, dt_e = get_models_errors(copy_train_df, copy_test_df)

    # Get the naive bayes feature importances and errors
    nb_perm_importances = permutation_importance(nb_m,
                                                 copy_test_df.drop("CARAVAN", axis=1),
                                                 copy_test_df["CARAVAN"])
    nb_importances, nb_model_errors = nb_perm_importances.importances_mean, nb_e

    # Get the decision tree feature importances and errors
    dt_perm_importances = permutation_importance(dt_m,
                                                 copy_test_df.drop("CARAVAN", axis=1),
                                                 copy_test_df["CARAVAN"])
    dt_importances, dt_model_errors = dt_perm_importances.importances_mean, dt_e

    # Initiate embeddings
    umap = UMAP(n_neighbors=5, min_dist=0.1, n_components=2)
    tsne = TSNE(n_components=2, perplexity=100, learning_rate=200, n_iter=1000, init="random")
    umap_transformed = umap.fit_transform(MinMaxScaler().fit_transform(copy_train_df.drop("CARAVAN", axis=1)))
    tsne_transformed = tsne.fit_transform(MinMaxScaler().fit_transform(copy_train_df.drop("CARAVAN", axis=1)))

    # Perform clustering
    dbscan_clusters = DBSCAN(eps=0.025, min_samples=50, metric='euclidean')
    umap_labels = dbscan_clusters.fit_predict(MinMaxScaler().fit_transform(umap_transformed))
    tsne_labels = dbscan_clusters.fit_predict(MinMaxScaler().fit_transform(tsne_transformed))
    lab_umap = pd.Series(umap_labels, dtype=str)
    lab_tsne = pd.Series(tsne_labels, dtype=str)

    # Instantiate custom views
    pcp_plot = PCPlot("Parallel coordinate plot (PCP)", train_df)
    heatmap_plot = Heatmap("heatmapplot", train_df)
    hist_single_plot = HistogramFrequencySingleAttr("HistogramFrequencySingleAttr", train_df)
    bar_group_plot = BarFrequencyGroupAttr("BarFrequencyGroupAttr", train_df)
    err_bar = ErrorBar("ErrorBar")
    horiz_feature_importances = FeatureImportances("FeatureImportances")
    cluster_scatter_plot = ClusterScatterPlot("ClusterScatterPlot")

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
                    heatmap_plot,
                    hist_single_plot,
                    bar_group_plot,
                    err_bar,
                    horiz_feature_importances,
                    cluster_scatter_plot
                ],
                # Custom styling to allow right column to scroll
                style={"flex": "1 1 auto",
                       "overflow": "auto"},
            ),
        ],
        style={"display": "flex", "height": "100vh"},
    )

    # Define interactions
    @app.callback(
        [Output(pcp_plot.html_id, "figure"),
         Output(heatmap_plot.html_id, "figure")],
        [Input("select-columns-pcp", "value")]
    )
    def update_pcp_and_heatmap(selected_columns):
        # Update the heatmap and pcp plot
        #  to display only the selected columns
        return pcp_plot.update(selected_columns), heatmap_plot.update(selected_columns)

    @app.callback(
        [Output(hist_single_plot.html_id, "figure"),
         Output("HistogramFrequencySingleAttr_HistogramFrequencySingleAttr", "children")],
        [Input("select-single-attr", "value"),
         Input("heatmapplot", "clickData")]
    )
    def update_single_attr_hist(attr1, clickdata):
        # Update histogram
        #  to display the selected attribute
        #  and update the color on clickdata of heatmap
        if clickdata:
            return \
                hist_single_plot.update(attr1, clickdata['points'][0]['x']), \
                f"Histogram distribution plot attribute {attr1}"
        else:
            return \
                hist_single_plot.update(attr1, "CARAVAN"), \
                f"Histogram distribution plot attribute {attr1}"

    @app.callback(
        [Output(bar_group_plot.html_id, "figure"),
         Output("BarFrequencyGroupAttr_BarFrequencyGroupAttr", "children")],
        Input("select-group-attr", "value")
    )
    def update_grouped_dist_bar(group_name):
        # Update group bar plot
        #  groups attributes are manually filtered and based on the dataset description

        # Filter columns based on group name
        if group_name == "Religion":
            df_cols = ["MGODRK", "MGODPR", "MGODOV", "MGODGE"]
            attr_names = ["Roman catholic", "Protestant …", "Other religion", "No religion"]
        elif group_name == "Relationship":
            df_cols = ["MRELGE", "MRELSA", "MRELOV", "MFALLEEN"]
            attr_names = ["Married", "Living together", "Other relation", "Singles"]
        elif group_name == "Children":
            df_cols = ["MFGEKIND", "MFWEKIND"]
            attr_names = ["Household without children", "Household with children"]
        elif group_name == "Education":
            df_cols = ["MOPLHOOG", "MOPLMIDD", "MOPLLAAG"]
            attr_names = ["High level education", "Medium level education", "Lower level education"]
        elif group_name == "Occupation":
            df_cols = ["MBERHOOG", "MBERZELF", "MBERBOER", "MBERMIDD", "MBERARBG", "MBERARBO"]
            attr_names = ["High status", "Entrepreneur", "Farmer", "Middle management", "Skilled labourers",
                          "Unskilled labourers"]
        elif group_name == "Social class":
            df_cols = ["MSKA", "MSKB1", "MSKB2", "MSKC", "MSKD"]
            attr_names = ["Social class A", "Social class B1", "Social class B2", "Social class C", "Social class D"]
        elif group_name == "House owner":
            df_cols = ["MHHUUR", "MHKOOP"]
            attr_names = ["Rented house", "Home owners"]
        elif group_name == "Cars owned":
            df_cols = ["MAUT1", "MAUT2", "MAUT0"]
            attr_names = ["1 car", "2 cars", "No car"]
        elif group_name == "Health insurance":
            df_cols = ["MZFONDS", "MZPART"]
            attr_names = ["National Health Service", "Private health insurance"]
        elif group_name == "Income":
            df_cols = ["MINKM30", "MINK3045", "MINK4575", "MINK7512", "MINK123M", "MINKGEM"]
            attr_names = ["Income < 30.000", "Income 30-45.000", "Income 45-75.000", "Income 75-122.000",
                          "Income >123.000", "Average income"]

        return \
            bar_group_plot.update(df_cols, attr_names), \
            f"Bar plot attribute group {group_name}"

    # Data description popup
    # https://dash-bootstrap-components.opensource.faculty.ai/docs/components/modal/
    @app.callback(
        Output("modal", "is_open"),
        Input("open", "n_clicks"),
        State("modal", "is_open"),
    )
    def dataset_description_popup(n1, is_open):
        # Open popup on button click.
        #  this was made by following the example on the dash bootstrap components website
        if n1:
            return not is_open
        return is_open

    @app.callback(
        [Output(horiz_feature_importances.html_id, "figure"),
         Output("FeatureImportances_FeatureImportances", "children"),
         Output(err_bar.html_id, "figure"),
         Output("ErrorBar_ErrorBar", "children")],
        Input("select-model", "value")
    )
    def update_model(model_name):
        # Update the feature importances and error bar plot
        #  to display the selected model
        cols = copy_test_df.drop("CARAVAN", axis=1).columns
        if model_name == "Naive Bayes classifier":
            return \
                horiz_feature_importances.update(nb_importances, cols), \
                f"Feature importances {model_name} (Accuracy: {round(nb_model_errors[0], 3)})", \
                err_bar.update(nb_model_errors, model_name), \
                f"Error bar plot {model_name}"

        elif model_name == "Decision Tree classifier":
            return \
                horiz_feature_importances.update(dt_importances, cols), \
                f"Feature importances {model_name} (Accuracy: {round(dt_model_errors[0], 3)})", \
                err_bar.update(dt_model_errors, model_name), \
                f"Error bar plot {model_name}"

    @app.callback(
        [Output(cluster_scatter_plot.html_id, "figure"),
         Output("clusterScatter_ClusterScatterPlot", "children")],
        [Input("select-embedding", "value"),
         Input("select-color-cluster", "value")]
    )
    def update_clusteringscatter(embedding_name, c):
        # Update the cluster scatter plot
        #  to display the selected embedding
        #  color the points based on the selected attribute
        if embedding_name == "UMAP":
            if c == "Cluster":
                color = lab_umap
            else:
                ix = copy_train_df.columns.tolist().index(c)
                color = copy_train_df.iloc[:, ix]
            return \
                cluster_scatter_plot.update(umap_transformed[:, 0], umap_transformed[:, 1], color), \
                f"Cluster scatter plot {embedding_name}"

        elif embedding_name == "t-SNE":
            if c == "Cluster":
                color = lab_tsne
            else:
                ix = copy_train_df.columns.tolist().index(c)
                color = copy_train_df.iloc[:, ix]
            return \
                cluster_scatter_plot.update(tsne_transformed[:, 0], tsne_transformed[:, 1], color), \
                f"Cluster scatter plot {embedding_name}"


    app.run_server(debug=True, dev_tools_ui=True)
