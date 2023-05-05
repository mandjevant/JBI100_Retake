from dash import dcc, html
import plotly.express as px
import pandas as pd


class BarFrequencyGroupAttr(html.Div):
    def __init__(self, name, df):
        """
        BarFrequencyGroupAttr class for the bar plot of grouped attributes.
        param df: dataframe for the bar plot
        """
        self.html_id = name.lower().replace(" ", "-")
        self.df = df

        # Equivalent to `html.Div([...])`
        super().__init__(
            className="graph_card",
            children=[
                html.H6(name, id=f"BarFrequencyGroupAttr_{name}"),
                dcc.Graph(id=self.html_id)
            ],
        )

    def update(self, group_cols, attr_names):
        # Map the group_cols to attr_names
        col_new_names = dict()
        for i in range(len(group_cols)):
            col_new_names.update({group_cols[i]: attr_names[i]})

        all_cols = group_cols.copy()
        all_cols.append("CARAVAN")

        # Get the data by grouping by caravan and mutating the df until we get our result
        sum_df = self.df[all_cols].groupby("CARAVAN").sum().T.reset_index()
        sum_df = pd.melt(sum_df, id_vars="index", var_name="bar", value_name="value")

        # Rename our columns with the new attr_names
        sum_df["index"] = sum_df["index"].map(col_new_names)

        # Create the bar chart
        self.fig = px.bar(sum_df,
                          x="bar",
                          y="value",
                          color="index",
                          barmode="stack",
                          labels={"value": "Frequency",
                                  "bar": "CARAVAN"})

        return self.fig
