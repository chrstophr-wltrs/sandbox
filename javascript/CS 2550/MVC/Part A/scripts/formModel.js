class Character {
  constructor(
    id = 0000,
    name = "",
    abilities = [0, 0, 0, 0, 0, 0],
    race = "",
    profession = "",
    sex = "",
    leftHanded = ""
  ) {
    this.id = id;
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
