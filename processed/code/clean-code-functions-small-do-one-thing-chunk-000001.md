# Chunk 000001

- Source: raw/code/pdf/Clean Code.pdf
- Slice: Chapter 3 excerpt (Small!/Do One Thing)
- From: processed/code/clean-code-functions-small-do-one-thing.md

---
Small!
The ﬁrst rule of functions is that they should be small. The second rule of functions is that
they should be smaller than that. This is not an assertion that I can justify. I can’t provide
any references to research that shows that very small functions are better. What I can tell
you is that for nearly four decades I have written functions of all different sizes. I’ve writ-
ten several nasty 3,000-line abominations. I’ve written scads of functions in the 100 to 300
line range. And I’ve written functions that were 20 to 30 lines long. What this experience
has taught me, through long trial and error, is that functions should be very small.
      In the eighties we used to say that a function should be no bigger than a screen-full.
Of course we said that at a time when VT100 screens were 24 lines by 80 columns, and
our editors used 4 lines for administrative purposes. Nowadays with a cranked-down font
and a nice big monitor, you can ﬁt 150 characters on a line and a 100 lines or more on a
screen. Lines should not be 150 characters long. Functions should not be 100 lines long.
Functions should hardly ever be 20 lines long.
      How short should a function be? In 1999 I went to visit Kent Beck at his home in Ore-
gon. We sat down and did some programming together. At one point he showed me a cute
little Java/Swing program that he called Sparkle. It produced a visual effect on the screen
very similar to the magic wand of the fairy godmother in the movie Cinderella. As you
moved the mouse, the sparkles would drip from the cursor with a satisfying scintillation,
falling to the bottom of the window through a simulated gravitational ﬁeld. When Kent
showed me the code, I was struck by how small all the functions were. I was used to func-
tions in Swing programs that took up miles of vertical space. Every function in this pro-
gram was just two, or three, or four lines long. Each was transparently obvious. Each told
a story. And each led you to the next in a compelling order. That’s how short your functions
should be!3




2. An open-source unit-testing tool for Java. www.junit.org
3. I asked Kent whether he still had a copy, but he was unable to ﬁnd one. I searched all my old computers too, but to no avail.
   All that is left now is my memory of that program.
