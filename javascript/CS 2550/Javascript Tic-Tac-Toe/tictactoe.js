/*
Investigate the page elements
	The given index.html file contains all needed page elements for a game of Tic-Tac-Toe:
		A div with ID gameBoard and 9 buttons forms the game board. CSS in tictactoe.css converts the div and buttons into a 3x3 grid.
		A paragraph with ID turnInfo, initially containing text "TURN INFO", indicates the turn is the player's or computer's.
		A "New game" button with ID newGameButton allows the player to clear the board and start a new game.


Investigate the stylesheet
	The given tictactoe.css file contains .x and .o rules to set the X and O button colors. Other CSS rules style the grid and buttons.

Investigate the JavaScript
	The given tictactoe.js script has six declarations:
		playerTurn: Boolean variable that is true when the turn belongs to the player and false when the turn belongs to the computer.
		computerMoveTimeout: ID of an active timeout for the computer's move, or 0 if no such timeout exists.
		gameStatus: Object that contains four possible game statuses. The checkForWinner() function returns the appropriate game status.
		domLoaded(): Function that is called when the DOM loads to start the game. Events for the "New game" button click and game board button clicks are registered. Then newGame() is called to start the game. The domLoaded() function is implemented for you and requires no alteration.
		getGameBoardButtons(): Function that returns an array of the 9 <button> elements from the game board. The first 3 elements are the top row, the next 3 the middle row, and the last 3 are the bottom row. The getGameBoard() function is implemented for you and requires no alteration.
		checkForWinner(): Function that returns a gameStatus value indicating if the human has won, if the computer has won, if a draw occurs, or if more moves are available.

Implement newGame() (2 points)
	Implement the newGame() function to do the following:
		Use clearTimeout() to clear the computer's move timeout and then set computerMoveTimeout back to 0.
		Loop through all game board buttons and set the inner HTML of each to an empty string. Also remove the class name and disabled attribute. The disabled attribute prevents the user from clicking the button, but all the buttons should be clickable when starting a new game.
		Allow the player to take a turn by setting playerTurn to true.
		Set the text of the turn information paragraph to "Your turn".

Implement boardButtonClicked() (2 points)
	Implement the boardButtonClicked() function to do the following:
		If playerTurn is true:
			Set the button's inner HTML to "X".
			Add the "x" class to the button.
			Set the button's disabled attribute to true so the button cannot be clicked again.
			Call switchTurn() so the computer can take a turn.

Implement switchTurn() (3 points)
	Implement the switchTurn() function to do the following:
		Call checkForWinner() to determine the game's status.
		If more moves are left, do the following:
			If switching from the player's turn to the computer's turn, use setTimeout() to call makeComputerMove() after 1 second (1000 milliseconds). Assign the return value of setTimeout() to computerMoveTimeout. The timeout simulates the computer "thinking", and prevents the nearly-instant response to each player move that would occur from a direct call to makeComputerMove().
			Toggle playerTurn's value from false to true or from true to false.
			Set the turn information paragraph's text content to "Your turn" if playerTurn is true, or "Computer's turn" if playerTurn is false.
		In the case of a winner or a draw game, do the following:
			Set playerTurn to false to prevent the user from being able to place an X after the game is over.
			If the human has won, display the text "You win!" in the turn info paragraph.
			If the computer has won, display the text "Computer wins!" in the turn info paragraph.
			If the game is a draw, display the text "Draw game" in the turn info paragraph.

Implement makeComputerMove() (3 points)
	Implement the makeComputerMove() function to do the following:
		Choose a random, available button, and set the button's inner HTML to "O".
		Add the "o" class to the button.
		Set the button's disabled attribute to true.
		Call switchTurn() at the end of the function to switch back to the player's turn.
*/

let playerTurn = true;
let computerMoveTimeout = 0;
let turnInfo

const gameStatus = {
	MORE_MOVES_LEFT: 1,
	HUMAN_WINS: 2,
	COMPUTER_WINS: 3,
	DRAW_GAME: 4
};

window.addEventListener("DOMContentLoaded", domLoaded);

function domLoaded() {
	// Setup the click event for the "New game" button
	const newBtn = document.getElementById("newGameButton");
	newBtn.addEventListener("click", newGame);
	turnInfo = document.getElementById("turnInfo")
	// Create click-event handlers for each game board button
	const buttons = getGameBoardButtons();
	for (let button of buttons) {
		button.addEventListener("click", function () { boardButtonClicked(button); });
	}

	// Clear the board
	newGame();
}

