Assumptions:
============
1. Script has been tested only on Ubuntu 15.10 and Firefox 45.0.
2. Python 2.7 is already installed.
3. Test Data has been hardcoded in the scripts to avoid development delays.
   Otherwise they can be moved to CSV or a database and can be read from there.
4. Python virtual environment is skipped for this POC purpose.

Pre-requisites:
===============
1. Install Firefox  - sudo apt-get install firefox
2. sudo apt-get install python-pip
3. Python dependencies - sudo pip install -r requirements.txt.
4. Used Pycharm Community Edition 5.0.4 edition as IDE.

Install and Run:
===============
1. Untar the folder.
   tar -xzvf surveyMonkeyPOC.tar.gz.
   Assuming Folder name - surveyMonkeyPOC
2. cd surveyMonkeyPOC
3. Run this command to execute createSurvey cases on FireFox
   py.test --base-url https://www.surveymonkey.com --driver Firefox --html results/report.html functional/test_createsurvey.py
4. We can also execute other test cases or all, depending upon the passed argument to the above command.
5. Also appropriately report path and name of the file can be changed as desired.


To Run against Chrome Browser:
==============================
To use Chrome, you will need to download ChromeDriver. and specify Chrome for the --driver command line option.
If the driver executable is not available on your path, you can use the --driver-path option to indicate where
it can be found
py.test --base-url https://www.surveymonkey.com --driver Chrome --driver-path /path/to/chromedriver --html results/chromeReport.html functional/test_*

To Run against Firefox Browser:
===============================
py.test --base-url https://www.surveymonkey.com --driver Firefox --html results/firefoxReport.html functional/test_*

Approach:
========
Page Object Model approach has been followed for this POC along with pytest with pytest-selenium plugin.
Evey page has been implemented in a class all the elements and actions are defined in that class for that page.

All test cases are annotated by fixtures , that defined whether the test cases can be apart of Smoke testing/Sanity testing
/Non Destructive testing. By default all test cases are considered as destructive that means they will not run on
Sensitive URLs or production environments.

All Screenshot and logs can be accessed by html report itself.

All Page Objects can be found at  ./surveyMonkeyPOC/pages/
All Test cases can be found at  ./surveyMonkeyPOC/functional/
All Reports can be found and generated at  ./surveyMonkey/reports

TODOS:
======
There are many many areas of improvement/enhancement, this is just a POC for demonstration purpose only.
0. There are very minimal or no assertions were used, to cover more of automation functionality.
   Assertions can be easily added
1. Data Separation from automation scripts.
2. Proper commenting of the code for future understanding and debugging. DOC strings can be added.
3. Copyright information/edit history on the coding files are missing, can be added.
4. PEP8 standards can be followed in a more strict way.
5. Delays(i.e time.sleep()) are were added that should be removed.
6. Explicit exception handling can be done. This has been automatically takencare by pytest as of now.
 etc etc .. :)

NOTE:
=====
More stress has been put on automating the Website inspite of putting assertions. Assertions can be easily placed
once functional actions on the webpage are automated.

Issues:
=======
1. I have found an issue while automating the website, please have a look ./surveyMonkey/reports/errorReport*.html.
   Due to this sometimes automation script is failing as it fail to loads the question to the UI.
   Same can be seen as "OOPS" message in the screenshot attached.