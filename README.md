# [Periodic checker](https://github.com/imjeremyhi/periodic-checker) &middot; [![GitHub license](https://img.shields.io/badge/license-MIT-blue.svg)](https://github.com/imjeremyhi/periodic-checker/blob/master/LICENSE)

## Motivation
I developed this simple tool out of laziness. I forget to check things regularly and miss out on updates I'm interested in.

## Description
Periodically checks content on any specified website. Extracts the relevant content and notifies the user via email **ONLY** when the data has changed. Feel free to customise the scripts to suit your needs.

## Set up
1. Install required dependencies globally. While a virtualenv could be used, this creates complexity when running a periodic job.
```bash
pip install bs4
```
2. Determine the URL of the website you are interested in
3. Determine the html selector whose contents you are interested in. This can be done by:
    1. opening inspect element in chrome
    2. selecting the specific element to inspect
    3. right clicking the relevant html component in the source code
    4. hovering copy
    5. clicking copy selector
4. Create the file `data.json` if it does not already exist. Store the URL and selector as a JSON key value pair in `data.json`. Example of the expected file format:
```json
{
    "url-1": "selector-1",
    "url-2": "selector-2"
}
```
5. If there are multiple websites or html elements you're interested in, repeat steps 1-3 for each case
6. Create the file `credentials.json`. Store your email username and password inside. Example of the expected file format:
```json
{
    "user-email-address": "user-email-password"
}
```
7. Add the script as a regular cron job / job executed at a specified time.
On OSX this can be done by running `crontab -e` where the format is:
`min hour day_of_month month day_of_week command`. You can verify the crontab has been setup by running `crontab -l`. Example of the expected crontab format:
```bash
0 12 * * * python3 <absolute-path-to-periodic_checker.py>
```