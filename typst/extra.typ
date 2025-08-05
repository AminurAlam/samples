#let starter(subject, name, roll_no, semester, department, course, institute, index: false) = [
  // TITLEPAGE
  #set align(center)
  #let year = datetime.today().year()

  #v(12%)
  #line(length: 100%, stroke: 1.6pt) #v(-6pt) #line(length: 100%, stroke: 0.4pt)
  #text(weight: "bold", 2.5em)[#upper[#subject]]
  #line(length: 100%, stroke: 0.4pt) #v(-6pt) #line(length: 100%, stroke: 1.6pt)

  #v(23%)
  #align(left)[
    #for (key, value) in (
      "SUBMITTED BY": name,
      "ROLL NO": roll_no,
      "SEMESTER": semester,
      "DEPARTMENT": department,
      "COURSE": course,
    ) [#text(1.2em)[#key:] #h(10pt) #text(1.8em)[#value] \ #v(2pt) ]
  ]
  #align(bottom)[#text(1.4em)[#institute #{ year }-#{ year - 1999 }]]

  // INDEX
  #set page(margin: (right: 8%, top: 8%))
  #show table.cell: it => {
    set text(1.6em)
    strong(it)
  }

  #if index [
    #table(
      columns: (.15fr, 1fr, .25fr, .25fr),
      rows: (.05fr, 1fr),
      align: horizon,
    )[No.][Topic][Date][Sign]
  ]
]

// TODO: auto detect filetype
#let code(question: [], path, lang: "") = [
  #import "@preview/zebraw:0.5.5": * // https://typst.app/universe/package/zebraw/
  #let txt = read(path, encoding: "utf8")

  #text(font: "Noto Sans", 1.6em)[#question]
  #zebraw(
    lang: false,
    numbering-separator: true,
    raw(txt, lang: lang, block: true, tab-size: 2),
  )
]