// Returns an array of 9 <button> elements that make up the game board. The first 3 
// elements are the top row, the next 3 the middle row, and the last 3 the 
// bottom row. 
function getGameBoardButtons() {
	return document.querySelectorAll("#gameBoard > button");
}

function checkForWinner() {
	
	const buttons = getGameBoardButtons();

	// Ways to win
	const possibilities = [
		[0, 1, 2], [3, 4, 5], [6, 7, 8], // rows
		[0, 3, 6], [1, 4, 7], [2, 5, 8], // columns
		[0, 4, 8], [2, 4, 6] // diagonals
	];

	// Check for a winner first
	for (let indices of possibilities) {
		if (buttons[indices[0]].innerHTML !== "" &&
			buttons[indices[0]].innerHTML === buttons[indices[1]].innerHTML &&
			buttons[indices[1]].innerHTML === buttons[indices[2]].innerHTML) {
			
			// Found a winner
			if (buttons[indices[0]].innerHTML === "X") {
				return gameStatus.HUMAN_WINS;
			}
			else {
				return gameStatus.COMPUTER_WINS;
			}
		}
	}

	// See if any more moves are left
	let foundEmpty = false;
	for (let button of buttons) {
		if (button.innerHTML !== "X" && button.innerHTML !== "O") {
			return gameStatus.MORE_MOVES_LEFT;
		}
	}

	// If no winner and no moves left, then it's a draw
	return gameStatus.DRAW_GAME;
}

function newGame() {
	// Use clearTimeout() to clear the computer's move timeout and
	clearTimeout(computerMoveTimeout)
	// then set computerMoveTimeout back to 0
	computerMoveTimeout = 0
	// Loop through all game board buttons and set the inner HTML of each to an empty string. Also remove the class name and disabled attribute.
	const buttons = getGameBoardButtons();
	for (let button of buttons) {
		button.innerHTML = ""
		button.removeAttribute("class")
		button.removeAttribute("disabled")
	}
	// Allow the player to take a turn by setting playerTurn to true
	playerTurn = true
	// Set the text of the turn information paragraph to "Your turn"
	turnInfo.innerText = "Your turn"
}

function boardButtonClicked(button) {
	// If playerTurn is true:
	if (playerTurn) {
		// Set the button's inner HTML to "X"
		button.innerHTML = "X"
		// Add the "x" class to the button
		button.classList.add("x")
		// Set the button's disabled attribute to true so the button cannot be clicked again
		button.disabled = true
		// Call switchTurn() so the computer can take a turn
		switchTurn()
	}

}

function switchTurn() {
	// Call checkForWinner() to determine the game's status
	switch (checkForWinner()) {
		case 1:
			// Toggle playerTurn's value from false to true or from true to false.
			playerTurn = !playerTurn
			// If switching from the player's turn to the computer's turn, use setTimeout() to call makeComputerMove() after 1 second (1000 milliseconds). Assign the return value of setTimeout() to computerMoveTimeout.
			computerMoveTimeout = playerTurn ? 0 : setTimeout(makeComputerMove, 1000)
			// Set the turn information paragraph's text content to "Your turn" if playerTurn is true, or "Computer's turn" if playerTurn is false.
			turnInfo.innerText = playerTurn ? "Your turn" : "Computer's turn"
			return
		case 2:
			// If the human has won, display the text "You win!" in the turn info paragraph
			turnInfo.innerText = "You win!"
			break
		case 3:
			// If the computer has won, display the text "Computer wins!" in the turn info paragraph
			turnInfo.innerText = "Computer wins!"
			break
		case 4:
			// If the game is a draw, display the text "Draw game" in the turn info paragraph
			turnInfo.innerText = "Draw game"
	}
	// In the case of a winner or a draw game, do the following:
	// Set playerTurn to false to prevent the user from being able to place an X after the game is over
	playerTurn = false
}

function makeComputerMove() {
	const buttons = getGameBoardButtons();
	while (true){
		// Choose a random
		button_to_click = buttons[Math.floor(Math.random() * buttons.length)]
		// available button
		if (button_to_click.innerHTML === ""){
			// and set the button's inner HTML to "O".
			button_to_click.innerHTML = "O"
			// Add the "o" class to the button
			button_to_click.classList.add("o")
			button_to_click.disabled = true
			// Call switchTurn() at the end of the function to switch back to the player's turn
			switchTurn()
			return
		}
		console.log(`Button ${index} is already ticked!`)
	}
}