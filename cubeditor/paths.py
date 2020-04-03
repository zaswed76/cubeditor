import os
from pathlib import Path

ROOT = Path(os.path.dirname(__file__))
MAIN_CONFIG = ROOT / "settings/main_config.yaml"
CSS_FOLDER = ROOT / "css"

if __name__ == '__main__':
    print(MAIN_CONFIG)