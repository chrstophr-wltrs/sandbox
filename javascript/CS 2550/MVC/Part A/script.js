const roll = function (diceString = "1d20") {
  let bonus = 0;
  let numberOfDice;
  let diceSize;
  if (!diceString.includes("d")) {
    throw new TypeError("Dice string must include 'd'");
  }
  let splitDice = diceString.split("d");
  if (splitDice[1].includes("+")) {
    let secondSplit = splitDice[1].split("+");
    splitDice = [splitDice[0], ...secondSplit];
    numberOfDice = parseFloat(splitDice[0]);
    diceSize = parseFloat(splitDice[1]);
    bonus = parseFloat(splitDice[2]);
  } else if (splitDice[1].includes("-")) {
    let secondSplit = splitDice[1].split("-");
    splitDice = [splitDice[0], ...secondSplit];
    numberOfDice = parseFloat(splitDice[0]);
    diceSize = parseFloat(splitDice[1]);
    bonus = parseFloat(splitDice[2]) * -1;
  } else {
    numberOfDice = parseFloat(splitDice[0]);
    diceSize = parseFloat(splitDice[1]);
  }
  let sum = 0;
  for (let i = 0; i < numberOfDice; i++) {
    sum = Math.floor(Math.random() * diceSize) + 1;
  }
  return sum + bonus;
};
