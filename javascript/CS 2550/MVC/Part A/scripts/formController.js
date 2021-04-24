const glob = {
  get init() {
    this.sections = {
      currentCharacters: document.getElementById("currentCharacters"),
      characterForm: document.getElementById("characterForm"),
    };
    this.traits = {
      name: document.getElementById("characterName"),
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
    this.invalidNameError = document.getElementById("invalidNameError");
    this.nameExistsError = document.getElementById("nameExistsError");
    this.characterTable = document
      .getElementById("characterTable")
      .getElementsByTagName("tbody")[0];
    this.formHead = document.getElementById("formHead");
  },
};

const domLoaded = function () {
  glob.init;
  document
    .getElementById("formCreateButton")
    .addEventListener("click", formCreateNew);
  document
    .getElementById("rerollStatsButton")
    .addEventListener("click", rerollStats);
  document
    .getElementById("addCharacterButton")
    .addEventListener("click", addCharacter);
  document
    .getElementById("cancelCreateButton")
    .addEventListener("click", formHide);
  populateTable();
};

window.addEventListener("DOMContentLoaded", domLoaded);

const populateTable = function () {
  const items = getAllItems();
  glob.characterTable.innerHTML = "";
  let newRow;
  let nameCell;
  let raceCell;
  let classCell;
  let sexCell;
  for (const character of items) {
    newRow = glob.characterTable.insertRow();
    nameCell = newRow.insertCell();
    nameCell.innerText = character.name;
    raceCell = newRow.insertCell();
    raceCell.innerText = titleMe(character.race);
    classCell = newRow.insertCell();
    classCell.innerText = titleMe(character.profession);
    sexCell = newRow.insertCell();
    sexCell.innerText = titleMe(character.sex);
  }
};

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
    sum += Math.floor(Math.random() * diceSize) + 1;
  }
  return sum + bonus;
};

const rerollStats = function () {
  const { str, dex, con, wis, int, cha } = glob.traits.abilities;
  str.value = roll("3d6");
  dex.value = roll("3d6");
  con.value = roll("3d6");
  wis.value = roll("3d6");
  int.value = roll("3d6");
  cha.value = roll("3d6");
};

const titleMe = function (string) {
  return string.charAt(0).toUpperCase() + string.slice(1);
};

const validateNameCollission = function () {
  const items = getAllItems();
  for (const character of items) {
    if (character.name == glob.traits.name.value) {
      glob.nameExistsError.classList.remove("d-none");
      glob.traits.name.classList.add("border");
      glob.traits.name.classList.add("border-danger");
      return false;
    }
  }
  glob.nameExistsError.classList.add("d-none");
  return true;
};

const validateNameCharacters = function () {
  if (/[!@#\$%\^&\*\(\)<>\/_\+=\\[\]\|:;\?]/gm.test(glob.traits.name.value)) {
    glob.invalidNameError.classList.remove("d-none");
    glob.traits.name.classList.add("border");
    glob.traits.name.classList.add("border-danger");
    return false;
  }
  glob.invalidNameError.classList.add("d-none");
  return true;
};

const resetForm = function () {
  glob.traits.name.value = "";
  rerollStats();
  glob.traits.race.value = "human";
  glob.traits.class.value = "artificer";
  glob.traits.hand.checked = false;
  document.getElementById("other").checked = true;
};

const showForm = function (header) {
  glob.formHead.innerText = header;
  glob.sections.currentCharacters.classList.add("d-none");
  glob.sections.characterForm.classList.remove("d-none");
};

const hideForm = function () {
  populateTable();
  glob.sections.characterForm.classList.add("d-none");
  glob.sections.currentCharacters.classList.remove("d-none");
};
