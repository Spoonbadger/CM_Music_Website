CS50 web - Capstone: cm_music_website
Craig Morley, September 2024


Introduction:
For the capstone project to CS50 web I have created a distinct website for my music which has numerous elements of complexity. Thank you for taking the time
to explore the web application.


Running the application:
To run the application please pull the files from the repository and use 'python3 manage.py runserver'. The website will also be hosted shortly
on www.craigmorley.com


Files:
I will start by describing the files in the app 'cm_music' and will go on to explore files added to the project folder and also any ammendments made to existing files
within the project

In views.py I created a view for each webpage of the app. 'index', 'bio', 'invest', and 'links'. Each of these are reasonably straight-forward render requests 
of each html page.  The 'contact_page' and 'music' page are more complex. For 'contact_page' I am beggining with a check to see if the form
on the contact page has been submitted (with a method of 'POST'). If the form has not been submitted yet (a request method of 'GET'), the contact-form page will load.
If the form has been sent I gather the information from the form with contactForm form class which I have imported from .forms. contactForm handles validation
checks and I save the infomation as the variable 'post'. With this information I can then use the built-in djangofunction .is_valid() to make sure the data is valid.
I can then use .cleaned_data to gather the data in the correct format and set the correct variables I need in order to save the new ContactMessage object and
have the data ready to use to send in a email using 'send_mail'.

For send_mail to work I had to add email host and and smtp information in order to have the form, once submitted, emailed to my own personal email!
In order not to publish my Gmail login and password on github I had to get an 'app password' from my Gmail account and use that, then move the username 
and password to a seperate .env file and link to this file from settings.py using 'from decouple import config'. I added the .env file to a new .gitignore
file so as to not publish my Gmail username and 'app password'.

There are checks on the client-side by using Django forms automated verification such as .is_valid() and .cleaned-data(). The backend model also checks
that the forms are not submitted blank on the server-side. If the form is not valid, the the page will reload with all the current information written on the form replaced, however, the django client-side checks shouldn't allow a form to be submitted if the fields are blank.

In the 'music' function in views.py, I'm gathering all the path names to videos that I have stored in the database. (The videos themselves are stored in static).
I am using the list() function to have the information stored as a python string. I have then imported random in order to put the videos in a random order
so upon each refresh or visit to the 'music.html' page, the videos will be displayed in a random order.

In urls.py I have created calls to action via a url pathname. These paths can be called on from the website, and calls upon the relevent function
in views.py.

In models.py I have created two models (actually three with User but that's for possible future development). The first is ContactMessage in which everytime a 
user leaves a message on the contact.html page, the data is stored in the database. I have include the fields, name, email, message and also included a
timestamp as an easy and helpful addition. I have created a string (__str__) method within the class so the model is easily readable in /admin. I have also
included an is valid message check which I can utilize to add further checks in tests.py.

I have also created a class of Videos which stores the videos name and the path name too, allowing me to easily add or remove videos using python shell
or by using django admin, and this data can easily be accessed from views.py.

In forms.py I created the form layout and my using some built-in django features I could add further checks to the form data such as Email Validator, 
serving client-side validation to the user, where if the user doesn't type in an email in a valid email format, the website will inform the user.

In admin.py I added the Videos and ContactMessage models in order to access these database items in Django admin.

in tests.py I ran a series of checks for the two models I created using TestCase. Although adding a number of relevant checks I see I can futher develop these 
checks by adding more checks to the view functions in views.py also.

In my static folder I have a CSS file where I have designed various aesthetic features using both flexbox and grid CSS. I have also incorporated @key_frames 
to add animation elements to the design of the website.

There are images, music and videos also stored here. These are large files and so when uploading to Github I had to install a large file tracker in order
to add these large items to a gitattributes file. I created some a Bio.js file in order add a dynamic music playing element to the bio.html page. On this page
music can be toggled off and on at the click of a text-only button.

I have also written Javascript in Video.js in order for the user to be able to play the short music videos on the music.html page by simply hovering over a
video element.

In my templates folder I have created a html page for each page of the website. In music.html I am using Jinja sytax in order to render data from views.py. Using for loops to create new rows for videos and using flex to have the videos dynamically shift depending upon the screen side and changing screen sizes.

Music is also rendered on this page by using the iframe code provided by Spotify.

I have a navbar featured on all the webpages as well as a footer and also links to social media accounts.

In the footer I also have a link which takes a user to a pay where they can 'invest' in the musician by donating through 'stripe' payment system.

I have also included .github folder including a YAML file which serves to run tests.py when uploading to github and the test results are easily checkable on github.


I have created a Dockerfile in order for the app to be able to run on a virtual environment. For this to work I also needed to include a requirements.txt file, which I have included.

I also kept track of what I needed to build in the app by using a roadmap.md file.


Distinctiveness and Complexity:
There are numerous distinctive and complex features of this webapp as described above. 

For example, creating a .env file and getting an app password in order to have users be able to contact my email direcly when submitting a contact form on the website. For this had to learn about the format on send_email() and also install decouple in order to link to the .env file from settings.py.

I have created a Dockerfile in order for the web app to be run in a virtual environment. 

I have utilized testing in multiple areas, from forms.py to checks in models.py to running tests in test.py and with a gihub automatic check using a yaml file. I have also used functions such as .is_valid() and .cleaned_data() to add further thorough checks.

I have also embedded music players and a donation form from other websites.

I have added CSS for all webpages and included a number of animation styles for multiple elements and some complex design elements such as a variety of ways of playing audio and video on the website.



Thank you very much for reviewing my work.