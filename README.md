## **AROUND THE WORLD**

This project is a website/app with the intent to act as a "free teaser" for a Travel Consultant. The website contains free tips and information about several cities across the world and to make it more interactive and interesting for the user, it allows to add information regarding cities that he/she has visited and editing information that's already in the website. There's also the option to delete cities.

The goal is that people who have fun navigating and contributing to this website would want to hire the Travel Consultant services for a more tailor made trip or even just to gather more information before making a decision about the next trip.


### **UX**

I believe the website is intuitive and easy to navigate. It has a few lines with instructions and information on how to use it to make the user's life easier. As mentioned before, it's possible to add, edit and delete a city. It also has a search page and a contacts page where the user can directly send an email to the travel consultant. For more details on how it works, please read on to the next topic "Features".


**Features**

When I first started this project I had an idea of how to organize it and it was based on that idea that I've created the first mockups. They can be found [here](https://www.dropbox.com/sh/ukmbb1fsrfvrf1g/AADSyrqA_N_bsEV41YFGrej6a?dl=0).

As I was building the project I've decided to make a few changes. The changes were motivated by several reasons: improving the user experience, making the website more user friendly in general and making it more simple and organized. The final result is, therefore, a bit different of the first idea to which I made the mockup.

When entering the website we have a simple page with a few lines of text provinding information on how the website works. After that we can see the cities displayed in a card format with an image of said city and a link to know more. By clicking the link the user is redirected to another page where he/she will find information regarding the city and a photo. It's also here that we can find the Edit and the Delete buttons. In the bottom of the page there's a Back button that will take the user back to the homepage.

Also in the *homepage* there's a navbar with several links: 
- Logo (when clicked, redirects the user to the home page);
- Home (that will take us to the home page); 
- Add a city (that redirects to the page where the user can add a city);
- Search (redirects the user to the search page);
- Get in touch (redirects the user to a page with a form to send an email to the travel consultant).
The navbar appears in all pages, making the navigation easily reachable no matter where the user is in the website.

The *Add a city* page displays a form with several input fields where the user can add information that will, after submission of the form, display in it's own card. It's also possible to add a link to an image. The Edit page is the same as the Add a city page, with the difference that, when it displays, the input fields are pre-populated with the information that was already there. At the bottom of this page there's a map displaying markers that corresponde to the cities that are in the cards.

The *search* page allows the user to search if a certain city or country is already on the website. This feature can be used to confirm that the city that the user wants to add doesn't exist yet or it can be used to search for information regarding a specific city instead of going through all the ones available on the homepage. The search feature searches for matches both in the city_name and the country_name field. This allows the user to search not only by city but also by country.
The search results are shown as a list of links that, when clicked, take the user to the correspondent page. In case there's no results matching the search, the user can follow the link on the message saying that if there's no results, they can add that city.

The *Get in touch* page displays a contact form that the user can fill with the name, email and message and send it directly to the travel consultant.

All the pages also display a footer with the links to the Instagram and Facebook accounts of the Travel Consultant.


### **Technologies used**


- I used Materialize documentation for the grid, responsiveness, navbar, cards, icons, between others: https://materializecss.com/
- I've used the Google Fonts Montserrat: https://fonts.google.com/
- jQuery library: https://code.jquery.com/
- Google Maps Javascript API and Geocoding API: https://developers.google.com/maps/documentation/javascript/tutorial
- EmailJS: https://www.emailjs.com/
- Javascript
- HTML
- CSS
- Flask (web framework)
- Python
- Jinja (templating language)
- MongoDB: https://account.mongodb.com/
- Heroku for deployment: https://dashboard.heroku.com/


### **Testing**

I used the following for validating the html, css and javascript code.

CSS validation in https://jigsaw.w3.org/css-validator/#validate_by_input came out with no errors.

HTML validation in https://validator.w3.org/nu/#textarea came out with a few errors in the aria controls of the resume page but because it doesn't hurt the website functioning and I have a deadline to finish this, I've decided to ignore it for now and investigate further afterwards and, if necessary, do any kind of correction.

