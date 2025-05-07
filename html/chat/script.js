addEventListener("input", () => {
  var txt = buf.value;

  char.innerText = txt.length;
  word.innerText = (txt.match(/\w+(\W|$)/g) || "").length;
  sen.innerText = txt.split(/[\.\?!\n]/).filter((sentence) => {
    return sentence && !sentence.match(/[\.\?!\n]/);
  }).length;
  para.innerText = txt.split(/\n\n+/).filter((str) => str).length;
});
