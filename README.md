## ! Important Notice !

This Plugin is unmaintained and significantly outdated.

Refer to the http://opal.openhealthcare.org.uk documentation for current information about Opal


# Opal Walk-in

Walk-in plugin for OPAL

## Dependencies

Requires the opal-dischargesummaries and the opal-observations plugins

## Installation

Add to your implementation's INSTALLED_APPLICATIONS.

Run

    $python manage.py migrate

Add walk-in to your schemas as required.

## Running the tests

Tests use the [OPAL test runner](http://opal.openhealthcare.org.uk/docs/guides/command_line_tool/#test-what) and require the requirements.txt to be available

   $ opal test
