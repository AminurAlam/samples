#show table: set block(breakable: false)
#show raw: set block(breakable: false)
#show par: it => block(breakable: false, it)

#set page(margin: 25pt)
#set par(justify: false)
#set text(1.35em)
#set math.mat(delim: "[")

#let horizontalrule = line(length: 100%)
#let sumin = $sum_(i=1)^n$
#let st = $sin theta$
#let ct = $cos theta$

#outline(depth: 2)
#pagebreak()

= HEADING

#lorem(50)

== Sub Heading

#lorem(50)

/ Term: #lorem(10)
