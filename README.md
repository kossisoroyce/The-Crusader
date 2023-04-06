# The-Crusader
"The Crusader" i is a repository containing a Python script designed to help protect web servers from malware and other types of malicious software.

The script scans web servers, including WordPress installations, for signs of malware and other malicious software. If any threats are detected, the script sends an email notification to the website owner, allowing them to take immediate action and prevent any further damage.

# Here's a general how-to guide to get started with using The Crusader:

# Step 1: Install necessary packages

1. Install Python 3

2. Install the requests package: pip install requests

3. Install the beautifulsoup4 package: "pip install beautifulsoup4"

4. Install the twilio package: "pip install twilio" (if you want to use SMS notifications)

# Set up a Twilio account (if you want to use SMS notifications)

5. Go to https://www.twilio.com/ and sign up for an account.

Follow the instructions to create a new project and obtain a Twilio account SID and auth token.
Purchase a phone number to use for sending SMS notifications.

# Modify the script with your website URL and email/SMS information

6. Open the Crusader.py file in a text editor.[I recommend Sublime Text]

7. Change the url variable to the URL of the WordPress website you want to scan. Also enter the path to the wp-content directory on your server.

8. If you want to receive SMS notifications, change the twilio_account_sid, twilio_auth_token, and twilio_phone_number variables to your Twilio account SID, auth token, and purchased phone number.

9. Change the recipient_email and recipient_phone variables to your email address and/or phone number.

# Run the script

10. Save the modified Crusader.py file and upload to your desired folder on your server.

11. Open a terminal/command prompt and navigate to the directory containing the file.

12. Run the script with the command python3 Crusader.py.[For shared hosting servers, you can just proceed to create a cron job. For tests, set to run with the quickest time range your hosting provider can afford you]

# Automate the script with a cron job

13. Open a terminal/command prompt and enter the command crontab -e.

14. Add a new line to the file with the desired schedule and the command to run the script. For example, to run the script every day at 9:00am, add the line "0 9 * * * python3 /path/to/Crusader.py.

15. Save and close the crontab file.

# Check for email/SMS notifications

16. If malware is found on the website, an email and/or SMS notification will be sent to the specified email address and/or phone number.

17. Check your email and/or phone for any notifications.

Note: This guide assumes a basic understanding of Python and command line usage. If you encounter any issues, consult the official documentation for the packages used in the script or seek assistance from a qualified developer.


