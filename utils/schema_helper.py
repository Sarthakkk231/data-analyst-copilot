def get_schema(df):

    columns = df.columns.tolist()

    schema = "\n".join(columns)

    return schema