/*
Make the following JavaScript modifications using clearInterval() and setInterval() where appropriate:
   In startAnimation(), add an if statement that stops the timer with the ID timerId if timerId is not null.
   In startAnimation(), start a timer that calls moveImage(clickX, clickY) every 10 milliseconds. Save the timer ID in the timerId variable.
   Add an if statement in moveImage() that stops the timer with the ID timerId if (imgX, imgY) is equal to (centerX, centerY). Also set timerId to null.
*/

let timerId = null;

window.addEventListener("DOMContentLoaded", function() {
   document.addEventListener("click", startAnimation);
});

function startAnimation(e) {
   console.log("Click registered!")
   // Get mouse coordinates
   let clickX = e.clientX;
   let clickY = e.clientY;
   console.log(`Click location is ${clickX}, ${clickY}`)
   
   if (timerId != null) {
      console.log(`Animation is already running!`)
      console.log(`Moving to new click location...`)
      clearInterval(timerId)
   }

   console.log("Beginning animation...")
   timerId = setInterval(() => moveImage(clickX, clickY), 10)
   
}

function moveImage(x, y) {
   const img = document.querySelector("img");
            
   // Determine location of image
   let imgX = parseInt(img.style.left);
   let imgY = parseInt(img.style.top);

   // Determine (x,y) coordinates that center the image 
   // around the clicked (x, y) coords
   const centerX = Math.round(x - (img.width / 2));
   const centerY = Math.round(y - (img.height / 2));

   if (centerX == imgX && centerY == imgY){
      clearInterval(timerId)
      timerId = null
      console.log(`Animation complete!`)
   }
   
   // Move 1 pixel in both directions toward the click
   if (imgX < centerX) {
      imgX++;
   }
   else if (imgX > centerX) {
      imgX--;
   }
   
   if (imgY < centerY) {
      imgY++;
   }
   else if (imgY > centerY) {
      imgY--;
   }
   
   img.style.left = imgX + "px";
   img.style.top = imgY + "px";
}