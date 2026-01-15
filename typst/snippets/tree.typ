https://typst.app/universe/package/tdtr
#import "@preview/tdtr:0.4.3": *

#tidy-tree-graph()[
  - $integral_0^infinity e^(-x) dif x = 1$
    - `int main() { return 0; }`
      - Hello
        - This
        - Continue
        - Hello World
      - This
    - _literally_
      - Like
    - *day*
      - tomorrow $1$
]

#v(50pt)

#tidy-tree-graph(
  spacing: (20pt, 20pt),
  node-inset: 4pt,
)[
  - $I_0$
    + $E$
    - $I_1$
      + $+$
      - $I_6$
        + $T$
        - $I_9$
          + $F$
          - $I_7$
        + $F$
        - $I_3$
        + $a$
        - $I_4$
        + $b$
        - $I_5$
    + $T$
    - $I_2$
      + $F$
      - $I_7$
        + $*$
        - $I_8$
      + $a$
      - $I_4$
      + $b$
      - $I_5$
    + $F$
    - $I_3$
      + $*$
      - $I_8$
    + $a$
    - $I_4$
    + $b$
    - $I_5$
]

#v(30pt)

#tidy-tree-graph(
  spacing: (20pt, 20pt),
  draw-edge: tidy-tree-draws.horizontal-vertical-draw-edge,
)[
  - Hello
    - World
      - How
        - Whats
          - Day
        - the
          - Nest
        - Time
          - World
            - Whats
              - Day
            - the
            - Time
              - Hello
            - Today
            - Something
              - Interesting
      - This
      - Day
        - Hello
      - People
    - Things
    - Become
    - Somehow
    - are
      - People
      - Hello
        - World
        - Day
          - Hello
          - World
          - Fine
          - I'm
          - Very
            - Happy
            - That
            - They
            - have
            - what
        - you
        - Byte
        - integer
        - Today
      - you
      - Among
]
