import os

login_url = 'https://myaccount.nytimes.com/auth/login'
register_url = 'https://myaccount.nytimes.com/auth/register'
existing_email = 'test.new.york.times@gmail.com'
password = os.environ.get("NYT_PASS")
already_associated_error = 'These credentials are already associated with an account. Please try again or'
invalid_email_error = 'Please enter a valid email address.'
empty_password_error = 'Please enter a password.'
invalid_password_error = 'Please provide a password that is between 6 and 255 characters in length.'
invalid_existing_creds_error = "The email address and password you entered don't match any NYTimes account. Please try again."
empty_email_error = 'Please enter your username or email address.'
