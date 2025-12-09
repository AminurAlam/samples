== syntax
- *bold*, _italic_, `raw!@#$%`
- enum
  + aaa
  + bbb
- 'qou' "ute"
- / Term: meaning

== functions
#outline()
#v(20pt)
#h(20pt)
#line(length: 100%, stroke: 1.6pt)
#upper[text]
#pagebreak()
#heading(numbering: none)[Abstract]

#figure(
  // image("svg/01.svg", height: auto),
  box(width: 7cm, height: 7cm, fill: orange),
  caption: [some text],
)

#grid(
  columns: (auto, auto),
  rows: (auto, auto),
  gutter: 10pt,
  [one], [two],
  [three], [four],
)

#columns()[
  Pros:
  - Fast and simple
  - Highly interpretable
  - Good baseline model when relationships are linear
  #colbreak()
  Cons:
  - Sensitive to outliers
  - Performs poorly under multicollinearity
  - Assumes linearity and constant variance
]


== scripting
#import "extra.typ": *
#set terms(separator: ":  ")
#set align(left)
#set par(justify: false)
#set page(margin: 50pt, numbering: "1", columns: 1)

#let year = datetime.today().year()
#let func(a, b) = [swapped: #b, #a. in #year]

#for (key, val) in (
  "foo": "bar",
  "marco": "polo",
  "something": "nothing",
) [#text(1.2em)[#key:] #h(10pt) #text(1.8em)[#val] \ #v(2pt) ]

#starter(course: "not a subject", index: false)
#pagebreak()


== packages


https://typst.app/universe/package/meander/ \
https://github.com/Vanille-N/meander.typ/releases/download/v0.3.0/docs.pdf \
#import "@preview/meander:0.3.0"

#let img1 = box(width: 7cm, height: 7cm, fill: orange)
#let img2 = box(width: 5cm, height: 3cm, fill: blue)
#let img3 = box(width: 8cm, height: 4cm, fill: green)

#meander.reflow({
  import meander: *

  placed(top + left, img1)
  placed(top + right, img2)
  placed(horizon + right, img3)

  container()
  content[
    #set par(justify: true)
    #lorem(280)
  ]
})


https://typst.app/universe/package/oxdraw \
https://github.com/RohanAdwankar/oxdraw \
#import "@preview/oxdraw:0.1.0": *

#oxdraw("
graph TD
    A[Start] --> B[End]
")

#oxdraw(
  ```
  graph TD
  A[Input] --> B[Process]
  B --> C[Output]
  ```,
  background: white,
  overrides: (
    node_styles: (
      A: (fill: "#4CAF50", stroke: "#2E7D32", text: "white"),
      B: (fill: "#2196F3", stroke: "#1976D2"),
      C: (fill: "#FF9800", stroke: "#F57C00"),
    ),
    edge_styles: (
      "A --> B": (color: "#666", line: "dashed"),
      "B --> C": (color: "#E91E63", arrow: "both"),
    ),
  ),
)

https://typst.app/universe/package/zebraw/ \
#import "@preview/zebraw:0.5.5": *

#text(font: "Noto Sans", 1.6em)[uh??]
#zebraw(
  lang: false,
  numbering-separator: true,
  raw("
def main():
  print('hello world')

main()
", lang: "python", block: true, tab-size: 2),
)

== math
$sin(pi) = y$ \
$sum(sin(pi)/x) = y$ \
$display(sum(sin(pi)/x = y))$ \
$ sin(pi) = y $


== table
#table(columns: 4)[No.][Topic][Date][Sign][][][][]
#table(
  columns: 10,
  inset: (x: 8pt, y: 7pt),
  [1.00], [1.00], [1.00], [0.99], [0.99], [1.00], [0.99], [0.93], [0.99], [0.78],
  [1.00], [1.00], [1.00], [0.99], [0.99], [0.99], [0.99], [0.95], [0.99], [0.81],
  [1.00], [1.00], [1.00], [1.00], [0.99], [1.00], [0.99], [0.93], [0.99], [0.78],
  [0.99], [0.99], [1.00], [1.00], [1.00], [1.00], [1.00], [0.94], [0.99], [0.77],
  [0.99], [0.99], [0.99], [1.00], [1.00], [1.00], [1.00], [0.93], [1.00], [0.75],
  [1.00], [0.99], [1.00], [1.00], [1.00], [1.00], [1.00], [0.93], [0.99], [0.76],
  [0.99], [0.99], [0.99], [1.00], [1.00], [1.00], [1.00], [0.93], [1.00], [0.75],
  [0.93], [0.95], [0.93], [0.94], [0.93], [0.93], [0.93], [1.00], [0.93], [0.93],
  [0.99], [0.99], [0.99], [0.99], [1.00], [0.99], [1.00], [0.93], [1.00], [0.75],
  [0.78], [0.81], [0.78], [0.77], [0.75], [0.76], [0.75], [0.93], [0.75], [1.00],
)
