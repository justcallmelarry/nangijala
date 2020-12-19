import json
from typing import Any, Dict, KeysView, Optional


class Data:
    """
    Data class for reading different data dicts, and make them easier to work with.
    """

    def __init__(self, data: Dict) -> None:
        self.__data = data

    def __str__(self) -> str:
        return str(self._data)

    def __repr__(self) -> str:
        return str(self._data)

    def __getitem__(self, key: str) -> Any:
        value = self._data.get(key, {})
        if isinstance(value, dict):
            return Data(value)

        if isinstance(value, list):
            if all([isinstance(o, dict) for o in value]):
                return [Data(o) for o in value]

        return value

    def __getattr__(self, key: str) -> Any:
        value = self._data.get(key, {})
        if isinstance(value, dict):
            return Data(value)

        if isinstance(value, list):
            if all([isinstance(o, dict) for o in value]):
                return [Data(o) for o in value]

        return value

    def __bool__(self) -> bool:
        if self._data:
            return True
        else:
            return False

    def __len__(self) -> int:
        return len(self._data)

    def __iter__(self) -> Any:
        return self._data.__iter__()

    def __contains__(self, item: Any) -> Any:
        return self._data.__contains__(item)

    def __eq__(self, other: Any) -> bool:
        if isinstance(other, Data):
            return bool(self._data == other._data)

        elif isinstance(other, dict):
            return bool(self._data == other)
        else:
            return False

    def __ne__(self, other: Any) -> bool:
        return not self == other

    def keys(self) -> KeysView:
        return self._data.keys()

    def get(self, key: str, default: Optional[Any] = None) -> Any:
        return self._data.get(key, default)

    @property
    def _data(self) -> Dict:
        return self.__data

    def json(self) -> str:
        return json.dumps(self.__data)
