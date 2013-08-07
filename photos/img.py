import Image
import ImageDraw
import ImageFont
import ImageOps
import sys

if __name__ == "__main__":

  # Yay for hardcoded values!
  footer = "CC BY-NC-SA 3.0 US : Eric Sigler : me@esigler.com"
  border_size = 8
  thumbnail_size = 256, 256

  # Make sure we were handed something sane
  # FIXME: Future rev - deal with paths
  if len(sys.argv) < 2:
    print "Usage: python img.py filename.jpg"
    sys.exit(1)

  # Get set up
  source_filename = sys.argv[1]
  source_basename = source_filename.split('.')[0]
  source_image = Image.open(source_filename)
  font = ImageFont.truetype('Inconsolata.otf', 7)

  # Add our black border/frame
  framed_image = ImageOps.expand(source_image,
                                 border=border_size,
                                 fill='black')

  # Add our footer text
  # FIXME: That 90 is a magic number, figure it out later
  drawer = ImageDraw.Draw(framed_image)
  text_size = drawer.textsize(footer)
  drawer.text((framed_image.size[0]-text_size[0]+90,
               framed_image.size[1]-border_size),
              footer,
              font=font)

  # Save out the new image, in PNG format
  framed_image.save(source_basename + '.png', 'png')

  # Make the thumbnails - yes, I know, this is a proportional
  # reduction, so the font looks tiny, and isn't the right ratio.
  # I'll fix it when I get around to it.
  framed_image.thumbnail(thumbnail_size, Image.ANTIALIAS)
  framed_image.save(source_basename + '.thumb.png', 'png')
