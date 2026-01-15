https://typst.app/universe/package/meander/ \
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
