import os
from typing import List

from src.logs.models import LogFileEntry


class FetchLogsFromFile:
    """
    Module for fetching logs from files in a specific directory.

    This class provides a method to execute the reading of log files
    stored in subdirectories within the 'logs' directory. Each log file
    is processed to extract log entries, which are returned as a list
    of LogFileEntry objects.
    """

    def execute(self) -> List[LogFileEntry]:
        automation_logs = os.listdir("logs")
        output = []
        for automation_id in automation_logs:
            log_files = os.listdir(f"logs/{automation_id}")
            for file in log_files:
                with open(f"logs/{automation_id}/{file}", "r") as f:
                    rows = f.readlines()
                    output.append(
                        [
                            LogFileEntry(
                                taskid=file.split(".")[0],
                                automation_id=int(automation_id),
                                message=row,
                                nivel=self.extract_status(row),
                            )
                            for row in rows
                        ]
                    )

        return sum(output, [])[::-1]

    def extract_status(self, message):
        import re

        pattern = r"- (INFO|WARNING|DEBUG|ERROR) -"
        match = re.search(pattern, message)
        if match:
            return match.group(1)
        else:
            return "Unknown"
