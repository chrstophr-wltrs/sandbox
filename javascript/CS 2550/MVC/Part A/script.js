const glob = {
  get init() {
    this.sections = {
      currentCharacters: document.getElementById("currentCharacters"),
      newCharacter: document.getElementById("newCharacterForm"),
    };
    this.buttons = {
      createNew: document.getElementById("openCreationFormButton"),
      reroll: document.getElementById("rerollStatsButton"),
      create: document.getElementById("createCharacterButton"),
      cancel: document.getElementById("cancelCreationButton"),
    };
    this.traits = {
      abilities: {
        str: document.getElementById("abilityStr"),
        dex: document.getElementById("abilityDex"),
        con: document.getElementById("abilityCon"),
        wis: document.getElementById("abilityWis"),
        int: document.getElementById("abilityInt"),
        cha: document.getElementById("abilityCha"),
      },
      race: document.getElementById("raceSelector"),
      class: document.getElementById("classSelector"),
      hand: document.getElementById("characterIsLeftHanded"),
    };
    this.nameError = document.getElementById("nameError");
  },
};

const domLoaded = function () {
  glob.init;
  glob.buttons.createNew.addEventListener("click", switchSection);
  glob.buttons.reroll.addEventListener("click", rerollStats);
  glob.buttons.create.addEventListener("click", addCharacter);
  glob.buttons.cancel.addEventListener("click", switchSection);
};

window.addEventListener("DOMContentLoaded", domLoaded);

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

const rerollStats = function () {
  for (i of glob.traits.abilities) {
    i.value = roll("3d6");
  }
};

const getTraits = function () {
  return {};
};
