let globalID = 1000;
let rides = [];

class Rider {
  constructor(name = "") {
    this.id = globalID;
    globalID++;
    this.name = name;
    this.time = 0;
    this.rides = 0;
  }
}
