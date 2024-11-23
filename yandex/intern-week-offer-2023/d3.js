module.exports = function (text, changeLang) {
  let res = '';
  const splitted = text.split('[_]').filter((item) => !!item);
  let isChanged = false;

  const getNextSymbol = (s) => {
    const res = isChanged ? changeLang(s.toLowerCase()) : s;

    return res || '';
  };

  for (let split of splitted) {
    if (split.includes('[v]')) {
      const count = split.split('[v]').length - 1;
      const regex = /\[v]/gi;
      split = split.replace(regex, '');
      if (count) {
        split = split.substring(0, split.length / count);
        res += split;
      }
    } else if (split.includes('[b]')) {
      res = res.length ? res.substring(0, res.length - 1) : '';
    } else if (split.includes('[l]')) {
      isChanged = !isChanged;
    } else {
      if (split[0].toLowerCase() !== split[0].toUpperCase()) {
        if (split[0] === split[0].toLowerCase()) {
          res += getNextSymbol(split[0].toLowerCase()).toLowerCase();
        } else {
          res += getNextSymbol(split[0].toUpperCase()).toUpperCase();
        }
      } else {
        res += split[0];
      }
    }
  }

  return res;
}
