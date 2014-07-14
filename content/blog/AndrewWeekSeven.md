Title: "Pointless"
Date: 2014-07-11 10:00:00
Tags: gsoc
Author: Andrew Wells

The clever pun you see at the top of the page accidentally made its way into one of my comments, but I decided to let it stay.  I also decided I could use it as the title of this post because I am currently working on removing points.  Ingenious no?

The R tree seems to be operational for everything except the point deletion.  However, it's performance is not what I would like (comparable to the cover tree).  Hopefully that can be solved by improving the tree construction strategy.

Point deletion is fairly close to completion (I hope).  I may even have the tests finished by lunch.  After that, it should be fairly simple to add support for R-trees and X-trees, indeed, this is already underway.

And now for my random ramblings:

Lately, I've felt kind of like Wally here: http://dilbert.com/fast/2001-01-09/ .  And it's been stormy.  I thought these might be correlated.  It may just be my imagination, but seems harder to work when it is overcast outside.  I would attribute it to darkness making me want to sleep, but then you would expect it to happen late in the evening, which isn't the case.  Finally, I googled it.

Apparently, there are some theories about connections to less oxygen, humidity, and constant noise that all can make you sleepy.  Ugh.  Psychology makes me tired too.  So much speculation.

What I now find more interesting is the second comment on this article:
http://www.thegeminigeek.com/why-do-rainy-days-make-us-sleepy/

The first sentence is a generic, "wow you are great" type sentence, commonly used in spam.  The rest is an unattributed quote.  It reminds me of a presentation given at my REU last year.  One of the professors conducted research in making spam bots to automate reviews on Amazon.  The general strategy was to use phrases that occur frequently in other reviews.  The professor joked: "It's not actually dishonest because we are only saying things that people think."