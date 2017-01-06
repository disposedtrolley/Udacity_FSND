# Starting Small

## The Viewport

+   the **viewport** is the area of the screen the browser can render content to
+   width and height are reported in **Device Independent Pixels (DIPs)**, which relates pixels to a real distance, regardless of the number of hardware pixels
+   unless the browser is told to render for mobile, it will set the viewport to **980dips wide**
    *   it also performs font-boosting; the browser guesses the main content and upsizes the font
+   setting the viewport: `<meta name-"viewport" content="width=device-width,initial-scale=1">`
    *   the `initial-scale` attribute instructs the browser to establish a 1:1 relationship between DIPs and CSS pixels. Without this, some browsers will keep the width constant when rotating devices and scale the content instead of allowing it to reflow

## Relative Units

+   since CSS pixels vary so wildly between devices, large CSS widths and/or absolute positions can result in elements not fitting correctly
+   relative units should be used instead, such as 100%
+   the `max-width` CSS property can be set on elements so they don't overflow their containers: ```img, embed, object, video {
    max-width: 100%;
}```

## Tap Targets

+   fingers are about 10mm wide, working out to be about 40 CSS pixels
    *   buttons should be at least 48x48px and have at least 40px of room between

## Starting Small

+   design for the smallest device up (phone -> tablet -> desktop)
+   forces you to prioritise content and think about performance


# Building Up

## Media Queries

+   easy logic for applying different CSS styles based on device specifications
+   can be implemented by linking to separate CSS files with a `media` attribute in the `<link>` tag
    *   `media="screen and (min-width:500px)"` will apply the linked stylesheet when the page is viewed on devices >= 500px wide
    *   can also be implemented by specifying an `@media` tag within the stylesheet, or by `@import`ing another stylesheet (avoid this one due to performance degradations)
    *   weigh up between linking (more bandwidth intensive), or using `@media` (larger stylesheets)
+   always use `min-width` rather than `min-device-width` as the latter queries the actual device size, not the renderable viewport area within the browser

## Breakpoints

+   a **breakpoint** is a point in which a responsive webpage changes its layout
+   **minor breakpoints** are those which only change the page layout slightly
+   reflowing text does not constitute a breakpoint
+   we shouldn't choose breakpoints, instead we should find them using our content as a guide
    *   view the page with the smallest viewport, and expand the width until the content desires a breakpoint

## Grids

+   the **grid fluid system** allows columns to wrap onto the next line as the browser width gets smaller
+   Bootstrap and 960 Grid are examples of existing grid systems

## Flexbox

+   flexbox automatically expands and shrinks elements depending on the amount of empty space available in its surrounds
+   `display: flex;`
+   the default **flex direction** is *row*, meaning that elements are resized and positioned next to each other in a single line
+   adding `flex-wrap: wrap` to the containing element tells the browser to wrap elements onto the next line (instead of resizing them) as the viewport gets narrower
+   the order of elements can be changed using the `order` CSS property on elements in an `@media` tag


# Common Responsive Patterns

## Intro

+   four main types of patterns:
    *   mostly fluid
    *   column drop
    *   layout shifter
    *   off canvas

## Column Drop

+   at its narrowest viewport, each element stacks vertically
+   as the viewport widens, elements begin to be positioned side by side
+   at its widest viewport, margins are typically added to the left and right of the columns instead of the columns expanding further

## Mostly Fluid

+   similar to *column drop*, but more grid-like
+   at its narrowest viewport, each element stacks vertically
+   as the viewport widens, the grid pattern starts to appear
+   at its widest viewport, margins are typically added to the left and right of the columns instead of the columns expanding further

## Layout Shifter

+   the most responsive pattern with the most breakpoints
+   the content doesn't simply reflow and drop below other columns; **flexbox** and the `order` attribute are used to specify complex arrangements


# Optimisations

## Images

+   common to use the same image but change its resolution depending on device properties, e.g. DPI
    *   use the `source-set` attribute in an `<img>` tag
+   **art direction** refers to changing the geometry of an image; cropping, orientation, to better fit a device
    *   the **picture element** uses media queries to select which image to use

## Tables

+   **hidden columns** - hide columns based on importance depending on the viewport size
    *   need to use caution when applying this technique as content is being hidden from the user; there's no way for them to see the hidden columns from a smaller device
+   **no more tables** - the table is collapsed into a list when the viewport is small
+   **contained scrolling** - the table is wrapped within a div and is scrollable horizontally

## Fonts

+   the ideal **measure** (the length of a line) is around 65 characters
+   choose `font-size: 16px` and `line-height: 1.25em` as minimum guidelines

## Minor Breakpoints

+   between major breakpoints, it may be helpful to adjust margins/paddings on elements, or increase the font size