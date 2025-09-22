import logging
import os

def get_logger(level="INFO"):
    os.makedirs("logs", exist_ok=True)
    
    logger = logging.getLogger("AudioTranscriber")
    logger.setLevel(level.upper())

    # Console handler
    ch = logging.StreamHandler()
    ch.setLevel(level.upper())
    formatter = logging.Formatter("[%(levelname)s] %(message)s")
    ch.setFormatter(formatter)
    logger.addHandler(ch)

    # File handler
    fh = logging.FileHandler("logs/transcriber.log", encoding="utf-8")
    fh.setLevel(level.upper())
    fh.setFormatter(logging.Formatter("%(asctime)s [%(levelname)s] %(message)s"))
    logger.addHandler(fh)

    return logger
