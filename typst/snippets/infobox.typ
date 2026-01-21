#let infobox(
  title: "",
  body,
  color: oklch(60%, 0.2, 20deg),
  bg: luma(240),
) = {
  block(
    width: 100%,
    stroke: (left: 3pt + color),
    inset: (left: 1em + 3pt, y: 0.6em),
    outset: (left: -3pt),
    spacing: 1.2em,
    fill: bg,
    {
      if title != "" {
        block(
          width: 100%,
          above: 0em,
          below: 0.8em,
          sticky: true,
          text(weight: "bold", fill: color, title),
        )
      }
      body
    },
  )
}

#infobox(
  title: "FOO",
  lorem(30),
)

#infobox(
  title: heading[BAR],
  color: blue,
  lorem(30),
)

#infobox[#lorem(30)]

#let todo(heading, body) = block(
  above: 2em,
  stroke: gray,
  width: 100%,
  inset: 14pt,
)[
  #place(
    dy: -6pt - 14pt,
    block(fill: white, inset: 2pt, text(1.2em, heading)),
  )
  #body
]

#todo("HELLO WOLRLD", lorem(50))
