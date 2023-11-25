import os


def get_file_path(symbol, data_type):
    # Ensure the folder exists, create it if not
    os.makedirs("reports", exist_ok=True)
    os.makedirs("reports/" + symbol.lower(), exist_ok=True)

    return os.path.join("reports", symbol.lower(), data_type + "_data.csv")
