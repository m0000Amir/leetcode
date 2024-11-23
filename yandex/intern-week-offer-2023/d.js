function a(text, changeLang) {
  let output = '';
  const textBetweenPresses = text.split('[_]').filter((item) => !!item);
  let isChanged = false;

  const getNextSymbol = (s) => {
    const res = isChanged ? changeLang(s.toLowerCase()) : s;

    return res || '';
  };

  for (let textBetweenPress of textBetweenPresses) {
    if (textBetweenPress.includes('[v]')) {
      const count = textBetweenPress.split('[v]').length - 1;
      const regex = /\[v]/gi;
      textBetweenPress = textBetweenPress.replace(regex, '');
      if (count) {
        textBetweenPress = textBetweenPress.substring(0, textBetweenPress.length / count);
        output += textBetweenPress;
      }
    } else if (textBetweenPress.includes('[b]')) {
      output = output.length ? output.substring(0, output.length - 1) : '';
    } else if (textBetweenPress.includes('[l]')) {
      isChanged = !isChanged;
    } else {
      if (textBetweenPress[0].toLowerCase() !== textBetweenPress[0].toUpperCase()) {
        if (textBetweenPress[0] === textBetweenPress[0].toLowerCase()) {
          output += getNextSymbol(textBetweenPress[0].toLowerCase()).toLowerCase();
        } else {
          output += getNextSymbol(textBetweenPress[0].toUpperCase()).toUpperCase();
        }
      } else {
        output += textBetweenPress[0];
      }
      output += textBetweenPress[0];
    }
  }

  return output;
}

let text1 = 'Y[_]aa[_]nnnn[_]d[_]e[_]xxx[_]![_][b][b][b]';
let text2 = 'H[_]e[_]l[_]ll[_]o[_]\n' + '[_][l][l][_]v[_]bb[_]h';
let text3 = 'T[_]o[_]d[_]o[_]:[_]\n' + '[_][v][v]';


const changeLang = () => {};
console.log(a(text2, changeLang));
