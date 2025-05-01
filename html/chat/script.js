addEventListener("input", (event) => {
  var txt = buf.value;
  var words = txt.match(/\w+(\W|$)/g);

  char.innerText = txt.length;
  alnum.innerText = (txt.match(/\w/g) || "").length;
  word.innerText = (words || "").length;
  vovl.innerText = (txt.match(/[aeiou]/g) || "").length;
  if (txt.length == 0) {
    sen.innerText = 0;
  } else {
    sen.innerText = txt.split(/[\.\?!\n]/).filter((sentence) => {
      return sentence && !sentence.match(/[\.\?!\n]/);
    }).length;
  }
  para.innerText = txt.split("\n\n").filter((str) => str).length;
});
