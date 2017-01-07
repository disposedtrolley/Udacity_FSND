# Getting Up and Running

## Why Responsive Images?

+   consume a lot of bandwidth; on average more than 60% of the data used to open a webpage
+   large images don't work well on smaller devices
+   "Create a product, don't re-imagine one for small screens. Great mobile products are created, never ported" - Brian Fling


# Units, Formats, Environments

## All about Bits and Pixels

+   there's a difference between **display resolution** and **natural resolution**
+   `total bits = pixels x bits per pixel`
+   the first rule for serving images to a range of devices it to save them at the lowest possible quality and smallest file size

## Requests and Revenue

+   Amazon: 1% profit loss for every 100ms of latency
+   Google: -20% ad revenue from 0.4 to 0.9 second latency

## Relative Sizing

+   `width: 100%`
    *   as the image is resized, it expands to fill the viewport and begins to pixelate
+   `max-width: 100%`
    *   the image expands but only ever as wide as its natural resolution
+   don't assume the window size is the same as the screen size, and that it will stay the same
+   the `calc` function in CSS can be used to perform calculations in CSS values, and is a great way to combine absolute and relative values
    *   `width: calc((100%-10px)/2);`


# Images with Markup

## Performance

+   the number of file requests can be just as significant as the size of the request - *aim to reduce the number of files to be served*
+   latency matters more than bandwidth
+   requests add roundtrips which are one of the biggest sources of latency on mobile

## CSS Background Images

+   `background-size: cover;` - the image is kept as small as possible so its smallest dimension matches the container's smallest dimension
+   `background-size: contain;` - the image is kept as large as possible so its largest dimension matches the container's largest dimension


# Full Responsiveness

## srcset

+   we can define a set of different image sizes using the `srcset` attribute of the `<img>` tag, and allow the browser to choose the correct one based on the viewport size and display density
    *   can use **Pixel Density Descriptors**: `1x`, `2x` etc., or **w** units: `500w`, `1500w`
+   if this is unsupported by the browser, it falls back to using the image specified in the `src` attribute

## Sizes Attribute

+   the browser can make a sensible choice as to which image to display based on the width we provide through **w** units, but what if the image isn't displayed at 100% of the viewport?
    *   since it parses HTML first and preloads images, before touching the CSS
+   the `sizes` attribute tells the browser the sizes at which an image will be displayed - can work out which image to request when parsing the HTML

## The Picture Element

+   the `<picture>` element can contain multiple `<source>` elements, which provide optional file sources for the browser to choose
    *   e.g. **webp** and **jpg**
+   a standard `<img>` tag is also present for fallback, and to actually display the image


