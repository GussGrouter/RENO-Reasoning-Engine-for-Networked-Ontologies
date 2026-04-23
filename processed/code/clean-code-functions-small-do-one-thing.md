# Clean Code — functions: small + do one thing

- Source: raw/code/pdf/Clean Code.pdf
- Extraction: pdftotext -f 55 -l 75 -layout
- Slice: from `Small!` up to (excluding) `Sections within Functions`

---

## Excerpt page 1

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

---

## Excerpt page 2

Do One Thing                                                                            35


    How short should your functions be? They should usually be shorter than Listing 3-2!
Indeed, Listing 3-2 should really be shortened to Listing 3-3.

      Listing 3-3
      HtmlUtil.java (re-refactored)
        public static String renderPageWithSetupsAndTeardowns(
          PageData pageData, boolean isSuite) throws Exception {
          if (isTestPage(pageData))
            includeSetupAndTeardownPages(pageData, isSuite);
          return pageData.getHtml();
        }

Blocks and Indenting
This implies that the blocks within if statements, else statements, while statements, and
so on should be one line long. Probably that line should be a function call. Not only does
this keep the enclosing function small, but it also adds documentary value because the
function called within the block can have a nicely descriptive name.
     This also implies that functions should not be large enough to hold nested structures.
Therefore, the indent level of a function should not be greater than one or two. This, of
course, makes the functions easier to read and understand.


Do One Thing
It should be very clear that Listing 3-1 is doing lots
more than one thing. It’s creating buffers, fetching
pages, searching for inherited pages, rendering paths,
appending arcane strings, and generating HTML,
among other things. Listing 3-1 is very busy doing
lots of different things. On the other hand, Listing 3-3
is doing one simple thing. It’s including setups and
teardowns into test pages.
     The following advice has appeared in one form
or another for 30 years or more.
          FUNCTIONS SHOULD DO ONE THING. THEY SHOULD DO IT WELL.
          THEY SHOULD DO IT ONLY.
     The problem with this statement is that it is hard to know what “one thing” is. Does
Listing 3-3 do one thing? It’s easy to make the case that it’s doing three things:

 1.   Determining whether the page is a test page.
 2.   If so, including setups and teardowns.
 3.   Rendering the page in HTML.

---

## Excerpt page 3

36                                                                                       Chapter 3: Functions


    So which is it? Is the function doing one thing or three things? Notice that the three
steps of the function are one level of abstraction below the stated name of the function. We
can describe the function by describing it as a brief TO4 paragraph:

     TO RenderPageWithSetupsAndTeardowns, we check to see whether the page is a test page
     and if so, we include the setups and teardowns. In either case we render the page in
     HTML.

     If a function does only those steps that are one level below the stated name of the
function, then the function is doing one thing. After all, the reason we write functions is to
decompose a larger concept (in other words, the name of the function) into a set of steps at
the next level of abstraction.
     It should be very clear that Listing 3-1 contains steps at many different levels of
abstraction. So it is clearly doing more than one thing. Even Listing 3-2 has two levels of
abstraction, as proved by our ability to shrink it down. But it would be very hard to mean-
ingfully shrink Listing 3-3. We could extract the if statement into a function named
includeSetupsAndTeardownsIfTestPage, but that simply restates the code without changing
the level of abstraction.
     So, another way to know that a function is doing more than “one thing” is if you can
extract another function from it with a name that is not merely a restatement of its imple-
mentation [G34].
