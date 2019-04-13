# DeleteTweets

This is a script to delete all tweets from your timeline. There are many services that let's you delete around 2500 tweeets a day but this will delete all your tweets.

Apply for a Twitter Developer account
  1. Create a Twitter Developer account:
  2. User profile: Use your current Twitter @username.
  3. Account details: Select I am requesting access for my own personal use, set your 'Account name' to your @username, and select your       'Primary country of operation.
  4. Use case details: select 'Other', and explain in at least 300 words that you want to create an app to semi-automatically clean up          your own tweets.
  5. Terms of service: Read and accept the terms.
  6. Email verification: Confirm your email address.
  7. Now wait for your Twitter Developer account to be reviewed and approved.
  
Create a Twitter app
  1. Create a new Twitter app (not available as long as your Twitter Developer account is pending review).
  2. Set 'Access permissions' of your app to Read and write.
  
Configure your environment
  1. Open your Twitter Developer's apps.
  2. Click the 'Details' button next to your newly created app.
  3. Click the 'Keys and tokens' tab, and find your keys, secret keys and access tokens. Paste it in to the config.json file in the repo
  
Get your tweet archive
  1. Open your Twitter account page.
  2. Scroll to the bottom of the page, click 'Request your archive' (not 'Your Twitter data' in the left sidebar!), and wait for the email      to arrive.
  3. Follow the link in the email to download your Tweet archive.
  4. Unpack the archive, and move tweets.csv to the same directory as this script.
  
Getting started

  First, install the required dependencies.

  pip install -r requirements.txt
  
  Then, delete all tweets from your timeline by running the following:

  python deletetweets.py
