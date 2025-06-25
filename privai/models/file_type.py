from enum import Enum


class FileType(str, Enum):
    CHUNKS = "chunks"
    PARSED_RESULT = "parsed_result"
    RAW_FILE = "raw_file"

    def __str__(self) -> str:
        return str(self.value)
