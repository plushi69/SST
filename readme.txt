Hello teacher, I am Puscasu Vlad and here is the automatic tests that i implemented in order to test
https://www.demoblaze.com/ website from the link that you gave to us
https://automationpanda.com/2021/12/29/want-to-practice-test-automation-try-these-demo-sites/

I want to mention that the website did not have that many features implemented, and I tried to come up
with different scenarios and test as many things as possible and every single button from the website

Requirments for the tests to run:
Use command: pip install <package> (in order to install all the libraries i have included)
If it is not working for some libraries (pytest) try to run this command: python -m pytest
it will tell you if you have it installed, and if yes, you need to change the Environment variables
in order to make it work, this is the guide I used: https://www.codewithharry.com/blogpost/python-is-not-recognized-error/

How to run the tests:
run this command in a terminal: python test_name.py
subsitute test_name with the actual name for the test
example: python test_navigate_through_website.py

Download the WebDriver executable for the Chrome browser, use ChromeDriver for Chrome
Ensure the WebDriver executable is in your system's PATH or provide its path in the run test command.
Also make sure not to have multiple Chrome engines run at the same time
(like work account and personal account in 2 different chrome engines)

After running a test, in the output console, the result of test will be shown.
If it doesn't show the result, try to delete the insides of the cache files,
I deleted them before submitting, but just in case.

Feel free to contact me for any help needed or questions: vlad.puscasu02@e-uvt.ro