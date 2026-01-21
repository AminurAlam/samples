// https://sitandr.github.io/typst-examples-book/book/typstonomicon/try_catch.html

#let img(path, ..args) = context {
  let path-label = label(path)
  let first-time = query((context {}).func()).len() == 0
  if first-time or query(path-label).len() > 0 {
    [#image(path, ..args)#path-label]
  } else {
    rect(
      stroke: 1pt,
      width: args.at("width", default: 50%),
      height: args.at("height", default: 50%),
      align(center + horizon, args.at("alt", default: "404 not found")),
    )
  }
}

#img("404.png", width: 100pt, height: 100pt)
#img("404.png", alt: "pic of nothing", height: 100pt)
#img("404.png")
