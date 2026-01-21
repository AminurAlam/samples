#let infobox(
  title: "",
  body: [],
  color: oklch(60%, 0.2, 20deg),
) = {
  block(
    width: 100%,
    stroke: (left: 3pt + color),
    inset: (left: 1em + 3pt, y: 0.6em),
    outset: (left: -3pt),
    spacing: 1.2em,
    {
      block(
        width: 100%,
        above: 0em,
        below: 0.8em,
        sticky: true,
        text(weight: "bold", fill: color, title),
      )
      body
    },
  )
}

#infobox(
  title: "FOO",
  body: lorem(30),
)

#infobox(
  title: "BAR",
  body: lorem(30),
  color: blue,
)
