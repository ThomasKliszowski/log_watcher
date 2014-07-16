# from log_watcher.cli import cli
from log_watcher.parser import LogParser
from log_watcher.tracker import Tracker
import time
import tempfile
import mock


class TestTracker(Tracker):
    def send_data(self):
        pass


def test_basic():
    fp = tempfile.NamedTemporaryFile()
    fp.write('test\n')
    fp.write('test match\n')
    fp.write('test match\n')
    fp.write('test\n')

    file_path = "/tmp/kern.log"
    regexp = r'match'
    period = 1

    parser = LogParser(file_path=file_path, regexp=regexp)
    tracker = TestTracker(name="Test", period=period)

    with mock.patch('tests.test_basic.TestTracker.send_data') as send_data:
        for line in parser.parse():
            tracker.track(1)

        time.sleep(period)
        tracker.track()

        send_data.assert_called_with()

    fp.close()
