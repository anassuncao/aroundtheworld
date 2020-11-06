## **AROUND THE WORLD**

This project is a website/app with the intent to act as a "free teaser" for a Travel Consultant. The website contains free tips and information about several cities across the world and to make it more interactive and interesting for the user, it allows to add information regarding cities that he/she has visited and editing information that's already in the website. There's also the option to delete cities.

The goal is that people who have fun navigating and contributing to this website would want to hire the Travel Consultant services for a more tailor made trip or even just to gather more information before making a decision about the next trip.


### **UX**

I believe the website is intuitive and easy to navigate. It has a few lines with instructions and information on how to use it to make the user's life easier. As mentioned before, it's possible to add, edit and delete a city. It also has a search page and a contacts page where the user can directly send an email to the travel consultant.


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

The *Add a city* page displays a form with several input fields where the user can add information that will, after submission of the form, display in it's own card. It's also possible to add a link to an image. The Edit page is the same as the Add a city page, with the difference that, when it displays, the input fields are pre-populated with the information that was already there.

The *search* page allows the user to search if a certain city or country is already on the website. This feature can be used to confirm that the city that the user wants to add doesn't exist yet or it can be used to search for information regarding a specific city instead of going through all the ones available on the homepage. The search feature searches for matches both in the city_name and the country_name field. This allows the user to search not only by city but also by country.
The search results are shown as a list of links that, when clicked, take the user to the correspondent page. In case there's no results matching the search, it returns a message saying that there's no results found and asking the user if he/she wants to add that city, It also provides the link to add a city.

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


### **Deployment**

I've published my website using GitHub pages. I followed these steps:

Inside my repository I clicked settings;
Under the GitHub Pages, in the Source drop-down menu I've selected "master branch"
The publishing link https://anassuncao.github.io/milestone1-anassuncao/index.html was generated imediatly.
For cloning my repository, the following steps must be taken:

On GitHub navigate to the main page of the repository: https://github.com/anassuncao/milestone1-anassuncao
Under the repository name click Clone or download
To clone the repository using HTTPS, under Clone with HTTPS, click the "notepad with an arrow" icon. To clone the repository using an SSH key, including a certificate issued by your organization's SSH certificate authority, click Use SSH, then click "notepad with an arrow" icon.
Open Terminal
Change the current working directory to the location where you want the cloned directory to be made
Type git clone and paste the URL you've copied in step 2.
Press Enter to create your local clone.


**Credits**

All the images on the website were taken by my friend and Travel Consultant Levina Ferreira during her trips. Except:

- Tilburg image was taken from this website: https://www.studiekeuze123.nl/steden/tilburg
- Lisbon image was taken from here: https://www.theguardian.com/travel/2017/jul/08/lisbon-portugal-stay-hotels-food-museums-city-guide

The logo was also made by a designer friend, Sérgio Filipe.

falar no codigo que foi retirado do mini projecto


**Improvements**








https://www.photowall.nl/san-francisco-city-skyline-rainbow-poster ---> foto do add a city




melhorias: os users poderem uploadar uma imagem em vez de colocarem um link