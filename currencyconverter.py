from currency_converter import ECB_URL, SINGLE_DAY_ECB_URL

# Load the packaged data (might not be up to date)
c = CurrencyConverter()

# Download the full history, this will be up to date. Current value is:
# https://www.ecb.europa.eu/stats/eurofxref/eurofxref-hist.zip
c = CurrencyConverter(ECB_URL)

# Dowload only the latest available day. Current value is:
# https://www.ecb.europa.eu/stats/eurofxref/eurofxref.zip
c = CurrencyConverter(SINGLE_DAY_ECB_URL)

# Load your custom file
c = CurrencyConverter('./path/to/currency/file.csv')