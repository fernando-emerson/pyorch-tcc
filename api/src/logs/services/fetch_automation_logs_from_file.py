import os
from typing import List
from src.logs.models import LogFileEntry


class FetchAutomationLogsFromFile:

    def execute(self, automation_id: int) -> List[LogFileEntry]:
        path = f"logs/{automation_id}"
        if not os.path.exists(path):
            raise FileNotFoundError("Diretório de logs não existe")
        output = []
        for file in os.listdir(path):
            with open(os.path.join(path, file), "r") as f:
                rows = f.readlines()
                output.append(
                    [
                        LogFileEntry(
                            taskid=file.split(".")[0],
                            automation_id=int(automation_id),
                            message=row,
                        )
                        for row in rows
                    ]
                )
            return sum(output, [])[::-1]