Javascript validation in https://esprima.org/demo/validate.html came out with no errors.

Python syntax validation in https://extendsclass.com/python-tester.html also came back with no errors.

Also used the devtools of Chrome to test the responsiveness in all the available models of cellphones and tablets.

I've tested the website manually. Went through all the pages and tested all the features, clicks and hovers. This manual testing was also made by someone else other than me to prevent bias. During the testing a few minor issues were found and corrected. All worked as expected in the end.

For testing the email, I've filled the form and sent the email. After that I've checked my inbox and the message I've sent through the form was there, proving that it was working. I've repeated this procedure several times from several laptops (Apple MacBook Air 2014, Lenovo from 2020, HP ProBook 430G4) and phones (Apple iphone X, iphone 11 and iphone 11Pro) to make sure it works in all of them. Also using different browsers: Safari, Chrome and Firefox.

The mentioned above laptops, phones and browsers were also used to manually test the website completely.

The manual testing, with the mentioned computers and phones was made by navigating to all available pages, using all the available links and making sure they've worked and led to where it was supposed to. Several cities were added, edited and deleted. The search feature was used making queries of cities that existed already in the website and other that didn't to make sure it was working properly. Countries that have several cities in the website were also used for queries to make sure that all the available results were returned. It all work properly.


### **Deployment**

I've published my website/app using Heroku. I followed these steps:

1. After making sure I have a requirements.txt file and a Procfile I have followed the documentation available on Heroku.
2. I've added, commited and pushed my files to heroku master:
    $ git add .
    $ git commit -am "make it better"
    $ git push heroku master)
3. Entering the Settings page, on the Confir Vars section I've set the IP (0.0.0.0) and the PORT (5000) values. Also the MONGO_URI link and credentials.
4. I've restarted all dynos
5. Run app - all was working properly.
6. Made another add and commit to add these last updates on the README-md file regarding the deployment procedure.

Deploy your application
Commit your code to the repository and deploy it to Heroku using Git.

$ git add .
$ git commit -am "make it better"
$ git push heroku master


**Credits**

All the images on the website were taken by my friend and Travel Consultant Levina Ferreira during her trips (Instagram and ). Except:

- Tilburg image was taken from this website: https://www.studiekeuze123.nl/steden/tilburg
- Lisbon image was taken from here: https://www.theguardian.com/travel/2017/jul/08/lisbon-portugal-stay-hotels-food-museums-city-guide

The logo was also made by a designer friend, [Sérgio Filipe](https://www.linkedin.com/in/sergiofilipe/).

I've used some chunks of code from the course mini project but I have changed and costumized so many things throughout the project that I believe that none stayed the same.


**Improvements**

There are a few improvements that I would like to implement in the near future. They were not made now due to lack of time to do the proper research and implementation but I consider them very important to add to this project before being released to the "general public" as a marketing tool for the services of Levina Ferreira. The main improvements are:

1. Add the account creation feature. The possibility of editing and especialy deleting someone else's cities is not very useful, I think and it can become dangerous to the proper funcitoning of the website. Being able to create an account would allow to make the edit and delete features available only for the cities that each users had add.
2. Make google maps display a marker for each city that it's added by a user.
3. Add code to validade if a city already exists in the website whenever someonte tries to add it. If it's already there, allow the user to edit it, only by addung information, not deleting it, even if it wasn't added by said user before.
4. Users being able to upload an image insted of submiting a link.

There's also one issue that can be considered an improvement but, for me, it's more of a big fixing. The images inside each city page do not display well in smaller devices. I have tried a few options to solve this but I could not find one that would suit all images that are currently in the website. For lack of time I've decided to leave it as it is for now but it's very important that this issue can be addressed and solved properly.

Overall I believe this website is a good start to help promote Levina's Ferreira travel consultant services and it was a very good exercise for me to be able to practice and lear so much more during this course. I also believe that by implementing the mentioned improvements, this project can be released publicly and will fufill its purpose.