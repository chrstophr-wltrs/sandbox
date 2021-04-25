const glob = {
  get init() {
    this.sections = {
      currentCharacters: document.getElementById("currentCharacters"),
      characterForm: document.getElementById("characterForm"),
    };
    this.buttons = {
      create: document.getElementById("formCreateButton"),
      update: document.getElementById("formUpdateButton"),
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
      profession: document.getElementById("professionSelector"),
      hand: document.getElementById("characterIsLeftHanded"),
    };
    this.nameError = document.getElementById("nameError");
    this.characterTable = document
      .getElementById("characterTable")
      .getElementsByTagName("tbody")[0];
    this.formHead = document.getElementById("formHead");
  },
};

const domLoaded = function () {
  glob.init;
  document
    .getElementById("createButton")
    .addEventListener("click", formCreateNew);
  document
    .getElementById("rerollStatsButton")
    .addEventListener("click", rerollStats);
  glob.buttons.create.addEventListener("click", addCharacter);
  document
    .getElementById("formCancelButton")
    .addEventListener("click", formHide);
  populateTable();
};

window.addEventListener("DOMContentLoaded", domLoaded);

const populateTable = function () {
  const allCharacters = modelGetAllCharacters();
  glob.characterTable.innerHTML = "";
  let newRow;
  let nameCell;
  let raceCell;
  let classCell;
  let sexCell;
  for (const character of allCharacters) {
    newRow = glob.characterTable.insertRow();
    nameCell = newRow.insertCell();
    nameCell.innerText = character.name;
    raceCell = newRow.insertCell();
    raceCell.innerText = titleMe(character.race);
    classCell = newRow.insertCell();
    classCell.innerText = titleMe(character.profession);
    sexCell = newRow.insertCell();
    sexCell.innerText = titleMe(character.sex);
    editCell = newRow.insertCell();
    editBtn = document.createElement("button");
    editBtn.type = "button";
    editBtn.classList.add("btn");
    editBtn.classList.add("btn-warning");
    editBtn.onclick = function () {
      formEditCharacter(character.id);
    };
    editBtn.innerText = "Edit";
    editCell.appendChild(editBtn);
    deleteCell = newRow.insertCell();
    deleteButton = document.createElement("button");
    deleteButton.type = "button";
    deleteButton.classList.add("btn");
    deleteButton.classList.add("btn-danger");
    deleteButton.onclick = function () {
      deleteCharacter(character);
    };
    deleteButton.innerText = "Delete";
    deleteCell.appendChild(deleteButton);
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

const validateName = function () {
  if (/[!@#\$%\^&\*\(\)<>\/_\+=\\[\]\|:;\?]/gm.test(glob.traits.name.value)) {
    glob.nameError.classList.remove("d-none");
    glob.traits.name.classList.add("border");
    glob.traits.name.classList.add("border-danger");
    return false;
  }
  glob.nameError.classList.add("d-none");
  glob.traits.name.classList.remove("border");
  glob.traits.name.classList.remove("border-danger");
  return true;
};

const populateForm = function (characterID) {
  const char = modelGetCharacterByID(characterID);
  resetForm();
  const { name, abilities, race, profession, hand } = glob.traits;
  const { str, dex, con, wis, int, cha } = abilities;
  name.value = char.name;
  str.value = char.abilities.str;
  dex.value = char.abilities.dex;
  con.value = char.abilities.con;
  wis.value = char.abilities.wis;
  int.value = char.abilities.int;
  cha.value = char.abilities.cha;
  race.value = char.race;
  profession.value = char.profession;
  document.getElementById(char.sex).checked = true;
  hand.checked = char.leftHanded;
};

const formEditCharacter = function (characterID) {
  populateForm(characterID);
  glob.buttons.create.classList.add("d-none");
  glob.buttons.update.classList.remove("d-none");
  glob.buttons.update.onclick = function () {
    updateCharacter(characterID);
  };
  formShow("Edit Character");
};

const updateCharacter = function (characterID) {
  if (validateName()) {
    const { name, abilities, race, profession, hand } = glob.traits;
    const { str, dex, con, wis, int, cha } = abilities;
    const abilityArray = [
      parseInt(str.value),
      parseInt(dex.value),
      parseInt(con.value),
      parseInt(wis.value),
      parseInt(int.value),
      parseInt(cha.value),
    ];
    const sex = document.querySelector("input[name=characterSex]:checked")
      .value;
    modelUpdateCharacter(
      characterID,
      name.value,
      abilityArray,
      race.value,
      profession.value,
      sex,
      hand.checked
    );
    formHide();
  }
};

const deleteCharacter = function (character) {
  if (confirm(`Are you sure you want to delete ${character.name}?`)) {
    modelDeleteCharacter(character.id);
    populateTable();
  }
};

const resetForm = function () {
  glob.traits.name.classList.remove("border");
  glob.traits.name.classList.remove("border-danger");
  glob.nameError.classList.add("d-none");
  glob.traits.name.value = "";
  rerollStats();
  glob.traits.race.value = "human";
  glob.traits.profession.value = "artificer";
  glob.traits.hand.checked = false;
  document.getElementById("other").checked = true;
};

const formShow = function (header = "Create New Character") {
  glob.formHead.innerText = header;
  glob.sections.currentCharacters.classList.add("d-none");
  glob.sections.characterForm.classList.remove("d-none");
};

const formHide = function () {
  populateTable();
  glob.sections.characterForm.classList.add("d-none");
  glob.sections.currentCharacters.classList.remove("d-none");
};

const formCreateNew = function () {
  resetForm();
  glob.buttons.create.classList.remove("d-none");
  glob.buttons.update.classList.add("d-none");
  formShow("Create New Character");
};

const addCharacter = function () {
  if (validateName()) {
    const { name, abilities, race, profession, hand } = glob.traits;
    const { str, dex, con, wis, int, cha } = abilities;
    const abilityArray = [
      parseInt(str.value),
      parseInt(dex.value),
      parseInt(con.value),
      parseInt(wis.value),
      parseInt(int.value),
      parseInt(cha.value),
    ];
    const sex = document.querySelector("input[name=characterSex]:checked")
      .value;
    modelCreateCharacter(
      name.value,
      abilityArray,
      race.value,
      profession.value,
      sex,
      hand.checked
    );
    formHide();
  }
};
