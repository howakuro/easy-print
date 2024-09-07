import sys
import io


def mock_stdout(testcase_inst):
    stdout = sys.stdout

    def cleanup():
        sys.stdout = stdout

    testcase_inst.addCleanup(cleanup)
    sys.stdout = io.StringIO()
