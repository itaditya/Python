## Requirements 

 1. Python 2.7
 2. Selenium for python
 2. geckodriver.exe (set it in PATH too.) -- For Firefox
 3. chromedriver.exe (set it in PATH too.) -- For Chrome

##How To Use ?
 1. Rename the credentials_demo.json file to credentials.json
 2. Change the email and password fields in the credentials.json file with your fb account details.
 3. Open terminal and cd into the folder containing this script.
 4. Run `python update_status.py`
 5. This will fire the browser , and log you in to Fb.
 6. You will be prompted for input in console.
 7. Type the status and press enter .
 8. Your status will be updated on FB and then the browser will quit.
 9. Done !!

##Configuration

 Specify the browser to use (Default - chrome) :
        ```
             python update_status.py -d firefox
        ```
         or 
        ```
             python update_status.py --driver chrome
        ```
   