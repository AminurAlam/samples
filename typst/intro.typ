== syntax
- *bold*, _italic_, `raw!@#$%`
- enum
  + aaa
  + bbb
- 'qou' "ute"
- / Term: meaning

#v(2em) // vfill


== scripting

#set terms(separator: ":  ")

#let code(topic, path, lang) = {
  import "@preview/zebraw:0.5.5": * // https://typst.app/universe/package/zebraw/
  let txt = read(path)

  text(font: "Noto Sans", 2em)[#topic]
  zebraw(
    lang: false,
    // header: lang,
    // indentation: 4,
    numbering-separator: true,
    raw(txt, lang: lang, block: true, tab-size: 2)
  )
}

#code("This is some code", "../python/algorithms/1_max_array.py", "python")


== code
```python
def bubble():
  return False
bubble()
```

== math
$sin(pi) = y$

== table
#table(columns: 4)[No.][Topic][Date][Sign][][][][]
