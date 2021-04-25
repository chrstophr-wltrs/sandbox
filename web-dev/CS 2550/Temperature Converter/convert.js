/*
Implement conversion functions (2 points)
Implement the convertCtoF() and convertFtoC() functions to convert between Celsius and Fahrenheit. convertCtoF() takes a single numerical argument for a temperature in Celsius and returns the temperature in Fahrenheit using the following conversion formula:

°F = °C * 9/5 + 32

Similarly, convertFtoC() takes a single numerical argument for a temperature in Fahrenheit and returns the temperature in Celsius using the following conversion formula:

°C = (°F - 32) * 5/9

Register Convert button's click event handler (2 points)
When the DOM finishes loading, the domLoaded() function is called. Implement domLoaded() to register a click event handler for the Convert button (id="convertButton"). Use addEventListener(), not onclick.

When the Convert button is pressed, the text box that contains a number should be converted into the opposing temperature. So if a number is in the Celsius text box (id="cInput"), the temperature should be converted into Fahrenheit and displayed in the Fahrenheit text box (id="fInput") and vice versa. Use parseFloat() to convert from a string to a number and do not round the result.

Ensure only one text field contains a value (2 points)
Ensure that only one text field contains a value at any moment in time unless the Convert button has been pressed. Ex: When the Celsius field has a number and the user enters a Fahrenheit entry, the Celsius field should be cleared as soon as the user begins to type. This will require implementing an input event handler for each of the text fields that clears the opposing text field when a change occurs. Register each input event handler in the domLoaded() function. Use addEventListener(), not oninput.

Change image to reflect temperature (2 points)
When the temperature is converted, change the image to reflect the temperature in Fahrenheit. Each image is in the same directory as your .html file. To change the image, change the image's src property to the appropriate filename.

Below 32 F = cold.png
32 - 50 F = cool.png
Above 50 F = warm.png

Handle bad input (2 points)
When parseFloat() returns NaN for the temperature to be converted, set errorMessage's innerHTML to the message: "X is not a number", where X is the string from the text input. When parseFloat() returns a valid number, set errorMessage's innerHTML to an empty string.
*/

window.addEventListener("DOMContentLoaded", domLoaded);

function domLoaded() {
   let cInput = document.querySelector('#cInput')
   let fInput = document.querySelector('#fInput')
   let weatherImage = document.querySelector("#weatherImage")
   let convertButton = document.querySelector("#convertButton")
   cInput.addEventListener("input", () => fInput.value = "")
   fInput.addEventListener("input", () => cInput.value = "")
   convertButton.addEventListener("click", convert)
}

function convert() {
   let error = document.querySelector("#errorMessage")
   let val
   if (cInput.value === "") {
      val = parseFloat(fInput.value)
      if (isNaN(val)) {
         error.innerHTML = `${fInput.value} is not a number`
         return
      }
      else {
         fInput.value = val
         cInput.value = convertFtoC(val)
      }
   }
   else {
      val = parseFloat(cInput.value)
      if (isNaN(val)) {
         error.innerHTML = `${cInput.value} is not a number`
         return
      }
      else {
         fInput.value = convertCtoF(val)
      }
   }
   error.innerHTML = ""
   switch(true) {
      case (isNaN(fInput.value)):
         return
      case fInput.value > 50:
         weatherImage.src = "warm.png"
         weatherImage.alt = "Warm"
         break
      case fInput.value > 31:
         weatherImage.src = "cool.png"
         weatherImage.alt = "Cool"
         break
      default:
         weatherImage.src = "cold.png"
         weatherImage.alt = "Cold"
   }
}

function convertCtoF(degreesCelsius) {
   return((degreesCelsius * 9/5) + 32)
}

function convertFtoC(degreesFahrenheit) {
   return((degreesFahrenheit - 32 ) * 5/9)
}

console.log(document.querySelector('#cInput'))
