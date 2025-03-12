function avg(words) {
  var sum = (words || [])
    .map((word) => word.match(/\w+/)[0].length)
    .reduce((acc, curr) => acc + curr, 0);
  return sum / (words || "1").length;
}

function ratio(a, b) {
  if (!a || !b) {
    return `${a}:${b}`;
  }
  var hcf = 1;
  var max = a > b ? a : b;
  for (i = 2; i <= max; i++) {
    if (a % i == 0 && b % i == 0) var hcf = i;
  }
  return `${a / hcf}:${b / hcf}`;
}

addEventListener("input", (event) => {
  var txt = buf.value;
  var words = txt.match(/\w+(\W|$)/g);

  char.innerText = txt.length;
  word.innerText = (words || "").length;
  vovl.innerText = (txt.match(/[aeiou]/g) || "").length;
  cpw.innerText = avg(words);
  vtoc.innerText = ratio(
    (txt.match(/[aeiou]/g) || "").length,
    (txt.match(/[b-df-hj-np-tv-z]/g) || "").length,
  );
});
