# Setup

virtualenv venv ( In case you dont have virtualenv, pip3 install virtualenv )
source venv/bin/activate
pip3 install -r requirements.txt
python3 crawler.py <keyword> <page_number>

# Miscellaneous

1) If you want to have spaces inside your keyword, it is not supported. Append "+" and then search. 
   For e.g. If we want keyword to be iphone samsung, put keyword as iphone+samsung
