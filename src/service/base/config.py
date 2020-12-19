import os
import toml
from typing import cast

from .data import Data

toml_string: str = os.environ["NANGIJALA_CONFIG"]
settings = Data(cast(dict, toml.loads(toml_string)))
