import pandas as pd

def load_dataset(uploaded_file):

    if uploaded_file.name.endswith(".csv"):

        try:
            df = pd.read_csv(uploaded_file)

        except UnicodeDecodeError:
            uploaded_file.seek(0)
            df = pd.read_csv(
                uploaded_file,
                encoding="latin1"
            )

    elif uploaded_file.name.endswith(".xlsx"):

        df = pd.read_excel(uploaded_file)

    else:
        return None

    return df