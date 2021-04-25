let globalID = 1000;
const currentCharacters = [];

class Character {
  constructor(
    name = "",
    abilities = [0, 0, 0, 0, 0, 0],
    race = "",
    profession = "",
    sex = "",
    leftHanded = false
  ) {
    this.id = globalID;
    globalID++;
    this.name = name;
    this.abilities = {
      str: abilities[0],
      dex: abilities[1],
      con: abilities[2],
      wis: abilities[3],
      int: abilities[4],
      cha: abilities[5],
    };
    this.race = race;
    this.profession = profession;
    this.sex = sex;
    this.leftHanded = leftHanded;
  }
  set updateAbilities(abilityArray) {
    this.abilities = {
      str: abilityArray[0],
      dex: abilityArray[1],
      con: abilityArray[2],
      wis: abilityArray[3],
      int: abilityArray[4],
      cha: abilityArray[5],
    };
  }
}

const modelCreateCharacter = function (
  name = "",
  abilities = [],
  race = "",
  profession = "",
  sex = "",
  leftHanded = false
) {
  currentCharacters.push(
    new Character(name, abilities, race, profession, sex, leftHanded)
  );
};

const modelGetAllCharacters = function () {
  return currentCharacters;
};

const modelGetCharacterByID = function (targetID = 0000) {
  for (const i of currentCharacters) {
    if (i.id == targetID) {
      return i;
    }
  }
  return undefined;
};

const modelUpdateCharacter = function (
  id = 0,
  name = "",
  abilities = [],
  race = "",
  profession = "",
  sex = "",
  leftHanded = false
) {
  const character = modelGetCharacterByID(id);
  if (character) {
    character.name = name;
    character.updateAbilities = abilities;
    character.race = race;
    character.profession = profession;
    character.sex = sex;
    character.leftHanded = leftHanded;
    return character;
  }
  return undefined;
};

const modelDeleteCharacter = function (targetId = 0) {
  for (let c = 0; c <= currentCharacters.length; c++) {
    if (currentCharacters[c].id == targetId) {
      return currentCharacters.splice(c, 1);
    }
  }
};
