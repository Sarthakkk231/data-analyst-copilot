import plotly.express as px

def create_chart(df):

    if df is None or df.empty:
        return None

    cols = df.columns

    # Case 1: Grouped + numeric (BAR CHART)
    if len(cols) == 2:
        x, y = cols[0], cols[1]

        if df[y].dtype in ["int64", "float64"]:
            return px.bar(df, x=x, y=y)

    # Case 2: Time series (LINE CHART)
    for col in cols:
        if "date" in col.lower():
            date_col = col
            value_col = [c for c in cols if c != col][0]

            return px.line(df, x=date_col, y=value_col)

    # Case 3: Numeric vs Numeric (SCATTER)
    numeric_cols = df.select_dtypes(include="number").columns

    if len(numeric_cols) >= 2:
        return px.scatter(df, x=numeric_cols[0], y=numeric_cols[1])

    # Case 4: Default BAR CHART
    if len(cols) >= 2:
        return px.bar(df, x=cols[0], y=cols[1])

    return None