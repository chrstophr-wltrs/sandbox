/*
The given web page displays a growing orange circle when the Show Circle button is clicked. Your goal is to show a text message inside the circle as show below, by creating callbacks for a Promise object.

https://static-resources.zybooks.com/static/zyLab/promises_circle.png

The circle.js file contains a click event handler showCircleClick() for the Show Circle button that calls showCircle() to display the orange circle.

The showCircle() function returns a Promise object that may be fulfilled or rejected.
   The promise is fulfilled in one second if showCircle() is not called a second time before the second elapses.
   The promise is rejected if showCircle() is called a second time before the second elapses.

Modify the showCircleClick() to call showCircle() and handle the fulfilled or rejected callbacks using the returned Promise's then() method.
   If the promise is fulfilled, the <div> containing the circle is passed to the callback function. The message "Ta da!" should be added to the <div>'s inner HTML.
   If the promise is rejected, an error message is passed to the callback function. The error message should be displayed using alert().

If your modifications are written correctly, you should see the "Ta da!" message appear one second after the Show Circle button is clicked. If you click Show Circle twice quickly, you should see the error message appear in the alert dialog box, as shown below.

https://static-resources.zybooks.com/static/zyLab/promises_error.png
*/

window.addEventListener("DOMContentLoaded", function () {
   document.querySelector("#showCircleBtn").addEventListener("click", showCircleClick);
});

function showCircleClick() {
   // TODO: Add modifications here
   let circlePromise = showCircle(160, 180, 120);
   circlePromise.then((div) => {
      div.innerHTML = "Ta da!"
   }).catch((rejectStr) => {
      window.alert(rejectStr)
   })
}

// Do not modify the code below

let timerId = null;

function showCircle(cx, cy, radius) {
   
   // Only allow one div to exist at a time
   let div = document.querySelector("div");
   if (div !== null) {
      div.parentNode.removeChild(div);
   }

   // Create new div and add to DOM
   div = document.createElement("div");
   div.style.width = 0;
   div.style.height = 0;
   div.style.left = cx + "px";
   div.style.top = cy + "px";
   div.className = "circle";
   document.body.append(div);

   // Set width and height after showCircle() completes so transition kicks in
   setTimeout(() => {
      div.style.width = radius * 2 + 'px';
      div.style.height = radius * 2 + 'px';		
   }, 10);

   let promise = new Promise(function(resolve, reject) {
      // Reject if showCircle() is called before timer finishes
      if (timerId !== null) {
         clearTimeout(timerId);
         timerId = null;
         div.parentNode.removeChild(div);
         reject("showCircle called too soon");
      }
      else {
         timerId = setTimeout(() => {
            resolve(div);
            timerId = null;
         }, 1000);
      }
   });

   return promise;
}