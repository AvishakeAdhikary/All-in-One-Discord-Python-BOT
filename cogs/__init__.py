import logging

# Configure logging for cogs
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Log that the cogs package has been initialized
logger.info('Cogs package initialized.')
