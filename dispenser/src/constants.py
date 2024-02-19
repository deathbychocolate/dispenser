"""File to hold frequently used project constants"""

import logging
import os

logging.basicConfig(level=logging.INFO)
LOGGER = logging.getLogger(__name__)

PATH_PROJECT_ROOT = os.getcwd()
PATH_PROJECT_STOCK_DATA_FILE = os.path.join(
    PATH_PROJECT_ROOT, "dispenser/src/data/stock.json"
)
PATH_PROJECT_AVAILABLE_CASH_DATA_FILE = os.path.join(
    PATH_PROJECT_ROOT, "dispenser/src/data/cash.json"
)
