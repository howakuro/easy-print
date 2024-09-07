import sys
import io


def stub_stdin(testcase_inst, inputs):
    stdin = sys.stdin

    def cleanup():
        sys.stdin = stdin

    testcase_inst.addCleanup(cleanup)
    sys.stdin = io.StringIO(inputs)


def stub_stdouts(testcase_inst):
    stdout = sys.stdout

    def cleanup():
        sys.stdout = stdout

    testcase_inst.addCleanup(cleanup)
    sys.stdout = io.StringIO()
