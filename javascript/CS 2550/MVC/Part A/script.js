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
    this.nameError = document.getElementById("nameError");
    this.characterTable = document.getElementById("characterTable");
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

const addCharacter = function () {
  if (validateName()) {
    glob.characterTable.innerHTML += `<tr>
    <td>${glob.traits.name.value}</td>
    <td>${titleMe(glob.traits.race.value)}</td>
    <td>${titleMe(glob.traits.class.value)}</td>
    <td>${titleMe(
      document.querySelector("input[name=characterSex]:checked").value
    )}</td>
    </tr>`;
  }
  switchSection();
};

const switchSection = function () {
  if (glob.sections.newCharacter.classList.contains("d-none")) {
    // creating a new character, reset character creation field
    glob.traits.name.value = "";
    rerollStats();
    glob.traits.race.value = "human";
    glob.traits.class.value = "artificer";
    glob.traits.hand.checked = false;
    document.getElementById("other").checked = true;
  }
  glob.sections.currentCharacters.classList.toggle("d-none");
  glob.sections.newCharacter.classList.toggle("d-none");
};
