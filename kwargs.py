 def read_data(filepath, **kwargs):
        # ...
 def read_data(filepath, **kwargs):
        encoding = kwargs.get('encoding', 'utf-8')  # Default to 'utf-8' if not provided
        header = kwargs.get('header', True)         # Default to True
        separator = kwargs.get('sep', ',')          # Default to comma

        # Example: using pandas to read a CSV
        import pandas as pd
        df = pd.read_csv(filepath, encoding=encoding, sep=separator, header=header)
        return df
        # Example usage:
    data_frame_1 = read_data('my_data.csv', encoding='latin-1', sep=';')
    data_frame_2 = read_data('another_data.txt', header=False, sep='\t')