#import "@preview/zebraw:0.5.5": * // https://typst.app/universe/package/zebraw/

#zebraw(
  lang: false,
  numbering-separator: true,
  raw(
    read("frontpage.typ", encoding: "utf8"),
    lang: "typ",
    block: true,
    tab-size: 2,
  ),
)
