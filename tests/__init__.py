import os
import mock

os.environ['SETTINGS_PATH'] = "/dev/null"


@mock.patch('log_watcher.tracker.CloudwatchTracker.send_data')
def send_data():
    print "ok"