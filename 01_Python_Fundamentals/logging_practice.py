import logging
from pathlib import Path

log_dir = Path("logs")
log_dir.mkdir(exist_ok=True)

logging.basicConfig(
    level=logging.DEBUG, 
    format="%(asctime)s | %(levelname)s | %(name)s - %(message)s",
    handlers=[
        logging.FileHandler(log_dir / "pipeline.log", encoding="utf-8"),
        logging.StreamHandler()
    ]                   
)

logger = logging.getLogger(__name__)

logger.info("Pipeline started")
logger.info("Reading the source data")
logger.warning("Some records failed validation")
logger.info("Pipeline completed successfully")

