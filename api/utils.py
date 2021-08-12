import os
import subprocess
import uuid
from timeit import default_timer as t
from typing import Tuple


def execute_code(code: str) -> Tuple[bytes, float]:
    """
    Executes the given code in the current shell and returns the output.
    :param code: The code to execute.
    :return: The output of the executed code.
    """
    filename = f"/tmp/{str(uuid.uuid4())}.py"
    with open(filename, "w") as f:
        f.write(code)
    start = t()
    try:
        result = subprocess.check_output(
            f"python3 {filename}",
            shell=True,
            stderr=subprocess.PIPE,
            env=dict(author="Amal Shaji"),
        )
    except subprocess.CalledProcessError as e:
        result = e.stderr
    end = t()
    # except TimeoutError:
    #     result = "Execution time exceeded 3 seconds"
    os.remove(filename)
    return result, end - start
