#import "@preview/catppuccin:1.0.1": catppuccin, flavors

#show: catppuccin.with(flavors.macchiato)

= HEADING

#lorem(50)

#set align(center)
#for (k, val) in flavors.macchiato.colors [
  #if (k == "text") { break }
  #box(
    width: 90pt,
    height: 40pt,
    radius: 7pt,
    fill: val.rgb,
    align(
      center + horizon,
      text(fill: black, upper(k)),
    ),
  )
  #h(4pt)
]
