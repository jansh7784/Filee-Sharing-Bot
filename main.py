#!/usr/bin/env python3
"""
Ansh Music Bot - Simple and Clean
"""

import logging
from bot import Bot

# Set up logging
logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S'
)

logger = logging.getLogger(__name__)

if __name__ == "__main__":
    logger.info("🚀 Starting Ansh Music Bot...")
    Bot().run()