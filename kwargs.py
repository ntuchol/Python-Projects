 def read_data(filepath, **kwargs):
 def read_data(filepath, **kwargs):
        encoding = kwargs.get('encoding', 'utf-8')  
        header = kwargs.get('header', True)         
        separator = kwargs.get('sep', ',')          

        # Example: using pandas to read a CSV
        import pandas as pd
        df = pd.read_csv(filepath, encoding=encoding, sep=separator, header=header)
        return df

    data_frame_1 = read_data('my_data.csv', encoding='latin-1', sep=';')
    data_frame_2 = read_data('another_data.txt', header=False, sep='\t')
