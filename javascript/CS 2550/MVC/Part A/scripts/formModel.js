let globalID = 0;
let currentCharacters = [];

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
}

const createItem = function (
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

const getAllItems = function () {
  return currentCharacters;
};

const getItemById = function (target) {
  for (const i of currentCharacters) {
    if (i.id == target) {
      return i;
    }
  }
  return undefined;
};
