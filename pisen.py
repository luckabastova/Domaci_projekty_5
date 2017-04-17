text_pisne="When your legs don't work like they used to before\
And I can't sweep you off of your feet\
Will your mouth still remember the taste of my love?\
Will your eyes still smile from your cheeks?\
\
And, darling, I will be loving you 'til we're seventy\
And, baby, my heart could still fall as hard at twenty-three\
And I'm thinking 'bout how\
People fall in love in mysterious ways\
Maybe just the touch of a hand\
Well me - I fall in love with you every single day\
And I just wanna tell you I am\
\
So honey now\
Take me into your lovin' arms\
Kiss me under the light of a thousand stars\
Place your head on my beating heart\
I'm thinking out loud\
Maybe we found love right where we are\
\
When my hair's all but gone\
And my memory fades\
And the crowds don't remember my name\
When my hands don't play the strings the same way\
I know you will still love me the same\
\
'Cause honey your soul, could never grow old\
It's evergreen\
And baby your smile's\
Forever in my mind and memory\
\
I'm thinking about how\
People fall in love in mysterious ways\
And maybe it's all part of a plan\
I'll just keep on making the same mistakes\
Hoping that you'll understand\
\
But, baby, now\
Take me into your loving arms\
Kiss me under the light of a thousand stars\
Place your head on my beating heart\
I'm thinking out loud\
Maybe we found love right where we are\
Oh\
\
So, baby, now\
Take me into your loving arms\
Kiss me under the light of a thousand stars\
Oh darlin'\
Place your head on my beating heart\
I'm thinking out loud\
Maybe we found love right where we are\
Oh maybe we found love right where we are\
And we found love right where we are"

pocet_pismen_k = 0

for pismeno in text_pisne:
    if pismeno=="k" or pismeno=="K":
        pocet_pismen_k = pocet_pismen_k + 1

print("V textu je {} písmen K.".format(pocet_pismen_k))
