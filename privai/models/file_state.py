from enum import Enum


class FileState(str, Enum):
    COMPLETED = "completed"
    DRAFT = "draft"
    FAILED = "failed"
    PROCESSING = "processing"

    def __str__(self) -> str:
        return str(self.value)
