https://typst.app/universe/package/zebraw/
#import "@preview/zebraw:0.5.5": *

#zebraw(
  lang: true,
  numbering-separator: false,
  ```py
  def main():
    print('hello world')

  main()
  ```,
)


#zebraw(
  lang: false,
  numbering-separator: true,
  raw(
    read("code.typ", encoding: "utf8"),
    lang: "typ",
    block: true,
    tab-size: 2,
  ),
)

