import logging
from flask import Flask, request

app = Flask(__name__)

# Configure logging
logging.basicConfig(
    filename='app.log',
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

# Create a logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

@app.route('/')
def index():
    logger.debug('This is a debug message.')
    logger.info('This is an info message.')
    logger.warning('This is a warning message.')
    logger.error('This is an error message.')
    logger.critical('This is a critical message.')
    return 'Hello, world!'

@app.route('/exception')
def exception_route():
    try:
        1 / 0
    except Exception as e:
       logger.exception("An exception occurred: %s", e)
       return "An error occurred, check the logs."

@app.before_request
def log_request_info():
    logger.info("Request: %s %s", request.method, request.path)
    logger.debug("Request Headers: %s", request.headers)
    if request.get_data():
        logger.debug("Request Body: %s", request.get_data().decode('utf-8'))

@app.after_request
def log_response_info(response):
     logger.info("Response status code: %s", response.status_code)
     logger.debug("Response headers: %s", response.headers)
     return response

if __name__ == '__main__':
    app.run(debug=True)