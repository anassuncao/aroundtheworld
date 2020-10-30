function sendMail(contactForm) {
    emailjs.send("gmail","levina", {
        "from_name": contactForm.name.value,
        "from_email": contactForm.email.value,
        "message": contactForm.message.value,
    })
    .then(
        function(response) {
            console.log("SUCCESS", response.status, response.text);
            alert("Email sent successfully!");
            location.reload("contacts.html"); /*To clear the form after the success message */
        },
        function(error) {
            console.log("FAIL", error);
            alert("Failed to send email!" + error);
        }
    );
    return false; 
}