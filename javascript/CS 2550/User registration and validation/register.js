/*
Create a web page consisting of HTML (register.html), CSS (style.css), and JavaScript (register.js) files that implements a user registration form with form validation.

Form validation: Complete checkForm() to verify that the user provided information is valid.

If there are form validation errors,
   The formErrors <div> should be shown by setting display to block
   Each of the associated error messages should be displayed in the formErrors <div> using an unordered list with red text. The error message must be displayed in the order the validation is performed, following the order specified below.
   Each <input> element with the invalid input should be styled with a 2 pixel, red, solid border.
      Otherwise, the default border should be used (1 pixel, solid, with color #aaa)

If there are no form validation errors,
   The formErrors <div> should not be shown (i.e., the display style should be none)
   All test, email, and password <input> elements should use the default border of 1 pixel, solid, color #aaa

Perform the following form validations in the order provided and display all error messages that apply
   Ensure a full name with a length greater than or equal to 1 was provided
      Otherwise, display "Missing full name."
   Ensure that an email address was provided and that the email address matches the regular expression: /^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,5}$/
      Otherwise, display "Invalid or missing email address."
   Ensure the password has 10 to 20 characters
      Otherwise, display "Password must be between 10 and 20 characters."
   Ensure the password contains at least one lowercase character (use a regular expression)
      Otherwise, display "Password must contain at least one lowercase character."
   Ensure the password contains at least one uppercase character (use a regular expression)
      Otherwise, display "Password must contain at least one uppercase character."
   Ensure the password contains at least one digit (use a regular expression)
      Otherwise, display "Password must contain at least one digit."
   Ensure the password and confirmation password match
      Otherwise, display "Password and confirmation password don't match."

*/

const validateName = function(){
   // Validate the name
   const fullName = document.getElementById("fullName")
   const errorFullName = document.getElementById("errorFullName")
   if (fullName.value.length <= 0){
      fullName.classList.remove("defaultBorder")
      fullName.classList.add("errorBorder")
      errorFullName.className = "showLi"
      return true
   }
   else{
      fullName.classList.remove("errorBorder")
      fullName.classList.add("defaultBorder")
      errorFullName.className = "hideMe"
      return false
   }
}

const validateEmail = function(){
   // Validate the email
   const email = document.getElementById("email")
   const errorEmail = document.getElementById("errorEmail")
   const emailReg = /^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,5}$/
   if ((email.value.length <= 0) || !emailReg.test(email.value)){
      email.classList.remove("defaultBorder")
      email.classList.add("errorBorder")
      errorEmail.className = "showLi"
      return true
   }
   else{
      email.classList.remove("errorBorder")
      email.classList.add("defaultBorder")
      errorEmail.className = "hideMe"
      return false
   }
}

const validatePassword = function(){
   // Grab the two password inputs
   const password = document.getElementById("password")
   const enteredPassword = password.value
   let passwordErrorFlag = false
   let passwordConfirmFlag = false
   // Grab the various password errors
   const errorPassLength = document.getElementById("errorPassLength")
   const errorPassLower = document.getElementById("errorPassLower")
   const errorPassUpper = document.getElementById("errorPassUpper")
   const errorPassDigit = document.getElementById("errorPassDigit")
   const errorPassConfirm = document.getElementById("errorPassConfirm")
   // Disable all the password errors until needed
   const passwordErrors = [errorPassLength, errorPassLower, errorPassUpper, errorPassDigit]
   for (let err of passwordErrors){
      err.className = "hideMe"
   }
   // Check the password conditions
   // Check password length
   if ((enteredPassword.length < 10) || (enteredPassword.length > 20)){
      errorPassLength.className = "showLi"
      passwordErrorFlag = true
   }
   // Check for lowercase
   if (!/[a-z]/.test(enteredPassword)){
      errorPassLower.className = "showLi"
      passwordErrorFlag = true
   }
   // Check for uppercase 
   if (!/[A-Z]/.test(enteredPassword)){
      errorPassUpper.className = "showLi"
      passwordErrorFlag = true
   }
   // Check for a digit
   if (!/\d/.test(enteredPassword)){
      errorPassDigit.className = "showLi"
      passwordErrorFlag = true
   }

   // There was some problem with the password, so change the border of the password input
   if (passwordErrorFlag){
      password.classList.remove("defaultBorder")
      password.classList.add("errorBorder")
   }
   else{
      password.classList.remove("errorBorder")
      password.classList.add("defaultBorder")
   }
   
   // Check the confirmed password matches (even if the password is bad)
   const passwordConfirm = document.getElementById("passwordConfirm")
   if (passwordConfirm.value !== enteredPassword){
      passwordConfirm.classList.remove("defaultBorder")
      passwordConfirm.classList.add("errorBorder")
      errorPassConfirm.className = "showLi"
      passwordConfirmFlag = true
   }
   else {
      passwordConfirm.classList.remove("errorBorder")
      passwordConfirm.classList.add("defaultBorder")
      errorPassConfirm.className = "hideMe"
   }
   // Check to see if there was a problem with either password input
   if (passwordErrorFlag || passwordErrorFlag){
      return true
   }
   else {
      return false
   }
}

const checkForm = function() {
   // Check each of the form elements
   // true = one or more errors
   const formErrors = document.getElementById("formErrors")
   formErrors.className = "hideMe"
   // Go through each form, make sure ALL proper errors are in the list
   const badName = validateName()
   const badEmail = validateEmail()
   const badPass = validatePassword()
   // Display the errors, if any occured
   if (badName || badEmail || badPass){
      formErrors.className = "showMe"
   }
}

/*
Some variales for user testing

Good name = Christopher
Bad Email = qwersdf
good email = christopherman2cool@gmail.com
bad pass = dferh
too short = 5Hft
no caps = fdfk645kgfru
no lower = WERDCF934JGF
no dig = fdEWRadfgr
good pass = trdgf45GFEDF

*/

document.getElementById("submit").addEventListener("click", function(event) {
   checkForm();

   // Prevent default form action. DO NOT REMOVE THIS LINE
   event.preventDefault();
});