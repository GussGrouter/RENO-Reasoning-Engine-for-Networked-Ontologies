# Chunk 000002

- Source: raw/code/pdf/Clean Code.pdf
- Slice: Chapter 3 excerpt (Small!/Do One Thing)
- From: processed/code/clean-code-functions-small-do-one-thing.md

---
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
