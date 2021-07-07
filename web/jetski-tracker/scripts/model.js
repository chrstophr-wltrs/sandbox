let globalID = 1000;
let outings = [];
let riders = [];

class Rider {
  constructor(name = "") {
    this.id = globalID;
    globalID++;
    this.name = name;
    this.time = 0;
    this.outings = 0;
  }
  reset() {
    this.time = 0;
    this.outings = 0;
  }
}

class Outing {
  constructor(riderName = "", leaveTime = 0, returnTime = 0) {
    this.rider = modelGetRiderByName(riderName);
    this.leaveTime = leaveTime;
    this.returnTime = returnTime;
    this.duration = returnTime - leaveTime;
  }
}

const modelCreateRider = function (name = "") {
  riders.push(new Rider(name));
};

const modelGetAllRiders = function () {
  return riders;
};

const modelGetRiderByID = function (targetID = 1000) {
  for (const i of riders) {
    if (i.id == targetID) {
      return i;
    }
  }
  return null;
};

const modelGetRiderByName = function (targetName = "") {
  for (const i of riders) {
    if (i.name == targetName) {
      return i;
    }
  }
  return null;
};

const modelAddOuting = function (
  riderName = "",
  leaveTime = 0,
  returnTime = 0
) {
  const out = new Outing(riderName, leaveTime, returnTime);
  outings.push(out);
  const rider = modelGetRiderByName(riderName);
  rider.time += out.duration;
  rider.outings++;
};

const modelResetAllRiders = function () {
  for (const i of riders) {
    i.reset();
  }
};
