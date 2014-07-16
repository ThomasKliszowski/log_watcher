# Log Watcher

Log Watcher is a package which allows a user to watch a log file and track some data.

[![Build Status](https://travis-ci.org/ThomasKliszowski/log_watcher.svg?branch=master)](https://travis-ci.org/ThomasKliszowski/log_watcher)

## Installation

Log Watcher is available on Pypi:
```
pip install log_watcher
```

However, you can pull from the Github repo:
```
git clone https://github.com/ThomasKliszowski/log_watcher.git
cd log_watcher
python setup.py develop
```

## Settings

Don't forget to add a settings file (.py) before using the script.
You can put your settings file where you want.

### Example

*/opt/log_watcher/settings.py*
```
AWS_ACCESS_KEY_ID = 'MY_ACCESS_KEY'
AWS_SECRET_ACCESS_KEY = 'MY_SECRET_KEY'
AWS_REGION = "MY_REGION"

CLOUDWATCH_NOTIFICATION_ARNS = [
    'my-arn'
]
```

Replace all of the values by yours.
If you want to use Sentry to track your errors, just add this setting in the same file:
```
SENTRY_DSN = 'MY-DSN'
```
Don't forget to replace the value.

## Usage

### Custom settings
You can use your settings file like this:
```
SETTINGS_PATH=/opt/log_watcher/settings.py log_watcher
```

### Help
```
$ log_watcher --help
Usage: log_watcher [OPTIONS]

Options:
  --file-path TEXT  File path to watch.
  --regexp TEXT     Regular expression to match.
  --period INTEGER  Period between each tracker sends.
  --help            Show this message and exit.
```

## Trackers

The list of all available trackers:
 - AWS Cloudwatch (http://aws.amazon.com/cloudwatch/)
