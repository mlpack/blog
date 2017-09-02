Title: "like a tomato struggling for self-expression."
Date: 2014-06-26 10:00:00
Tags: gsoc
Author: Andrew Wells

The title comes from P.G. Wodehouse--perhaps my favorite English language author.  For those who don't know who he is,
he was a commic writer who wrote mostly between WWI and WWII.  A few excerpts should give you a general
idea of his style:

"A certain critic—for such men, I regret to say, do exist—made the nasty remark about my last novel that it contained ‘all the old Wodehouse characters under different names’. He has probably now been eaten by bears, like the children who made mock of the prophet Elisha: but if he still survives he will not be able to make a similar charge against Summer Lightning. With my superior intelligence, I have outgeneralled this man by putting in all the old Wodehouse characters under the same names. Pretty silly it will make him feel, I rather fancy."

or his description of a protest:

WHATEVER THESE BIMBOS were protesting about, it was obviously something they were taking to heart rather. By the time I had got into their midst not a few of them had decided that animal cries were insufficient to meet the case and were saying it with bottles and brickbats, and the police who were present in considerable numbers seemed not to be liking it much. It must be rotten being a policeman on these occasions. Anyone who has got a bottle can throw it at you, but if you throw it back, the yell of police brutality goes up and there are editorials in the papers next day.

"But the mildest cop can stand only so much, and it seemed to me, for I am pretty shrewd in these matters, that in about another shake of a duck’s tail hell’s foundations would be starting to quiver. I hoped nobody would scratch my paint."

or his description of a rugby game:

"There had been a great deal of rain in the last few days, and the going appeared to be a bit sticky.  In fact, I have seen swamps that were drier than this particular bit of ground.  The red-haired bloke whom I had encountered in the pub paddled up and kicked off amidst cheers from the populace, and the ball went straight to where Tuppy was standing, a pretty colour-scheme in light blue and orange.  Tuppy caught it neatly, and hoofed it back, and it was at this point that I understood that an Upper Bleaching versus Hockley-cum-Meston game had certain features not usually seen on the football-field.
  For Tuppy, having done his bit, was just standing there, looking modest, when there was a thunder of large feet and the red-haired bird, galloping up, seized him by the neck, hurled him to earth, and fell on him.  I had a glimpse of Tippy's face, as it registered horror, dismay, and a general suggestion of stunned dissatisfaction with the scheme of things, and then he disappeared.  By the time he had come to the surface, a sort fo mob-warfare was going on at the other sife of the field.  Two assortments of sons of the soil had got their heads down and were shoving earnestly against each other, with the ball somewhere in the middle.
  Tuppy wiped a fair portion of Hampshire out of his eye, peered round him in a dazed sort of way, saw the mass-meeting and ran towards it, arriving just in time for a couple of heavyweights to gather him in and give him the mud-treatment again.  This placed him in an admirable position for a third heavyweight to kick him in the ribs with a boot like a violin-case.  The red-haired man then fell on him.  It was all good, brisk play, and looked fine from my side of the ropes."

According to Stroustrup and many others, the language you use effects the way you think.  I'm not sure I'm entirely sold on this, as it seems it may just change the way you express your thoughts, but it is an interesting question to consider.
Java is the language I primarily use, though the first language I learned was C.  This causes issues when I try to write C++.  For exaple, a few days ago I discovered a bug that ran roughly as follows:

I wanted a constructor to create a node with a given parent.  I didn't actually need to change the parent, since the node will be split and then destroyed, so I followed the convention recommended by Stroustrup and passed the parent as a reference rather than a pointer.
In Java, doing something like this would be fine.  In C++, I accidentally made a copy constructor.  Several hours of debugging turned up my mistake, but it was rather unpleasant. Or as Wodehouse would say:

"He had the look of one who had drunk the cup of life and found a dead beetle at the bottom."

( Many of Wodehouse's works can be found on project Gutenberg: http://www.gutenberg.org/ebooks/author/783 )