import plotly.express as px


class Heatmap:
    def __init__(self, df):
        """
        Heatmap class for the heatmap graph.
        param df: dataframe for the heat map plot
        """
        self.df = df
        corr_df = self.df.corr(numeric_only=True)
        self.fig = px.imshow(corr_df,
                             x=corr_df.columns,
                             y=corr_df.index,
                             height=800,
                             width=800)
