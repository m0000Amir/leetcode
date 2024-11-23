function solution({ users, rooms }) {
  // intervals
  let incomingUsers = new Map();
  let outGoingUsers = new Map();
  let roomsFilling = [];

  const sum = rooms.reduce((a, b) => a + b, 0);

  for (let i = 0; i <= 23; i++) {
    incomingUsers.set(i, []);
    outGoingUsers.set(i, []);
  }

  users.forEach((user, index) => {
    if (user[0] !== user[1]) {
      incomingUsers.set(user[0], [...incomingUsers.get(user[0]), index]);
      outGoingUsers.set(user[1], [...outGoingUsers.get(user[1]), index]);
    }
  });

  for (let i = 0; i < rooms.length; i++) {
    roomsFilling[i] = [];

    for (let j = 0; j < rooms[i]; j++) {
      roomsFilling[i].push(undefined);
    }
  }

  const roomsFillingByHours = () => {
    let localRes = [];
    let currentSum = 0;

    for (let i = 0; i <= 22; i++) {
      let comeUsers = incomingUsers.get(i);
      let outUsers = outGoingUsers.get(i);

      let found = false;

      outUsers.forEach((user) => {
        found = false;

        for (let i = 0; i < rooms.length; i++) {
          if (found) {
            break;
          }

          for (let j = 0; j < roomsFilling[i].length; j++) {
            if (roomsFilling[i][j] === user) {
              roomsFilling[i][j] = undefined;
              found = true;
              currentSum--;
              break;
            }
          }
        }
      });

      found = false;

      comeUsers.forEach((user) => {
        if (currentSum < sum) {
          found = false;
          for (let i = 0; i < rooms.length; i++) {
            if (found) {
              break;
            }

            for (let j = 0; j < roomsFilling[i].length; j++) {
              if (roomsFilling[i][j] === undefined) {
                roomsFilling[i][j] = user;
                found = true;
                currentSum++;
                break;
              }
            }
          }
        }
      });

      for (let fill = 0; fill < rooms.length; fill++) {
        if (
          roomsFilling[fill].length > 1 &&
          roomsFilling[fill].filter((item) => item !== undefined).length === 1
        ) {
          localRes.push([i, i + 1]);
          break;
        }
      }
    }

    return localRes;
  };

  const mergeIntervals = (intervals) => {
    const res = [];

    if (!intervals.length) return [];

    let [first, second] = intervals[0];

    let index = 1;

    while (index < intervals.length) {
      if (second === intervals[index][0]) {
        second = intervals[index][1];
      } else {
        res.push([first, second]);
        [first, second] = intervals[index];
      }
      index++;
    }

    if (first !== undefined && second !== undefined) {
      res.push([first, second]);
    }

    return res;
  };

  let localRes = roomsFillingByHours();

  return mergeIntervals(localRes);
}


let data = {
  "users": [
    [10, 12],
    [13, 17],
    [14, 15]
  ],
  "rooms": [2]
};


console.log(solution(data));
