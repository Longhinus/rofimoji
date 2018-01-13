#!/usr/bin/python
# -*- coding: utf-8 -*-

from subprocess import Popen, PIPE
import sys
reload(sys)  # Reload does the trick!
sys.setdefaultencoding('UTF8')


emojis=u"""⠀(Bowing with m Hands)
⠀(Bowing with < and > hands)
⠀(Bowing with o Hands)
⠀(Bowing from the Side)
⠀(Apologizing with One Hand)
⠀(Words)
⠀(Miscellaneous)
⠀(Famous, Special, or Just Plain Awesome Bears)
⠀(ʕ•ᴥ•ʔ Style Bears)
⠀(Multiple Bears)
⠀(Tiny Bears)
⠀(エ Style Bears)
⠀(㉨ or ᄌ Style Bears)
⠀(ʕु•̫͡•ʔु Style Bears)
⠀(Miscellaneous Bears)
⠀(Complex Bears)
⠀(Rounded Beaks)
⠀(Sharp Beaks)
⠀(Diamond Beaks)
⠀(Half Rounded Beaks)
⠀(Fat Birds?)
⠀(Laughing Birds)
⠀(Miscellaneous Birds)
⠀(Bats)
⠀(Cats with Anime Eyes)
⠀(Simple Cat Kaomojis)
⠀(Fancy Eyed Cats)
⠀(Stylish Cats)
⠀(Fancy Cats)
⠀(Cute Fluffy Kittens)
⠀(Cats with Paws)
⠀(Cats and Fish)
⠀(Cats Doing Things)
⠀(Giant Cats)
⠀(The Lenny Face)
⠀(Raise Your Dongers)
⠀(Other Internet Memes)
⠀(Pokemon)
⠀(Simple Clouds)
⠀(Complex Clouds)
⠀(Head scratching)
⠀(Head Scratching With a ∑)
⠀(Blank Look)
⠀(Raised Arms)
⠀(Raised Hands)
⠀(Quizzical)
⠀(General Confusion)
⠀(Complex)
⠀(Words)
⠀(Cats with Anime Eyes)
⠀(Simple Cat Kaomojis)
⠀(Fancy Eyed Cats)
⠀(Stylish Cats)
⠀(Fancy Cats)
⠀(Cute Fluffy Kittens)
⠀(Cats with Paws)
⠀(Cats and Fish)
⠀(Cats Doing Things)
⠀(Giant Cats)
⠀(The Lenny Face)
⠀(Raise Your Dongers)
⠀(Other Internet Memes)
⠀(Pokemon)
⠀(Simple Clouds)
⠀(Complex Clouds)
⠀(Head scratching)
⠀(Head Scratching With a ∑)
⠀(Blank Look)
⠀(Raised Arms)
⠀(Raised Hands)
⠀(Quizzical)
⠀(General Confusion)
⠀(Complex)
⠀(Words)
⠀(Flailing Arms)
⠀(Crazy Eyes)
⠀(Small Eyes)
⠀(Miscellaneous Craziness)
⠀(Dancing to the Right with Arms Up)
⠀(Dancing to the Left with Arms Up)
⠀(Dancing Forwards with Arms Up)
⠀(Dancing to the Right with Arms to the Side or Down)
⠀(Dancing to the Left with Arms to the Side or Down)
⠀(Dancing Forwards with Arms to the Side or Down)
⠀(One Arm Up and One Arm Down)
⠀(Multiple Kaomojis Dancing)
⠀(X Eyes)
⠀(+ Eyes)
⠀(Ghosts)
⠀(Funerals)
⠀(Miscellaneous)
⠀(Stylized or Just Plain Awesome Dogs)
⠀(Dogs with Pointy Ears)
⠀(Big Floppy Ears)
⠀(Bulldogs)
⠀(Triangle Ears)
⠀(૮( ꒦ິ࿄꒦ີ)ა Style Dogs)
⠀(ᴥ Style Dogs)
⠀(Dog Interactions)
⠀(Sideways Dogs)
⠀(Miscellaneous Dogs)
⠀(Complex)
⠀(Evil Hands)
⠀(Evil Teamwork)
⠀(Demons and Devils)
⠀(General Evilness)
⠀(Circle Hands)
⠀(Excited to the Right)
⠀(Excited to the Left)
⠀(Both Arms Up)
⠀(No Arms)
⠀(٩ and ۶ Arms)
⠀(Elaborate Excitement)
⠀(Looking back and forth)
⠀(Words)
⠀(Fists or Grabby Hands)
⠀(Miscellaneous)
⠀(Giant Emoticons)
⠀(Kicking)
⠀(Punching)
⠀(Guns)
⠀(Swords)
⠀(Bombs)
⠀(Arrows and Other Projectiles)
⠀(Spray)
⠀(Hammers)
⠀(Being a Jerk)
⠀(Two People Fighting)
⠀(Miscellaneous)
⠀(Words)
⠀(Fish)
⠀(Crabs)
⠀(Squids)
⠀(Jellyfish)
⠀(Whales)
⠀(Turtles)
⠀(Other Various Sea Creatures)
⠀(Fishing)
⠀(Food)
⠀(Drink)
⠀(High Five)
⠀(Holding Hands)
⠀(Close Together)
⠀(Cheering Up)
⠀(Lots of Friends)
⠀(Words)
⠀(Complex)
⠀(Miscellaneous)
⠀(Drops of Sweat)
⠀(Waving a Flag to Surrender)
⠀(Arms Up in a Minimal Effort Giving Up Sort of Way)
⠀(Arms Up with More Enthusiasm)
⠀(Arms Down)
⠀(Miscellaneous forms of Defeat)
⠀(Famous Happy Emoticons)
⠀(Triangle Mouths)
⠀(Upside Down A Mouths)
⠀(Squiggly Mouths)
⠀(V Mouths)
⠀(Simple Flat Mouths)
⠀(Squiggly W Mouth Emoticons)
⠀(Standard Smily Mouth Emoticons)
⠀(Tiny or no Mouths)
⠀(Big Wide Open Mouths)
⠀(Miscellaneous Mouths)
⠀(High Energy Happiness)
⠀(Grabby Hands)
⠀(Prayer Hands)
⠀(Tongues)
⠀(Happiness Dance)
⠀(No Cheeks)
⠀(Complex Emoticons)
⠀(Happy Emotions with Words)
⠀(Giant Emoticons)
⠀(Hiding Behind a |)
⠀(Hiding Behind a Big Wall)
⠀(Hiding From People)
⠀(Miscellaneous Hiding)
⠀(Christmas or Winter Holidays)
⠀(Halloween)
⠀(New Years and New Years Eve)
⠀(Birthdays)
⠀(Other Holidays and Events)
⠀(Wide Open Hug Arms)
⠀(Hugging to the Right)
⠀(Hugging to the Left)
⠀(Running Hugs)
⠀(Multiple People Hugging Each Other)
⠀(Grabbing Hands)
⠀(Words)
⠀(Devouring Mouths)
⠀(Licking Lips ڡ Style)
⠀(Licking Lips ൧͑ Style)
⠀(Drooling with hunger)
⠀(Forks ─∈)
⠀(General Pain and Injuries)
⠀(Inflicting Pain on Others)
⠀(Tripping or Falling Down)
⠀(General Sickness)
⠀(Throwing Up, Puking, or Barfing)
⠀(Coughing)
⠀(Drowning)
⠀(Complex Pain and Sickness)
⠀(Kissing with Lips Aimed to the Right)
⠀(Kissing with Lips Aimed to the Left)
⠀(Miscellaneous Mouths)
⠀(Clasping Hands)
⠀(Grabby Hands)
⠀(One Person Kissing Another)
⠀(Two People Kissing Each Other)
⠀(Three or More People Kissing)
⠀(Words)
⠀(Complex)
⠀(Stifling Laughter)
⠀(Tears)
⠀(Waving arms)
⠀(Big Wide Open Mouths)
⠀(Little Hands)
⠀(Words and Sounds)
⠀(ਊ Style Mouths)
⠀(Simple or Miscellaneous Laughter)
⠀(Complex Forms of Laughter)
⠀(Love Eyes)
⠀(Left Love)
⠀(Right Love)
⠀(Forward Love)
⠀(Shy Love)
⠀(Excited Love)
⠀(Thinking &#8216;Bout Love)
⠀(Kissing Lips)
⠀(Couples)
⠀(Objects of Love)
⠀(Animal Love)
⠀(Complex)
⠀(Love Hurts)
⠀(Words About Love)
⠀(Giant)
⠀(General Pain and Injuries)
⠀(Inflicting Pain on Others)
⠀(Tripping or Falling Down)
⠀(General Sickness)
⠀(Throwing Up, Puking, or Barfing)
⠀(Coughing)
⠀(Drowning)
⠀(Complex Pain and Sickness)
⠀(Kissing with Lips Aimed to the Right)
⠀(Kissing with Lips Aimed to the Left)
⠀(Miscellaneous Mouths)
⠀(Clasping Hands)
⠀(Grabby Hands)
⠀(One Person Kissing Another)
⠀(Two People Kissing Each Other)
⠀(Three or More People Kissing)
⠀(Words)
⠀(Complex)
⠀(Stifling Laughter)
⠀(Tears)
⠀(Waving arms)
⠀(Big Wide Open Mouths)
⠀(Little Hands)
⠀(Words and Sounds)
⠀(ਊ Style Mouths)
⠀(Simple or Miscellaneous Laughter)
⠀(Complex Forms of Laughter)
⠀(Love Eyes)
⠀(Left Love)
⠀(Right Love)
⠀(Forward Love)
⠀(Shy Love)
⠀(Excited Love)
⠀(Thinking &#8216;Bout Love)
⠀(Kissing Lips)
⠀(Couples)
⠀(Objects of Love)
⠀(Animal Love)
⠀(Complex)
⠀(Love Hurts)
⠀(Words About Love)
⠀(Giant)
⠀(Star Magic)
⠀(Fire Magic)
⠀(Flower Magic)
⠀(Bomb Magic)
⠀(Energy Balls)
⠀(Miscellaneous Magic)
⠀(Shrug Faces)
⠀(Straight Arms)
⠀(┐and ┌ Arms)
⠀(Raised up 90 Degree Arms)
⠀(╮and╭ Style Arms)
⠀(╰ and ╯Style Arms)
⠀(Curved Arms)
⠀(乁 andㄏStyle Arms)
⠀(ƪ and ʃ Style Arms)
⠀(Words)
⠀(Complex)
⠀(Miscellaneous)
⠀(@ Style Ears)
⠀(⊂ Style Ears)
⠀(Ϛ⃘๑•͡ .̫•๑꒜ Style Monkeys)
⠀(Miscellaneous Monkeys)
⠀(Singing)
⠀(Whistling)
⠀(Multiple People Enjoying Music Together)
⠀(Musical Instruments and Devices)
⠀(Regular Emoticons with Musical Notes)
⠀(Miscellaneous)
⠀(┏ and ┓Style Moustaches)
⠀(෴ Style Moustaches)
⠀(Other Moustaches)
⠀(Movember 2014)
⠀(Single Line Nosebleeds)
⠀(Multiple Line Nosebleeds)
⠀(Touching Things)
⠀(The Slow Clap)
⠀(Pointing)
⠀(Movement Related)
⠀(Yelling)
⠀(Farting)
⠀(Blowing)
⠀(Thumbs Up or Down)
⠀(Fanning)
⠀(Peace Signs)
⠀(Various Other Actions)
⠀(Generic Animals with ω Mouths)
⠀(Seals)
⠀(Porcupines)
⠀(Otters)
⠀(Snakes)
⠀(Hedgehogs)
⠀(Llamas or Alpacas)
⠀(Insects)
⠀(Mice and or Rats)
⠀(Cows, Bison, Oxes or Maybe Wildebeests)
⠀(Spiders)
⠀(Buck Tooth Animals)
⠀(Other Miscellaneous Animal-like Emoticons)
⠀(General Miscellaneous)
⠀(No Idea)
⠀(Decorations or Embellishments)
⠀(Multiple Lines)
⠀(Round Snout Holes)
⠀(Infinity Sign Snouts)
⠀(Solid Circle Snouts)
⠀(Miscellaneous Pigs)
⠀(Big Floppy Ears)
⠀(Straight Down Ears)
⠀(Rounded Ears)
⠀(Straight Out Ears)
⠀(No Ears)
⠀(Tiny Rabbits)
⠀(Hopping Rabbits)
⠀(Miscellaneous Rabbits)
⠀(Running with One Arm Up and One Arm Down)
⠀(Running with Arms Out Going for a Hug)
⠀(Running with Arms Up for No Particular Reason)
⠀(Running Away in Fear)
⠀(Lines of Speed)
⠀(Running with Lines Behind)
⠀(Running Because of Reasons)
⠀(Hedgehogs)
⠀(Bears)
⠀(In a Blur)
⠀(Running Back and Forth)
⠀(Running with Large Clouds of Dust Behind)
⠀(Running with Small Clouds of Dust Behind)
⠀(Miscellaneous Running Emoticons)
⠀(Complex Running Emoticons)
⠀(No tears)
⠀(Vertical Tears)
⠀(Flying Tears)
⠀(A Single Tear)
⠀(T Style Tears)
⠀(꒦ິ Style Tears)
⠀(Tears that Freak Me Out)
⠀(Rubbing Eyes)
⠀(Complex)
⠀(Two People)
⠀(Words)
⠀(Crazy and or Broken)
⠀(ω Mouths)
⠀(ε Mouths)
⠀(∀ Mouths)
⠀(Sharp Triangle Mouths)
⠀(Д Mouths)
⠀(Flat Mouths)
⠀(Diamond Mouths)
⠀(益 Mouths)
⠀(Square Mouths)
⠀(X Mouths)
⠀(U Mouths)
⠀(Saluting Bears)
⠀(Miscellaneous Saluting Emoticons)
⠀(Covering Your Eyes and or Face in Fear)
⠀(Big Wide Open Eyes of Fear)
⠀(Scared Д Mouths)
⠀(Surrounded by Fear)
⠀(Running Away in Fear)
⠀(Miscellaneous Fear)
⠀(Words)
⠀(Ꮚ Ꮚ Style Sheep)
⠀({@ @} Style Sheep)
⠀(Oh You&#8230;)
⠀(Blushing Cheeks with an Asterisk)
⠀(Blushing Cheeks with a #)
⠀(Blushing Cheeks with a ๑)
⠀(Flushed Cheeks with Vertical and Sometimes Slightly Diagonal Lines)
⠀(Circles for Cheeks)
⠀(Miscellaneous Cheeks)
⠀(Shy but not Blushing)
⠀(A Drop of Sweat)
⠀(Covering Your Face Because of Shyness)
⠀(Complex Shyness)
⠀(Multiple People Being Shy)
⠀(Shyness and Words)
⠀(Regular Sleeping or Sleepy Kaomojis)
⠀(Laying Down on Your Side)
⠀(Sleeping in an Actual Bed)
⠀(Coffee)
⠀(Stretching)
⠀(Yawning)
⠀(Waking Someone Up)
⠀(Falling Asleep or Waking Up)
⠀(Dreaming, Astral Projection or some other Craziness)
⠀(Words)
⠀(Covering Your Eyes and or Face in Fear)
⠀(Big Wide Open Eyes of Fear)
⠀(Scared Д Mouths)
⠀(Surrounded by Fear)
⠀(Running Away in Fear)
⠀(Miscellaneous Fear)
⠀(Words)
⠀(Ꮚ Ꮚ Style Sheep)
⠀({@ @} Style Sheep)
⠀(Oh You&#8230;)
⠀(Blushing Cheeks with an Asterisk)
⠀(Blushing Cheeks with a #)
⠀(Blushing Cheeks with a ๑)
⠀(Flushed Cheeks with Vertical and Sometimes Slightly Diagonal Lines)
⠀(Circles for Cheeks)
⠀(Miscellaneous Cheeks)
⠀(Shy but not Blushing)
⠀(A Drop of Sweat)
⠀(Covering Your Face Because of Shyness)
⠀(Complex Shyness)
⠀(Multiple People Being Shy)
⠀(Shyness and Words)
⠀(Regular Sleeping or Sleepy Kaomojis)
⠀(Laying Down on Your Side)
⠀(Sleeping in an Actual Bed)
⠀(Coffee)
⠀(Stretching)
⠀(Yawning)
⠀(Waking Someone Up)
⠀(Falling Asleep or Waking Up)
⠀(Dreaming, Astral Projection or some other Craziness)
⠀(Words)
⠀(ヘ Mouths)
⠀(ω Mouths)
⠀(~ Mouths)
⠀(ェ Mouths)
⠀(Flat Mouths)
⠀(Happy Mouths)
⠀(Å Mouths)
⠀(Nose Up)
⠀(Miscellaneous Smugness)
⠀(Complex)
⠀(Catch)
⠀(Ping Pong or Table Tennis)
⠀(Regular Tennis)
⠀(Yoyos)
⠀(Volleyball)
⠀(Bowling)
⠀(Soccer or Football)
⠀(Basketball)
⠀(Swimming)
⠀(Cheerleaders)
⠀(Miscellaneous Activities)
⠀(Square Mouths)
⠀(Д Style Mouths)
⠀(Small Round Mouths)
⠀(Medium Sized Round Mouths)
⠀(Large Round Mouths)
⠀(Miscellaneous Mouths)
⠀(OMG!)
⠀(WOW!)
⠀(Hands of Shock)
⠀(Square Shaped Sunglasses)
⠀(Triangle Shaped Sunglasses)
⠀(Other Shaped Sunglasses)
⠀(Monocles)
⠀(Flipping a Large Table)
⠀(Flipping a Medium Sized Table)
⠀(Flipping a Small Table)
⠀(Flipping Two Tables at Once)
⠀(Flipping Other Tables)
⠀(Hitting People With Tables)
⠀(Putting the Table Back)
⠀(Flipping People)
⠀(Table Flips You!)
⠀(Flipping Words)
⠀(Flipping Other Things)
⠀(Seriously?)
⠀(I See What You Did There)
⠀(Colour Me Intrigued&#8230;)
⠀(Facepalms)
⠀(Thinking Real Hard)
⠀(Thought Bubbles)
⠀(Lost in Thought)
⠀(Some Kind of Style)
⠀(Miscellaneous Thinking Emoticons)
⠀(On Hand up Success Fist)
⠀(One Hand Up Success Fist, Other Direction!)
⠀(Two Hands Up, Double Success Fist!)
⠀(Super Success)
⠀(Waving to the Right)
⠀(Waving to the Left)
⠀(Waving both Hands)
⠀(Waving Forward)
⠀(Waving Back and Forth)
⠀(Multiple People Waving)
⠀(Oh You)
⠀(Forget it!)
⠀(Side Arms)
⠀(Hiding)
⠀(Miscellaneous)
⠀(Dash Winks)
⠀(^ Style Winks)
⠀(ゝStyle Winks)
⠀(Winking Flower Kaomojis With Stars)
⠀(Two People Winking at Someone and Making them Uncomfortable)
⠀(Complex Winking)
⠀(Miscellaneous Winks)
⠀(Hello)
⠀(Goodbye)
⠀(Good Morning)
⠀(Good Evening)
⠀(Good Night)
⠀(Holidays)
⠀(Love Themed)
⠀(Thank You)
⠀(Sorry)
⠀(Nice to Meet You)
⠀(Yes)
⠀(No)
⠀(Miscellaneous)
⠀(Triangle Shaped Worried Mouths)
⠀(Д Style Mouths)
⠀(Squiggly Mouths)
⠀(Crescent Mouths)
⠀(Rhombus Mouths)
⠀(Square Mouths)
⠀(House Shaped Mouths)
⠀(Drops of Sweat)
⠀(Raised Arms)
⠀(Fancy Faces)
⠀(Words)
⠀(Miscellaneous Forms of Worry)
⠀(Complex)
⠀(Writing with a φ)
⠀(Writing with a ψ)
⠀(Writing with a 〆)
⠀(Writing with a ￠)
⠀(Writing with an Actual Pencil)
⠀(Writing with an Actual Hand Holding a Pencil)
⠀(Writing on a Laptop)
⠀(Baka)
⠀(Other Words)
⠀(Miscellaneous)
⠀(Freaky or Bizarre Looking)
⠀(Freaky Eyes)
⠀(Buttmoji)
⠀(Probably NSFW)

ｍ（＿　＿；；ｍ⠀Bowing with m Hands 1
m(_ _)m⠀Bowing with m Hands 2
m(._.)m⠀Bowing with m Hands 3
ｍ（．＿．）ｍ⠀Bowing with m Hands 4
m(￢0￢)m⠀Bowing with m Hands 5
ｍ（｡≧ _ ≦｡）ｍ⠀Bowing with m Hands 6
ｍ(｡≧Д≦｡)ｍ⠀Bowing with m Hands
m(@´ё｀@)m⠀Bowing with m Hands 8
m(*- -*)m⠀Bowing with m Hands 9
(*m＿　_)m⠀Bowing with m Hands 10
m(*-ω-)m⠀Bowing with m Hands 11
m(_ _<m)⠀Bowing with m Hands 12
(m<_ _)m⠀Bowing with m Hands 13
m(_ _<m)三(m<_ _)m⠀Bowing with m Hands 14
( m-ｪ-)m))⠀Bowing with m Hands 15
m(＠´＿｀＠)m⠀Bowing with m Hands 16
m(￣ｰ￣)m⠀Bowing with m Hands 17
m(｡_｡；))m⠀Bowing with m Hands 18
(m。_。)m⠀Bowing with m Hands 19
<<<<(_ _)<><<⠀Bowing with < and > hands 1
＜(。_。)＞⠀Bowing with < and > hands 2
≦(._.)≧⠀Bowing with < and > hands 3
<<<<(￢0￢)<><<⠀Bowing with < and > hands 4
<<<<(．＿．)<><<⠀Bowing with < and > hands 5
<<<<(*- -*)<><<⠀Bowing with < and > hands 6
<<<<(＠´＿｀＠)<><<⠀Bowing with < and > hands 7
<<<<(_ _<<<<(_ _<<<<(_ _)<><<_ _)<><<_ _)<><<⠀Bowing with < and > hands 8
o(_ _)o⠀Bowing with o Hands 1
(o_ _)o ～～～ †⠀Bowing with o Hands 2
(o_ _)o⠀Bowing with o Hands 3
o(´д｀o)⠀Bowing with o Hands 4
o(_ _<o)⠀Bowing with o Hands 5
(o<_ _)o⠀Bowing with o Hands 6
(o。_。)o⠀Bowing with o Hands 7
(o´д｀)o⠀Bowing with o Hands 8
(*o＿　_)o⠀Bowing with o Hands 9
＿|￣|○))　((○|￣|＿⠀Bowing from the Side 1
＿|￣|●))　((●|￣|＿⠀Bowing from the Side 2
＿|￣|●⠀Bowing from the Side 3
＿|￣|○⠀Bowing from the Side 4
○|￣|＿⠀Bowing from the Side 5
●|￣|＿⠀Bowing from the Side 6
_/＼○_⠀Bowing from the Side 7
_/＼●_⠀Bowing from the Side 8
(￣^￣ﾒ)＼(_ _ <)⠀Apologizing with One Hand 1
ヾ(_ _*)⠀Apologizing with One Hand 2
ヾ(_ _。）⠀Apologizing with One Hand 3
(m｡_ _)/⠀Apologizing with One Hand 4
๑•́ㅿ•̀๑) ᔆᵒʳʳᵞ⠀Words 1
･ﾟ･(〃´∩｀p◇SΟЯЯΥ◆q´∩｀〃)･ﾟ･⠀Words 2
･ﾟ･δояяу･ﾟ･(○ﾉдﾉ)⠀Words 3
ʎɹɹoS ʎɹɹos’ɥO ¨●౹౽‥ㆀ⠀Words 4
ヾ((●＞□＜)ﾉ*:..｡o○ＳＯЯЯЧ○o。..:*ヽ(＞□＜●))ﾉｼ⠀Words 5
Ｓ○ЯЯΥ＿φ┃´･ι_ｑ｀ ┃ﾟｏ｡⠀Words 6
ＳΟЯЯΥ＿φ（･益ｑ｡｀)･ﾟ･ｏ｡⠀Words 7
(シ_ _)シ⠀Miscellaneous 1
(ノ_．)ノ⠀Miscellaneous 2
_:(´□`」 ∠):_⠀Miscellaneous 3
（ﾉ´д｀）⠀Miscellaneous 4
( .. )⠀Miscellaneous 5
へ(´д｀へ)⠀Miscellaneous 6
／(* o *／)≡(＼* o *)＼⠀Miscellaneous 7
ʕ •́؈•̀ ₎⠀Famous, Special, or Just Plain Awesome Bears 1
ᶘ ᵒᴥᵒᶅ⠀Famous, Special, or Just Plain Awesome Bears 2
ʕノ•ᴥ•ʔノ ︵ ┻━┻⠀Famous, Special, or Just Plain Awesome Bears 3
ᵔᴥᵔ⠀Famous, Special, or Just Plain Awesome Bears 4
ଘ( ິ•ᆺ⃘• )ິଓ⠀Famous, Special, or Just Plain Awesome Bears 5
ᵋ₍⚬ɷ⚬₎ᵌ⠀Famous, Special, or Just Plain Awesome Bears 6
ˁ̡̡̡∗⁎⃙ ̫⁎⃙ˀ̡̡̡ ̩˳♡⃝⠀Famous, Special, or Just Plain Awesome Bears 7
( ິ•ᆺ⃘• )ິฅ✧⠀Famous, Special, or Just Plain Awesome Bears 8
ต( ິᵒ̴̶̷̤ ﻌ ᵒ̴̶̷̤ )ິ ♬⠀Famous, Special, or Just Plain Awesome Bears 9
ฅ( ̳͒•ಲ• ̳͒)♪⠀Famous, Special, or Just Plain Awesome Bears 10
ᶘ ᵒ㉨ᵒᶅ⠀Famous, Special, or Just Plain Awesome Bears 11
ᶘ ͡°ᴥ͡°ᶅ⠀Famous, Special, or Just Plain Awesome Bears 12
ต( ິᵒ̴̶̷̤́ᆺ⃘ᵒ̴̶̷̤̀ )ິต⠀Famous, Special, or Just Plain Awesome Bears 13
٩ʕ•͡×•ʔ۶⠀ʕ•ᴥ•ʔ Style Bears 1
v.ʕʘ‿ʘʔ.v⠀ʕ•ᴥ•ʔ Style Bears 2
ʔ•̫͡•ʔ⠀ʕ•ᴥ•ʔ Style Bears 3
ʕ·͡ˑ·ཻʔ⠀ʕ•ᴥ•ʔ Style Bears 4
ʕ•͡-•ʔ⠀ʕ•ᴥ•ʔ Style Bears 5
ʕ•̫͡•ʔ♡*:.✧⠀ʕ•ᴥ•ʔ Style Bears 6
ʕ•̫͡•ིʔྀ⠀ʕ•ᴥ•ʔ Style Bears 7
ʕ•͡ɛ•͡ʼʼʔ⠀ʕ•ᴥ•ʔ Style Bears 8
ʕ•͡ω•ʔ⠀ʕ•ᴥ•ʔ Style Bears 9
ʕ•̀ω•́ʔ✧⠀ʕ•ᴥ•ʔ Style Bears 10
ʕ•ӫ̫͡•ʔ⠀ʕ•ᴥ•ʔ Style Bears 11
ʕ•͡દ•ʔ⠀ʕ•ᴥ•ʔ Style Bears 12
ʕʽɞʼʔ⠀ʕ•ᴥ•ʔ Style Bears 13
ʕʘ̅͜ʘ̅ʔ⠀ʕ•ᴥ•ʔ Style Bears 14
ʢٛ•ꇵٛ•ʡ⠀ʕ•ᴥ•ʔ Style Bears 15
ฅʕ•̫͡•ʔฅ⠀ʕ•ᴥ•ʔ Style Bears 16
ʕ•̫͡•ʔ♬✧⠀ʕ•ᴥ•ʔ Style Bears 17
ʕ•ᴥ•ʔ⠀ʕ•ᴥ•ʔ Style Bears 18
ʕ•͡౪•ʔ⠀ʕ•ᴥ•ʔ Style Bears 19
ʕ•͡•ʔ⠀ʕ•ᴥ•ʔ Style Bears 20
ʕ⁰̈●̫⁰̈ʔ⠀ʕ•ᴥ•ʔ Style Bears 21
ʕ•ૅૄ•ʔ⠀ʕ•ᴥ•ʔ Style Bears 22
ʕ⁎̯͡⁎ʔ༄⠀ʕ•ᴥ•ʔ Style Bears 23
ʕ-͏̶̶̶̯͡-ʔ⠀ʕ•ᴥ•ʔ Style Bears 24
ʢ•ꇵ͡•ʡ✩⃛⠀ʕ•ᴥ•ʔ Style Bears 25
ʢ•ꇵ͡•ʡ✩⃛⠀ʕ•ᴥ•ʔ Style Bears 26
ʕ๑◞◟๑ʔ⠀ʕ•ᴥ•ʔ Style Bears 27
✌.ʕʘ‿ʘʔ.✌⠀ʕ•ᴥ•ʔ Style Bears 28
ʕ灬￫ᴥ￩灬ʔ⠀ʕ•ᴥ•ʔ Style Bears 29
ʕ•⍝͡•ʔ⠀ʕ•ᴥ•ʔ Style Bears 30
ʕ ·(エ)· ʔ⠀ʕ•ᴥ•ʔ Style Bears 31
ʕథ౪థʔ⠀ʕ•ᴥ•ʔ Style Bears 32
ʕ￫ᴥ￩ʔ⠀ʕ•ᴥ•ʔ Style Bears 33
ʕ•̫๑͡•ʔ∣ժ̅ʒ∾ෆ⃛⠀ʕ•ᴥ•ʔ Style Bears 34
ʕ•༘͡.•ʔ⠀ʕ•ᴥ•ʔ Style Bears 35
=͟͟͞͞•̫͡•ʔ⠀ʕ•ᴥ•ʔ Style Bears 36
ʕ•̫͡•ʔ⠀ʕ•ᴥ•ʔ Style Bears 37
ʢᵕᴗᵕʡ⠀ʕ•ᴥ•ʔ Style Bears 38
ʕ•̬͡•ʔ⠀ʕ•ᴥ•ʔ Style Bears 39
ʕ•͕͡•ʔ⠀ʕ•ᴥ•ʔ Style Bears 40
ʕ•̫͡•ʔ⠀ʕ•ᴥ•ʔ Style Bears 41
ʕ•͚͡•ʔ⠀ʕ•ᴥ•ʔ Style Bears 42
ʕ•͓͡•ʔ⠀ʕ•ᴥ•ʔ Style Bears 43
ʕ•͈͡•ʔ⠀ʕ•ᴥ•ʔ Style Bears 44
ʕ•̬͡•ʔ⠀ʕ•ᴥ•ʔ Style Bears 45
ʕ•̥͡•ʔ⠀ʕ•ᴥ•ʔ Style Bears 46
ʕ•̠͡•ʔ⠀ʕ•ᴥ•ʔ Style Bears 47
ʕ•̮͡•ʔ⠀ʕ•ᴥ•ʔ Style Bears 48
ʕº̫͡ºʔ⠀ʕ•ᴥ•ʔ Style Bears 49
◟ʕ´∀`ʔ◞⠀ʕ•ᴥ•ʔ Style Bears 50
ʕ　·ᴥ·ʔ⠀ʕ•ᴥ•ʔ Style Bears 51
ʕ·ᴥ·　ʔ⠀ʕ•ᴥ•ʔ Style Bears 52
ʕ*̫͡*ʔ⠀ʕ•ᴥ•ʔ Style Bears 53
˓˓ʕ՚Ջ՝ूɁ॰∘☼⠀ʕ•ᴥ•ʔ Style Bears 54
ʕ•͡દ•ʔ❥ꋧ⠀ʕ•ᴥ•ʔ Style Bears 55
ʕ•͜ ͢ ͞ •ʔ⠀ʕ•ᴥ•ʔ Style Bears 56
ʕ∙ჲ∙ʔ⠀ʕ•ᴥ•ʔ Style Bears 57
ʕっ•ᴥ•ʔっ⠀ʕ•ᴥ•ʔ Style Bears 58
ʕ ∗ •́ ڡ •̀ ∗ ʔ⠀ʕ•ᴥ•ʔ Style Bears 59
୧ʕ ⇀ ⌂ ↼ ʔ୨⠀ʕ•ᴥ•ʔ Style Bears 60
ʕ •̀ o •́ ʔ⠀ʕ•ᴥ•ʔ Style Bears 61
ʕ·͡ᴥ·ʔ⠀ʕ•ᴥ•ʔ Style Bears 62
ʕง•ᴥ•ʔง⠀ʕ•ᴥ•ʔ Style Bears 63
ʕっ˘ڡ˘ςʔ⠀ʕ•ᴥ•ʔ Style Bears 64
ʕ≧㉨≦ʔ⠀ʕ•ᴥ•ʔ Style Bears 65
ʕ　·㉨·ʔ⠀ʕ•ᴥ•ʔ Style Bears 66
ʕ´•㉨•`ʔ⠀ʕ•ᴥ•ʔ Style Bears 67
ʕ•㉨•ʔ⠀ʕ•ᴥ•ʔ Style Bears 68
ʕ￫ᴥ￩　ʔ⠀ʕ•ᴥ•ʔ Style Bears 69
╲ʕ·ᴥ·　╲ʔ⠀ʕ•ᴥ•ʔ Style Bears 70
ʕ； •`ᴥ•´ʔ⠀ʕ•ᴥ•ʔ Style Bears 71
ʕ≧ᴥ≦ʔ⠀ʕ•ᴥ•ʔ Style Bears 72
ʕ♡˙ᴥ˙♡ʔ⠀ʕ•ᴥ•ʔ Style Bears 73
ʕ´•ᴥ•`ʔ⠀ʕ•ᴥ•ʔ Style Bears 74
ʕᴥ• ʔ☝⠀ʕ•ᴥ•ʔ Style Bears 75
ʕ☞ᴥ ☜ʔ⠀ʕ•ᴥ•ʔ Style Bears 76
ʕ╯• ⊱ •╰ʔ⠀ʕ•ᴥ•ʔ Style Bears 77
ʕ/　·ᴥ·ʔ/⠀ʕ•ᴥ•ʔ Style Bears 78
ʕノ)ᴥ(ヾʔ⠀ʕ•ᴥ•ʔ Style Bears 79
ʅʕ•ᴥ•ʔʃ⠀ʕ•ᴥ•ʔ Style Bears 80
ʕ´•ᴥ•`ʔσ”⠀ʕ•ᴥ•ʔ Style Bears 81
ʕ*ﾉᴥﾉʔ⠀ʕ•ᴥ•ʔ Style Bears 82
“φʕ•ᴥ•oʔ⠀ʕ•ᴥ•ʔ Style Bears 83
Σʕﾟᴥﾟﾉʔﾉ⠀ʕ•ᴥ•ʔ Style Bears 84
ʕ ﾟ ● ﾟʔ⠀ʕ•ᴥ•ʔ Style Bears 85
ʕ •ᴥ•ʔ⠀ʕ•ᴥ•ʔ Style Bears 86
ʕᴥ·　ʔ⠀ʕ•ᴥ•ʔ Style Bears 87
ʕ　·ᴥʔ⠀ʕ•ᴥ•ʔ Style Bears 88
ʕ ⊃･ ◡ ･ ʔ⊃⠀ʕ•ᴥ•ʔ Style Bears 89
ʕ ಡ ﹏ ಡ ʔ⠀ʕ•ᴥ•ʔ Style Bears 90
୧ʕ•̀ᴥ•́ʔ୨⠀ʕ•ᴥ•ʔ Style Bears 91
ʕ·ᴥ·ʔ⠀ʕ•ᴥ•ʔ Style Bears 92
ʕº́גº̀ʔ⠀ʕ•ᴥ•ʔ Style Bears 93
ʕ ᵒ̌ ‸ ᵒ̌ ʔ⠀ʕ•ᴥ•ʔ Style Bears 94
ʕ•͡•ʔ⠀ʕ•ᴥ•ʔ Style Bears 95
ʕ ´ ل͜ ´ ʔ⠀ʕ•ᴥ•ʔ Style Bears 96
ʕ – ▃ – ʔ⠀ʕ•ᴥ•ʔ Style Bears 97
ʕ ˵ ̿ ౪ ̿ ˵ ʔ⠀ʕ•ᴥ•ʔ Style Bears 98
ʕ-ᴥ – ʔԅ(`ɛ`ԅ)⠀ʕ•ᴥ•ʔ Style Bears 99
ʕ ” – ∧ – ” ʔ⠀ʕ•ᴥ•ʔ Style Bears 100
ʕ ▀ ਊ ▀ ʔ⠀ʕ•ᴥ•ʔ Style Bears 101
ʕ ▀ ڡ ▀ ʔ⠀ʕ•ᴥ•ʔ Style Bears 102
ʕ ି ڡ ି ʔ⠀ʕ•ᴥ•ʔ Style Bears 103
ʕ ” ￣ Ĺ̯ ￣ ” ʔ⠀ʕ•ᴥ•ʔ Style Bears 104
ʕ ཀ ⌂ ཀ ʔ⠀ʕ•ᴥ•ʔ Style Bears 105
ʕ ☯ ڡ ☯ ʔ⠀ʕ•ᴥ•ʔ Style Bears 106
ʕ ಡ Ĺ̯ ಡ ʔ⠀ʕ•ᴥ•ʔ Style Bears 107
ԅʕ ◖ ᴥ ◗ ʔ୨⠀ʕ•ᴥ•ʔ Style Bears 108
୧ʕ ◕ o ◕ ʔ୨⠀ʕ•ᴥ•ʔ Style Bears 109
ʕ • ₒ • ʔ⠀ʕ•ᴥ•ʔ Style Bears 110
ʕ ˵ ͒ ʖ̯ ͒ ˵ ʔ⠀ʕ•ᴥ•ʔ Style Bears 111
ᕦʕ . ☯ ᴥ ☯ . ʔᕤ⠀ʕ•ᴥ•ʔ Style Bears 112
ʕ”̣̫Ɂ⠀ʕ•ᴥ•ʔ Style Bears 113
ʕ•͡ȅ•ʔ⠀ʕ•ᴥ•ʔ Style Bears 114
ᕦʕ ⊙ ◡ ⊙ ʔᕤ⠀ʕ•ᴥ•ʔ Style Bears 115
୧ʕ ⊚ ͟ل͜ ⊚ ʔ୨⠀ʕ•ᴥ•ʔ Style Bears 116
ʕ ಡ ﹏ ಡ ʔ⊃―{}@{}@{}-⠀ʕ•ᴥ•ʔ Style Bears 117
ʕﾉﾉﾉ؈ㅎʔ⠀ʕ•ᴥ•ʔ Style Bears 118
ʕﾉﾉﾉ_ㅎʔ⠀ʕ•ᴥ•ʔ Style Bears 119
ʕﾉﾉﾉ_ʖʘʔ⠀ʕ•ᴥ•ʔ Style Bears 120
ʕﾉﾉﾉ_ɔㅎʔ⠀ʕ•ᴥ•ʔ Style Bears 121
ʕ╹ヮ╹｡ʔ⠀ʕ•ᴥ•ʔ Style Bears 122
ʕ≧⌄≦｡ʔ⠀ʕ•ᴥ•ʔ Style Bears 123
ʕ๑廿ڡ廿ʔ⠀ʕ•ᴥ•ʔ Style Bears 124
ʕʘʟ_ʘʔ⠀ʕ•ᴥ•ʔ Style Bears 125
ʕ<><<⌓<<<<｡ʔ⠀ʕ•ᴥ•ʔ Style Bears 126
ʕ ◔ᴥ◔ ʔ⠀ʕ•ᴥ•ʔ Style Bears 127
ʕ ␥_␥ʔ⠀ʕ•ᴥ•ʔ Style Bears 128
ʕ ᏫᎲᏫ ʔ⠀ʕ•ᴥ•ʔ Style Bears 129
ʕ ჽ ჟ ჽ ʔ⠀ʕ•ᴥ•ʔ Style Bears 130
ʕ = •́ .̫ •̀ = ʔ⠀ʕ•ᴥ•ʔ Style Bears 131
ʕ ⸋⸛⸋ʔ⠀ʕ•ᴥ•ʔ Style Bears 132
ʕ ᘎ ჟ ᘏ ʔ⠀ʕ•ᴥ•ʔ Style Bears 133
ʕ Ⴔ ჟ Ⴔ ʔ⠀ʕ•ᴥ•ʔ Style Bears 134
ʕ ࿃࿆ _ ࿃࿆ ʔ⠀ʕ•ᴥ•ʔ Style Bears 135
ʕ◉ᴥ◉ʔ⠀ʕ•ᴥ•ʔ Style Bears 136
ʕつ ͡◔ ᴥ ͡◔ʔつ⠀ʕ•ᴥ•ʔ Style Bears 137
ʕ ᓀ ᴥ ᓂ ʔ⠀ʕ•ᴥ•ʔ Style Bears 138
ʕ´• ᴥ •`ʔ⠀ʕ•ᴥ•ʔ Style Bears 139
ʕ◕ ͜ʖ◕ʔ⠀ʕ•ᴥ•ʔ Style Bears 140
ʕ•͓͡•ʔ-̫͡-ʕ•̫͡•ʔ⠀Multiple Bears 1
ʕ·͡ˑ·ཻʔෆ⃛ʕ•̫͡•ོʔ⠀Multiple Bears 2
ʕ͙•̫͑͡•ʔͦʕͮ•̫ͤ͡•ʔ͙⠀Multiple Bears 3
ʕ•̫͡•ʕ•̫͡•ʔ•̫͡•ʔ⠀Multiple Bears 4
ʕ•̼͛͡•ʕ-̺͛͡•ʔ•̮͛͡•ʔ⠀Multiple Bears 5
ʕ•̭͡•ʕ•̯ͦ͡•ʕ•̻̀•́ʔ⠀Multiple Bears 6
ʕ•̫͡•ོʔ•̫͡•ཻʕ•̫͡•ʔ•͓͡•ʔ⠀Multiple Bears 7
ʕ•̫͡•ʔ❣ʕ-̼͡-ʔ⠀Multiple Bears 8
ʕ•̫͡•ʕ*̫͡*ʕ•͓͡•ʔ-̫͡-ʕ•̫͡•ʔ*̫͡*ʔ-̫͡-ʔ⠀Multiple Bears 9
– =͟͟͞͞ʕ•̫͡•ʔ=͟͟͞͞ʕ•̫͡•ʔ=͟͟͞͞ʕ•̫͡•ʔ⠀Multiple Bears 10
ʕ•̫͡•ʕ*̫͡*ʕ•͓͡•ʔ-̫͡-ʕ•̫͡•ʔ*̫͡*ʔ⠀Multiple Bears 11
ʕ·͡ˑ·ཻʔෆ⃛ʕ•̫͡•ོʔ⠀Multiple Bears 12
ʕ•ི̮͡•ྀʕ•̹͡-ʔ•ི̬͡•ྀʔ⠀Multiple Bears 13
ʕ•̼͡•ʕ-̺͡•ʔ•̮͡•ʔ⠀Multiple Bears 14
ʕ•̬͡•ʕ•̫͡•♥⠀Multiple Bears 15
ʕ•̫͡•ིʔྀʕ•̫͡•ིʔྀʕ•̫͡•ིʔྀ⠀Multiple Bears 16
◟ʕ´∀`ʔ◞◟ʕ´∀`ʔ ◞⠀Multiple Bears 17
ʕ•̫͡•ʔ♡ʕ•̫͡•ʔ⠀Multiple Bears 18
ʕ•͡ω•ʔʕ•͡-•ʔ⠀Multiple Bears 19
ʕ•̫͡ʕ•̫͡ʕ•̫͡ʕ•̫͡•ʔ•̫͡•ʔ•̫͡•ʔ•̫͡•ʔ⠀Multiple Bears 20
=͟͟͞͞ʕ•̀=͟͟͞͞ʕ•̀▿•́=͟͟͞͞ʕ•̀▿•́ʔ=͟͟͞͞ʕ•̀▿•⠀Multiple Bears 21
ʕ•̫͡•ʕ*̫͡*ʕ•͓͡•ʔ-̫͡-ʕ•̫͡•ʔ*̫͡*ʔ-̫͡-ʔ⠀Multiple Bears 22
•̫͡•ʔʕ•̫͡•ʕ•̫͡•ʔ•̫͡•ʔ•̫͡•ʕ•̫͡•ʔ•̫͡•⠀Multiple Bears 23
ʕ•̫͡•ʕ̫͡ʕ•͓͡•ʔ-̫͡-ʕ•̫͡•ʔ̫͡ʔ-̫͡-ʔ⠀Multiple Bears 24
ʕ•̫͡•ʕ•̫͡•ʔ•̫͡•ʔ•̫͡•ʕ•̫͡•ʔ•̫͡•ʔ⠀Multiple Bears 25
ʕ･_･ <ʔ≡ʕ< ･_･ʔ⠀Multiple Bears 26
ʕㅎ_ㅎ ʔっ)´ζ｀<ʔ⠀Multiple Bears 27
ʕ•̫͡•ʕ*̫͡*ʕ•͡•ʔ-̫͡-ʕ•̫͡•ʔ*̫͡*ʔ-̫͡-ʔ⠀Multiple Bears 28
ʕ•̫͡•ʔ❤ʕ•̫͡•ʔ⠀Multiple Bears 29
ʕ•̫͡•ʕ•̫͡•ʔ•̫͡•ʔ•̫͡•ʕ•̫͡•ʔ•̫͡•ʕ•̫͡•ʕ•̫͡•ʔ•̫͡•ʔ•̫͡•ʕ•̫͡•ʔ•̫͡•ʔ♡⠀Multiple Bears 30
=͟͟͞͞ʕ•̫͡•ʔ =͟͟͞͞ʕ•̫͡•ʔ =͟͟͞͞ʕ•̫͡•ʔ =͟͟͞͞ʕ•̫͡•ʔ =͟͟͞͞ʕ•̫͡•ʔ⠀Multiple Bears 31
ʕ•̫͡•ʔ →ʕ•̫͡•̫͡•ʔ →ʕ•̫͡•=•̫͡•ʔ →ʕ•̫͡•ʔ ʕ•̫͡•ʔ⠀Multiple Bears 32
ʕ•͕͡•ʔ ʕ•̫͡•ʔ ʕ•͚͡•ʔ ʕ•͓͡•ʔ ʕ•͈͡•ʔ ʕ•̬͡•ʔ ʕ•̥͡•ʔ ʕ•̠͡•ʔ ʕ•̮͡•ʔ⠀Multiple Bears 33
♡ღ‿ღ♡ ʕ•̫͡•ʕ*̫͡*ʕ•͓͡•ʔ-̫͡-ʕ•̫͡•ʔ*̫͡*ʔ-̫͡-ʔ ♡ღ‿ღ♡⠀Multiple Bears 34
ˁ˙˟˙ˀ⠀Tiny Bears 1
ˁ˙͠˟˙ˀ⠀Tiny Bears 2
ˁ˙͡˟˙ˀ⠀Tiny Bears 3
ˁᵒ͡ˑ̉ᵒˀ⠀Tiny Bears 4
ˁ῁̩ˀ⠀Tiny Bears 5
⁽͑˙˚̀Ꮉ˚́˙⁾̉⠀Tiny Bears 6
ˁ῁͓ˀ⠀Tiny Bears 7
ˁ῁̭ˀ⠀Tiny Bears 8
ˁ῁̮ˀ⠀Tiny Bears 9
ˁ῁̱ˀ⠀Tiny Bears 10
ˁ῁̥ˀ⠀Tiny Bears 11
ˁ῁̼ˀ⠀Tiny Bears 12
ˁ῁̩ˀ⠀Tiny Bears 13
ˁ῁̬ˀ⠀Tiny Bears 14
ˁ῁̯ˀ⠀Tiny Bears 15
ˁ῁̰ˀ⠀Tiny Bears 16
“(`(エ)´)ノ⠀エ Style Bears 1
(/-(ｴ)-＼)⠀エ Style Bears 2
(｀(エ)´)ﾉ⠀エ Style Bears 3
(´(エ)｀)⠀エ Style Bears 4
(*￣(ｴ)￣*)⠀エ Style Bears 5
(／(ｴ)＼)⠀エ Style Bears 6
(／￣(ｴ)￣)／⠀エ Style Bears 7
(^(エ)^)⠀エ Style Bears 8
(￣(エ)￣)⠀エ Style Bears 9
(￣(エ)￣)ゞ⠀エ Style Bears 10
(￣(ｴ)￣)ﾉ⠀エ Style Bears 11
(●｀･(ｴ)･´●)⠀エ Style Bears 12
(●￣(ｴ)￣●)⠀エ Style Bears 13
《/(￣(ｴ)￣)ゞ》⠀エ Style Bears 14
＼(・｀(ｪ)・)/⠀エ Style Bears 15
⊂(・(ェ)・)⊃⠀エ Style Bears 16
⊂(^(工)^)⊃⠀エ Style Bears 17
⊂(￣(ｴ)￣)⊃⠀エ Style Bears 18
⊂(￣(工)￣)⊃⠀エ Style Bears 19
⊂(◎(工)◎)⊃⠀エ Style Bears 20
ヾ(T(エ)Tヽ)⠀エ Style Bears 21
ヽ(￣(ｴ)￣)ﾉ⠀エ Style Bears 22
ヾ(´(ｴ)｀ﾉﾞ⠀エ Style Bears 23
Ψ(￣(ｴ)￣)Ψ⠀エ Style Bears 24
┏((＝￣(ｴ)￣=))┛⠀エ Style Bears 25
＼＼\ ٩(`(エ)´ )و //／／⠀エ Style Bears 26
(///◔(ｪ)◔///)⠀エ Style Bears 27
(･(ｪ)･)⠀エ Style Bears 28
(∪￣ ㋓ ￣∪)⠀エ Style Bears 29
(இ(エ)இ｀)⠀エ Style Bears 30
(Θ(ｴ)Θ*)⠀エ Style Bears 31
⊂(▼(工)▼ﾒ)⊃⠀エ Style Bears 32
(<ﾟ(ｴ)ﾟ)⠀エ Style Bears 33
＿〆ヾ(￣(エ)￣)⠀エ Style Bears 34
|](ｴ)￣)⠀エ Style Bears 35
( <-(ｴ)-)ゞ⠀エ Style Bears 36
( -(ｴ)-)ゞ⠀エ Style Bears 37
┐(´(エ)｀)┌⠀エ Style Bears 38
∑(＿(工)＿<)⠀エ Style Bears 39
(●￣(ｴ)￣●)ゞ⠀エ Style Bears 40
|ｴ)･)⊃⠀エ Style Bears 41
┳┳ヾ(T(エ)Tヽ)⠀エ Style Bears 42
〔´（エ）｀〕⠀エ Style Bears 43
( ´ﾉ(ｴ)｀)´(ｴ)｀)⠀エ Style Bears 44
(´･(ｪ)･｀)⠀エ Style Bears 45
（＊￣（エ）￣）ノ⠀エ Style Bears 46
(*ゝ(ェ)･)ﾉ.｡o○⠀エ Style Bears 47
⊂(*’(ェ)’)⊃⠀エ Style Bears 48
(｡ﾉ･(ｴ)･｡)ﾉ⠀エ Style Bears 49
┣o(￣(エ)￣o )≡(/￣(エ)￣)/┳┳⠀エ Style Bears 50
(/￣(ｴ)￣)/ ⌒ ○┼<<<<⠀エ Style Bears 51
(=(=(=(=(=(／(ｴ)￣)／⠀エ Style Bears 52
|￣(ｴ)￣) |(ｴ)￣) |￣) |⠀エ Style Bears 53
,,,,,,,,((*￣(ｴ)￣)ﾉ ⌒☆ o*＿(x)_)⠀エ Style Bears 54
ヾ(ﾟﾛﾟ((≡◯≠≠(￣(ｪ)￣ )⠀エ Style Bears 55
ε-(￣(ｴ)￣*)/ ⌒<><<ﾟ)##)彡⠀エ Style Bears 56
<<<<(￣(エ)￣<))((<￣(エ)￣)ゞ⠀エ Style Bears 57
。゜（゜＾ェ＾゜）゜。⠀エ Style Bears 58
∑(<￣(ｴ)￣)o/￣￣￣￣￣￣~ ゞ●)))彡⠀エ Style Bears 59
<><<<<<<(((( ﾟ<<<<~￣￣￣＼o(￣(ｴ)￣)o/￣￣￣~<><<ﾟ ))))<><<<<<<⠀エ Style Bears 60
<><<ﾟ<)))彡=3=3=3=3 ＼(￣(ｴ)￣＼))⠀エ Style Bears 61
†┏┛墓┗┓† ~((～~~(m￣(ｴ)￣)m⠀エ Style Bears 62
⊂(ﾉ￣￣￣(工)￣￣￣)⊃ﾉ~~~~~━━━┻━━┻━━━⠀エ Style Bears 63
♪(*￣(ｴ)￣)o/￣￣￣￣￣￣~ <><<ﾟ )))<><<彡⠀エ Style Bears 64
(“￣(ｴ)￣)o/￣￣￣￣~<><<ﾟ )++++<<<<<<<<⠀エ Style Bears 65
,,,((／￣(ｴ)￣)／ ε=ε=ε=ε=ミ(((<ﾟ<<<<⠀エ Style Bears 66
☆｡､::｡.::･’ﾟ＼＼￣(ｴ)￣)♪c<ap c<ap♪(￣(ｴ)￣／／ﾟ’･::.｡::､｡☆⠀エ Style Bears 67
ヽ(￣(エ)￣(￣(エ)￣⊂(●￣(エ)￣●)⊃￣(エ)￣)￣(エ)￣)ﾉ⠀エ Style Bears 68
⊂(ﾉ-(工)-)⊃ﾉ 中☆(o_ _)o ．ｚＺ⠀エ Style Bears 69
(*｀ェ(*｀ェ(*｀ェ(*`ェ´*)ェ´*)ェ´*)ェ´*)⠀エ Style Bears 70
(✪㉨✪)⠀㉨ or ᄌ Style Bears 1
(ó㉨ò)⠀㉨ or ᄌ Style Bears 2
・㉨・⠀㉨ or ᄌ Style Bears 3
(♥ó㉨ò)ﾉ♡⠀㉨ or ᄌ Style Bears 4
ヾ(<￫㉨￩)ﾉ⠀㉨ or ᄌ Style Bears 5
⊂(ο･㉨･ο)⊃⠀㉨ or ᄌ Style Bears 6
✧(๑•́ᄌ⃝ก̀๑)⋆*ೃ:.⠀㉨ or ᄌ Style Bears 7
(๑･㉨･๑)⠀㉨ or ᄌ Style Bears 8
(๏㉨๏)⠀㉨ or ᄌ Style Bears 9
(♥ó㉨ò)ノ⠀㉨ or ᄌ Style Bears 10
ヾ(♥ó㉨ò)ﾉ⠀㉨ or ᄌ Style Bears 11
(´ᄌ⃝`๑)⠀㉨ or ᄌ Style Bears 12
(❝᷁ॕᄌ❝᷁ॕ)⠀㉨ or ᄌ Style Bears 13
(ó㉨ò)ﾉ♡⠀㉨ or ᄌ Style Bears 14
ヾ(๑￫ˇ㉨￩)ノ⠀㉨ or ᄌ Style Bears 15
⊂(ο･㉨･ο）⊃⠀㉨ or ᄌ Style Bears 16
(人´㉨｀)♡⠀㉨ or ᄌ Style Bears 17
[｡◉㉨◉]⠀㉨ or ᄌ Style Bears 18
ლ(❤◕㉨◕❤ლ⠀㉨ or ᄌ Style Bears 19
(人･㉨･)♡⠀㉨ or ᄌ Style Bears 20
( ͒•ㅈ• ͒)⠀㉨ or ᄌ Style Bears 21
( ᵌ ㅊ ᵌ )⠀㉨ or ᄌ Style Bears 22
(੭ ◕㉨◕)੭ =͟͟͞͞=͟͟͞͞三❆)’дº)<,<#8217<:=͟͟͞͞⠀㉨ or ᄌ Style Bears 23
=ﾟ*｡:ﾟ+Hi>h(￫㉨￩)ﾊ(￫㉨￩)Five!+ﾟ*｡:ﾟ+⠀㉨ or ᄌ Style Bears 24
⁝⁞⁝⁞ʕु•̫͡•ʔु☂⁝⁞⁝⁝⠀ʕु•̫͡•ʔु Style Bears 1
ʕु-̫͡-ʔु”♬⠀ʕु•̫͡•ʔु Style Bears 2
ʕ”̮ुॽु✚⃞ྉ*✲ﾟ*｡⋆⠀ʕु•̫͡•ʔु Style Bears 3
ʕु-̫͡-ʔु”⠀ʕु•̫͡•ʔु Style Bears 4
ʕु•̫͡•ʔु ✧⠀ʕु•̫͡•ʔु Style Bears 5
ʕु•̫͡•ʔु☂⠀ʕु•̫͡•ʔु Style Bears 6
ʕु-̫͡-ʔु”⠀ʕु•̫͡•ʔु Style Bears 7
ʕ•̫͡•ॽु✚⃞ྉ*✲ﾟ*｡⋆⠀ʕु•̫͡•ʔु Style Bears 8
 ʕु•̫͡•ʔुʔ•̫͡•ཻʕʕु•̫͡•ʔु⠀ʕु•̫͡•ʔु Style Bears 9
°◦=͟͟͞͞ʕ̡̢̡ु•̫͡•ʔ̡̢̡ु ☏⠀ʕु•̫͡•ʔु Style Bears 10
(I)^)⠀Miscellaneous Bears 1
( (ﾐ´ω`ﾐ))⠀Miscellaneous Bears 2
(⋈⚭⃛ ⌅⃝⚭⃛)ᕘ⠀Miscellaneous Bears 3
( ´ิ(ꈊ) ´ิ)⠀Miscellaneous Bears 4
૮(ੱꀧੱ ⋆)ა⠀Miscellaneous Bears 5
(･(仝)･)⠀Miscellaneous Bears 6
( ◍•㉦•◍ )⠀Miscellaneous Bears 7
∩(☉⌄⃝☉)∩⠀Miscellaneous Bears 8
｡•ﻌ•｡ฅ ✩⠀Miscellaneous Bears 9
(⚬॔ꀦ॓⚬)⠀Miscellaneous Bears 10
❃ႣᄎႣ❃⠀Miscellaneous Bears 11
ᑦ(⁎ᐡᆺᐡ)ᐣ⠀Miscellaneous Bears 12
తꀧత⠀Miscellaneous Bears 13
╰໒( ͡ຈ ᴥ ຈ͡ )७╯⠀Miscellaneous Bears 14
⪿ ◠﹏◠ ⫀⠀Miscellaneous Bears 15
⊂(●´(Ω)｀●)⊃⠀Miscellaneous Bears 16
(͒ˊ(❢)ˋ)⠀Miscellaneous Bears 17
(｡･ω･｡)⠀Miscellaneous Bears 18
(*ノ・ω・）⠀Miscellaneous Bears 19
川´･ω･`川⠀Miscellaneous Bears 20
(ʘ(∀)ʘ)⠀Miscellaneous Bears 21
（￣(仝)￣）人（￣(仝)￣）人（￣(仝)￣）⠀Miscellaneous Bears 22
ʕ̡̢̡̡̢̡̡̢̡✩˃̶͈̀ ॢ³˂̴`͈ॢʔ̢̡̢̢̡̢̢̡̢♡⃛⠀Complex Bears 1
ʕ̡̢̡̡̢̡̡̢♡ᵒ̴̷͈艸ᵒ̴̷͈॰ʔ̢̡̢̢̡̢̢̡̢✧⠀Complex Bears 2
✧ʕ̢̣̣̣̣̩̩̩̩·͡˔·ོɁ̡̣̣̣̣̩̩̩̩✧⠀Complex Bears 3
ʕ ⁎❛ั ुꈊ͒ੁ❛ั ु)⠀Complex Bears 4
ʕ̡̢̡*✪௰✪ૢʔ̢̡̢⠀Complex Bears 5
ʕ̡̢̡ॢ•̫͡ॢ•ʔ̢̡̢⠀Complex Bears 6
˞͛ʕ̡̢̡๑꒪͒ꇴ꒪͒๑ʔ̢̡̢˞͛⠀Complex Bears 7
˞͛ʕ̡̢̡◌･ꄃ･◌ʔ̢̡̢˞͛⠀Complex Bears 8
˞͛ʕ̡̢̡⚭◞₀͒◟⚭̀ʔ̢̡̢˞͛⠀Complex Bears 9
ʕ̡̢̡ʘ̅͟͜͡ʘ̲̅ʔ̢̡̢⠀Complex Bears 10
˞͛ʕ̡̢̡,,Ծ‸Ծ,, ʔ̢̡̢˞͛⠀Complex Bears 11
˞͛ʕ̡̢̡ ͡͝ ືྀ͋ ◡ु ͡͝ ືི͋ ʔ̢̡̢˞͛⠀Complex Bears 12
ৎ｡ ॄཻ͡⁎̥̥̥̥̥̥ૂॽ⠀Complex Bears 13
ৎ⁎́ ॄཻ͡⁎̀ूॽ྆྆⠀Complex Bears 14
✧.*◌̗·͡˔·ོᵔ̩̩͔·͡˔·◌̖*·✧⠀Complex Bears 15
ৎˊ̣̣̣࿄ˋ̣̣ूॽ ༘ؓ ँั๊ྃ⠀Complex Bears 16
ৎ•ु·̫•ूॽ⠀Complex Bears 17
o͡͡͡╮ʕ ¯͒ ~ ¯͒ ʔ╭o͡͡͡⠀Complex Bears 18
ʕ ㅎ.̸̸̸̸̸̸̸̸̸̸̸̸̸̸̸̸̸̸̸̸̸̸̸̸̨̨̨̨̨̨̨̨̨̨̨̨.̸̸̨̨ㅎʔ⠀Complex Bears 19
ก็็็็็็็็็็็็็ʕ•͡ᴥ•ʔ ก้้้้้้้้้้้⠀Complex Bears 20
˓ٛ˃̵̢̡̢ˊ͈ˣੰॢˋ͈ॢٛٛ˂̵̡̢̡༿˒˒৳ɦ੨৸кઽ❣༚˚·° ஐ｡✼⠀Complex Bears 21
꒰♥︎꒱ઽᵘᵏⁱ♡ৎˊ͈ˣੰૢˋ͈ॢॽ∗｡⠀Complex Bears 22
（・⊝・）⠀Rounded Beaks 1
（・⊝・∞）⠀Rounded Beaks 2
（`･⊝･´ ）⠀Rounded Beaks 3
(`･⊝･´)⠀Rounded Beaks 4
(｀Θ´)⠀Rounded Beaks 5
（・θ・）⠀Rounded Beaks 6
(◉Θ◉)⠀Rounded Beaks 7
(•ө•)⠀Rounded Beaks 8
(｡･ө･｡)⠀Rounded Beaks 9
(￣･Θ･￣)⠀Rounded Beaks 10
♩є(･Θ･｡)э⠀Rounded Beaks 11
ㄟ( ･ө･ )ㄏ⠀Rounded Beaks 12
є(･Θ･｡)э››⠀Rounded Beaks 13
_:(‘Θ’ 」 ∠):_⠀Rounded Beaks 14
ლ(⁰⊖⁰ლ)⠀Rounded Beaks 15
ლ(◉◞⊖◟◉｀ლ)⠀Rounded Beaks 16
( ˙Θ˙(˙Θ˙)˙Θ˙ )⠀Rounded Beaks 17
（´◉◞⊖◟◉｀）⠀Rounded Beaks 18
( ˘⊖˘)⠀Rounded Beaks 19
⋛⋋( ‘Θ’)⋌⋚⠀Rounded Beaks 20
(･Θ･)⠀Rounded Beaks 21
ϵ( ‘Θ’ )϶⠀Rounded Beaks 22
(･Θ･<)⠀Rounded Beaks 23
(⁽ؔ˙⁾⊝⁽ؔ˙⁾)⠀Rounded Beaks 24
（´≝◞⊖◟≝｀)⠀Rounded Beaks 25
o(｀Θ´)○⠀Rounded Beaks 26
⋋(‘Θ’◍)⋌ :.。✯*⠀Rounded Beaks 27
(⁎′ꃪ‵)˞ᵋᵌ⠀Rounded Beaks 28
(´◉◞⊖◟◉｀)⠀Rounded Beaks 29
ヾ(ﾟΘﾟ )ヾ⠀Rounded Beaks 30
░ฺ|◕ฺΘ◕ฺ)ノ⠀Rounded Beaks 31
 ∧( ‘Θ’ )∧⠀Rounded Beaks 32
(✿´◉◞⊖◟◉｀✿)⠀Rounded Beaks 33
( ⌒⃘ ◞⊖◟ ⌒⃘ )⠀Rounded Beaks 34
⋋(◍’Θ’◍)⋌⠀Rounded Beaks 35
(＋Θ＋)⠀Rounded Beaks 36
⋋(◍’Θ’◍)⋌⠀Rounded Beaks 37
|⁰⊖⁰)⠀Rounded Beaks 38
|⁰⊖⁰) |⊖⁰) |)⠀Rounded Beaks 39
ꉂꆭ(☼⃝◞⊖◟☼⃝ )⠀Rounded Beaks 40
( ‘Θ’)ﾉ⠀Rounded Beaks 41
(o｀Θ´)o⠀Rounded Beaks 42
o(｀Θ´o)⠀Rounded Beaks 43
(•ө•)♡⠀Rounded Beaks 44
(　＾Θ＾)⠀Rounded Beaks 45
♪( ‘Θ’)ﾉ~☆⠀Rounded Beaks 46
(∞ ❛ั ⊝❛ั )⠀Rounded Beaks 47
( ･⊝･∞)⠀Rounded Beaks 48
⊹⋛⋋(◐⊝◑)⋌⋚⊹⠀Rounded Beaks 49
(°<<<<°)⠀Sharp Beaks 1
◎▼◎⠀Sharp Beaks 2
(⁰▿⁰三⁰▿⁰ ‧̣̥̇)⠀Sharp Beaks 3
o(ŎㅿŎ o≡o ŎㅿŎ)o⠀Sharp Beaks 4
ヾ(*ㅿ*๑)ﾂ⠀Sharp Beaks 5
ヾ(๑ ³ㅿ³)ﾉ⠀Sharp Beaks 6
（ꉺ▿ꉺ）⠀Sharp Beaks 7
[●▲●]⠀Sharp Beaks 8
(๑ŏ⋖⋗ŏ)⠀Sharp Beaks 9
(•͈⌔•͈⑅)⠀Sharp Beaks 10
⚈̤꒫⚈̤⠀Sharp Beaks 11
(∘❛ั⌔❛ั∘)⠀Sharp Beaks 12
๏ ⌔̮ ๏⠀Sharp Beaks 13
⋆ඹ͈⌔ඹ͈⋆⠀Sharp Beaks 14
(○∇○)⠀Sharp Beaks 15
(ؔᶿ̷⌔ؔᶿ̷)⠀Sharp Beaks 16
(ඔ⸝⍢⸜ඔ)⠀Sharp Beaks 17
(০▿০)⠀Sharp Beaks 18
(⑅⚈᷀᷁⌔⚈᷀᷁⑅)⠀Sharp Beaks 19
(⑅´•⌔•`)*✲ﾟ*｡⠀Sharp Beaks 20
(๑☌▽☌๑)⠀Sharp Beaks 21
ತ ⌔̫ ತ⠀Sharp Beaks 22
छੂ▵छੂ⠀Sharp Beaks 23
⋋( ◕ ∧ ◕ )⋌⠀Sharp Beaks 24
♫.(◕∠◕).♫⠀Sharp Beaks 25
⊚▿⊚⠀Sharp Beaks 26
❑▿❒⠀Sharp Beaks 27
⋋║ ՞ ▽ ՞ ║⋌⠀Sharp Beaks 28
乁[ᓀ˵▾˵ᓂ]ㄏ⠀Sharp Beaks 29
ミ◕ฺｖ◕ฺ彡⠀Sharp Beaks 30
ლ(ʘ▽ʘ)ლ⠀Sharp Beaks 31
ヽ(○･▽･○)ﾉﾞ⠀Sharp Beaks 32
(*◎ｖ◎*)⠀Sharp Beaks 33
| •́ ▾ •̀ |⠀Sharp Beaks 34
〳 ° ▾ ° 〵⠀Sharp Beaks 35
╰༼ ∗ ಡ ▾ ಡ ∗ ༽╯⠀Sharp Beaks 36
♡ඩ⌔ඩ♡⠀Sharp Beaks 37
|▰◕△◕▰|⠀Sharp Beaks 38
(´Ο∇Ο)⠀Sharp Beaks 39
꒪̔⌔̫꒪̕⠀Sharp Beaks 40
（＠◇＠）⠀Diamond Beaks 1
ξ(｡◕ˇ◊ˇ◕｡)ξ⠀Diamond Beaks 2
━=͟͟͞͞(Ŏ◊Ŏ ‧̣̥̇)━⠀Diamond Beaks 3
( ↂ⃝✧⃟ོↂ⃝ )⠀Diamond Beaks 4
(╮ꏿ ◊ ꏿ╭)⠀Diamond Beaks 5
⊚◊⊚⠀Diamond Beaks 6
(•͈◇•͈⑅)⠀Diamond Beaks 7
◎◊◎⠀Diamond Beaks 8
⋋(◍’◊’◍)⋌⠀Diamond Beaks 9
o(｀◇´)○⠀Diamond Beaks 10
⋛⋋( ‘◇’)⋌⋚⠀Diamond Beaks 11
ϵ( ‘◇’ )϶⠀Diamond Beaks 12
♩є(･◇･｡)э⠀Diamond Beaks 13
[ᓀ˵◇˵ᓂ]⠀Diamond Beaks 14
| •́ ◇ •̀ |⠀Diamond Beaks 15
ㄟ( ･◇･ )ㄏ⠀Diamond Beaks 16
(•∋•)⠀Half Rounded Beaks 1
(●∈∋●)⠀Half Rounded Beaks 2
／(￣ ∈∋ ￣)＼⠀Half Rounded Beaks 3
（ﾟ∈ﾟ）⠀Half Rounded Beaks 4
／(#｀ ∈∋ ´)＼⠀Half Rounded Beaks 5
(°∋°)⠀Half Rounded Beaks 6
(°∈°)⠀Half Rounded Beaks 7
o(｀∋´)○⠀Half Rounded Beaks 8
(๑ŏ∈∋ŏ)⠀Half Rounded Beaks 9
♫.(◕∈◕).♫⠀Half Rounded Beaks 10
 ˏ₍•ɞ•₎ˎ⠀Fat Birds? 1
ˎ₍•ʚ•₎ˏ⠀Fat Birds? 2
꜀( ˊ̠˂˃ˋ̠ )꜆⠀Fat Birds? 3
(ฅˊ̱˂˃ˋ̱ฅ)♪⠀Fat Birds? 4
⸜₍๑•⌔•๑ ₎⸝⠀Fat Birds? 5
( ˊ̱˂˃ˋ̱ )⠀Fat Birds? 6
˱(ْ۬ ˂̵ْ۬ )˲⠀Fat Birds? 7
˓˓⸃₍̗⁽ˆ⁰ˆ⁾͕₎͔˒˒⠀Fat Birds? 8
ˏ₍•ɞ•₎ˎˎ₍•ʚ•₎ˏ⠀Fat Birds? 9
˓˓( ˊ̱˂( ˊ̱˂˃ˋ̱ )˒˒⠀Fat Birds? 10
( ˊ̱˂˃ˋ̱ )◞⸜₍ ˍ́˱˲ˍ̀ ₎⸝◟( ˊ̱˂˃ˋ̱ )⠀Fat Birds? 11
♡⃛◟( ˊ̱˂˃ˋ̱ )◞⸜₍ ˍ́˱˲ˍ̀ ₎⸝◟( ˊ̱˂˃ˋ̱ )◞♡⃛⠀Fat Birds? 12
⊹⋛⋋( ՞ਊ ՞)⋌⋚⊹⠀Laughing Birds 1
♡(㋭ ਊ ㋲)♡⠀Laughing Birds 2
ꉂ (๑¯ਊ¯)σ⠀Laughing Birds 3
♫ꉂ (๑¯ਊ¯)σ⠀Laughing Birds 4
(灬㋭ ਊ ㋲灬)⠀Laughing Birds 5
＜(´ ՞)ਊ( ՞ )＞⠀Laughing Birds 6
୯ૃ(⁎⁾̵ ਊ ⁽̵)੭ુ⁼³₌₃⠀Laughing Birds 7
＜●＞ਊ＜●＞⠀Laughing Birds 8
c( ¯ ਊ ¯ )つ⠀Laughing Birds 9
⋋〳 ･ ਊ ･ 〵⋌⠀Laughing Birds 10
┌░ : ◔ ਊ ◔ : ░┐⠀Laughing Birds 11
(ּ⌔̀௰ּ⌔́)⠀Miscellaneous Birds 1
(ꀹʚ ꀹ)⠀Miscellaneous Birds 2
ʚ(ȉˬȉ⁎)ɞ˒˒⠀Miscellaneous Birds 3
ʚ(•”̮•)ɞ⠀Miscellaneous Birds 4
(ʾ̌ˆʿ̌)⠀Miscellaneous Birds 5
ε(*´･∀･)з⠀Miscellaneous Birds 6
˳⚆ɞ⚆˳⠀Miscellaneous Birds 7
గ౬గ⠀Miscellaneous Birds 8
(∙⃘˱̵˲̵•)⠀Miscellaneous Birds 9
ପ(⚈᷉ʙ⚈᷉)੭̸୫൦⃛⠀Miscellaneous Birds 10
മ്റ്മ്⠀Miscellaneous Birds 11
(⌯⚈ै೧̇⚈ै)⠀Miscellaneous Birds 12
⋋╏ ❛ ◡ ❛ ╏⋌⠀Miscellaneous Birds 13
◞(○⊱○)◟⠀Miscellaneous Birds 14
ε(*´･∀･｀)зﾞ⠀Miscellaneous Birds 15
<<<<（ё）<><<⠀Miscellaneous Birds 16
˂⁽ˈ₍ ⁾˲₎₌⠀Miscellaneous Birds 17
~~……ヾლ∩з…….~~⠀Miscellaneous Birds 18
/|\( <,<)/|\⠀Bats 1
^v^(<,,<)^v^⠀Bats 2
/|^<-<^/|⠀Bats 3
(^+.+^)⠀Bats 4
^v^⠀Bats 5
/|\( <,< )/|\⠀Bats 6
（ΦωΦ）⠀Cats with Anime Eyes 1
((ΦωΦ))⠀Cats with Anime Eyes 2
(*ΦωΦ*)⠀Cats with Anime Eyes 3
(=ΦｴΦ=)⠀Cats with Anime Eyes 4
(ΦωΦ)⠀Cats with Anime Eyes 5
(ΦзΦ)⠀Cats with Anime Eyes 6
(Ф∀Ф)⠀Cats with Anime Eyes 7
(ФДФ)⠀Cats with Anime Eyes 8
（三ФÅФ三）⠀Cats with Anime Eyes 9
<<<<(*ΦωΦ*)<><<⠀Cats with Anime Eyes 10
|ΦωΦ|⠀Cats with Anime Eyes 11
ヾ(*ΦωΦ)ﾉ⠀Cats with Anime Eyes 12
٩(ↀДↀ)۶⠀Cats with Anime Eyes 13
(ↀДↀ)✧⠀Cats with Anime Eyes 14
(ↀДↀ)⠀Cats with Anime Eyes 15
(ↀДↀ)⁼³₌₃⠀Cats with Anime Eyes 16
(=ↀωↀ=)✧⠀Cats with Anime Eyes 17
(๑ↀᆺↀ๑)✧⠀Cats with Anime Eyes 18
(=ↀωↀ=)⠀Cats with Anime Eyes 19
(●ↀωↀ●)⠀Cats with Anime Eyes 20
(๑ↀᆺↀ๑)⠀Cats with Anime Eyes 21
ლ(=ↀωↀ=)ლ⠀Cats with Anime Eyes 22
ლ(●ↀωↀ●)ლ⠀Cats with Anime Eyes 23
^ↀᴥↀ^⠀Cats with Anime Eyes 24
～((Φ◇Φ)‡⠀Cats with Anime Eyes 25
ヽ(ΦωΦヽ)⠀Cats with Anime Eyes 26
(ﾉΦωΦ)ﾉ⠀Cats with Anime Eyes 27
(ΦωΦσ)σ⠀Cats with Anime Eyes 28
]*ΦωΦ)ノ⠀Cats with Anime Eyes 29
(*Φ皿Φ*)⠀Cats with Anime Eyes 30
（ФоФ)⠀Cats with Anime Eyes 31
(=ΦÅΦ=)⠀Cats with Anime Eyes 32
ฅ(*ΦωΦ*) ฅ⠀Cats with Anime Eyes 33
(ﾉ*ФωФ)ﾉ⠀Cats with Anime Eyes 34
(^-人-^)⠀Simple Cat Kaomojis 1
(^・ω・^ )⠀Simple Cat Kaomojis 2
(=<ェ<=)⠀Simple Cat Kaomojis 3
(=^-ω-^=)⠀Simple Cat Kaomojis 4
(=^･ω･^)y＝⠀Simple Cat Kaomojis 5
~(=^‥^)_旦~⠀Simple Cat Kaomojis 6
ヽ(^‥^=ゞ)⠀Simple Cat Kaomojis 7
b(=^‥^=)o⠀Simple Cat Kaomojis 8
=＾● ⋏ ●＾=⠀Simple Cat Kaomojis 9
｡＾･ｪ･＾｡⠀Simple Cat Kaomojis 10
( ^..^)ﾉ⠀Simple Cat Kaomojis 11
(・∀・)⠀Simple Cat Kaomojis 12
(.=^・ェ・^=)⠀Simple Cat Kaomojis 13
((≡^⚲͜^≡))⠀Simple Cat Kaomojis 14
(^･o･^)ﾉ”⠀Simple Cat Kaomojis 15
(^._.^)ﾉ⠀Simple Cat Kaomojis 16
(^人^)⠀Simple Cat Kaomojis 17
(=；ェ；=)⠀Simple Cat Kaomojis 18
(=｀ω´=)⠀Simple Cat Kaomojis 19
(=｀ェ´=)⠀Simple Cat Kaomojis 20
（=´∇｀=）⠀Simple Cat Kaomojis 21
(=^･^=)⠀Simple Cat Kaomojis 22
(=^･ｪ･^=)⠀Simple Cat Kaomojis 23
(=^‥^=)⠀Simple Cat Kaomojis 24
(=ＴェＴ=)⠀Simple Cat Kaomojis 25
(=ｘェｘ=)⠀Simple Cat Kaomojis 26
＼(=^‥^)/’`⠀Simple Cat Kaomojis 27
~(=^‥^)/⠀Simple Cat Kaomojis 28
└(=^‥^=)┐⠀Simple Cat Kaomojis 29
ヾ(=ﾟ･ﾟ=)ﾉ⠀Simple Cat Kaomojis 30
ヽ(=^･ω･^=)丿⠀Simple Cat Kaomojis 31
d(=^･ω･^=)b⠀Simple Cat Kaomojis 32
o(^・x・^)o⠀Simple Cat Kaomojis 33
V(=^･ω･^=)v⠀Simple Cat Kaomojis 34
(⁎˃ᆺ˂)⠀Simple Cat Kaomojis 35
(,,^・⋏・^,,)⠀Simple Cat Kaomojis 36
(ะ^・ω・^ะ)⠀Simple Cat Kaomojis 37
(ะ`・ω・´ะ)⠀Simple Cat Kaomojis 38
ฅ(≚ᄌ≚)⠀Simple Cat Kaomojis 39
(≚ᄌ≚)ƶƵ⠀Simple Cat Kaomojis 40
(≚ᄌ≚)ℒℴѵℯ❤⠀Simple Cat Kaomojis 41
(^･ｪ･^)⠀Simple Cat Kaomojis 42
(^-x-^*)⠀Simple Cat Kaomojis 43
σ((=ﾟｴﾟ=))⠀Simple Cat Kaomojis 44
((≡ﾟ♀ﾟ≡))⠀Simple Cat Kaomojis 45
(=^･ｪ･^=))ﾉ彡☆⠀Simple Cat Kaomojis 46
（（≡￣♀￣≡））⠀Simple Cat Kaomojis 47
~(=^‥^)ノ☆⠀Simple Cat Kaomojis 48
(^･ω･^=)~⠀Simple Cat Kaomojis 49
┌(=^‥^=)┘⠀Simple Cat Kaomojis 50
┌(=^‥^=)┐⠀Simple Cat Kaomojis 51
└(=^‥^=)┘⠀Simple Cat Kaomojis 52
(^･o･^)ﾉ”⠀Simple Cat Kaomojis 53
(=･ｪ･=?⠀Simple Cat Kaomojis 54
ﾍ(^･･^=)~⠀Simple Cat Kaomojis 55
(´pゝω･)⠀Simple Cat Kaomojis 56
ﾍ(=^･ω･^= )ﾉ⠀Simple Cat Kaomojis 57
=^∇^*=⠀Simple Cat Kaomojis 58
~(=^–^)⠀Simple Cat Kaomojis 59
v(=∩_∩=)⠀Simple Cat Kaomojis 60
o(=´∇｀=)o⠀Simple Cat Kaomojis 61
|n＾ω＾|η⠀Simple Cat Kaomojis 62
(o^‥^)o⠀Simple Cat Kaomojis 63
(＾*･.･*＾)⠀Simple Cat Kaomojis 64
~(=^┬ ┬^)⠀Simple Cat Kaomojis 65
o(^・x・^)w⠀Simple Cat Kaomojis 66
ω(=＾・＾=)ω⠀Simple Cat Kaomojis 67
(^=˃ᆺ˂)⠀Simple Cat Kaomojis 68
=( ^<><<w<<<< ^)=⠀Simple Cat Kaomojis 69
( =①ω①=)⠀Fancy Eyed Cats 1
=’①。①’=⠀Fancy Eyed Cats 2
(*✧×✧*)⠀Fancy Eyed Cats 3
(ꀄꀾꀄ)⠀Fancy Eyed Cats 4
(✦థ ｪ థ)⠀Fancy Eyed Cats 5
=ộ⍛ộ=⠀Fancy Eyed Cats 6
(ꅈꇅꅈ)⠀Fancy Eyed Cats 7
ಠಿ ˑ̫ ಠಿ⠀Fancy Eyed Cats 8
ʘ̥ꀾʘ̥⠀Fancy Eyed Cats 9
(⌯⊙⍛⊙)⠀Fancy Eyed Cats 10
චᆽච⠀Fancy Eyed Cats 11
(ꏨ º̖̫º̖̫ ꏨ)⠀Fancy Eyed Cats 12
((≡ຶ⚲͜≡ຶ))⠀Fancy Eyed Cats 13
( ⓛ ω ⓛ *)⠀Fancy Eyed Cats 14
ଲ( ⓛ ω ⓛ *)ଲ⠀Fancy Eyed Cats 15
ὃ⍜ὅ⠀Fancy Eyed Cats 16
(ㅇㅅㅇ❀)⠀Stylish Cats 1
ㅇㅅㅇ⠀Stylish Cats 2
[^._.^]ﾉ彡⠀Stylish Cats 3
โ๏∀๏ใ⠀Stylish Cats 4
⋆ටᆼට⋆⠀Stylish Cats 5
ऴिाी⠀Stylish Cats 6
ि०॰०ॢी⠀Stylish Cats 7
ଲ(⁃̗̀̂❍⃓ˑ̫❍⃓⁃̠́̂)ଲ⠀Stylish Cats 8
=^._.^= ∫⠀Stylish Cats 9
ि०॰͡०ी⠀Stylish Cats 10
=ටᆼට=⠀Stylish Cats 11
ㄱ(ㅇㅅㅇ<#8221< )ㄴ⠀Stylish Cats 12
] ‘͇̂•̩̫’͇̂ ͒)ฅ ﾆｬ❣⠀Fancy Cats 1
(ٛ₌டுͩ ˑ̭ டுͩٛ₌)ฅ⠀Fancy Cats 2
₍˄ุ.͡˳̫.˄ุ₎ฅ˒˒⠀Fancy Cats 3
✩⃛( ͒ ु•·̫• ू ͒)⠀Fancy Cats 4
( ͒ ु- •̫̮ – ू ͒)⠀Fancy Cats 5
ฅ(⌯͒• ɪ •⌯͒)ฅ❣⠀Fancy Cats 6
ฅ⃛(⌯͒꒪ั ˑ̫ ꒪ั ⌯͒) ﾆｬｯ❣⠀Fancy Cats 7
(ٛ⁎꒪̕ॢ ˙̫ ꒪ٛ̕ॢ⁎)⠀Fancy Cats 8
( ͒ ˘̩̩̩̩̩̩ꇵ͒˘̩̩̩̩̩̩ ͒)⠀Fancy Cats 9
ฅ ̂⋒ิ ˑ̫ ⋒ิ ̂ฅ⠀Fancy Cats 10
ฅ( ͒ᵕ̳ωᵕ̳ ͒)｡o○⠀Fancy Cats 11
˚₊✩‧₊(⌯͒o̶̶̷̤ ꀾ o̴̶̷̤⌯͒)* ✩‧₊˚⠀Fancy Cats 12
(⌯͒ᵕɪᵕ⌯͒)zzZ⠀Fancy Cats 13
₍˄⌓⃘ ˳̫̬ ⌓⃘˄₎ค˒˒⠀Fancy Cats 14
✧ٛ˃̶̨̡˙ˣੰ͚˙͚ٛ˂̶̧̢༿˒˒⠀Fancy Cats 15
₍ ̂ˑ̫̈̄ ̂₎⠀Fancy Cats 16
( ‘͇̂•̩̫’͇̂ )ﾆｬ-♡⠀Fancy Cats 17
(ꃋิꎴꃋิ)⠀Fancy Cats 18
(⌯꒪͒ ૢ࿄ ૢ꒪͒)⠀Fancy Cats 19
(ꃪꄳꃪ)⠀Fancy Cats 20
(ٛɲ′᷄ ˑ̣̮ ‵᷅ٛɳ)՞⠀Fancy Cats 21
ʕ⌯˃ꎤु˂⌯ʔ⌕⠀Fancy Cats 22
ᖇ(( ͇ꆨ ꉴ ꉺ ͇))ᖆ≈ᘊ⠀Fancy Cats 23
♡͙♡͚₍⸉ॢ⸍͕͈ ˕̫ ⸌͔͈⸊ॢ₎♡͚♡͙⠀Fancy Cats 24
₍꒵꒱′͈ॢㅈ‵͈ॢ꒰꒵₎*·✧⠀Fancy Cats 25
ฅ(⌯͒•ꈊ͒ू •⌯͒)⠀Fancy Cats 26
( ¤̴̶̷̤́ ‧̫̮ ¤̴̶̷̤̀ )⠀Fancy Cats 27
(⁎ꆤ ̵ູ̫ꆤ)⠀Fancy Cats 28
(˵¯͒࿄¯͒˵)⠀Fancy Cats 29
६  ͇♞͂ۜ ˑ̫♞͂ƫ⍝⠀Fancy Cats 30
ʘ̵ ˤ̵̫ ʘ̵⠀Fancy Cats 31
⁽͑ʺ˚ˠ̫˚ʺ⁾̉⠀Fancy Cats 32
(ꀂǒꀂ)⠀Fancy Cats 33
§ꊘ⃑٥ꊘ⃐§⠀Fancy Cats 34
₍˄·͈༝·͈˄₎◞ ̑̑ෆ⃛⠀Cute Fluffy Kittens 1
₍˄·͈༝·͈˄₎ฅ˒˒⠀Cute Fluffy Kittens 2
(ृ˄·͈༝·͈˄ ृ )⠀Cute Fluffy Kittens 3
(ृʾ́꒳ʿ̀ ृ　)ु⠀Cute Fluffy Kittens 4
₍ᵔ·͈༝·͈ᵔ₎⠀Cute Fluffy Kittens 5
(˙̂·̫ॅ˙̂)⠀Cute Fluffy Kittens 6
꒰⌯͒•ɷ•⌯͒꒱ฅ⠀Cute Fluffy Kittens 7
ৎˊ͈ˣੰૢˋ͈ॢॽ∗｡⠀Cute Fluffy Kittens 8
♡ॢ₍⸍⸌̣ʷ̣̫⸍̣⸌₎⠀Cute Fluffy Kittens 9
˓˓ฅ₍˄ุ.͡ ̫.˄ุ₎ฅ˒˒⠀Cute Fluffy Kittens 10
₍˄·͈༝·͈˄*₎◞ ̑̑⠀Cute Fluffy Kittens 11
|˄·͈༝·͈˄₎.｡oO⠀Cute Fluffy Kittens 12
ฅ^•ﻌ•^ฅ⠀Cats with Paws 1
ฅ⁽͑ ˚̀ ˙̭ ˚́ ⁾̉ฅ⠀Cats with Paws 2
ฅ ̳͒•ˑ̫• ̳͒ฅ♡⠀Cats with Paws 3
ฅ(⌯͒• ɪ •⌯͒)ฅnya～ﾝ❣⠀Cats with Paws 4
˓˓ก₍⸍⸌̣ʷ̣̫⸍̣⸌₎ค˒˒⠀Cats with Paws 5
(ฅ•.•ฅ)⠀Cats with Paws 6
ฅ(*°ω°*ฅ)⠀Cats with Paws 7
◥(ฅº￦ºฅ)◤⠀Cats with Paws 8
(´ฅω•ฅ｀)⠀Cats with Paws 9
ฅ(˘ω˘ )ฅ⠀Cats with Paws 10
ฅ(⌯͒•̩̩̩́ ˑ̫ •̩̩̩̀⌯͒)ฅ⠀Cats with Paws 11
ฅ( ̳͒ᵕ ˑ̫ ᵕ ̳͒)ฅ⠀Cats with Paws 12
ฅ(⌯͒⚭̈́ ˑ̫ ⚭̈́⌯͒)ฅ⠀Cats with Paws 13
❣ฅ(⌯͒▾ ˑ̫ ▾⌯͒)ฅ⠀Cats with Paws 14
ฅ⃛(⌯͒▾ ˑ̫ ▾⌯͒)ฅ⃛⠀Cats with Paws 15
ฅ(三´ ͡ (ェ)´ ͡ 三)ฅ⠀Cats with Paws 16
ฅ(۩۞ω۞۩) ฅ⠀Cats with Paws 17
(ฅ^･ω･^ ฅ)⠀Cats with Paws 18
ฅ(´-ω-`)ฅ⠀Cats with Paws 19
ฅ ̳͒•ˑ̫• ̳͒ฅ⠀Cats with Paws 20
~(=^･ω･^)ﾍ <><<ﾟ)))彡⠀Cats and Fish 1
~(=^･･^)ﾉ<><<ﾟ)##)彡⠀Cats and Fish 2
~(=^･･^)ﾍ <><<ﾟ)))彡⠀Cats and Fish 3
₍˄·͈༝·͈˄*₎◞ ̑̑❤️くコ:≡⠀Cats and Fish 4
₍˄·͈༝·͈˄*₎◞ ̑̑ᗦ↞◃⠀Cats and Fish 5
Zzz(=^–^)｡o○{{ <><<ﾟ)++++<<<<<<<< }}⠀Cats and Fish 6
~(=^･･^)_旦~ (ﾟoﾟ<)⠀Cats Doing Things 1
ｰ8-(^._.^)ﾉ☆( _ _).oO⠀Cats Doing Things 2
~(=^‥^)ﾉ◎～⠀Cats Doing Things 3
┫o(^‥^=)~ ~(=^‥^)o┳⠀Cats Doing Things 4
ε=ε=((( ^-x-^)ﾉ⠀Cats Doing Things 5
ε=ε=ε=ヾ(э^・ｪ・^)э⠀Cats Doing Things 6
0( =^･_･^)=〇⠀Cats Doing Things 7
~(=^･ω･^)ヾ(^^ )⠀Cats Doing Things 8
ヾ(=^・ｪ・^)ヾ(^^ )⠀Cats Doing Things 9
ヾ(=^・・^)ヾ(^^ )⠀Cats Doing Things 10
┏━o(=´∇｀=)o━┓⠀Cats Doing Things 11
目=ﾍ(=^･ω･^)⠀Cats Doing Things 12
~□Pヘ(^‥^=)~⠀Cats Doing Things 13
~(=^‥^)_｡⠀Cats Doing Things 14
~(=^･ω･^)ﾉ◎～⠀Cats Doing Things 15
(*･∀･)／(=^・^=)⠀Cats Doing Things 16
○)))ﾍ(^･･^=)~⠀Cats Doing Things 17
(=^・ω・^)ﾉ＝＝＝Θ☆(＋＿＋)⠀Cats Doing Things 18
~(=^･ω･^)y＝ ‥… *→<ﾟoﾟ)⠀Cats Doing Things 19
♪♪♪ Ｕ・ｪ・Ｕ人(^･x･^=) ♪♪♪⠀Cats Doing Things 20
0( = ฅ^･_･^)= ฅ= ฅ= ฅ ฅ⠀Cats Doing Things 21
‘`ﾛｰヽ(⊡ㅂ⊡｡ Ξ ｡⊡ㅂ⊡)ﾉ ‘`ﾛｰ⠀Giant Cats 1
₍˄·͈༝·͈˄₍˄·͈༝·͈˄( ͒ ु•·̫• ू ͒)˄·͈༝·͈˄₎˄·͈༝·͈˄₎⠀Giant Cats 2
【～～～ヽ(=^‥^=)丿～～～】⠀Giant Cats 3
( ͡ຈ╭͜ʖ╮͡ຈ )⠀The Lenny Face 1
( ͡ಠ ʖ̯ ͡ಠ)⠀The Lenny Face 2
( ͡~ ͜ʖ ͡~)⠀The Lenny Face 3
( ͡~ ͜ʖ ͡°)⠀The Lenny Face 4
( ͠° ͟ʖ ͡°)⠀The Lenny Face 5
( ͡ʘ╭͜ʖ╮͡ʘ)⠀The Lenny Face 6
( ͝סּ ͜ʖ͡סּ)⠀The Lenny Face 7
( ͡ᵔ ͜ʖ ͡ᵔ )⠀The Lenny Face 8
( ͡^ ͜ʖ ͡^ )⠀The Lenny Face 9
[̲̅$̲̅(̲̅ ͡° ͜ʖ ͡°̲̅)̲̅$̲̅]⠀The Lenny Face 10
( ͡ຈ ͜ʖ ͡ຈ)⠀The Lenny Face 11
( ͡° ʖ̯ ͡°)⠀The Lenny Face 12
( ͡ ͜ʖ ͡ )⠀The Lenny Face 13
(☞ ͡° ͜ʖ ͡°)☞⠀The Lenny Face 14
ᕕ( ͡° ͜ʖ ͡° )ᕗ⠀The Lenny Face 15
( ͡° ͜ʖ ͡°)⠀The Lenny Face 16
( ͡°╭͜ʖ╮͡° )⠀The Lenny Face 17
(▀ ͜ʖ ͡°)⠀The Lenny Face 18
(つ ͡° ͜ʖ ͡°)つ⠀The Lenny Face 19
( ͡⚆ ͜ʖ ͡⚆)⠀The Lenny Face 20
¯\_( ͠° ͟ʖ °͠ )_/¯⠀The Lenny Face 21
( ͡° ͜ʖ ( ͡° ͜ʖ ( ͡° ͜ʖ ( ͡° ͜ʖ ͡°) ͜ʖ ͡°)ʖ ͡°)ʖ ͡°)⠀The Lenny Face 22
༼ ºل͟º ༽⠀Raise Your Dongers 1
┌༼ຈل͜ຈ༽┐⠀Raise Your Dongers 2
༼ ಠل͟ಠ༽⠀Raise Your Dongers 3
୧༼ ͡◉ل͜ ͡◉༽୨⠀Raise Your Dongers 4
ヽ༼ ಠ益ಠ ༽ﾉ⠀Raise Your Dongers 5
༼ ༎ຶ ෴ ༎ຶ༽⠀Raise Your Dongers 6
༼ ༏༏ີཻ༾ﾍ ༏༏ີཻ༾༾༽༽⠀Raise Your Dongers 7
༼･ิɷ･ิ༽⠀Raise Your Dongers 8
༼ ͒ ̶ ͒༽⠀Raise Your Dongers 9
༼༼<< <°<ਊ°<༽⠀Raise Your Dongers 10
༼( ⁍ืེ <#8211< ⁍ื༽༽⠀Raise Your Dongers 11
༼•͟ ͜ •༽⠀Raise Your Dongers 12
༼•̃͡ ɷ•̃͡༽⠀Raise Your Dongers 13
༼ ͒ ͓ ͒༽⠀Raise Your Dongers 14
༼༭ຶཬ༤ຶ༽⠀Raise Your Dongers 15
༼ꉺˇɷˇꉺ༽⠀Raise Your Dongers 16
༼இɷஇ༽⠀Raise Your Dongers 17
༼✷ɷ✷༽⠀Raise Your Dongers 18
༼ԾɷԾ༽⠀Raise Your Dongers 19
༼≖ɷ≖༽⠀Raise Your Dongers 20
༼ꉺ✺ꉺ༽⠀Raise Your Dongers 21
༼ꉺლꉺ༽⠀Raise Your Dongers 22
ヽ༼ຈل͜ຈ༽ﾉ⠀Raise Your Dongers 23
༼ꉺ౪ꉺ༽⠀Raise Your Dongers 24
༼ꉺεꉺ༽⠀Raise Your Dongers 25
༼<´༎ຶ ༎ຶ ༽⠀Raise Your Dongers 26
༼⁰o⁰；༽⠀Raise Your Dongers 27
༼(⁽͇ˊ̑⁾ ἴृ ⁽ˋ̑⁾͇)༽⠀Raise Your Dongers 28
˓ ू༼ ்ͦ॔ཀ ்ͦ॓ू༽⠀Raise Your Dongers 29
༼ ु ்ͦ॔ཫ ்ͦ॓༽ु˒˒⠀Raise Your Dongers 30
／༼ ༏༏ີཻ༾ﾍ ༏༏ີཻ༾༾༽༽⠀Raise Your Dongers 31
༼ ்ͦ॔ཫ ்ͦ॓༽⠀Raise Your Dongers 32
༼ᶿ᷇ཫᶿ᷆༽⠀Raise Your Dongers 33
༼  ऀืົཀ  ऀืົ༽⠀Raise Your Dongers 34
༼՟ິͫཀ՟ິͫ༽⠀Raise Your Dongers 35
ˋ̧̧̖⁽⁽༼ ु˳̮̑̈༽ु⁾⁾ˋ̧̧̖♪⠀Raise Your Dongers 36
༼❁ɷ❁༽⠀Raise Your Dongers 37
༼ ຶཽཀ ຶཽ༽⠀Raise Your Dongers 38
ヽ༼၀-၀༽ﾉ⠀Raise Your Dongers 39
༼(❛)㇁(❛)༽⠀Raise Your Dongers 40
ヽ༼⊙_⊙༽ﾉ⠀Raise Your Dongers 41
༼⺤`皿′⺤༽⠀Raise Your Dongers 42
ヽ༼࿃っ࿃༽ﾉ⠀Raise Your Dongers 43
ヽ༼௵ل͜௵༽ﾉ⠀Raise Your Dongers 44
༼ ºل͟º༼ ºل͟º ༽ºل͟º ༽ºل͟º ༽⠀Raise Your Dongers 45
༼つಠ益ಠ༽つ ─=≡ΣO))⠀Raise Your Dongers 46
༼⌐■ل͟■༽⠀Raise Your Dongers 47
༼ง=ಠ益ಠ=༽ง⠀Raise Your Dongers 48
╰༼=ಠਊಠ=༽╯⠀Raise Your Dongers 49
ᕙ༼*◕_◕*༽ᕤ⠀Raise Your Dongers 50
ヽ༼ಢ_ಢ༽ﾉ⠀Raise Your Dongers 51
ヽ༼ ʘ̚ل͜ʘ̚༼◕_◕༽◉_◔ ༽ﾉ⠀Raise Your Dongers 52
┌༼ ⊘ _ ⊘ ༽┐⠀Raise Your Dongers 53
༼ : ౦ ‸ ౦ : ༽⠀Raise Your Dongers 54
༼∗ღ۝ღ∗༽⠀Raise Your Dongers 55
༼ง ͠ຈ ͟ل͜ ͠ຈ༽o:[]:::::::<><<⠀Raise Your Dongers 56
༼ᕗຈل͜ຈ༽ᕗ⠀Raise Your Dongers 57
ヽ༼ຈل͜ರೃ༽ﾉ⠀Raise Your Dongers 58
ヽヽ༼༼ຈຈل͜ل͜ຈຈ༽༽ﾉﾉ⠀Raise Your Dongers 59
༼ ᕤ◕◡◕ ༽ᕤ⠀Raise Your Dongers 60
ᕙ༼˵͠ ͠°ل͜͠ ͠°˵༽ᕗ⠀Raise Your Dongers 61
ᕦ༼::ಥ෴ಠೃ::༽ノ⠀Raise Your Dongers 62
༼ •̀ ں •́ ༽⠀Raise Your Dongers 63
♫ ┌༼ຈل͜ຈ༽┘ ♪⠀Raise Your Dongers 64
༼ ಥل͟ಥ ༽⠀Raise Your Dongers 65
༼ﾉƟ͆ل͜Ɵ͆༽ﾉ⠀Raise Your Dongers 66
༼୨Ɵ͆ل͜Ɵ͆༽୨⠀Raise Your Dongers 67
ヽ༼Ɵ͆ل͜Ɵ͆ヽ༽⠀Raise Your Dongers 68
୧༼Ɵ͆ل͜Ɵ͆୧༽⠀Raise Your Dongers 69
┌༼ຈل͜ຈ༽┘⠀Raise Your Dongers 70
へ༼ ✪ Ĺ̯ ✪ ༽و⠀Raise Your Dongers 71
c༼ ͡° ͜ʖ ͡° ༽⊃⠀Raise Your Dongers 72
༼ ಠ ͟ʖ ಠ ༽⠀Raise Your Dongers 73
୧༼ ” ✖ ‸ ✖ ” ༽୨⠀Raise Your Dongers 74
¯\_༼ᴼل͜ᴼ༽_/¯⠀Raise Your Dongers 75
┏༼ ◉ ╭╮ ◉༽┓⠀Raise Your Dongers 76
ᕕ༼✿•̀︿•́༽ᕗ⠀Raise Your Dongers 77
└༼ •́ ͜ʖ •̀ ༽┘⠀Raise Your Dongers 78
୧༼ ヘ ᗜ ヘ ༽୨⠀Raise Your Dongers 79
༼ ◔ ͜ʖ ◔ ༽⠀Raise Your Dongers 80
╰༼⇀︿⇀༽つ-]═──⠀Raise Your Dongers 81
乁༼☯‿☯✿༽ㄏ⠀Raise Your Dongers 82
ヽ༼<><<ل͜<<<<༽ﾉ⠀Raise Your Dongers 83
ɳ༼ຈل͜ຈ༽ɲ⠀Raise Your Dongers 84
¯\_༼ ି ~ ି ༽_/¯⠀Raise Your Dongers 85
ᕦ༼ ˵ ◯ ਊ ◯ ˵ ༽ᕤ⠀Raise Your Dongers 86
¯\_༼ ಥ ‿ ಥ ༽_/¯⠀Raise Your Dongers 87
༼♥ل͜♥༽⠀Raise Your Dongers 88
Ѱζ༼ᴼل͜ᴼ༽ᶘѰ⠀Raise Your Dongers 89
ζ༼Ɵ͆ل͜Ɵ͆༽ᶘ⠀Raise Your Dongers 90
ᕦ༼ ͡° ͜ ͝° ༽ᕤ⠀Raise Your Dongers 91
ヽ༼ ☭ل͜☭ ༽ﾉ⠀Raise Your Dongers 92
˓˓ ू༼ ⠁⃘ཀ ⠁⃘ू༽⠀Raise Your Dongers 93
༼ ु⠁⃘ཫ ⠁⃘༽ु˒˒⠀Raise Your Dongers 94
ᕕ༼ ͠ຈ Ĺ̯ ͠ຈ ༽┌∩┐⠀Raise Your Dongers 95
⋌༼ •̀ ⌂ •́ ༽⋋⠀Raise Your Dongers 96
└༼ ಥ ᗜ ಥ ༽┘⠀Raise Your Dongers 97
୧༼✿ ͡◕ д ◕͡ ༽୨⠀Raise Your Dongers 98
ᕙ༼=ݓ益ݓ=༽ᕗ⠀Raise Your Dongers 99
༼ ∗ ି ﹏ ି ∗ ༽⠀Raise Your Dongers 100
o͡͡͡╮༼ ʘ̆ ۝ ʘ̆ ༽╭o͡͡͡⠀Raise Your Dongers 101
o͡͡͡╮༼ • ʖ̯ • ༽╭o͡͡͡⠀Raise Your Dongers 102
ヽ༼ຈل͜ຈ༽ﾉ гคเรє ๏г ๔เє ヽ༼ຈل͜ຈ༽ﾉ⠀Raise Your Dongers 103
༼ ºل͟º ༼ ºل͟º ༼ ºل͟º ༽ ºل͟º ༽ ºل͟º ༽⠀Raise Your Dongers 104
༼ ºل͟º༼ ºل͟º( ͡° ͜ʖ ͡°)ºل͟º ༽ºل͟º ༽⠀Raise Your Dongers 105
ヽ༼ ☯‿☯༼ ಠ益ಠ༽◕ل͜◕༽つ⠀Raise Your Dongers 106
S<ru<<in> Leo⠀Other Internet Memes 1
ᕕ(ᐛ)ᕗ⠀Other Internet Memes 2
(•̀ᴗ•́)و ̑̑⠀Other Internet Memes 3
| (•□•) | (❍ᴥ❍ʋ)⠀Other Internet Memes 4
∠( ᐛ 」∠)＿⠀Other Internet Memes 5
(´°ω°`)⠀Other Internet Memes 6
~=[,,_,,]:3⠀Other Internet Memes 7
(￣ｍ￣〃)⠀Other Internet Memes 8
щ(゜ロ゜щ)⠀Other Internet Memes 9
(/_<<<<。)⠀Other Internet Memes 10
( ՞ਊ ՞)☝⠀Other Internet Memes 11
(°ロ°)☝⠀Other Internet Memes 12
φ(ﾟﾛﾟ*)ﾉ⠀Other Internet Memes 13
(ভ_ ভ) ރ ／/ ┊ \＼⠀Other Internet Memes 14
┌( ಠ_ಠ)┘⠀Other Internet Memes 15
(－‸ლ)⠀Other Internet Memes 16
(ლ‸－)(－‸ლ)⠀Other Internet Memes 17
( ﾉ ﾟｰﾟ)ﾉ☀️⠀Other Internet Memes 18
☀️ヽ(ﾟｰﾟヽ)⠀Other Internet Memes 19
Pikachu⠀Pokemon 1
ϞϞ(๑⚈ ․̫ ⚈๑)∩⠀Pokemon 2
Y● ❛ ̫.❛●)´෴ϞϞ⠀Pokemon 3
Ƶƶ(☄￣▵—▵￣)⠀Pokemon 4
ζ,,ﾟДﾟζ⠀Pokemon 5
╭<<<<<<<<◕°ω°◕<><<<><<╮⠀Pokemon 6
╰ᕦ╯( O++O )╰ᕤ╯⠀Pokemon 7
⊹⋛⋋(◐⊝◑)⋌⋚⊹⠀Pokemon 8
<<<<:0OOoo<><<⠀Pokemon 9
卅(•‿•)卅⠀Pokemon 10
卅(◕‿◕)卅⠀Pokemon 11
卅( ͡° ͜ ͡°)卅⠀Pokemon 12
└(oѪo)┘⠀Pokemon 13
♫꒰･‿･๑꒱⠀Simple Clouds 1
꒰✘Д✘◍꒱⠀Simple Clouds 2
٩꒰ಂ❛ ▿❛ಂ꒱۶♡⠀Simple Clouds 3
꒰ *๑•ૅʖ̫•́๑꒱⠀Simple Clouds 4
꒰✩’ω`ૢ✩꒱⠀Simple Clouds 5
٩꒰๑ ´∇`๑꒱۶⠀Simple Clouds 6
꒰｡•`ｪ´•｡꒱۶⠀Simple Clouds 7
꒰๑ ᷄ω ᷅꒱⠀Simple Clouds 8
٩꒰๑• ̫•๑꒱۶♡⠀Simple Clouds 9
꒰(@｀꒳´)꒱⠀Simple Clouds 10
꒰๑•̮̮́౪•̮̮̀๑꒱⠀Simple Clouds 11
٩꒰๑• ³•๑꒱۶⠀Simple Clouds 12
꒰•ི̫͡ુ•ྀૂ꒱⠀Simple Clouds 13
꒰ღ˘‿˘ற꒱❤⃛⠀Simple Clouds 14
٩꒰ɵ̥̥▿ɵ̥̥●꒱۶⠀Simple Clouds 15
꒰˘̩̩̩⌣˘̩̩̩๑꒱♡⠀Simple Clouds 16
٩꒰ ̃•ε• ̃๑꒱۶⁼³₌₃⠀Simple Clouds 17
٩꒰ʘʚʘ๑꒱۶⠀Simple Clouds 18
꒰⌯͒•̩̩̩́ ˑ̫ •̩̩̩̀⌯͒꒱⠀Simple Clouds 19
٩꒰ ´ᆺ`꒱۶⠀Simple Clouds 20
ꉂꉂ꒰•̤▿•̤*ૢ꒱⠀Simple Clouds 21
꒰⌯͒•ɷ•⌯͒꒱⠀Simple Clouds 22
٩꒰ ˘ ³˘꒱۶~♡⠀Simple Clouds 23
꒰⑅ᵕ༚ᵕ꒱˖♡⠀Simple Clouds 24
꒰⑅•ᴗ•⑅꒱⠀Simple Clouds 25
٩꒰｡•‿•｡꒱۶⠀Simple Clouds 26
♡˖꒰ᵕ༚ᵕ⑅꒱⠀Simple Clouds 27
꒰●꒡ ̫ ꒡●꒱⠀Simple Clouds 28
٩꒰• ε •꒱۶⁼³⠀Simple Clouds 29
꒰⁎❛⃘ͫ ⍘⃘ ❛⃘ͫ⁎꒱⠀Simple Clouds 30
꒰•̫͡•ོ꒱⠀Simple Clouds 31
꒰⌯͒•·̫•⌯͒꒱⠀Simple Clouds 32
٩꒰´·⌢•｀꒱۶⁼³₌₃⠀Simple Clouds 33
꒰╬•᷅д•᷄╬꒱⠀Simple Clouds 34
ଽ꒰⌓̈ ॢ꒱ ̉ ̉⠀Simple Clouds 35
꒰⌗´͈ ᵕ ॣ`͈⌗꒱৩⠀Simple Clouds 36
꒰◍ᐡᐤᐡ◍꒱⠀Simple Clouds 37
꒰๑•௰•๑꒱⠀Simple Clouds 38
‘٩꒰｡•◡•｡꒱۶’⠀Simple Clouds 39
ᔪ꒰ ꒪ω꒪ |||꒱⠀Simple Clouds 40
꒰๑˃͈꒳˂͈๑꒱ﾉ*ﾞ̥⠀Simple Clouds 41
꒰´꒳`∗꒱⠀Simple Clouds 42
꒰´꒳`꒱⠀Simple Clouds 43
꒰∗´꒳`꒱⠀Simple Clouds 44
.꒰ϱ﹏-๑꒱‧*Zz｡⠀Simple Clouds 45
꒰⌯͒•̩̩̩́ ᴗ •̩̩̩̀⌯͒꒱⠀Simple Clouds 46
꒰๑•‧̮ૣ•ૣ๑꒱*･.｡⠀Simple Clouds 47
꒰✩˙˟˙✩꒱⠀Simple Clouds 48
*¨*•.¸꒰๑ ᷄ω ᷅꒱⠀Simple Clouds 49
♪.*⁽⁽ ◝꒰´꒳`∗꒱◟ ₎₎₊·*⠀Simple Clouds 50
꒰◍ᐡᐤᐡ◍꒱ᐝ.∗̥✩⁺˚⑅⠀Simple Clouds 51
꒰ ꒪⌑꒪꒱˖ꂚ*ᵎ⠀Simple Clouds 52
∠꒰’౪’꒱✧⠀Simple Clouds 53
꒰ •͈́ ̫ •͈̀ ꒱ˉ̞̭⠀Simple Clouds 54
⁽⁽꒰๑•‧̮ૣ•ૣ๑꒱⁾⁾⠀Simple Clouds 55
꒰๑꒪ɷ꒪꒱⠀Simple Clouds 56
꒰⁎❛⃘ੌ ᵕ ❛⃘ੌ⁎꒱⠀Simple Clouds 57
꒰⁎′̥̥̥ ⌑ ‵̥̥̥ ꒱⠀Simple Clouds 58
˖*٩꒰｡‾᷅⌑‾᷅｡<꒱۶ఽ*.·⠀Simple Clouds 59
꒰๑*´ᗜ`*꒱*›◡‹꒱꒱⠀Simple Clouds 60
*+:꒰◍•ᴗ•◍꒱:+*⠀Simple Clouds 61
꒰｡ › ·̮ ‹ ｡꒱⠀Simple Clouds 62
◟꒰⌳̈ ꒱⠀Simple Clouds 63
꒰๑͒•௰•๑͒꒱ℒℴѵℯ❤⠀Simple Clouds 64
꒰⁎❛⃘ੌ ⍘⃘ ❛⃘ੌ⁎꒱⠀Simple Clouds 65
ｑ꒰*ゝω・꒱ﾉ″⠀Simple Clouds 66
◟꒰∗⌵̈꒱◞✩◟꒰⌔̈∗꒱◞⠀Simple Clouds 67
꒰̤◴ㅈ◴̵̤꒱⠀Simple Clouds 68
꒰⍨꒱⠀Simple Clouds 69
꒰⑅ˊ͈ ˙̫ ˋ͈⑅꒱⠀Simple Clouds 70
꒰✪ૢꇵ✪ૢ꒱ෆ⃛⠀Simple Clouds 71
♫꒰･◡･๑꒱⠀Simple Clouds 72
꒰#’ω`#꒱੭⠀Simple Clouds 73
୧꒰๑͒•͈ꇵ͒•͈๑͒꒱୨ᵎᵎ✧⠀Simple Clouds 74
꒰⑅ᵕ༚ᵕ꒱˖♡ªʳⁱ૭ªᵗ°♡˖꒰ᵕ༚ᵕ⑅꒱⠀Simple Clouds 75
٩꒰ ˘ ³˘꒱۶ⒽⓤⒼ♥♡̷♡̷⠀Simple Clouds 76
˞͛꒰๑ऀ •̆ꈊ͒ू•̆๑ऀ꒱⠀Complex Clouds 1
꒰ ॢö৺ö ૢ๑꒱⠀Complex Clouds 2
꒰･᷄ु௰･᷅ू꒱⠀Complex Clouds 3
꒰｡•ॢ◡-ॢ｡꒱⠀Complex Clouds 4
꒰·͡ुˑ·ཻू꒱ෆ⃛⠀Complex Clouds 5
꒰•ू꒪͒·̫̮꒪͒•ू꒱⠀Complex Clouds 6
꒰♡ˊ͈ ु꒳ ूˋ͈꒱.⑅*♡⠀Complex Clouds 7
꒰๑͒•̀ुꇵ͒•꒱و ̑̑⠀Complex Clouds 8
͛꒰ू ऀ•̥́ꈊ͒ੁ•ૅू॰˳ऀ꒱ ͟͟͞ ̊ ̥ ̥⠀Complex Clouds 9
꒰ू•௰ू•๑꒱⠀Complex Clouds 10
꒰ෆ❛ั ु▿❛ั ु꒱⠀Complex Clouds 11
٩꒰･ัε･ั ꒱۶⠀Complex Clouds 12
٩꒰•௰︡๑꒱ु⠀Complex Clouds 13
ू꒰ꇐωꇐ ू꒱⠀Complex Clouds 14
ପ꒰⑅°͈꒳°͈꒱੭ु⁾⁾⠀Complex Clouds 15
꒰*⑅˃̶͈ ৺˂̶͈⑅꒱੭ु⁾⁾·°⠀Complex Clouds 16
˞͛꒰๑ऀ •̆ꈊ͒ू•̆๑ऀ꒱⁇⠀Complex Clouds 17
꒰๑͒ ु•ꇵ͒•`๑͒꒱⠀Complex Clouds 18
ᵎᵎᵎ꒰ฅ ͒•ૅꇵ͒•⌯͒꒱ฅ⠀Complex Clouds 19
꒰♡˃̶̤́ ॢ꒳ ॢ˂̶̤̀ ꒱·◌*.♡⠀Complex Clouds 20
꒰⁎ᵉ̷͈ ॣ꒵ ॢᵉ̷͈⁎꒱໊⠀Complex Clouds 21
⋆⑅˚₊*୧⃛꒰ɞ̴̶̷◟◞ʚ̴̶̷̷꒱୨⃛*₊˚⠀Complex Clouds 22
✬̴⃛꒰⁍̴ꈊ ॢ⁍̴⌯꒱⠀Complex Clouds 23
꒰•́ॢ৺•̀ॢ๑͒꒱⠀Complex Clouds 24
꒰◍•̤ु௰•̤ु꒱* ∗◌+*♡⠀Complex Clouds 25
ପ꒰*⑅ ॢ˘͈ꀧ˘͈ ॢ⑅꒱✩.*˚⠀Complex Clouds 26
˪৹⌵ೕ꒰๑•‧̮ૣ•ૣ๑꒱⠀Complex Clouds 27
↷꒰ू´•௰ू• `꒱↷⠀Complex Clouds 28
꒰๑⃙⃘ϱ॔꒳˘͈( ˘͈꒳˘͈๑⃙⃘꒱♡⠀Complex Clouds 29
❤︎⁄⁄꒰* ॢꈍ◡ꈍ ॢ꒱.*˚‧⠀Complex Clouds 30
·˚*୨୧꒰∗ɞ̴̶̷ु ·̮ ूɞ̴̶̷∗꒱୨୧*˚·⠀Complex Clouds 31
ू꒰΄ ิ̤۝ ิ ̤꒱ु⠀Complex Clouds 32
꒰ ்ͦੰ ⍘⃘  ்ͦੰ꒱⠀Complex Clouds 33
꒰ ॢ꒱˶´ꇵ͒`˶꒰ ॢ꒱⠀Complex Clouds 34
꒰๑ ̇̅ ॄ ̇̅๑꒱⠀Complex Clouds 35
꒰♡ᵒ̴̶̷ꇵ͒ᵒ̴̶̷♡꒱*ೄ˚⠀Complex Clouds 36
꒰ꄬຶູྀ ॄ ꄬຶູི ꒱⠀Complex Clouds 37
꒰ꄬຶູྀ ॄ ꄬຶູི ꒱ ⃛˚⠀Complex Clouds 38
꒰ ︠ु௰•꒱ु♡⠀Complex Clouds 39
*⋆⑅⃟◌˚꒰ˊૢᵕˋૢෆ꒱⠀Complex Clouds 40
⅀⑈꒰′Ꮌ̮‵꒵꒱՞⠀Complex Clouds 41
*͛꒰ू ऀ•̥́◟◞•ૅू॰˳ऀ꒱ ͟͟͞ ̊ ̥ ̥⠀Complex Clouds 42
꒰♡⌯́ॢ³⌯̀ॢ꒱⠀Complex Clouds 43
꒰ˇ❝͋ꊗ❝͋ˇ꒱ค˒˒⠀Complex Clouds 44
꒰ີ∗ˊ↥ˋ∗ ꒱ີˉ̶̡̭̭⠀Complex Clouds 45
◌ต꒰｡•̤༝•̤｡꒱ต◌⠀Complex Clouds 46
꒰(ू•‧̫•ू )꒱⠀Complex Clouds 47
꒰ ु•̫•̫ ु꒱⠀Complex Clouds 48
꒰੭ु ऀᵒ̴̶̷̤́ꋢᵒ̴̶̷̤̀ ऀ꒱੭ु⁾⁾⠀Complex Clouds 49
♡⃛=͟͟͞͞꒰ˇ❝͋ुꈊ❝͋ुˇ꒱⁼³₌₃⠀Complex Clouds 50
꒰⁎❛⃘ ⍘⃘ ❛⃘⁎꒱⠀Complex Clouds 51
꒰⌯͒ඹ ·̫ ඹ⌯͒꒱⠀Complex Clouds 52
*͛꒰ू ऀ•̥́◟◞•ૅू॰˳ऀ꒱ ͟͟͞ ̊ ̥ ̥⠀Complex Clouds 53
✧.*꒰⁎❝͋॔༶̶❝͋॓⁎ॢ꒱*·✧⠀Complex Clouds 54
꒰⁎˃ ॢꇴ ॢ˂⁎꒱➴ෆ⃛⠀Complex Clouds 55
Σ꒰๑•ॢд •ॢ๑꒱⠀Complex Clouds 56
꒰ ੭ु・ω ・꒱ ੭ु⁾⁾⠀Complex Clouds 57
꒰⁎ ✪̼ ◡ ✪̼` ⁎꒱﹡Տҽҽ վօմ⁎☪*✩⠀Complex Clouds 58
꒰·͡ुˑ·ཻू꒱*̫ෆ๋*̫꒰•ི̫͡ુ•ྀૂ꒱⠀Complex Clouds 59
꒰·͡ुˑ·ཻू꒱*̫ෆ๋*̫꒰•ི̫͡ુ•ྀૂ꒱*̫ෆ๋*̫꒰•̻̀ु•́ू໊꒱*̫ෆ๋*̫꒰•̹͡ु-ོू꒱*̫ෆ๋*̫꒰•̹͡ິु•ິू꒱⠀Complex Clouds 60
(・_・ヾ⠀Head scratching 1
｢(ﾟﾍﾟ)⠀Head scratching 2
(・・。)ゞ⠀Head scratching 3
(｀_´)ゞ⠀Head scratching 4
(´−｀) ﾝｰ⠀Head scratching 5
｡(*^▽^*)ゞ⠀Head scratching 6
(^^ゞ⠀Head scratching 7
(^～^<)ゞ⠀Head scratching 8
(￣(エ)￣)ゞ⠀Head scratching 9
(-_-)ゞ゛⠀Head scratching 10
(＃⌒∇⌒＃)ゞ⠀Head scratching 11
(⌒▽⌒)ゞ⠀Head scratching 12
(●´ω｀●)ゞ⠀Head scratching 13
〈(゜。゜)⠀Head scratching 14
「(°ヘ°)⠀Head scratching 15
く（＾_・）ゝ⠀Head scratching 16
σ(´し_｀〃)ゞ⠀Head scratching 17
δ(´д｀< )⠀Head scratching 18
↷( ó╻ò)⠀Head scratching 19
(≖ლ≖๑ )ﾌ⠀Head scratching 20
(<＾◇＾<)ゝ⠀Head scratching 21
(・∧‐)ゞ⠀Head scratching 22
ଽ (৺ੋ ௦ ৺ੋ )৴⠀Head scratching 23
( <-(ｴ)-)ゞ⠀Head scratching 24
(；´д｀)ゞ⠀Head scratching 25
(≧д≦ヾ)⠀Head scratching 26
｢(ﾟ<<<<ﾟ)ﾞ??⠀Head scratching 27
?(ﾉ)・´ω・(ヾ)⠀Head scratching 28
/(@ﾟﾍﾟ@)⠀Head scratching 29
℃ↂ_ↂ⠀Head scratching 30
∑(O_O；)⠀Head Scratching With a ∑ 1
Σ(‘◉⌓◉’)⠀Head Scratching With a ∑ 2
Σ(-᷅_-᷄๑)⠀Head Scratching With a ∑ 3
Σ(ＴωＴ)⠀Head Scratching With a ∑ 4
Σ(●ꉺ▱ꉺ●)⠀Head Scratching With a ∑ 5
Σ”(⚙♊⚙ﾉ)ﾉ⠀Head Scratching With a ∑ 6
Σ(‘◉⌓◉’)⠀Head Scratching With a ∑ 7
∑（｡･Д･｡）???⠀Head Scratching With a ∑ 8
∑(⌒◇⌒；)⠀Head Scratching With a ∑ 9
Σ(๛д๛)⠀Head Scratching With a ∑ 10
Σ(･ิ¬･ิ)⠀Head Scratching With a ∑ 11
Σ(´д｀<)⠀Head Scratching With a ∑ 12
Σʕﾟᴥﾟﾉʔﾉ⠀Head Scratching With a ∑ 13
Σ(`‐ｪ‐´)⠀Head Scratching With a ∑ 14
Σ(´д ` ﾒ)⠀Head Scratching With a ∑ 15
Σ(・Д・)!?⠀Head Scratching With a ∑ 16
Σ(￣ロ￣<<<)⠀Head Scratching With a ∑ 17
∑(ﾟ台ﾟ<<<⠀Head Scratching With a ∑ 18
Σ(￣□￣<<<)⠀Head Scratching With a ∑ 19
Σ（￣□￣；）⠀Head Scratching With a ∑ 20
Σ(⠀Head Scratching With a ∑ 21
[emai<<#160<pro<ec<ed]⠀Head Scratching With a ∑ 22
)!?⠀Head Scratching With a ∑ 23
Σ(ﾟﾛ､ﾟ<)⠀Head Scratching With a ∑ 24
∑(´ﾟωﾟ｀*)⠀Head Scratching With a ∑ 25
Σ(； ･`д･´)⠀Head Scratching With a ∑ 26
Σ(<･益･<<<)!!!⠀Head Scratching With a ∑ 27
∑（´△｀○）⠀Head Scratching With a ∑ 28
Σ(´△｀Ⅲ)⠀Head Scratching With a ∑ 29
Σ(•’╻’• ۶)۶⠀Head Scratching With a ∑ 30
(•ิ_•ิ)?⠀Blank Look 1
(?・・)σ⠀Blank Look 2
(´･_･`)⠀Blank Look 3
(‘◇’)?⠀Blank Look 4
(゜-゜)⠀Blank Look 5
( ・◇・)？⠀Blank Look 6
(゜。゜)⠀Blank Look 7
(◎_◎<)⠀Blank Look 8
(◎-◎；)⠀Blank Look 9
(●__●)⠀Blank Look 10
(☉_☉)⠀Blank Look 11
(ﾟｰﾟ<)⠀Blank Look 12
【・_・?】⠀Blank Look 13
【・ヘ・?】⠀Blank Look 14
c( O.O )ɔ⠀Blank Look 15
ఠ_ఠ⠀Blank Look 16
(๑ ́ᄇ`๑)⠀Blank Look 17
੨੨(´･･`)⠀Blank Look 18
(꒪ȏ꒪)ｴｯ?⠀Blank Look 19
(ﾒ・ん・)？⠀Blank Look 20
(o*｡_｡)o⠀Blank Look 21
ॽ̥(૦்૦)ˀ̣⠀Blank Look 22
ɾ◉⊆◉ɹ⠀Blank Look 23
(・・？)⠀Blank Look 24
(o゜ー゜o)??⠀Blank Look 25
(ﾟヘﾟ)？⠀Blank Look 26
（・∩・）？⠀Blank Look 27
??r(･x･｡)???⠀Blank Look 28
: ◉ ∧ ◉ : ╏⠀Blank Look 29
σ(゜◆゜<)⠀Blank Look 30
(<゜◆゜)σ⠀Blank Look 31
( ゜Д゜；)！？⠀Blank Look 32
(｡・ω・｡)?⠀Blank Look 33
(｀◎△◎)!?⠀Blank Look 34
(ﾟ▽ﾟ｀*)?⠀Blank Look 35
（＊｀〇Д〇）？⠀Blank Look 36
(*OчO*)⠀Blank Look 37
（*・∧・*）?⠀Blank Look 38
(*。0 – 0。*)？⠀Blank Look 39
（●´・×・｀●）？⠀Blank Look 40
?(ο´･д･)??⠀Blank Look 41
(⊙＿⊙<#8217<)⠀Blank Look 42
٩(͡๏̯͡๏)۶⠀Raised Arms 1
(」・ω・)」⠀Raised Arms 2
(」゜ロ゜)」⠀Raised Arms 3
(」ﾟヘﾟ)」⠀Raised Arms 4
(」ﾟﾛﾟ)｣⠀Raised Arms 5
(❀｣╹□╹)｣*･⠀Raised Arms 6
(」๏้♓๏้)」⠀Raised Arms 7
ι(´Д`ι)⠀Raised Arms 8
( ｣｡╹o╹｡)｣⠀Raised Arms 9
ƪ(•̃͡•̃͡ ƪ⠀Raised Arms 10
(」｡≧□≦)」⠀Raised Arms 11
(」ﾟДﾟ)」⠀Raised Arms 12
(」°ロ°)」⠀Raised Arms 13
ʅฺ(・ω・。)ʃฺ？？⠀Raised Arms 14
(。「´-ω・)ﾝ？⠀Raised Arms 15
(*「･ω･)ﾝ？⠀Raised Arms 16
(屮゜Д゜)屮⠀Raised Hands 1
щ(゜ロ゜щ)⠀Raised Hands 2
щ(ºДºщ)⠀Raised Hands 3
ლ(ಠ_ಠლ)⠀Raised Hands 4
(ლಠ益ಠ)ლ⠀Raised Hands 5
ლ(ٱ٥ٱლ)⠀Raised Hands 6
щ(ﾟдﾟщ)⠀Raised Hands 7
ლ(｡-﹏-｡ ლ)⠀Raised Hands 8
ლ(∘◕‵ƹ′◕ლ)⠀Raised Hands 9
꜡( ˃ ﹆̬ ˂꜡)⠀Raised Hands 10
ლ(<< ิ益 ิ<‘ლ)⠀Raised Hands 11
Щ(º̩̩́Дº̩̩̀щ)⠀Raised Hands 12
ლ(́⚈人⚈‵ლ)⠀Raised Hands 13
щ(▼ﾛ▼щ)⠀Raised Hands 14
щ(´Д｀щ)⠀Raised Hands 15
щ(｀D´#щ)⠀Raised Hands 16
щ(ﾟﾛﾟщ)⠀Raised Hands 17
Щ(◣д◢)艸⠀Raised Hands 18
ლ(ಠ_ಠ ლ）⠀Raised Hands 19
ლ(´Д`ლ)⠀Raised Hands 20
ლ(ಥ Д ಥ )ლ⠀Raised Hands 21
щ(ಥдಥщ)⠀Raised Hands 22
ಠ_ರೃ⠀Quizzical 1
( •᷄ὤ•᷅)？⠀Quizzical 2
(⊙_◎)⠀Quizzical 3
(⊙_☉)⠀Quizzical 4
(⊙.☉)7⠀Quizzical 5
⁀⊙﹏☉⁀⠀Quizzical 6
●.◉⠀Quizzical 7
(｡☉︵ ಠ╬)⠀Quizzical 8
(๑•̌.•̑๑)ˀ̣ˀ̣⠀Quizzical 9
ʕ•ૅૄ•ʔ⠀Quizzical 10
(๑•ૅૄ•๑)⠀Quizzical 11
| ͠° ▃ °͠ |⠀Quizzical 12
( -_・)?⠀Quizzical 13
▐ ˵ ͠° (oo) °͠ ˵ ▐⠀Quizzical 14
(。ヘ°)⠀General Confusion 1
(´｀<) ？⠀General Confusion 2
( ?´_ゝ｀)⠀General Confusion 3
ヾ(´･ ･｀｡)ノ”⠀General Confusion 4
ヽ(゜Q。)ノ？⠀General Confusion 5
?(*´･д･)ﾉ⠀General Confusion 6
(，，ﾟДﾟ)∩⠀General Confusion 7
（（´‐公‐｀））⠀General Confusion 8
<<<<｜＾□＾#｜/⠀General Confusion 9
(￣■￣<)!?⠀General Confusion 10
(<><<囗＜?)⠀General Confusion 11
( ⌡ ຶम⌡ ຶ )⠀General Confusion 12
(๑ಕ̴ _̆ ಕ̴) ﾝ？⠀General Confusion 13
(ﾟДﾟ?)⠀General Confusion 14
?(°Д°≡°Д°)?⠀General Confusion 15
(♠_♦)⠀General Confusion 16
(C_C)⠀General Confusion 17
( ⧉ ⦣ ⧉ )⠀General Confusion 18
¿(❦﹏❦)?⠀General Confusion 19
(<´@へ@｀)⠀General Confusion 20
( ؕؔʘ̥̥̥̥ ه ؔؕʘ̥̥̥̥ )?⠀Complex 1
﴾͡๏̯͡๏﴿⠀Complex 2
`(๑ △ ๑)`*⠀Complex 3
٩(̾●̮̮̃̾•̃̾)۶⠀Complex 4
˞͛꒰๑ऀ •̆ꈊ͒ू•̆๑ऀ꒱⁇⠀Complex 5
( ؔ⚈͟ ◡ ؔ⚈͟ ๑)…ﾝ？⠀Complex 6
»ू(͒ˑ•᷄͡ꇵ͒•᷅͒)ू?!⠀Complex 7
(૦ୂ૦ॢ)ɂ̥Ɂ̥⠀Complex 8
(⸝⸝⸝՞̐ˀ̝՞̐ू)˖̛̠͉⠀Complex 9
⅀(╹╹͞ू)՞✰⁎⠀Complex 10
(•ॢ՞˝̼̮՞)•••Ɂ̥⠀Complex 11
(◕ฺ ▿ฺ ◕ฺ)??⠀Complex 12
ɿ(｡･ɜ･)ɾⓌⓗⓨ？⠀Words 1
ɿ(｡･ɜ･)ɾⓌⓗⓐⓣ？⠀Words 2
(｢๑•₃•)｢ ʷʱʸ?⠀Words 3
(ㆀ˘･з･˘)ωҺaｔ？⠀Words 4
Ⓦⓗⓐⓣ(☉൧ ಠ ꐦ)⠀Words 5
(ㆀ˘･з･˘)ωҺa ƭ？⠀Words 6
Σ(‘Д’⁕)ահɑԵ’Տ up !?⠀Words 7
(」ﾟﾛﾟ)｣NOOOooooo━⠀Words 8
（ΦωΦ）⠀Cats with Anime Eyes 1
((ΦωΦ))⠀Cats with Anime Eyes 2
(*ΦωΦ*)⠀Cats with Anime Eyes 3
(=ΦｴΦ=)⠀Cats with Anime Eyes 4
(ΦωΦ)⠀Cats with Anime Eyes 5
(ΦзΦ)⠀Cats with Anime Eyes 6
(Ф∀Ф)⠀Cats with Anime Eyes 7
(ФДФ)⠀Cats with Anime Eyes 8
（三ФÅФ三）⠀Cats with Anime Eyes 9
<<<<(*ΦωΦ*)<><<⠀Cats with Anime Eyes 10
|ΦωΦ|⠀Cats with Anime Eyes 11
ヾ(*ΦωΦ)ﾉ⠀Cats with Anime Eyes 12
٩(ↀДↀ)۶⠀Cats with Anime Eyes 13
(ↀДↀ)✧⠀Cats with Anime Eyes 14
(ↀДↀ)⠀Cats with Anime Eyes 15
(ↀДↀ)⁼³₌₃⠀Cats with Anime Eyes 16
(=ↀωↀ=)✧⠀Cats with Anime Eyes 17
(๑ↀᆺↀ๑)✧⠀Cats with Anime Eyes 18
(=ↀωↀ=)⠀Cats with Anime Eyes 19
(●ↀωↀ●)⠀Cats with Anime Eyes 20
(๑ↀᆺↀ๑)⠀Cats with Anime Eyes 21
ლ(=ↀωↀ=)ლ⠀Cats with Anime Eyes 22
ლ(●ↀωↀ●)ლ⠀Cats with Anime Eyes 23
^ↀᴥↀ^⠀Cats with Anime Eyes 24
～((Φ◇Φ)‡⠀Cats with Anime Eyes 25
ヽ(ΦωΦヽ)⠀Cats with Anime Eyes 26
(ﾉΦωΦ)ﾉ⠀Cats with Anime Eyes 27
(ΦωΦσ)σ⠀Cats with Anime Eyes 28
]*ΦωΦ)ノ⠀Cats with Anime Eyes 29
(*Φ皿Φ*)⠀Cats with Anime Eyes 30
（ФоФ)⠀Cats with Anime Eyes 31
(=ΦÅΦ=)⠀Cats with Anime Eyes 32
ฅ(*ΦωΦ*) ฅ⠀Cats with Anime Eyes 33
(ﾉ*ФωФ)ﾉ⠀Cats with Anime Eyes 34
(^-人-^)⠀Simple Cat Kaomojis 1
(^・ω・^ )⠀Simple Cat Kaomojis 2
(=<ェ<=)⠀Simple Cat Kaomojis 3
(=^-ω-^=)⠀Simple Cat Kaomojis 4
(=^･ω･^)y＝⠀Simple Cat Kaomojis 5
~(=^‥^)_旦~⠀Simple Cat Kaomojis 6
ヽ(^‥^=ゞ)⠀Simple Cat Kaomojis 7
b(=^‥^=)o⠀Simple Cat Kaomojis 8
=＾● ⋏ ●＾=⠀Simple Cat Kaomojis 9
｡＾･ｪ･＾｡⠀Simple Cat Kaomojis 10
( ^..^)ﾉ⠀Simple Cat Kaomojis 11
(・∀・)⠀Simple Cat Kaomojis 12
(.=^・ェ・^=)⠀Simple Cat Kaomojis 13
((≡^⚲͜^≡))⠀Simple Cat Kaomojis 14
(^･o･^)ﾉ”⠀Simple Cat Kaomojis 15
(^._.^)ﾉ⠀Simple Cat Kaomojis 16
(^人^)⠀Simple Cat Kaomojis 17
(=；ェ；=)⠀Simple Cat Kaomojis 18
(=｀ω´=)⠀Simple Cat Kaomojis 19
(=｀ェ´=)⠀Simple Cat Kaomojis 20
（=´∇｀=）⠀Simple Cat Kaomojis 21
(=^･^=)⠀Simple Cat Kaomojis 22
(=^･ｪ･^=)⠀Simple Cat Kaomojis 23
(=^‥^=)⠀Simple Cat Kaomojis 24
(=ＴェＴ=)⠀Simple Cat Kaomojis 25
(=ｘェｘ=)⠀Simple Cat Kaomojis 26
＼(=^‥^)/’`⠀Simple Cat Kaomojis 27
~(=^‥^)/⠀Simple Cat Kaomojis 28
└(=^‥^=)┐⠀Simple Cat Kaomojis 29
ヾ(=ﾟ･ﾟ=)ﾉ⠀Simple Cat Kaomojis 30
ヽ(=^･ω･^=)丿⠀Simple Cat Kaomojis 31
d(=^･ω･^=)b⠀Simple Cat Kaomojis 32
o(^・x・^)o⠀Simple Cat Kaomojis 33
V(=^･ω･^=)v⠀Simple Cat Kaomojis 34
(⁎˃ᆺ˂)⠀Simple Cat Kaomojis 35
(,,^・⋏・^,,)⠀Simple Cat Kaomojis 36
(ะ^・ω・^ะ)⠀Simple Cat Kaomojis 37
(ะ`・ω・´ะ)⠀Simple Cat Kaomojis 38
ฅ(≚ᄌ≚)⠀Simple Cat Kaomojis 39
(≚ᄌ≚)ƶƵ⠀Simple Cat Kaomojis 40
(≚ᄌ≚)ℒℴѵℯ❤⠀Simple Cat Kaomojis 41
(^･ｪ･^)⠀Simple Cat Kaomojis 42
(^-x-^*)⠀Simple Cat Kaomojis 43
σ((=ﾟｴﾟ=))⠀Simple Cat Kaomojis 44
((≡ﾟ♀ﾟ≡))⠀Simple Cat Kaomojis 45
(=^･ｪ･^=))ﾉ彡☆⠀Simple Cat Kaomojis 46
（（≡￣♀￣≡））⠀Simple Cat Kaomojis 47
~(=^‥^)ノ☆⠀Simple Cat Kaomojis 48
(^･ω･^=)~⠀Simple Cat Kaomojis 49
┌(=^‥^=)┘⠀Simple Cat Kaomojis 50
┌(=^‥^=)┐⠀Simple Cat Kaomojis 51
└(=^‥^=)┘⠀Simple Cat Kaomojis 52
(^･o･^)ﾉ”⠀Simple Cat Kaomojis 53
(=･ｪ･=?⠀Simple Cat Kaomojis 54
ﾍ(^･･^=)~⠀Simple Cat Kaomojis 55
(´pゝω･)⠀Simple Cat Kaomojis 56
ﾍ(=^･ω･^= )ﾉ⠀Simple Cat Kaomojis 57
=^∇^*=⠀Simple Cat Kaomojis 58
~(=^–^)⠀Simple Cat Kaomojis 59
v(=∩_∩=)⠀Simple Cat Kaomojis 60
o(=´∇｀=)o⠀Simple Cat Kaomojis 61
|n＾ω＾|η⠀Simple Cat Kaomojis 62
(o^‥^)o⠀Simple Cat Kaomojis 63
(＾*･.･*＾)⠀Simple Cat Kaomojis 64
~(=^┬ ┬^)⠀Simple Cat Kaomojis 65
o(^・x・^)w⠀Simple Cat Kaomojis 66
ω(=＾・＾=)ω⠀Simple Cat Kaomojis 67
(^=˃ᆺ˂)⠀Simple Cat Kaomojis 68
=( ^<><<w<<<< ^)=⠀Simple Cat Kaomojis 69
( =①ω①=)⠀Fancy Eyed Cats 1
=’①。①’=⠀Fancy Eyed Cats 2
(*✧×✧*)⠀Fancy Eyed Cats 3
(ꀄꀾꀄ)⠀Fancy Eyed Cats 4
(✦థ ｪ థ)⠀Fancy Eyed Cats 5
=ộ⍛ộ=⠀Fancy Eyed Cats 6
(ꅈꇅꅈ)⠀Fancy Eyed Cats 7
ಠಿ ˑ̫ ಠಿ⠀Fancy Eyed Cats 8
ʘ̥ꀾʘ̥⠀Fancy Eyed Cats 9
(⌯⊙⍛⊙)⠀Fancy Eyed Cats 10
චᆽච⠀Fancy Eyed Cats 11
(ꏨ º̖̫º̖̫ ꏨ)⠀Fancy Eyed Cats 12
((≡ຶ⚲͜≡ຶ))⠀Fancy Eyed Cats 13
( ⓛ ω ⓛ *)⠀Fancy Eyed Cats 14
ଲ( ⓛ ω ⓛ *)ଲ⠀Fancy Eyed Cats 15
ὃ⍜ὅ⠀Fancy Eyed Cats 16
(ㅇㅅㅇ❀)⠀Stylish Cats 1
ㅇㅅㅇ⠀Stylish Cats 2
[^._.^]ﾉ彡⠀Stylish Cats 3
โ๏∀๏ใ⠀Stylish Cats 4
⋆ටᆼට⋆⠀Stylish Cats 5
ऴिाी⠀Stylish Cats 6
ि०॰०ॢी⠀Stylish Cats 7
ଲ(⁃̗̀̂❍⃓ˑ̫❍⃓⁃̠́̂)ଲ⠀Stylish Cats 8
=^._.^= ∫⠀Stylish Cats 9
ि०॰͡०ी⠀Stylish Cats 10
=ටᆼට=⠀Stylish Cats 11
ㄱ(ㅇㅅㅇ<#8221< )ㄴ⠀Stylish Cats 12
] ‘͇̂•̩̫’͇̂ ͒)ฅ ﾆｬ❣⠀Fancy Cats 1
(ٛ₌டுͩ ˑ̭ டுͩٛ₌)ฅ⠀Fancy Cats 2
₍˄ุ.͡˳̫.˄ุ₎ฅ˒˒⠀Fancy Cats 3
✩⃛( ͒ ु•·̫• ू ͒)⠀Fancy Cats 4
( ͒ ु- •̫̮ – ू ͒)⠀Fancy Cats 5
ฅ(⌯͒• ɪ •⌯͒)ฅ❣⠀Fancy Cats 6
ฅ⃛(⌯͒꒪ั ˑ̫ ꒪ั ⌯͒) ﾆｬｯ❣⠀Fancy Cats 7
(ٛ⁎꒪̕ॢ ˙̫ ꒪ٛ̕ॢ⁎)⠀Fancy Cats 8
( ͒ ˘̩̩̩̩̩̩ꇵ͒˘̩̩̩̩̩̩ ͒)⠀Fancy Cats 9
ฅ ̂⋒ิ ˑ̫ ⋒ิ ̂ฅ⠀Fancy Cats 10
ฅ( ͒ᵕ̳ωᵕ̳ ͒)｡o○⠀Fancy Cats 11
˚₊✩‧₊(⌯͒o̶̶̷̤ ꀾ o̴̶̷̤⌯͒)* ✩‧₊˚⠀Fancy Cats 12
(⌯͒ᵕɪᵕ⌯͒)zzZ⠀Fancy Cats 13
₍˄⌓⃘ ˳̫̬ ⌓⃘˄₎ค˒˒⠀Fancy Cats 14
✧ٛ˃̶̨̡˙ˣੰ͚˙͚ٛ˂̶̧̢༿˒˒⠀Fancy Cats 15
₍ ̂ˑ̫̈̄ ̂₎⠀Fancy Cats 16
( ‘͇̂•̩̫’͇̂ )ﾆｬ-♡⠀Fancy Cats 17
(ꃋิꎴꃋิ)⠀Fancy Cats 18
(⌯꒪͒ ૢ࿄ ૢ꒪͒)⠀Fancy Cats 19
(ꃪꄳꃪ)⠀Fancy Cats 20
(ٛɲ′᷄ ˑ̣̮ ‵᷅ٛɳ)՞⠀Fancy Cats 21
ʕ⌯˃ꎤु˂⌯ʔ⌕⠀Fancy Cats 22
ᖇ(( ͇ꆨ ꉴ ꉺ ͇))ᖆ≈ᘊ⠀Fancy Cats 23
♡͙♡͚₍⸉ॢ⸍͕͈ ˕̫ ⸌͔͈⸊ॢ₎♡͚♡͙⠀Fancy Cats 24
₍꒵꒱′͈ॢㅈ‵͈ॢ꒰꒵₎*·✧⠀Fancy Cats 25
ฅ(⌯͒•ꈊ͒ू •⌯͒)⠀Fancy Cats 26
( ¤̴̶̷̤́ ‧̫̮ ¤̴̶̷̤̀ )⠀Fancy Cats 27
(⁎ꆤ ̵ູ̫ꆤ)⠀Fancy Cats 28
(˵¯͒࿄¯͒˵)⠀Fancy Cats 29
६  ͇♞͂ۜ ˑ̫♞͂ƫ⍝⠀Fancy Cats 30
ʘ̵ ˤ̵̫ ʘ̵⠀Fancy Cats 31
⁽͑ʺ˚ˠ̫˚ʺ⁾̉⠀Fancy Cats 32
(ꀂǒꀂ)⠀Fancy Cats 33
§ꊘ⃑٥ꊘ⃐§⠀Fancy Cats 34
₍˄·͈༝·͈˄₎◞ ̑̑ෆ⃛⠀Cute Fluffy Kittens 1
₍˄·͈༝·͈˄₎ฅ˒˒⠀Cute Fluffy Kittens 2
(ृ˄·͈༝·͈˄ ृ )⠀Cute Fluffy Kittens 3
(ृʾ́꒳ʿ̀ ृ　)ु⠀Cute Fluffy Kittens 4
₍ᵔ·͈༝·͈ᵔ₎⠀Cute Fluffy Kittens 5
(˙̂·̫ॅ˙̂)⠀Cute Fluffy Kittens 6
꒰⌯͒•ɷ•⌯͒꒱ฅ⠀Cute Fluffy Kittens 7
ৎˊ͈ˣੰૢˋ͈ॢॽ∗｡⠀Cute Fluffy Kittens 8
♡ॢ₍⸍⸌̣ʷ̣̫⸍̣⸌₎⠀Cute Fluffy Kittens 9
˓˓ฅ₍˄ุ.͡ ̫.˄ุ₎ฅ˒˒⠀Cute Fluffy Kittens 10
₍˄·͈༝·͈˄*₎◞ ̑̑⠀Cute Fluffy Kittens 11
|˄·͈༝·͈˄₎.｡oO⠀Cute Fluffy Kittens 12
ฅ^•ﻌ•^ฅ⠀Cats with Paws 1
ฅ⁽͑ ˚̀ ˙̭ ˚́ ⁾̉ฅ⠀Cats with Paws 2
ฅ ̳͒•ˑ̫• ̳͒ฅ♡⠀Cats with Paws 3
ฅ(⌯͒• ɪ •⌯͒)ฅnya～ﾝ❣⠀Cats with Paws 4
˓˓ก₍⸍⸌̣ʷ̣̫⸍̣⸌₎ค˒˒⠀Cats with Paws 5
(ฅ•.•ฅ)⠀Cats with Paws 6
ฅ(*°ω°*ฅ)⠀Cats with Paws 7
◥(ฅº￦ºฅ)◤⠀Cats with Paws 8
(´ฅω•ฅ｀)⠀Cats with Paws 9
ฅ(˘ω˘ )ฅ⠀Cats with Paws 10
ฅ(⌯͒•̩̩̩́ ˑ̫ •̩̩̩̀⌯͒)ฅ⠀Cats with Paws 11
ฅ( ̳͒ᵕ ˑ̫ ᵕ ̳͒)ฅ⠀Cats with Paws 12
ฅ(⌯͒⚭̈́ ˑ̫ ⚭̈́⌯͒)ฅ⠀Cats with Paws 13
❣ฅ(⌯͒▾ ˑ̫ ▾⌯͒)ฅ⠀Cats with Paws 14
ฅ⃛(⌯͒▾ ˑ̫ ▾⌯͒)ฅ⃛⠀Cats with Paws 15
ฅ(三´ ͡ (ェ)´ ͡ 三)ฅ⠀Cats with Paws 16
ฅ(۩۞ω۞۩) ฅ⠀Cats with Paws 17
(ฅ^･ω･^ ฅ)⠀Cats with Paws 18
ฅ(´-ω-`)ฅ⠀Cats with Paws 19
ฅ ̳͒•ˑ̫• ̳͒ฅ⠀Cats with Paws 20
~(=^･ω･^)ﾍ <><<ﾟ)))彡⠀Cats and Fish 1
~(=^･･^)ﾉ<><<ﾟ)##)彡⠀Cats and Fish 2
~(=^･･^)ﾍ <><<ﾟ)))彡⠀Cats and Fish 3
₍˄·͈༝·͈˄*₎◞ ̑̑❤️くコ:≡⠀Cats and Fish 4
₍˄·͈༝·͈˄*₎◞ ̑̑ᗦ↞◃⠀Cats and Fish 5
Zzz(=^–^)｡o○{{ <><<ﾟ)++++<<<<<<<< }}⠀Cats and Fish 6
~(=^･･^)_旦~ (ﾟoﾟ<)⠀Cats Doing Things 1
ｰ8-(^._.^)ﾉ☆( _ _).oO⠀Cats Doing Things 2
~(=^‥^)ﾉ◎～⠀Cats Doing Things 3
┫o(^‥^=)~ ~(=^‥^)o┳⠀Cats Doing Things 4
ε=ε=((( ^-x-^)ﾉ⠀Cats Doing Things 5
ε=ε=ε=ヾ(э^・ｪ・^)э⠀Cats Doing Things 6
0( =^･_･^)=〇⠀Cats Doing Things 7
~(=^･ω･^)ヾ(^^ )⠀Cats Doing Things 8
ヾ(=^・ｪ・^)ヾ(^^ )⠀Cats Doing Things 9
ヾ(=^・・^)ヾ(^^ )⠀Cats Doing Things 10
┏━o(=´∇｀=)o━┓⠀Cats Doing Things 11
目=ﾍ(=^･ω･^)⠀Cats Doing Things 12
~□Pヘ(^‥^=)~⠀Cats Doing Things 13
~(=^‥^)_｡⠀Cats Doing Things 14
~(=^･ω･^)ﾉ◎～⠀Cats Doing Things 15
(*･∀･)／(=^・^=)⠀Cats Doing Things 16
○)))ﾍ(^･･^=)~⠀Cats Doing Things 17
(=^・ω・^)ﾉ＝＝＝Θ☆(＋＿＋)⠀Cats Doing Things 18
~(=^･ω･^)y＝ ‥… *→<ﾟoﾟ)⠀Cats Doing Things 19
♪♪♪ Ｕ・ｪ・Ｕ人(^･x･^=) ♪♪♪⠀Cats Doing Things 20
0( = ฅ^･_･^)= ฅ= ฅ= ฅ ฅ⠀Cats Doing Things 21
‘`ﾛｰヽ(⊡ㅂ⊡｡ Ξ ｡⊡ㅂ⊡)ﾉ ‘`ﾛｰ⠀Giant Cats 1
₍˄·͈༝·͈˄₍˄·͈༝·͈˄( ͒ ु•·̫• ू ͒)˄·͈༝·͈˄₎˄·͈༝·͈˄₎⠀Giant Cats 2
【～～～ヽ(=^‥^=)丿～～～】⠀Giant Cats 3
( ͡ຈ╭͜ʖ╮͡ຈ )⠀The Lenny Face 1
( ͡ಠ ʖ̯ ͡ಠ)⠀The Lenny Face 2
( ͡~ ͜ʖ ͡~)⠀The Lenny Face 3
( ͡~ ͜ʖ ͡°)⠀The Lenny Face 4
( ͠° ͟ʖ ͡°)⠀The Lenny Face 5
( ͡ʘ╭͜ʖ╮͡ʘ)⠀The Lenny Face 6
( ͝סּ ͜ʖ͡סּ)⠀The Lenny Face 7
( ͡ᵔ ͜ʖ ͡ᵔ )⠀The Lenny Face 8
( ͡^ ͜ʖ ͡^ )⠀The Lenny Face 9
[̲̅$̲̅(̲̅ ͡° ͜ʖ ͡°̲̅)̲̅$̲̅]⠀The Lenny Face 10
( ͡ຈ ͜ʖ ͡ຈ)⠀The Lenny Face 11
( ͡° ʖ̯ ͡°)⠀The Lenny Face 12
( ͡ ͜ʖ ͡ )⠀The Lenny Face 13
(☞ ͡° ͜ʖ ͡°)☞⠀The Lenny Face 14
ᕕ( ͡° ͜ʖ ͡° )ᕗ⠀The Lenny Face 15
( ͡° ͜ʖ ͡°)⠀The Lenny Face 16
( ͡°╭͜ʖ╮͡° )⠀The Lenny Face 17
(▀ ͜ʖ ͡°)⠀The Lenny Face 18
(つ ͡° ͜ʖ ͡°)つ⠀The Lenny Face 19
( ͡⚆ ͜ʖ ͡⚆)⠀The Lenny Face 20
¯\_( ͠° ͟ʖ °͠ )_/¯⠀The Lenny Face 21
( ͡° ͜ʖ ( ͡° ͜ʖ ( ͡° ͜ʖ ( ͡° ͜ʖ ͡°) ͜ʖ ͡°)ʖ ͡°)ʖ ͡°)⠀The Lenny Face 22
༼ ºل͟º ༽⠀Raise Your Dongers 1
┌༼ຈل͜ຈ༽┐⠀Raise Your Dongers 2
༼ ಠل͟ಠ༽⠀Raise Your Dongers 3
୧༼ ͡◉ل͜ ͡◉༽୨⠀Raise Your Dongers 4
ヽ༼ ಠ益ಠ ༽ﾉ⠀Raise Your Dongers 5
༼ ༎ຶ ෴ ༎ຶ༽⠀Raise Your Dongers 6
༼ ༏༏ີཻ༾ﾍ ༏༏ີཻ༾༾༽༽⠀Raise Your Dongers 7
༼･ิɷ･ิ༽⠀Raise Your Dongers 8
༼ ͒ ̶ ͒༽⠀Raise Your Dongers 9
༼༼<< <°<ਊ°<༽⠀Raise Your Dongers 10
༼( ⁍ืེ <#8211< ⁍ื༽༽⠀Raise Your Dongers 11
༼•͟ ͜ •༽⠀Raise Your Dongers 12
༼•̃͡ ɷ•̃͡༽⠀Raise Your Dongers 13
༼ ͒ ͓ ͒༽⠀Raise Your Dongers 14
༼༭ຶཬ༤ຶ༽⠀Raise Your Dongers 15
༼ꉺˇɷˇꉺ༽⠀Raise Your Dongers 16
༼இɷஇ༽⠀Raise Your Dongers 17
༼✷ɷ✷༽⠀Raise Your Dongers 18
༼ԾɷԾ༽⠀Raise Your Dongers 19
༼≖ɷ≖༽⠀Raise Your Dongers 20
༼ꉺ✺ꉺ༽⠀Raise Your Dongers 21
༼ꉺლꉺ༽⠀Raise Your Dongers 22
ヽ༼ຈل͜ຈ༽ﾉ⠀Raise Your Dongers 23
༼ꉺ౪ꉺ༽⠀Raise Your Dongers 24
༼ꉺεꉺ༽⠀Raise Your Dongers 25
༼<´༎ຶ ༎ຶ ༽⠀Raise Your Dongers 26
༼⁰o⁰；༽⠀Raise Your Dongers 27
༼(⁽͇ˊ̑⁾ ἴृ ⁽ˋ̑⁾͇)༽⠀Raise Your Dongers 28
˓ ू༼ ்ͦ॔ཀ ்ͦ॓ू༽⠀Raise Your Dongers 29
༼ ु ்ͦ॔ཫ ்ͦ॓༽ु˒˒⠀Raise Your Dongers 30
／༼ ༏༏ີཻ༾ﾍ ༏༏ີཻ༾༾༽༽⠀Raise Your Dongers 31
༼ ்ͦ॔ཫ ்ͦ॓༽⠀Raise Your Dongers 32
༼ᶿ᷇ཫᶿ᷆༽⠀Raise Your Dongers 33
༼  ऀืົཀ  ऀืົ༽⠀Raise Your Dongers 34
༼՟ິͫཀ՟ິͫ༽⠀Raise Your Dongers 35
ˋ̧̧̖⁽⁽༼ ु˳̮̑̈༽ु⁾⁾ˋ̧̧̖♪⠀Raise Your Dongers 36
༼❁ɷ❁༽⠀Raise Your Dongers 37
༼ ຶཽཀ ຶཽ༽⠀Raise Your Dongers 38
ヽ༼၀-၀༽ﾉ⠀Raise Your Dongers 39
༼(❛)㇁(❛)༽⠀Raise Your Dongers 40
ヽ༼⊙_⊙༽ﾉ⠀Raise Your Dongers 41
༼⺤`皿′⺤༽⠀Raise Your Dongers 42
ヽ༼࿃っ࿃༽ﾉ⠀Raise Your Dongers 43
ヽ༼௵ل͜௵༽ﾉ⠀Raise Your Dongers 44
༼ ºل͟º༼ ºل͟º ༽ºل͟º ༽ºل͟º ༽⠀Raise Your Dongers 45
༼つಠ益ಠ༽つ ─=≡ΣO))⠀Raise Your Dongers 46
༼⌐■ل͟■༽⠀Raise Your Dongers 47
༼ง=ಠ益ಠ=༽ง⠀Raise Your Dongers 48
╰༼=ಠਊಠ=༽╯⠀Raise Your Dongers 49
ᕙ༼*◕_◕*༽ᕤ⠀Raise Your Dongers 50
ヽ༼ಢ_ಢ༽ﾉ⠀Raise Your Dongers 51
ヽ༼ ʘ̚ل͜ʘ̚༼◕_◕༽◉_◔ ༽ﾉ⠀Raise Your Dongers 52
┌༼ ⊘ _ ⊘ ༽┐⠀Raise Your Dongers 53
༼ : ౦ ‸ ౦ : ༽⠀Raise Your Dongers 54
༼∗ღ۝ღ∗༽⠀Raise Your Dongers 55
༼ง ͠ຈ ͟ل͜ ͠ຈ༽o:[]:::::::<><<⠀Raise Your Dongers 56
༼ᕗຈل͜ຈ༽ᕗ⠀Raise Your Dongers 57
ヽ༼ຈل͜ರೃ༽ﾉ⠀Raise Your Dongers 58
ヽヽ༼༼ຈຈل͜ل͜ຈຈ༽༽ﾉﾉ⠀Raise Your Dongers 59
༼ ᕤ◕◡◕ ༽ᕤ⠀Raise Your Dongers 60
ᕙ༼˵͠ ͠°ل͜͠ ͠°˵༽ᕗ⠀Raise Your Dongers 61
ᕦ༼::ಥ෴ಠೃ::༽ノ⠀Raise Your Dongers 62
༼ •̀ ں •́ ༽⠀Raise Your Dongers 63
♫ ┌༼ຈل͜ຈ༽┘ ♪⠀Raise Your Dongers 64
༼ ಥل͟ಥ ༽⠀Raise Your Dongers 65
༼ﾉƟ͆ل͜Ɵ͆༽ﾉ⠀Raise Your Dongers 66
༼୨Ɵ͆ل͜Ɵ͆༽୨⠀Raise Your Dongers 67
ヽ༼Ɵ͆ل͜Ɵ͆ヽ༽⠀Raise Your Dongers 68
୧༼Ɵ͆ل͜Ɵ͆୧༽⠀Raise Your Dongers 69
┌༼ຈل͜ຈ༽┘⠀Raise Your Dongers 70
へ༼ ✪ Ĺ̯ ✪ ༽و⠀Raise Your Dongers 71
c༼ ͡° ͜ʖ ͡° ༽⊃⠀Raise Your Dongers 72
༼ ಠ ͟ʖ ಠ ༽⠀Raise Your Dongers 73
୧༼ ” ✖ ‸ ✖ ” ༽୨⠀Raise Your Dongers 74
¯\_༼ᴼل͜ᴼ༽_/¯⠀Raise Your Dongers 75
┏༼ ◉ ╭╮ ◉༽┓⠀Raise Your Dongers 76
ᕕ༼✿•̀︿•́༽ᕗ⠀Raise Your Dongers 77
└༼ •́ ͜ʖ •̀ ༽┘⠀Raise Your Dongers 78
୧༼ ヘ ᗜ ヘ ༽୨⠀Raise Your Dongers 79
༼ ◔ ͜ʖ ◔ ༽⠀Raise Your Dongers 80
╰༼⇀︿⇀༽つ-]═──⠀Raise Your Dongers 81
乁༼☯‿☯✿༽ㄏ⠀Raise Your Dongers 82
ヽ༼<><<ل͜<<<<༽ﾉ⠀Raise Your Dongers 83
ɳ༼ຈل͜ຈ༽ɲ⠀Raise Your Dongers 84
¯\_༼ ି ~ ି ༽_/¯⠀Raise Your Dongers 85
ᕦ༼ ˵ ◯ ਊ ◯ ˵ ༽ᕤ⠀Raise Your Dongers 86
¯\_༼ ಥ ‿ ಥ ༽_/¯⠀Raise Your Dongers 87
༼♥ل͜♥༽⠀Raise Your Dongers 88
Ѱζ༼ᴼل͜ᴼ༽ᶘѰ⠀Raise Your Dongers 89
ζ༼Ɵ͆ل͜Ɵ͆༽ᶘ⠀Raise Your Dongers 90
ᕦ༼ ͡° ͜ ͝° ༽ᕤ⠀Raise Your Dongers 91
ヽ༼ ☭ل͜☭ ༽ﾉ⠀Raise Your Dongers 92
˓˓ ू༼ ⠁⃘ཀ ⠁⃘ू༽⠀Raise Your Dongers 93
༼ ु⠁⃘ཫ ⠁⃘༽ु˒˒⠀Raise Your Dongers 94
ᕕ༼ ͠ຈ Ĺ̯ ͠ຈ ༽┌∩┐⠀Raise Your Dongers 95
⋌༼ •̀ ⌂ •́ ༽⋋⠀Raise Your Dongers 96
└༼ ಥ ᗜ ಥ ༽┘⠀Raise Your Dongers 97
୧༼✿ ͡◕ д ◕͡ ༽୨⠀Raise Your Dongers 98
ᕙ༼=ݓ益ݓ=༽ᕗ⠀Raise Your Dongers 99
༼ ∗ ି ﹏ ି ∗ ༽⠀Raise Your Dongers 100
o͡͡͡╮༼ ʘ̆ ۝ ʘ̆ ༽╭o͡͡͡⠀Raise Your Dongers 101
o͡͡͡╮༼ • ʖ̯ • ༽╭o͡͡͡⠀Raise Your Dongers 102
ヽ༼ຈل͜ຈ༽ﾉ гคเรє ๏г ๔เє ヽ༼ຈل͜ຈ༽ﾉ⠀Raise Your Dongers 103
༼ ºل͟º ༼ ºل͟º ༼ ºل͟º ༽ ºل͟º ༽ ºل͟º ༽⠀Raise Your Dongers 104
༼ ºل͟º༼ ºل͟º( ͡° ͜ʖ ͡°)ºل͟º ༽ºل͟º ༽⠀Raise Your Dongers 105
ヽ༼ ☯‿☯༼ ಠ益ಠ༽◕ل͜◕༽つ⠀Raise Your Dongers 106
S<ru<<in> Leo⠀Other Internet Memes 1
ᕕ(ᐛ)ᕗ⠀Other Internet Memes 2
(•̀ᴗ•́)و ̑̑⠀Other Internet Memes 3
| (•□•) | (❍ᴥ❍ʋ)⠀Other Internet Memes 4
∠( ᐛ 」∠)＿⠀Other Internet Memes 5
(´°ω°`)⠀Other Internet Memes 6
~=[,,_,,]:3⠀Other Internet Memes 7
(￣ｍ￣〃)⠀Other Internet Memes 8
щ(゜ロ゜щ)⠀Other Internet Memes 9
(/_<<<<。)⠀Other Internet Memes 10
( ՞ਊ ՞)☝⠀Other Internet Memes 11
(°ロ°)☝⠀Other Internet Memes 12
φ(ﾟﾛﾟ*)ﾉ⠀Other Internet Memes 13
(ভ_ ভ) ރ ／/ ┊ \＼⠀Other Internet Memes 14
┌( ಠ_ಠ)┘⠀Other Internet Memes 15
(－‸ლ)⠀Other Internet Memes 16
(ლ‸－)(－‸ლ)⠀Other Internet Memes 17
( ﾉ ﾟｰﾟ)ﾉ☀️⠀Other Internet Memes 18
☀️ヽ(ﾟｰﾟヽ)⠀Other Internet Memes 19
Pikachu⠀Pokemon 1
ϞϞ(๑⚈ ․̫ ⚈๑)∩⠀Pokemon 2
Y● ❛ ̫.❛●)´෴ϞϞ⠀Pokemon 3
Ƶƶ(☄￣▵—▵￣)⠀Pokemon 4
ζ,,ﾟДﾟζ⠀Pokemon 5
╭<<<<<<<<◕°ω°◕<><<<><<╮⠀Pokemon 6
╰ᕦ╯( O++O )╰ᕤ╯⠀Pokemon 7
⊹⋛⋋(◐⊝◑)⋌⋚⊹⠀Pokemon 8
<<<<:0OOoo<><<⠀Pokemon 9
卅(•‿•)卅⠀Pokemon 10
卅(◕‿◕)卅⠀Pokemon 11
卅( ͡° ͜ ͡°)卅⠀Pokemon 12
└(oѪo)┘⠀Pokemon 13
♫꒰･‿･๑꒱⠀Simple Clouds 1
꒰✘Д✘◍꒱⠀Simple Clouds 2
٩꒰ಂ❛ ▿❛ಂ꒱۶♡⠀Simple Clouds 3
꒰ *๑•ૅʖ̫•́๑꒱⠀Simple Clouds 4
꒰✩’ω`ૢ✩꒱⠀Simple Clouds 5
٩꒰๑ ´∇`๑꒱۶⠀Simple Clouds 6
꒰｡•`ｪ´•｡꒱۶⠀Simple Clouds 7
꒰๑ ᷄ω ᷅꒱⠀Simple Clouds 8
٩꒰๑• ̫•๑꒱۶♡⠀Simple Clouds 9
꒰(@｀꒳´)꒱⠀Simple Clouds 10
꒰๑•̮̮́౪•̮̮̀๑꒱⠀Simple Clouds 11
٩꒰๑• ³•๑꒱۶⠀Simple Clouds 12
꒰•ི̫͡ુ•ྀૂ꒱⠀Simple Clouds 13
꒰ღ˘‿˘ற꒱❤⃛⠀Simple Clouds 14
٩꒰ɵ̥̥▿ɵ̥̥●꒱۶⠀Simple Clouds 15
꒰˘̩̩̩⌣˘̩̩̩๑꒱♡⠀Simple Clouds 16
٩꒰ ̃•ε• ̃๑꒱۶⁼³₌₃⠀Simple Clouds 17
٩꒰ʘʚʘ๑꒱۶⠀Simple Clouds 18
꒰⌯͒•̩̩̩́ ˑ̫ •̩̩̩̀⌯͒꒱⠀Simple Clouds 19
٩꒰ ´ᆺ`꒱۶⠀Simple Clouds 20
ꉂꉂ꒰•̤▿•̤*ૢ꒱⠀Simple Clouds 21
꒰⌯͒•ɷ•⌯͒꒱⠀Simple Clouds 22
٩꒰ ˘ ³˘꒱۶~♡⠀Simple Clouds 23
꒰⑅ᵕ༚ᵕ꒱˖♡⠀Simple Clouds 24
꒰⑅•ᴗ•⑅꒱⠀Simple Clouds 25
٩꒰｡•‿•｡꒱۶⠀Simple Clouds 26
♡˖꒰ᵕ༚ᵕ⑅꒱⠀Simple Clouds 27
꒰●꒡ ̫ ꒡●꒱⠀Simple Clouds 28
٩꒰• ε •꒱۶⁼³⠀Simple Clouds 29
꒰⁎❛⃘ͫ ⍘⃘ ❛⃘ͫ⁎꒱⠀Simple Clouds 30
꒰•̫͡•ོ꒱⠀Simple Clouds 31
꒰⌯͒•·̫•⌯͒꒱⠀Simple Clouds 32
٩꒰´·⌢•｀꒱۶⁼³₌₃⠀Simple Clouds 33
꒰╬•᷅д•᷄╬꒱⠀Simple Clouds 34
ଽ꒰⌓̈ ॢ꒱ ̉ ̉⠀Simple Clouds 35
꒰⌗´͈ ᵕ ॣ`͈⌗꒱৩⠀Simple Clouds 36
꒰◍ᐡᐤᐡ◍꒱⠀Simple Clouds 37
꒰๑•௰•๑꒱⠀Simple Clouds 38
‘٩꒰｡•◡•｡꒱۶’⠀Simple Clouds 39
ᔪ꒰ ꒪ω꒪ |||꒱⠀Simple Clouds 40
꒰๑˃͈꒳˂͈๑꒱ﾉ*ﾞ̥⠀Simple Clouds 41
꒰´꒳`∗꒱⠀Simple Clouds 42
꒰´꒳`꒱⠀Simple Clouds 43
꒰∗´꒳`꒱⠀Simple Clouds 44
.꒰ϱ﹏-๑꒱‧*Zz｡⠀Simple Clouds 45
꒰⌯͒•̩̩̩́ ᴗ •̩̩̩̀⌯͒꒱⠀Simple Clouds 46
꒰๑•‧̮ૣ•ૣ๑꒱*･.｡⠀Simple Clouds 47
꒰✩˙˟˙✩꒱⠀Simple Clouds 48
*¨*•.¸꒰๑ ᷄ω ᷅꒱⠀Simple Clouds 49
♪.*⁽⁽ ◝꒰´꒳`∗꒱◟ ₎₎₊·*⠀Simple Clouds 50
꒰◍ᐡᐤᐡ◍꒱ᐝ.∗̥✩⁺˚⑅⠀Simple Clouds 51
꒰ ꒪⌑꒪꒱˖ꂚ*ᵎ⠀Simple Clouds 52
∠꒰’౪’꒱✧⠀Simple Clouds 53
꒰ •͈́ ̫ •͈̀ ꒱ˉ̞̭⠀Simple Clouds 54
⁽⁽꒰๑•‧̮ૣ•ૣ๑꒱⁾⁾⠀Simple Clouds 55
꒰๑꒪ɷ꒪꒱⠀Simple Clouds 56
꒰⁎❛⃘ੌ ᵕ ❛⃘ੌ⁎꒱⠀Simple Clouds 57
꒰⁎′̥̥̥ ⌑ ‵̥̥̥ ꒱⠀Simple Clouds 58
˖*٩꒰｡‾᷅⌑‾᷅｡<꒱۶ఽ*.·⠀Simple Clouds 59
꒰๑*´ᗜ`*꒱*›◡‹꒱꒱⠀Simple Clouds 60
*+:꒰◍•ᴗ•◍꒱:+*⠀Simple Clouds 61
꒰｡ › ·̮ ‹ ｡꒱⠀Simple Clouds 62
◟꒰⌳̈ ꒱⠀Simple Clouds 63
꒰๑͒•௰•๑͒꒱ℒℴѵℯ❤⠀Simple Clouds 64
꒰⁎❛⃘ੌ ⍘⃘ ❛⃘ੌ⁎꒱⠀Simple Clouds 65
ｑ꒰*ゝω・꒱ﾉ″⠀Simple Clouds 66
◟꒰∗⌵̈꒱◞✩◟꒰⌔̈∗꒱◞⠀Simple Clouds 67
꒰̤◴ㅈ◴̵̤꒱⠀Simple Clouds 68
꒰⍨꒱⠀Simple Clouds 69
꒰⑅ˊ͈ ˙̫ ˋ͈⑅꒱⠀Simple Clouds 70
꒰✪ૢꇵ✪ૢ꒱ෆ⃛⠀Simple Clouds 71
♫꒰･◡･๑꒱⠀Simple Clouds 72
꒰#’ω`#꒱੭⠀Simple Clouds 73
୧꒰๑͒•͈ꇵ͒•͈๑͒꒱୨ᵎᵎ✧⠀Simple Clouds 74
꒰⑅ᵕ༚ᵕ꒱˖♡ªʳⁱ૭ªᵗ°♡˖꒰ᵕ༚ᵕ⑅꒱⠀Simple Clouds 75
٩꒰ ˘ ³˘꒱۶ⒽⓤⒼ♥♡̷♡̷⠀Simple Clouds 76
˞͛꒰๑ऀ •̆ꈊ͒ू•̆๑ऀ꒱⠀Complex Clouds 1
꒰ ॢö৺ö ૢ๑꒱⠀Complex Clouds 2
꒰･᷄ु௰･᷅ू꒱⠀Complex Clouds 3
꒰｡•ॢ◡-ॢ｡꒱⠀Complex Clouds 4
꒰·͡ुˑ·ཻू꒱ෆ⃛⠀Complex Clouds 5
꒰•ू꒪͒·̫̮꒪͒•ू꒱⠀Complex Clouds 6
꒰♡ˊ͈ ु꒳ ूˋ͈꒱.⑅*♡⠀Complex Clouds 7
꒰๑͒•̀ुꇵ͒•꒱و ̑̑⠀Complex Clouds 8
͛꒰ू ऀ•̥́ꈊ͒ੁ•ૅू॰˳ऀ꒱ ͟͟͞ ̊ ̥ ̥⠀Complex Clouds 9
꒰ू•௰ू•๑꒱⠀Complex Clouds 10
꒰ෆ❛ั ु▿❛ั ु꒱⠀Complex Clouds 11
٩꒰･ัε･ั ꒱۶⠀Complex Clouds 12
٩꒰•௰︡๑꒱ु⠀Complex Clouds 13
ू꒰ꇐωꇐ ू꒱⠀Complex Clouds 14
ପ꒰⑅°͈꒳°͈꒱੭ु⁾⁾⠀Complex Clouds 15
꒰*⑅˃̶͈ ৺˂̶͈⑅꒱੭ु⁾⁾·°⠀Complex Clouds 16
˞͛꒰๑ऀ •̆ꈊ͒ू•̆๑ऀ꒱⁇⠀Complex Clouds 17
꒰๑͒ ु•ꇵ͒•`๑͒꒱⠀Complex Clouds 18
ᵎᵎᵎ꒰ฅ ͒•ૅꇵ͒•⌯͒꒱ฅ⠀Complex Clouds 19
꒰♡˃̶̤́ ॢ꒳ ॢ˂̶̤̀ ꒱·◌*.♡⠀Complex Clouds 20
꒰⁎ᵉ̷͈ ॣ꒵ ॢᵉ̷͈⁎꒱໊⠀Complex Clouds 21
⋆⑅˚₊*୧⃛꒰ɞ̴̶̷◟◞ʚ̴̶̷̷꒱୨⃛*₊˚⠀Complex Clouds 22
✬̴⃛꒰⁍̴ꈊ ॢ⁍̴⌯꒱⠀Complex Clouds 23
꒰•́ॢ৺•̀ॢ๑͒꒱⠀Complex Clouds 24
꒰◍•̤ु௰•̤ु꒱* ∗◌+*♡⠀Complex Clouds 25
ପ꒰*⑅ ॢ˘͈ꀧ˘͈ ॢ⑅꒱✩.*˚⠀Complex Clouds 26
˪৹⌵ೕ꒰๑•‧̮ૣ•ૣ๑꒱⠀Complex Clouds 27
↷꒰ू´•௰ू• `꒱↷⠀Complex Clouds 28
꒰๑⃙⃘ϱ॔꒳˘͈( ˘͈꒳˘͈๑⃙⃘꒱♡⠀Complex Clouds 29
❤︎⁄⁄꒰* ॢꈍ◡ꈍ ॢ꒱.*˚‧⠀Complex Clouds 30
·˚*୨୧꒰∗ɞ̴̶̷ु ·̮ ूɞ̴̶̷∗꒱୨୧*˚·⠀Complex Clouds 31
ू꒰΄ ิ̤۝ ิ ̤꒱ु⠀Complex Clouds 32
꒰ ்ͦੰ ⍘⃘  ்ͦੰ꒱⠀Complex Clouds 33
꒰ ॢ꒱˶´ꇵ͒`˶꒰ ॢ꒱⠀Complex Clouds 34
꒰๑ ̇̅ ॄ ̇̅๑꒱⠀Complex Clouds 35
꒰♡ᵒ̴̶̷ꇵ͒ᵒ̴̶̷♡꒱*ೄ˚⠀Complex Clouds 36
꒰ꄬຶູྀ ॄ ꄬຶູི ꒱⠀Complex Clouds 37
꒰ꄬຶູྀ ॄ ꄬຶູི ꒱ ⃛˚⠀Complex Clouds 38
꒰ ︠ु௰•꒱ु♡⠀Complex Clouds 39
*⋆⑅⃟◌˚꒰ˊૢᵕˋૢෆ꒱⠀Complex Clouds 40
⅀⑈꒰′Ꮌ̮‵꒵꒱՞⠀Complex Clouds 41
*͛꒰ू ऀ•̥́◟◞•ૅू॰˳ऀ꒱ ͟͟͞ ̊ ̥ ̥⠀Complex Clouds 42
꒰♡⌯́ॢ³⌯̀ॢ꒱⠀Complex Clouds 43
꒰ˇ❝͋ꊗ❝͋ˇ꒱ค˒˒⠀Complex Clouds 44
꒰ີ∗ˊ↥ˋ∗ ꒱ີˉ̶̡̭̭⠀Complex Clouds 45
◌ต꒰｡•̤༝•̤｡꒱ต◌⠀Complex Clouds 46
꒰(ू•‧̫•ू )꒱⠀Complex Clouds 47
꒰ ु•̫•̫ ु꒱⠀Complex Clouds 48
꒰੭ु ऀᵒ̴̶̷̤́ꋢᵒ̴̶̷̤̀ ऀ꒱੭ु⁾⁾⠀Complex Clouds 49
♡⃛=͟͟͞͞꒰ˇ❝͋ुꈊ❝͋ुˇ꒱⁼³₌₃⠀Complex Clouds 50
꒰⁎❛⃘ ⍘⃘ ❛⃘⁎꒱⠀Complex Clouds 51
꒰⌯͒ඹ ·̫ ඹ⌯͒꒱⠀Complex Clouds 52
*͛꒰ू ऀ•̥́◟◞•ૅू॰˳ऀ꒱ ͟͟͞ ̊ ̥ ̥⠀Complex Clouds 53
✧.*꒰⁎❝͋॔༶̶❝͋॓⁎ॢ꒱*·✧⠀Complex Clouds 54
꒰⁎˃ ॢꇴ ॢ˂⁎꒱➴ෆ⃛⠀Complex Clouds 55
Σ꒰๑•ॢд •ॢ๑꒱⠀Complex Clouds 56
꒰ ੭ु・ω ・꒱ ੭ु⁾⁾⠀Complex Clouds 57
꒰⁎ ✪̼ ◡ ✪̼` ⁎꒱﹡Տҽҽ վօմ⁎☪*✩⠀Complex Clouds 58
꒰·͡ुˑ·ཻू꒱*̫ෆ๋*̫꒰•ི̫͡ુ•ྀૂ꒱⠀Complex Clouds 59
꒰·͡ुˑ·ཻू꒱*̫ෆ๋*̫꒰•ི̫͡ુ•ྀૂ꒱*̫ෆ๋*̫꒰•̻̀ु•́ू໊꒱*̫ෆ๋*̫꒰•̹͡ु-ོू꒱*̫ෆ๋*̫꒰•̹͡ິु•ິू꒱⠀Complex Clouds 60
(・_・ヾ⠀Head scratching 1
｢(ﾟﾍﾟ)⠀Head scratching 2
(・・。)ゞ⠀Head scratching 3
(｀_´)ゞ⠀Head scratching 4
(´−｀) ﾝｰ⠀Head scratching 5
｡(*^▽^*)ゞ⠀Head scratching 6
(^^ゞ⠀Head scratching 7
(^～^<)ゞ⠀Head scratching 8
(￣(エ)￣)ゞ⠀Head scratching 9
(-_-)ゞ゛⠀Head scratching 10
(＃⌒∇⌒＃)ゞ⠀Head scratching 11
(⌒▽⌒)ゞ⠀Head scratching 12
(●´ω｀●)ゞ⠀Head scratching 13
〈(゜。゜)⠀Head scratching 14
「(°ヘ°)⠀Head scratching 15
く（＾_・）ゝ⠀Head scratching 16
σ(´し_｀〃)ゞ⠀Head scratching 17
δ(´д｀< )⠀Head scratching 18
↷( ó╻ò)⠀Head scratching 19
(≖ლ≖๑ )ﾌ⠀Head scratching 20
(<＾◇＾<)ゝ⠀Head scratching 21
(・∧‐)ゞ⠀Head scratching 22
ଽ (৺ੋ ௦ ৺ੋ )৴⠀Head scratching 23
( <-(ｴ)-)ゞ⠀Head scratching 24
(；´д｀)ゞ⠀Head scratching 25
(≧д≦ヾ)⠀Head scratching 26
｢(ﾟ<<<<ﾟ)ﾞ??⠀Head scratching 27
?(ﾉ)・´ω・(ヾ)⠀Head scratching 28
/(@ﾟﾍﾟ@)⠀Head scratching 29
℃ↂ_ↂ⠀Head scratching 30
∑(O_O；)⠀Head Scratching With a ∑ 1
Σ(‘◉⌓◉’)⠀Head Scratching With a ∑ 2
Σ(-᷅_-᷄๑)⠀Head Scratching With a ∑ 3
Σ(ＴωＴ)⠀Head Scratching With a ∑ 4
Σ(●ꉺ▱ꉺ●)⠀Head Scratching With a ∑ 5
Σ”(⚙♊⚙ﾉ)ﾉ⠀Head Scratching With a ∑ 6
Σ(‘◉⌓◉’)⠀Head Scratching With a ∑ 7
∑（｡･Д･｡）???⠀Head Scratching With a ∑ 8
∑(⌒◇⌒；)⠀Head Scratching With a ∑ 9
Σ(๛д๛)⠀Head Scratching With a ∑ 10
Σ(･ิ¬･ิ)⠀Head Scratching With a ∑ 11
Σ(´д｀<)⠀Head Scratching With a ∑ 12
Σʕﾟᴥﾟﾉʔﾉ⠀Head Scratching With a ∑ 13
Σ(`‐ｪ‐´)⠀Head Scratching With a ∑ 14
Σ(´д ` ﾒ)⠀Head Scratching With a ∑ 15
Σ(・Д・)!?⠀Head Scratching With a ∑ 16
Σ(￣ロ￣<<<)⠀Head Scratching With a ∑ 17
∑(ﾟ台ﾟ<<<⠀Head Scratching With a ∑ 18
Σ(￣□￣<<<)⠀Head Scratching With a ∑ 19
Σ（￣□￣；）⠀Head Scratching With a ∑ 20
Σ(⠀Head Scratching With a ∑ 21
[emai<<#160<pro<ec<ed]⠀Head Scratching With a ∑ 22
)!?⠀Head Scratching With a ∑ 23
Σ(ﾟﾛ､ﾟ<)⠀Head Scratching With a ∑ 24
∑(´ﾟωﾟ｀*)⠀Head Scratching With a ∑ 25
Σ(； ･`д･´)⠀Head Scratching With a ∑ 26
Σ(<･益･<<<)!!!⠀Head Scratching With a ∑ 27
∑（´△｀○）⠀Head Scratching With a ∑ 28
Σ(´△｀Ⅲ)⠀Head Scratching With a ∑ 29
Σ(•’╻’• ۶)۶⠀Head Scratching With a ∑ 30
(•ิ_•ิ)?⠀Blank Look 1
(?・・)σ⠀Blank Look 2
(´･_･`)⠀Blank Look 3
(‘◇’)?⠀Blank Look 4
(゜-゜)⠀Blank Look 5
( ・◇・)？⠀Blank Look 6
(゜。゜)⠀Blank Look 7
(◎_◎<)⠀Blank Look 8
(◎-◎；)⠀Blank Look 9
(●__●)⠀Blank Look 10
(☉_☉)⠀Blank Look 11
(ﾟｰﾟ<)⠀Blank Look 12
【・_・?】⠀Blank Look 13
【・ヘ・?】⠀Blank Look 14
c( O.O )ɔ⠀Blank Look 15
ఠ_ఠ⠀Blank Look 16
(๑ ́ᄇ`๑)⠀Blank Look 17
੨੨(´･･`)⠀Blank Look 18
(꒪ȏ꒪)ｴｯ?⠀Blank Look 19
(ﾒ・ん・)？⠀Blank Look 20
(o*｡_｡)o⠀Blank Look 21
ॽ̥(૦்૦)ˀ̣⠀Blank Look 22
ɾ◉⊆◉ɹ⠀Blank Look 23
(・・？)⠀Blank Look 24
(o゜ー゜o)??⠀Blank Look 25
(ﾟヘﾟ)？⠀Blank Look 26
（・∩・）？⠀Blank Look 27
??r(･x･｡)???⠀Blank Look 28
: ◉ ∧ ◉ : ╏⠀Blank Look 29
σ(゜◆゜<)⠀Blank Look 30
(<゜◆゜)σ⠀Blank Look 31
( ゜Д゜；)！？⠀Blank Look 32
(｡・ω・｡)?⠀Blank Look 33
(｀◎△◎)!?⠀Blank Look 34
(ﾟ▽ﾟ｀*)?⠀Blank Look 35
（＊｀〇Д〇）？⠀Blank Look 36
(*OчO*)⠀Blank Look 37
（*・∧・*）?⠀Blank Look 38
(*。0 – 0。*)？⠀Blank Look 39
（●´・×・｀●）？⠀Blank Look 40
?(ο´･д･)??⠀Blank Look 41
(⊙＿⊙<#8217<)⠀Blank Look 42
٩(͡๏̯͡๏)۶⠀Raised Arms 1
(」・ω・)」⠀Raised Arms 2
(」゜ロ゜)」⠀Raised Arms 3
(」ﾟヘﾟ)」⠀Raised Arms 4
(」ﾟﾛﾟ)｣⠀Raised Arms 5
(❀｣╹□╹)｣*･⠀Raised Arms 6
(」๏้♓๏้)」⠀Raised Arms 7
ι(´Д`ι)⠀Raised Arms 8
( ｣｡╹o╹｡)｣⠀Raised Arms 9
ƪ(•̃͡•̃͡ ƪ⠀Raised Arms 10
(」｡≧□≦)」⠀Raised Arms 11
(」ﾟДﾟ)」⠀Raised Arms 12
(」°ロ°)」⠀Raised Arms 13
ʅฺ(・ω・。)ʃฺ？？⠀Raised Arms 14
(。「´-ω・)ﾝ？⠀Raised Arms 15
(*「･ω･)ﾝ？⠀Raised Arms 16
(屮゜Д゜)屮⠀Raised Hands 1
щ(゜ロ゜щ)⠀Raised Hands 2
щ(ºДºщ)⠀Raised Hands 3
ლ(ಠ_ಠლ)⠀Raised Hands 4
(ლಠ益ಠ)ლ⠀Raised Hands 5
ლ(ٱ٥ٱლ)⠀Raised Hands 6
щ(ﾟдﾟщ)⠀Raised Hands 7
ლ(｡-﹏-｡ ლ)⠀Raised Hands 8
ლ(∘◕‵ƹ′◕ლ)⠀Raised Hands 9
꜡( ˃ ﹆̬ ˂꜡)⠀Raised Hands 10
ლ(<< ิ益 ิ<‘ლ)⠀Raised Hands 11
Щ(º̩̩́Дº̩̩̀щ)⠀Raised Hands 12
ლ(́⚈人⚈‵ლ)⠀Raised Hands 13
щ(▼ﾛ▼щ)⠀Raised Hands 14
щ(´Д｀щ)⠀Raised Hands 15
щ(｀D´#щ)⠀Raised Hands 16
щ(ﾟﾛﾟщ)⠀Raised Hands 17
Щ(◣д◢)艸⠀Raised Hands 18
ლ(ಠ_ಠ ლ）⠀Raised Hands 19
ლ(´Д`ლ)⠀Raised Hands 20
ლ(ಥ Д ಥ )ლ⠀Raised Hands 21
щ(ಥдಥщ)⠀Raised Hands 22
ಠ_ರೃ⠀Quizzical 1
( •᷄ὤ•᷅)？⠀Quizzical 2
(⊙_◎)⠀Quizzical 3
(⊙_☉)⠀Quizzical 4
(⊙.☉)7⠀Quizzical 5
⁀⊙﹏☉⁀⠀Quizzical 6
●.◉⠀Quizzical 7
(｡☉︵ ಠ╬)⠀Quizzical 8
(๑•̌.•̑๑)ˀ̣ˀ̣⠀Quizzical 9
ʕ•ૅૄ•ʔ⠀Quizzical 10
(๑•ૅૄ•๑)⠀Quizzical 11
| ͠° ▃ °͠ |⠀Quizzical 12
( -_・)?⠀Quizzical 13
▐ ˵ ͠° (oo) °͠ ˵ ▐⠀Quizzical 14
(。ヘ°)⠀General Confusion 1
(´｀<) ？⠀General Confusion 2
( ?´_ゝ｀)⠀General Confusion 3
ヾ(´･ ･｀｡)ノ”⠀General Confusion 4
ヽ(゜Q。)ノ？⠀General Confusion 5
?(*´･д･)ﾉ⠀General Confusion 6
(，，ﾟДﾟ)∩⠀General Confusion 7
（（´‐公‐｀））⠀General Confusion 8
<<<<｜＾□＾#｜/⠀General Confusion 9
(￣■￣<)!?⠀General Confusion 10
(<><<囗＜?)⠀General Confusion 11
( ⌡ ຶम⌡ ຶ )⠀General Confusion 12
(๑ಕ̴ _̆ ಕ̴) ﾝ？⠀General Confusion 13
(ﾟДﾟ?)⠀General Confusion 14
?(°Д°≡°Д°)?⠀General Confusion 15
(♠_♦)⠀General Confusion 16
(C_C)⠀General Confusion 17
( ⧉ ⦣ ⧉ )⠀General Confusion 18
¿(❦﹏❦)?⠀General Confusion 19
(<´@へ@｀)⠀General Confusion 20
( ؕؔʘ̥̥̥̥ ه ؔؕʘ̥̥̥̥ )?⠀Complex 1
﴾͡๏̯͡๏﴿⠀Complex 2
`(๑ △ ๑)`*⠀Complex 3
٩(̾●̮̮̃̾•̃̾)۶⠀Complex 4
˞͛꒰๑ऀ •̆ꈊ͒ू•̆๑ऀ꒱⁇⠀Complex 5
( ؔ⚈͟ ◡ ؔ⚈͟ ๑)…ﾝ？⠀Complex 6
»ू(͒ˑ•᷄͡ꇵ͒•᷅͒)ू?!⠀Complex 7
(૦ୂ૦ॢ)ɂ̥Ɂ̥⠀Complex 8
(⸝⸝⸝՞̐ˀ̝՞̐ू)˖̛̠͉⠀Complex 9
⅀(╹╹͞ू)՞✰⁎⠀Complex 10
(•ॢ՞˝̼̮՞)•••Ɂ̥⠀Complex 11
(◕ฺ ▿ฺ ◕ฺ)??⠀Complex 12
ɿ(｡･ɜ･)ɾⓌⓗⓨ？⠀Words 1
ɿ(｡･ɜ･)ɾⓌⓗⓐⓣ？⠀Words 2
(｢๑•₃•)｢ ʷʱʸ?⠀Words 3
(ㆀ˘･з･˘)ωҺaｔ？⠀Words 4
Ⓦⓗⓐⓣ(☉൧ ಠ ꐦ)⠀Words 5
(ㆀ˘･з･˘)ωҺa ƭ？⠀Words 6
Σ(‘Д’⁕)ահɑԵ’Տ up !?⠀Words 7
(」ﾟﾛﾟ)｣NOOOooooo━⠀Words 8
ヘ（。□°）ヘ⠀Flailing Arms 1
(☉ε　⊙ﾉ)ﾉ⠀Flailing Arms 2
＼(●o○<)ノ⠀Flailing Arms 3
＼(☆o◎)／⠀Flailing Arms 4
⁀⊙﹏☉⁀⠀Flailing Arms 5
¯\(°_o)/¯⠀Flailing Arms 6
~(๑ñ﹏ ⊙☆)ノ⠀Flailing Arms 7
ヾ (✿＞﹏ ⊙〃)ノ⠀Flailing Arms 8
ヽ(。_°)ノ⠀Flailing Arms 9
ヽ(｡ゝω・｡)ﾉ⠀Flailing Arms 10
ヾ(｡ꏿ﹏ꏿ)ﾉﾞ⠀Flailing Arms 11
ヽ(‘ ∇‘ )ノ⠀Flailing Arms 12
ヾ(@゜∇゜@)ノ⠀Flailing Arms 13
ヾ(@°▽°@)ノ⠀Flailing Arms 14
ヽ(゜Q。)ノ⠀Flailing Arms 15
Σ(♡＠﹏ ＠☆)ﾉ”⠀Flailing Arms 16
щ (*ㅇ△ Φ☆)ノ⠀Flailing Arms 17
へ(゜∇、°)へ⠀Flailing Arms 18
ヘ（゜◇、゜）ノ⠀Flailing Arms 19
ヘ(゜Д、゜)ノ⠀Flailing Arms 20
ヘ(°◇、°)ノ⠀Flailing Arms 21
ミ●﹏☉ミ⠀Flailing Arms 22
⁽⁽◝(ˊʂ˴⁎)◞՞⠀Flailing Arms 23
ヽ(°▽、°)ﾉ⠀Flailing Arms 24
(ლ ۞ิ ჴ ۞ิ)ლ⠀Flailing Arms 25
(/●◔∀◐●)/⠀Flailing Arms 26
ヾ|`･､●･|ﾉ⠀Flailing Arms 27
(ノ)ʘ﹃ʘ(ヾ)⠀Flailing Arms 28
＼(´◓Д◔`)／⠀Flailing Arms 29
◝₍ᴑ̑ДO͝₎◞⠀Flailing Arms 30
(╯⊙ ⊱⊙╰ )⠀Flailing Arms 31
੧| ⊗ ▾ ⊗ |୨⠀Flailing Arms 32
⊂(©෴©)つ⠀Flailing Arms 33
ゞ(ↂ ω ↂ)ゞ⠀Flailing Arms 34
ﾍ(ﾟ∇ﾟﾍ)⠀Flailing Arms 35
(⑅ 「O_o)「⠀Flailing Arms 36
(⑅∫°ਊ°)∫⠀Flailing Arms 37
ヽ(๏∀◕ )ﾉ⠀Flailing Arms 38
へ[ ᴼ ▃ ᴼ ]_/¯⠀Flailing Arms 39
(｡□ﾟﾉ)ﾉ⠀Flailing Arms 40
Σ(+Oдo<艸<)⠀Flailing Arms 41
⁽⁽◝(∗ ❛⃘ ꒫ ❜⃘⃘ ∗)◜⁾⁾⠀Flailing Arms 42
⁽⁽◝(๑꒪່౪̮꒪່๑)◜⁾⁾≡₍₍◞(๑꒪່౪̮꒪່๑)◟₎₎⠀Flailing Arms 43
┌(｡°з ┐ )┘三└( ┌ ε°｡)┐┘⠀Flailing Arms 44
(⊙﹏⊙✿)⠀Crazy Eyes 1
(⊙_◎)⠀Crazy Eyes 2
(♠_♦)⠀Crazy Eyes 3
( ख़ืིڞ◟྄ख़ืི)⠀Crazy Eyes 4
(｡☉౪ ⊙｡)⠀Crazy Eyes 5
(๑꒪͒∀꒪͒๑)⠀Crazy Eyes 6
(ּơ̑ළּơ̑)⠀Crazy Eyes 7
(ʺʘੂ๔̈ੁʘੂ)⠀Crazy Eyes 8
⊙_ʘ⠀Crazy Eyes 9
◴_◶⠀Crazy Eyes 10
◖|◔◡◉|◗⠀Crazy Eyes 11
˛˛(๑ּగ˞ּగ๑) ̉ ̉⠀Crazy Eyes 12
ಠ ּ͜೦⠀Crazy Eyes 13
( ◎⃝⃘∀◎⃝⃘ )⠀Crazy Eyes 14
⊆◍益◍⊇⠀Crazy Eyes 15
(＊☉౪ ⊙｡)⠀Crazy Eyes 16
∑（*☼＿☉*）⠀Crazy Eyes 17
(╬☉д⊙)⊰⊹ฺ⠀Crazy Eyes 18
~(-◎ω◎)⠀Crazy Eyes 19
~(-◎y◎)⠀Crazy Eyes 20
(◎ω◎*)⠀Crazy Eyes 21
( ◎⃝✦⃟ོ◎⃝ )⠀Crazy Eyes 22
(◦△☆)~~!!!⠀Crazy Eyes 23
（͡°͜ʖ͡°）⠀Crazy Eyes 24
✦⍜✧⠀Crazy Eyes 25
v(〄_〄)v⠀Crazy Eyes 26
(。ヘ°)⠀Small Eyes 1
(゜▼゜＊）⠀Small Eyes 2
(゜▽゜<)⠀Small Eyes 3
`(๑ △ ๑)`*⠀Small Eyes 4
(*ﾟ∀ﾟ*)⠀Small Eyes 5
(*°∀°)⠀Small Eyes 6
ъ川ﾟд^川⠀Small Eyes 7
(o≧▽ﾟ)o⠀Small Eyes 8
Σ(・A゜)⠀Small Eyes 9
┏( .-. ┏ ) ┓⠀Miscellaneous Craziness 1
( ┐΄✹ਊ✹)┐⠀Miscellaneous Craziness 2
σ(●ﾟ┏∀┛｡●)ﾉ⠀Miscellaneous Craziness 3
.(⁎ꈍ﹃ก⁎)๛⠀Miscellaneous Craziness 4
ര.༵ര⠀Miscellaneous Craziness 5
(/・・)ノ⠀Dancing to the Right with Arms Up 1
(ﾉ･ｪ･)ﾉ⠀Dancing to the Right with Arms Up 2
(ﾉ*ﾟｰﾟ)ﾉ⠀Dancing to the Right with Arms Up 3
(ノ￣ー￣)ノ⠀Dancing to the Right with Arms Up 4
( ﾉ^ω^)ﾉﾟ⠀Dancing to the Right with Arms Up 5
(*ﾉ´□`)ﾉ⠀Dancing to the Right with Arms Up 6
(ﾉ･o･)ﾉ⠀Dancing to the Right with Arms Up 7
(ノ‥)ノ⠀Dancing to the Right with Arms Up 8
(ノ´＿ゝ｀）ノ⠀Dancing to the Right with Arms Up 9
(ノ^_^)ノ⠀Dancing to the Right with Arms Up 10
(ノ^o^)ノ⠀Dancing to the Right with Arms Up 11
(ノ￣ω￣)ノ⠀Dancing to the Right with Arms Up 12
(ノ°ο°)ノ⠀Dancing to the Right with Arms Up 13
(ﾉ≧∀≦)ﾉ⠀Dancing to the Right with Arms Up 14
(ﾉﾟ▽ﾟ)ﾉ⠀Dancing to the Right with Arms Up 15
〈( ^.^)ノ⠀Dancing to the Right with Arms Up 16
ヾ(⌐■_■)ノ♪⠀Dancing to the Right with Arms Up 17
ヽ(⌐■_■)ノ♪♬⠀Dancing to the Right with Arms Up 18
(｢･ω･)｢⠀Dancing to the Right with Arms Up 19
(┌ﾟдﾟ)┌⠀Dancing to the Right with Arms Up 20
♪(┌・。・)┌⠀Dancing to the Right with Arms Up 21
(｢`･ω･)｢⠀Dancing to the Right with Arms Up 22
ヾ( ͝° ͜ʖ͡°)ノ♪⠀Dancing to the Right with Arms Up 23
(ﾉ´∀｀)ﾉ⠀Dancing to the Right with Arms Up 24
(ノ〝∩｡∩)ﾉ⠀Dancing to the Right with Arms Up 25
┛´Д｀┃┛))⠀Dancing to the Right with Arms Up 26
(ノ´m｀)ノ⠀Dancing to the Right with Arms Up 27
(Г・ω・)г⠀Dancing to the Right with Arms Up 28
(´「^o^)「⠀Dancing to the Right with Arms Up 29
(ﾉﾟ⊿ﾟ)ﾉ⠀Dancing to the Right with Arms Up 30
＼(ﾟｰﾟ＼)⠀Dancing to the Left with Arms Up 1
ヽ(･ω･ゞ)⠀Dancing to the Left with Arms Up 2
ヽ(^‥^=ゞ)⠀Dancing to the Left with Arms Up 3
＼(^ω^＼)⠀Dancing to the Left with Arms Up 4
ヾ(-_- )ゞ⠀Dancing to the Left with Arms Up 5
ヽ(<^o^ヽ)⠀Dancing to the Left with Arms Up 6
ヾ(´▽｀<)ゝ⠀Dancing to the Left with Arms Up 7
ヾ(^ ^ゞ⠀Dancing to the Left with Arms Up 8
ヾ(^^ゞ)⠀Dancing to the Left with Arms Up 9
ヾ(ﾟ∀ﾟゞ)⠀Dancing to the Left with Arms Up 10
ヽ(ﾟｰﾟ*ヽ)⠀Dancing to the Left with Arms Up 11
ヘ(^_^ヘ)⠀Dancing to the Left with Arms Up 12
ヘ(^o^ヘ)⠀Dancing to the Left with Arms Up 13
ヘ(￣ー￣ヘ)⠀Dancing to the Left with Arms Up 14
ヘ(￣ω￣ヘ)⠀Dancing to the Left with Arms Up 15
乁( ˙ ω˙乁)⠀Dancing to the Left with Arms Up 16
˺⁽ˆ⁰ˆ˺ ⁾˺⠀Dancing to the Left with Arms Up 17
ﾍ(´∀｀ﾍ)⠀Dancing to the Left with Arms Up 18
ヽ(∩。∩゛ヽ)⠀Dancing to the Left with Arms Up 19
ゝ(▽｀*ゝ)⠀Dancing to the Left with Arms Up 20
ヾ(´▽｀*<)ゝ”⠀Dancing to the Left with Arms Up 21
へ(ﾟ◇ﾟへ)⠀Dancing to the Left with Arms Up 22
♪L(´▽｀L )♪⠀Dancing to the Left with Arms Up 23
ヾ(￣ー￣ヾ)⠀Dancing to the Left with Arms Up 24
ヘ(´m｀ヘ)⠀Dancing to the Left with Arms Up 25
ヘ(^0^)ヘ⠀Dancing to the Left with Arms Up 26
＼(^▽^＠)ノ⠀Dancing Forwards with Arms Up 1
ヽ(*ﾟｰﾟ*)ﾉ⠀Dancing Forwards with Arms Up 2
ヽ( °◇°)ノ⠀Dancing Forwards with Arms Up 3
ヾ(･ω･*)ﾉ⠀Dancing Forwards with Arms Up 4
ヾ(＠^∇^＠)ノ⠀Dancing Forwards with Arms Up 5
ヾ(*´∇`)ﾉ⠀Dancing Forwards with Arms Up 6
ヽ(*´Д｀*)ﾉ⠀Dancing Forwards with Arms Up 7
ヾ（*⌒ヮ⌒*）ゞ⠀Dancing Forwards with Arms Up 8
ヾ(*д*)ﾉ⠀Dancing Forwards with Arms Up 9
ヽ(´ー`)ﾉ⠀Dancing Forwards with Arms Up 10
ヽ(°◇° )ノ⠀Dancing Forwards with Arms Up 11
ƪ(˘⌣˘)ʃ⠀Dancing Forwards with Arms Up 12
╰(°ㅂ°)╯⠀Dancing Forwards with Arms Up 13
₍₍⁽⁽(ી(^‿ゝ^)ʃ)₎₎⁾⁾⠀Dancing Forwards with Arms Up 14
₍₍⁽⁽(ી(´<ω<` )ʃ)₎₎⁾⁾⠀Dancing Forwards with Arms Up 15
ヾ｜￣ー￣｜ﾉ⠀Dancing Forwards with Arms Up 16
ヘ| ´ω｀ |ﾉ⠀Dancing Forwards with Arms Up 17
└( ＾ω＾ )」⠀Dancing Forwards with Arms Up 18
┗(｀O´)┛⠀Dancing Forwards with Arms Up 19
└| ∵ |┘⠀Dancing Forwards with Arms Up 20
♪└|∵|┘♪⠀Dancing Forwards with Arms Up 21
└(･･ ･･･)」⠀Dancing Forwards with Arms Up 22
⁽⁽(ી₍₍⁽⁽(ી⁽⁽(ી₍₍⁽⁽(ી( ˆoˆ )ʃ)₎₎⁾⁾ʃ)₎₎ʃ)₎₎⁾⁾ʃ)₎₎⠀Dancing Forwards with Arms Up 23
（〜^∇^)〜⠀Dancing to the Right with Arms to the Side or Down 1
(〜￣△￣)〜⠀Dancing to the Right with Arms to the Side or Down 2
(。⌒∇⌒)。⠀Dancing to the Right with Arms to the Side or Down 3
(~‾⌣‾)~⠀Dancing to the Right with Arms to the Side or Down 4
(~‾▿‾)~⠀Dancing to the Right with Arms to the Side or Down 5
(~’.’)~⠀Dancing to the Right with Arms to the Side or Down 6
(~￣▽￣)~⠀Dancing to the Right with Arms to the Side or Down 7
(~˘▾˘)~⠀Dancing to the Right with Arms to the Side or Down 8
(o^^)o⠀Dancing to the Right with Arms to the Side or Down 9
ˋ̧̧̖⁽⁽༼ ु˳̮̑̈༽ु⁾⁾ˋ̧̧̖♪⠀Dancing to the Right with Arms to the Side or Down 10
(o´･_･)っ⠀Dancing to the Right with Arms to the Side or Down 11
（゛８＾－＾）８ﾞ⠀Dancing to the Right with Arms to the Side or Down 12
（゛８＾－＾）８ﾞ⠀Dancing to the Right with Arms to the Side or Down 13
|o∵|o⠀Dancing to the Right with Arms to the Side or Down 14
(Φ￣▽￣)Φ”⠀Dancing to the Right with Arms to the Side or Down 15
。(⌒∇⌒。)⠀Dancing to the Left with Arms to the Side or Down 1
〜(￣△￣〜)⠀Dancing to the Left with Arms to the Side or Down 2
〜(^∇^〜）⠀Dancing to the Left with Arms to the Side or Down 3
~(‾⌣‾~)⠀Dancing to the Left with Arms to the Side or Down 4
~(‾▿‾~)⠀Dancing to the Left with Arms to the Side or Down 5
~(‘.’~)⠀Dancing to the Left with Arms to the Side or Down 6
~(˘▾˘~)⠀Dancing to the Left with Arms to the Side or Down 7
o(^^o)⠀Dancing to the Left with Arms to the Side or Down 8
◟(ꉺᴗꉺ๑◝)⠀Dancing to the Left with Arms to the Side or Down 9
˄̙ ̊₍₍◟(⁰^⁰∗)⌟˄̙ ̊⠀Dancing to the Left with Arms to the Side or Down 10
o(ﾟｰﾟ*o)⠀Dancing to the Left with Arms to the Side or Down 11
８（＾－＾゛８）⠀Dancing to the Left with Arms to the Side or Down 12
o|∵o|⠀Dancing to the Left with Arms to the Side or Down 13
“Φ(￣▽￣Φ)⠀Dancing to the Left with Arms to the Side or Down 14
7(^-^7)⠀Dancing to the Left with Arms to the Side or Down 15
₍₍ ◝(・ω・)◟ ⁾⁾⠀Dancing Forwards with Arms to the Side or Down 1
~(‾▿‾)~⠀Dancing Forwards with Arms to the Side or Down 2
~(˘▾˘)~⠀Dancing Forwards with Arms to the Side or Down 3
⁽⁽◝( •௰• )◜⁾⁾⠀Dancing Forwards with Arms to the Side or Down 4
₍₍◞( •௰• )◟₎₎⠀Dancing Forwards with Arms to the Side or Down 5
╭(°ㅂ°)╮⠀Dancing Forwards with Arms to the Side or Down 6
〜(꒪꒳꒪<)〜⠀Dancing Forwards with Arms to the Side or Down 7
〜(꒪꒳꒪)〜⠀Dancing Forwards with Arms to the Side or Down 8
⁽⁽⁕◟(.öˬö.)◞⁕⁾⁾⠀Dancing Forwards with Arms to the Side or Down 9
ح˚௰˚づ⠀Dancing Forwards with Arms to the Side or Down 10
✺◟(∗❛ัᴗ❛ั∗)◞✺⠀Dancing Forwards with Arms to the Side or Down 11
₍₍(꒪່౪̮꒪່)⁾⁾⠀Dancing Forwards with Arms to the Side or Down 12
♪.*⁽⁽ ◝꒰´꒳`∗꒱◟ ₎₎₊·*⠀Dancing Forwards with Arms to the Side or Down 13
₍₍◝(°꒳°*)◜₎₎⠀Dancing Forwards with Arms to the Side or Down 14
१|˚–˚|५⠀Dancing Forwards with Arms to the Side or Down 15
₍₍ ◝( ･’ω’･ )◟ ⁾⁾⠀Dancing Forwards with Arms to the Side or Down 16
₍₍ ◝(　ﾟ∀ ﾟ )◟ ⁾⁾⠀Dancing Forwards with Arms to the Side or Down 17
┏(｀o´)┓⠀Dancing Forwards with Arms to the Side or Down 18
“:♡.•♬✧⁽⁽ଘ( ˊᵕˋ )ଓ⁾⁾*+:•*∴⠀Dancing Forwards with Arms to the Side or Down 19
(（（（o┤｀･ｪ･´├o））））)⠀Dancing Forwards with Arms to the Side or Down 20
((┌|o^▽^o|┘))♪⠀One Arm Up and One Arm Down 1
┌(・。・)┘♪⠀One Arm Up and One Arm Down 2
┌(˘⌣˘)ʃ⠀One Arm Up and One Arm Down 3
┌（★ｏ☆）┘⠀One Arm Up and One Arm Down 4
┌(ﾟдﾟ)┘⠀One Arm Up and One Arm Down 5
┌|゜з゜｜┘⠀One Arm Up and One Arm Down 6
┌|°з°|┘⠀One Arm Up and One Arm Down 7
┌U･ｪ･U┘⠀One Arm Up and One Arm Down 8
┏((＝￣(ｴ)￣=))┛⠀One Arm Up and One Arm Down 9
┏(｀ー´)┛⠀One Arm Up and One Arm Down 10
┏(＾0＾)┛⠀One Arm Up and One Arm Down 11
└(^o^)┐⠀One Arm Up and One Arm Down 12
└(=^‥^=)┐⠀One Arm Up and One Arm Down 13
└（★ｏ★）┐⠀One Arm Up and One Arm Down 14
└(ﾟдﾟ)┐⠀One Arm Up and One Arm Down 15
└@(･ｪ･)@┐⠀One Arm Up and One Arm Down 16
└｜゜ε゜｜┐⠀One Arm Up and One Arm Down 17
└|°ε°|┐⠀One Arm Up and One Arm Down 18
┗(｀ー´)┓⠀One Arm Up and One Arm Down 19
┗(＾0＾)┓⠀One Arm Up and One Arm Down 20
♪((└|o^▽^o|┐))⠀One Arm Up and One Arm Down 21
ƪ(‾.‾“)┐⠀One Arm Up and One Arm Down 22
ƪ(˘⌣˘)┐⠀One Arm Up and One Arm Down 23
⌌⌈╹드╹⌉⌏⠀One Arm Up and One Arm Down 24
┌|*ﾟｏﾟ|┘⠀One Arm Up and One Arm Down 25
┌|*ﾟ０ﾟ|┘⠀One Arm Up and One Arm Down 26
┌|*ﾟ-ﾟ|┘⠀One Arm Up and One Arm Down 27
┌|*ﾟ｡ﾟ|┘⠀One Arm Up and One Arm Down 28
⌌⌈╹므╹⌉⌏⠀One Arm Up and One Arm Down 29
┌༼▀̿̿Ĺ̯̿̿▀̿༽┘⠀One Arm Up and One Arm Down 30
↙(ↂ⼼_ↂ)↗⠀One Arm Up and One Arm Down 31
┌(▼▼メ)┘⠀One Arm Up and One Arm Down 32
└( ▼▼ )┐⠀One Arm Up and One Arm Down 33
┌(メ▼▼)┘⠀One Arm Up and One Arm Down 34
┌|ﾟзﾟ|┘⠀One Arm Up and One Arm Down 35
└|ﾟεﾟ|┐⠀One Arm Up and One Arm Down 36
┌|ﾟэﾟ|┘⠀One Arm Up and One Arm Down 37
♫ ┌༼ຈل͜ຈ༽┘ ♪⠀One Arm Up and One Arm Down 38
┗(｀o´)┓⠀One Arm Up and One Arm Down 39
┏(｀○´)┛⠀One Arm Up and One Arm Down 40
└|∵┌|⠀One Arm Up and One Arm Down 41
|┐∵|┘⠀One Arm Up and One Arm Down 42
♪└|∵|┐♪⠀One Arm Up and One Arm Down 43
♪┌|∵|┘♪⠀One Arm Up and One Arm Down 44
┌(★o☆)┘⠀One Arm Up and One Arm Down 45
└(★o★)┐⠀One Arm Up and One Arm Down 46
┌(☆o★)┘⠀One Arm Up and One Arm Down 47
┌|≧∇≦|┘⠀One Arm Up and One Arm Down 48
♪┏(・o･)┛♪⠀One Arm Up and One Arm Down 49
⌎⌈╹우╹⌉⌍⠀One Arm Up and One Arm Down 50
(._.) ƪ(‘-‘ ƪ)(ʃ ‘-‘)ʃ (/._.)/⠀Multiple Kaomojis Dancing 1
˓˓(ृ　 ु ॑꒳’)ु(ृ’꒳ ॑ ृ　)ु˒˒˒⠀Multiple Kaomojis Dancing 2
♪(((#^-^)八(^_^*)))♪⠀Multiple Kaomojis Dancing 3
ʅ(◔౪◔ʅ)三(ʃ◔౪◔)ʃ⠀Multiple Kaomojis Dancing 4
♫͙◟̊₍ꃓ₎◞◟₍ꃔ₎◞̊♫͙⠀Multiple Kaomojis Dancing 5
♪～(◔◡◔ิ)人(╹◡╹๑)～♪⠀Multiple Kaomojis Dancing 6
˄̞⁽⁽୧(꒪ͦᴗ̵̍꒪ͦ=͟͟͞͞ ꒪ͦ ˈ̫̮ ꒪ͦ)୨⁾⁾˄̩̞⠀Multiple Kaomojis Dancing 7
\(ϋ)/\(ϋ)/♩⠀Multiple Kaomojis Dancing 8
♪ヽ(▽￣ )ﾉ/(＿△＿)ヽ( ￣▽)ﾉ⠀Multiple Kaomojis Dancing 9
♪♪＼(^ω^＼)( /^ω^)/♪♪⠀Multiple Kaomojis Dancing 10
ヽ(○｀･v･)人(･v･´●)ﾉ⠀Multiple Kaomojis Dancing 11
♪(o=゜▽゜)人(゜▽゜=o)♪⠀Multiple Kaomojis Dancing 12
L(‘ω’)┘三└(‘ω’)」⠀Multiple Kaomojis Dancing 13
┗( ^o^)┛≡┏( ^o^)┓≡┗( ^o^)┛⠀Multiple Kaomojis Dancing 14
╭(°ㅂ°)╮╰(°ㅂ°)╯╭(°ㅂ°)╮╰(°ㅂ°)╯⠀Multiple Kaomojis Dancing 15
♪└|ﾟ皿ﾟ |┐♪└| ﾟ皿ﾟ |┘♪┌| ﾟ皿ﾟ|┘♪⠀Multiple Kaomojis Dancing 16
(✖╭╮✖)⠀X Eyes 1
(´×ω×`)⠀X Eyes 2
ヽ༼xل͜x༽ﾉ⠀X Eyes 3
(×_×<）⠀X Eyes 4
(✖´╹‸╹`✖)⠀X Eyes 5
(X_X) ☜ (◉▂◉ )⠀X Eyes 6
(×_×#⠀X Eyes 7
꒰ლ✘ㅿ✘ლ꒱⠀X Eyes 8
१|✘`皿′✘|५⠀X Eyes 9
(=ｘェｘ=)⠀X Eyes 10
(´×д×`三꒪д꒪ <)⠀X Eyes 11
╭✖⊆✖╮⠀X Eyes 12
（x_x；）⠀X Eyes 13
(⁎×ㅂ×⁎)༘⠀X Eyes 14
(((＼（✘෴✘）／)))⠀X Eyes 15
✖‿✖⠀X Eyes 16
¿ⓧ_ⓧﮌ⠀X Eyes 17
⊆✕ڡ✕⊇⠀X Eyes 18
꒰✘Д✘◍꒱⠀X Eyes 19
( ✖ ਊ ✖)⠀X Eyes 20
( ×m×）⠀X Eyes 21
ヾ(×× ) ﾂ⠀X Eyes 22
⁽͑˙˟́˙̭˟̀˙⁾̉⠀X Eyes 23
Ｕ×Å×Ｕ⠀X Eyes 24
٩(×̯×)۶⠀X Eyes 25
c༽✖﹏✖༼ᓄ⠀X Eyes 26
･ﾟﾟ･(×_×)･ﾟﾟ･｡⠀X Eyes 27
╭( ✖_✖ )╮⠀X Eyes 28
ヽ༼, ͡X ͜ʖ ͡X,༽ﾉ⠀X Eyes 29
┌╏✖_✖╏┘⠀X Eyes 30
(✖﹏✖)⠀X Eyes 31
୧| ✖ ﹏ ✖ |୨⠀X Eyes 32
( ✖ ︿ ✖ )⠀X Eyes 33
໒( ” x ͟ʖ x ” )७⠀X Eyes 34
║ : x ل͜ x : ║⠀X Eyes 35
୧༼ ” ✖ ‸ ✖ ” ༽୨⠀X Eyes 36
(ꀻꎁꀻ )⠀X Eyes 37
╰▐ ✖ 〜 ✖ ▐╯⠀X Eyes 38
( x ~ x )⠀X Eyes 39
（*ｘ＿ｘ）⠀X Eyes 40
（×ω×）⠀X Eyes 41
(×□×；)⠀X Eyes 42
∑(✘Д✘๑)⠀X Eyes 43
Σ(×_×<)!⠀X Eyes 44
¯\_| ✖ 〜 ✖ |_/¯⠀X Eyes 45
* ूི×̺͡×ू ྀ⁎*☠⁎ꂚ*ᵎᵎᵎ⠀X Eyes 46
꒰⁎×﹏×⁎꒱ ༘ؓ ँั๊ྃ⠀X Eyes 47
┌▒ ⊗ ▃ ⊗ ▒┐⠀X Eyes 48
（（（（（（BOMB）））））） ⌒⌒⌒⌒⌒／(x~x)＼⠀X Eyes 49
(#+_+)⠀+ Eyes 1
(+_+)⠀+ Eyes 2
(｡´✚ฺω✚ฺ｀｡)⠀+ Eyes 3
(´+ω+｀)⠀+ Eyes 4
༼ +ل͟+ ༽⠀+ Eyes 5
(+o+)⠀+ Eyes 6
Σ(＋Θ＋)<⠀+ Eyes 7
ゞ(++) シ⠀+ Eyes 8
〓■●＿ ～ □○0⠀Ghosts 1
〓■●～～=□○0⠀Ghosts 2
m(~ー~m)～⠀Ghosts 3
～(m~ー~)m⠀Ghosts 4
m(~ｰ~m)~⠀Ghosts 5
0(:3　)～ =͟͟͞͞(’､3)_ヽ)＿⠀Ghosts 6
ꐑ(*ꐌ◡ꐌꐐ*)࿐࿔࿓⠀Ghosts 7
m(@益@m)～⠀Ghosts 8
†┏┛墓┗┓† ~((～~~(m￣(ｴ)￣)m⠀Ghosts 9
・・・・・～～～～～～～(m￣ー￣)m⠀Ghosts 10
ー=≡Σ[▓▓]ε¦)　　ー=≡Σ( ε¦) 0⠀Ghosts 11
m(ﾟДﾟm)～【†】～(m´ρ`)m⠀Ghosts 12
⎧ᴿᴵᴾ⎫◟◟◟◟◟◟◟◟ ❀◟(ó ̯ ò, )⠀Funerals 1
~~(m´□｀)/ﾟ･:*†┏┛呪┗┓†*:･ﾟ＼(´□｀m)~~⠀Funerals 2
(ñ_ñ)⠀Miscellaneous 1
(u_u)⠀Miscellaneous 2
(ヘ。ヘ)⠀Miscellaneous 3
ｍ（＿　＿；；ｍ⠀Miscellaneous 4
彡(-_-<)彡⠀Miscellaneous 5
(-Ω-メ)⠀Miscellaneous 6
(＊0＊<)⠀Miscellaneous 7
(*_*)⠀Miscellaneous 8
(o_-)⠀Miscellaneous 9
(º_º)⠀Miscellaneous 10
（Ω_Ω）⠀Miscellaneous 11
≖‿≖⠀Miscellaneous 12
(≖͞_≖̥)⠀Miscellaneous 13
Σ(๑+⌓ o｡)シ⠀Miscellaneous 14
へ（<><<_<<<<へ)⠀Miscellaneous 15
(｡≍ฺ‿ฺ≍ฺ)⠀Miscellaneous 16
ฅ^•ﻌ•^ฅ⠀Stylized or Just Plain Awesome Dogs 1
੯ੁૂ‧̀͡u⠀Stylized or Just Plain Awesome Dogs 2
(❍ᴥ❍ʋ)⠀Stylized or Just Plain Awesome Dogs 3
₍ᐢ•ﻌ•ᐢ₎*･ﾟ｡⠀Stylized or Just Plain Awesome Dogs 4
ཥමཙමཤ⠀Stylized or Just Plain Awesome Dogs 5
ং” ა⠀Stylized or Just Plain Awesome Dogs 6
(^・(I)・^)⠀Dogs with Pointy Ears 1
(^・x・^)⠀Dogs with Pointy Ears 2
ｖ・。・Ｖ⠀Dogs with Pointy Ears 3
V●ᴥ●V⠀Dogs with Pointy Ears 4
V◕ฺω◕ฺV⠀Dogs with Pointy Ears 5
(V●ᴥ●V)⠀Dogs with Pointy Ears 6
∪･ω･∪⠀Big Floppy Ears 1
(U・x・U)⠀Big Floppy Ears 2
┌U･ｪ･U┘⠀Big Floppy Ears 3
ｏ（Ｕ・ω・）⊃⠀Big Floppy Ears 4
U ´꓃ ` U⠀Big Floppy Ears 5
U・♀・U⠀Big Floppy Ears 6
U｡･ｪ･｡U⠀Big Floppy Ears 7
U＾ェ＾U⠀Big Floppy Ears 8
Ｕ^皿^Ｕ⠀Big Floppy Ears 9
U￣ｰ￣U⠀Big Floppy Ears 10
Uo･ｪ･oU⠀Big Floppy Ears 11
ＵＴｪＴＵ⠀Big Floppy Ears 12
(U •́ .̫ •̀ U)⠀Big Floppy Ears 13
(꒪ω꒪υ)⠀Big Floppy Ears 14
(υ◉ω◉υ)⠀Big Floppy Ears 15
Uo-ｪ-oU⠀Big Floppy Ears 16
(Ｕ◕ฺ㉨◕ฺ)ノ⠀Big Floppy Ears 17
(υŏᆺŏυ)⠀Big Floppy Ears 18
ヽUﾟ●_ﾟ*Uﾉ⠀Big Floppy Ears 19
U｡-ｪ-｡U。⠀Big Floppy Ears 20
u(´Д`u)⠀Big Floppy Ears 21
(Ｕ^ω^)⠀Big Floppy Ears 22
(∪＾ω＾)⠀Big Floppy Ears 23
♪o(･x･o∪ ∪o･x･)o♪⠀Big Floppy Ears 24
.+:｡ヽUﾟДﾟUﾉﾟ.+:｡⠀Big Floppy Ears 25
(〓￣(∵エ∵)￣〓)⠀Bulldogs 1
“v(〓￣(∵エ∵)￣〓)v”⠀Bulldogs 2
ヾ(〓￣(∵エ∵)￣〓)⠀Bulldogs 3
▼o・ェ・o▼⠀Triangle Ears 1
▽・ｗ・▽⠀Triangle Ears 2
▽・ω・▽⠀Triangle Ears 3
▿‧͈•̻‧͈▿⠀Triangle Ears 4
▼･。･▼⠀Triangle Ears 5
▽･ｪ･▽ﾉ”⠀Triangle Ears 6
૮( ꒦ິ࿄꒦ີ)ა⠀૮( ꒦ິ࿄꒦ີ)ა Style Dogs 1
૮(•⚈͒࿄⚈͒•)ა⠀૮( ꒦ິ࿄꒦ີ)ა Style Dogs 2
૮( ꒦ິ⍣꒦ີ)ა⠀૮( ꒦ິ࿄꒦ີ)ა Style Dogs 3
૮( ᵒ̌ૢ௰ᵒ̌ૢ )ა⠀૮( ꒦ິ࿄꒦ີ)ა Style Dogs 4
૮(꒦ິཅ꒦ິ)ა⠀૮( ꒦ິ࿄꒦ີ)ა Style Dogs 5
૮( ᵒ̌ૢཪᵒ̌ૢ )ა⠀૮( ꒦ິ࿄꒦ີ)ა Style Dogs 6
૮(¹ ˕̫ ¹)ა⠀૮( ꒦ິ࿄꒦ີ)ა Style Dogs 7
૮(꒦ິ ˙̫̮ ꒦ິ)ა⠀૮( ꒦ິ࿄꒦ີ)ა Style Dogs 8
૮(꒦໊ཅ꒦໊)ა ̉ ̉⠀૮( ꒦ິ࿄꒦ີ)ა Style Dogs 9
૮(•̀ꐧ•́)ა⠀૮( ꒦ິ࿄꒦ີ)ა Style Dogs 10
૮(˳❛ ⌔̫ ❛˳)ა⠀૮( ꒦ິ࿄꒦ີ)ა Style Dogs 11
૮(༎ິཅ༎ິ)ა⠀૮( ꒦ິ࿄꒦ີ)ა Style Dogs 12
૮( ᵒ̌ૢ〰ᵒ̌ૢ )ა⠀૮( ꒦ິ࿄꒦ີ)ა Style Dogs 13
૮( ¯͒▱๋¯͒ )ა⠀૮( ꒦ິ࿄꒦ີ)ა Style Dogs 14
૮(ꎿຶ꒫ꎿຶ)ა⠀૮( ꒦ິ࿄꒦ີ)ა Style Dogs 15
◖⚆ᴥ⚆◗⠀ᴥ Style Dogs 1
⎩ ♨ᴥ♨ ⎭⠀ᴥ Style Dogs 2
-ᄒᴥᄒ-⠀ᴥ Style Dogs 3
[⑇◍ᴥ◍•⑇]⠀ᴥ Style Dogs 4
(ノ ̿ ̿ᴥ ̿ ̿)ノ⠀ᴥ Style Dogs 5
୧༼◕ ᴥ ◕༽୨⠀ᴥ Style Dogs 6
ᕙ༼◕ ᴥ ◕༽ᕗ⠀ᴥ Style Dogs 7
(_/¯⊘_ᴥ_⊘)_/¯⠀ᴥ Style Dogs 8
⊆ↂᴥↂ⊇⠀ᴥ Style Dogs 9
⎰≀.⎔ᴥ⎔≀⎰⠀ᴥ Style Dogs 10
⊂▶ᴥ◀⊃⠀ᴥ Style Dogs 11
°˖✧◝(ਠᴥਠ)◜✧˖°⠀ᴥ Style Dogs 12
(っ⊂•⊃_ᴥ_⊂•⊃)っ⠀ᴥ Style Dogs 13
●ᴥ●⠀ᴥ Style Dogs 14
ヽ(°ᴥ°)ﾉ⠀ᴥ Style Dogs 15
└(°ᴥ°)┘⠀ᴥ Style Dogs 16
┏(°ᴥ°)┓⠀ᴥ Style Dogs 17
へ║ ◉ ᴥ ◉ ║〜⠀ᴥ Style Dogs 18
乁[ ◕ ᴥ ◕ ]ㄏ⠀ᴥ Style Dogs 19
(‷\(ᓄ ᴥ ᓇ)/‴)⠀ᴥ Style Dogs 20
▐ ☯ ᴥ ☯ ▐⠀ᴥ Style Dogs 21
໒( ̿ ᴥ ̿ )७⠀ᴥ Style Dogs 22
໒( ◉ ᴥ ◉ )७⠀ᴥ Style Dogs 23
| * O ᴥ O * |⠀ᴥ Style Dogs 24
٩། ಠ ᴥ ಠ །ᕗ⠀ᴥ Style Dogs 25
୧╏ ~ ᴥ ~ ╏୨⠀ᴥ Style Dogs 26
⋋〳 ￣ ᴥ ￣ 〵⋌⠀ᴥ Style Dogs 27
╏ ◯ ᴥ ◯ ╏⠀ᴥ Style Dogs 28
੧〳 ˵ ಠ ᴥ ಠ ˵ 〵ノ⌒.⠀ᴥ Style Dogs 29
( ͡° ᴥ ͡°)⠀ᴥ Style Dogs 30
…(๑╯ﻌ╰๑)=3⠀ᴥ Style Dogs 31
୧| ⁰ ᴥ ⁰ |୨⠀ᴥ Style Dogs 32
໒(◉ᴥ◉)७⠀ᴥ Style Dogs 33
ᘳ´• ᴥ •`ᘰ⠀ᴥ Style Dogs 34
⁞ ✿ ᵒ̌ ᴥ ᵒ̌ ✿ ⁞⠀ᴥ Style Dogs 35
｜｡･)‐⌒ε==3 ﾍU^ｪ^U⠀Dog Interactions 1
♪♪♪ Ｕ・ｪ・Ｕ人(^･x･^=) ♪♪♪⠀Dog Interactions 2
o(･ω･｡)o—∈･^ミ┬┬~⠀Dog Interactions 3
o(^-^ )o——–⊆^U)┬┬~⠀Dog Interactions 4
o(￣_￣|||)o——–⊆◎U)┬┬ﾉ~”♪♪…⠀Dog Interactions 5
o(^^ )o——–⊆^U)┬┬~…⠀Dog Interactions 6
ヾ(<ﾟ皿ﾟ)ﾉ･･･ ⊆￣U)┬┬ﾉ~”　=3 =3⠀Dog Interactions 7
⊂ﾟＵ┬────┬~⠀Sideways Dogs 1
⊂’Ｕ⠀Sideways Dogs 2
ε==3 ⊆＾ ￣⊇ゝ⠀Sideways Dogs 3
∈･^ミ┬┬~⠀Sideways Dogs 4
⊆^U)┬┬~⠀Sideways Dogs 5
⊆◎U)┬┬⠀Sideways Dogs 6
⊆￣U)┬┬ﾉ~⠀Sideways Dogs 7
ヾ(●ω●)ノ⠀Miscellaneous Dogs 1
(●⌇ຶ ཅ⌇ຶ●)⠀Miscellaneous Dogs 2
└@(･ｪ･)@┐⠀Miscellaneous Dogs 3
Ψ( ◉ཅ◉ )Ψ⠀Miscellaneous Dogs 4
Ψ(●` ཅ ´●)Ψ⠀Miscellaneous Dogs 5
( ͒꒪̛ཅ꒪̛ ͒)✧⠀Miscellaneous Dogs 6
(⌯꒪͒ ૢཅ ૢ꒪͒)｡*ﾟ✧⠀Miscellaneous Dogs 7
Ψ(●°̥̥̥̥̥̥̥̥ ཅ °̥̥̥̥̥̥̥̥●)Ψ⠀Complex 1
(๑•ิཬ•ั๑)⠀Complex 2
༲ྕ༲⠀Complex 3
(❝᷁॔Ꭳ❝᷀॓)⠀Complex 4
“ψ(｀∇´)ψ⠀Evil Hands 1
(ц｀ω´ц*)⠀Evil Hands 2
ψ(*｀ー´)ψ⠀Evil Hands 3
ψ(｀∇´)ψ⠀Evil Hands 4
Ψ(｀▽´)Ψ⠀Evil Hands 5
Ψ(｀◇´)Ψ⠀Evil Hands 6
(屮｀∀´)屮⠀Evil Hands 7
Щ(･｀ω´･Щ)⠀Evil Hands 8
Ψ(￣∀￣)Ψ⠀Evil Hands 9
Ψ(☆ｗ☆)Ψ⠀Evil Hands 10
Ψ( ●｀▽´● )Ψ⠀Evil Hands 11
ψ（｀Д´）ψ⠀Evil Hands 12
ლ(｀∀´ლ)⠀Evil Hands 13
＜(●｀∀´●)＞”⠀Evil Hands 14
o(○｀ω´○)9⠀Evil Hands 15
ρ(｀.´)ρ⠀Evil Hands 16
(○｀ε´○)／＼(○｀ε´○)⠀Evil Teamwork 1
(*-`ω´- )人(*-`ω´- )⠀Evil Teamwork 2
(◞≼◉ื≽◟ <益<◞≼◉ื≽◟)Ψ⠀Demons and Devils 1
^(#｀∀´)_Ψ⠀Demons and Devils 2
^（｀ω´ ）^ψ⠀Demons and Devils 3
←～（o ｀▽´ )oΨ⠀Demons and Devils 4
←~∋(｡Ψ▼ｰ▼)∈⠀Demons and Devils 5
∋━━o(｀∀´oメ）～→⠀Demons and Devils 6
ƪ(`▿▿▿▿´ƪ)⠀Demons and Devils 7
ಠﭛಠ⠀Demons and Devils 8
⁞⁝•ֱ̀␣̍•́⁝⁞⠀Demons and Devils 9
↜(͛ ꒪͒৫͏̈́꒪͒)͛⌰⠀Demons and Devils 10
↑_(ΦwΦ<)Ψ⠀Demons and Devils 11
Ψ(｀∀´#)ﾉ⠀Demons and Devils 12
ψ`ー´)ﾉψ`ー´)ﾉψ`ー´)ﾉψ`ー´)ﾉψ`ー´)ﾉψ`ー´)⠀Demons and Devils 13
(。-`ω´-)⠀General Evilness 1
(=｀(∞)´=)⠀General Evilness 2
(・｀ω´・)⠀General Evilness 3
(｡･｀ω´･｡)⠀General Evilness 4
（｀ー´）⠀General Evilness 5
(｀ε´)⠀General Evilness 6
(｀Д´*)⠀General Evilness 7
（=｀〜´=）⠀General Evilness 8
(=｀ω´=)⠀General Evilness 9
(=｀ェ´=)⠀General Evilness 10
(☼Д☼)⠀General Evilness 11
(σ-`д･´)⠀General Evilness 12
(ﾒ｀ﾛ´)/⠀General Evilness 13
| ｀Д´|⠀General Evilness 14
꒰(@｀꒳´)꒱⠀General Evilness 15
o(｀ω´*)o⠀General Evilness 16
p(｀ε´q）⠀General Evilness 17
ﾍ(｀▽´*)⠀General Evilness 18
(-｀ω´-,,)⠀General Evilness 19
(｀▽´)⠀General Evilness 20
(｀∀´)Ψ⠀General Evilness 21
ψ`ー´)ﾉ⠀General Evilness 22
(･｀ω´･+)⠀General Evilness 23
()`艸´()⠀General Evilness 24
(*｀▽´)_旦~~⠀General Evilness 25
（　｀ハ´）⠀General Evilness 26
` ͜ʖ´⠀General Evilness 27
(ʃƪ¬‿¬)⠀General Evilness 28
٢ ` ౪´ ì⠀General Evilness 29
(((o(*ﾟ▽ﾟ*)o)))⠀Circle Hands 1
o((*^▽^*))o⠀Circle Hands 2
Ｏ(≧▽≦)Ｏ⠀Circle Hands 3
o(〃＾▽＾〃)o⠀Circle Hands 4
o(^▽^)o⠀Circle Hands 5
Ｏ(≧∇≦)Ｏ⠀Circle Hands 6
o(≧∇≦o)⠀Circle Hands 7
σ(≧ε≦ｏ)⠀Circle Hands 8
o(*^▽^*)o⠀Circle Hands 9
⌒°(❛ᴗ❛)°⌒⠀Circle Hands 10
o(^∀^*)o⠀Circle Hands 11
o(^◇^)o⠀Circle Hands 12
《《o(≧◇≦)o》》⠀Circle Hands 13
o(*≧□≦)o⠀Circle Hands 14
o(*<><<ω<<<<*)o⠀Circle Hands 15
(ﾉ･ｪ･)ﾉ⠀Excited to the Right 1
(/^▽^)/⠀Excited to the Right 2
(ﾉ´ヮ´)ﾉ*:･ﾟ✧⠀Excited to the Right 3
(ﾉ≧∀≦)ﾉ⠀Excited to the Right 4
(ﾉ^ヮ^)ﾉ*:・ﾟ✧⠀Excited to the Right 5
(/ ‘з’)/⠀Excited to the Right 6
(۶ꈨຶꎁꈨຶ )۶ʸᵉᵃʰᵎ⠀Excited to the Right 7
⁽(◍˃̵͈̑ᴗ˂̵͈̑)⁽⠀Excited to the Right 8
(╯✧∇✧)╯⠀Excited to the Right 9
Σ(ノ°▽°)ノ⠀Excited to the Right 10
( ƅ°ਉ°)ƅ⠀Excited to the Right 11
ヽ(　･∀･)ﾉ⠀Excited to the Right 12
˭̡̞(◞⁎˃ᆺ˂)◞*✰⠀Excited to the Right 13
(p^-^)p⠀Excited to the Right 14
(ﾉ^∇^)ﾉﾟ⠀Excited to the Right 15
ヽ(〃･ω･)ﾉ⠀Excited to the Right 16
(۶* ‘ꆚ’)۶”⠀Excited to the Right 17
（。＞ω＜）。⠀Excited to the Right 18
（ﾉ｡≧◇≦）ﾉ⠀Excited to the Right 19
ヾ(｡･ω･)ｼ⠀Excited to the Right 20
(ﾉ･д･)ﾉ⠀Excited to the Right 21
.+:｡(ﾉ･ω･)ﾉﾞ⠀Excited to the Right 22
Σ(*ﾉ´<><<ω<<<<｡`)ﾉ⠀Excited to the Right 23
ヾ（〃＾∇＾）ﾉ♪⠀Excited to the Right 24
.ﾟ☆(ノё∀ё)ノ☆ﾟ.⠀Excited to the Right 25
⌒ﾟ(❀<><<◞౪◟<<<<)ﾟ⌒⠀Excited to the Right 26
ヽ/❀o ل͜ o\ﾉ⠀Excited to the Right 27
⤴︎ ε=ε=(ง ˃̶͈̀ᗨ˂̶͈́)۶ ⤴︎⠀Excited to the Right 28
୧༼✿ ͡◕ д ◕͡ ༽୨⠀Excited to the Right 29
ヽ(<^o^ヽ)⠀Excited to the Left 1
╰(✧∇✧╰)⠀Excited to the Left 2
٩(◕ั ∀◕ั๑٩)⠀Excited to the Left 3
٩(•౪•٩)三⠀Excited to the Left 4
₍•͟ ͜ • ₎⠀Excited to the Left 5
q(^-^q)⠀Excited to the Left 6
＼（・c＿・●）ゞ⠀Excited to the Left 7
۹⌤_⌤۹⠀Excited to the Left 8
ヾ(０∀０*★)ﾟ*･.｡⠀Excited to the Left 9
ヾ│・ェ・ヾ│⠀Excited to the Left 10
╰(・∇・╰)⠀Excited to the Left 11
。（＞ω＜。）⠀Excited to the Left 12
ヾ(･ω･｡)ｼ⠀Excited to the Left 13
ヾ(･д･ヾ)⠀Excited to the Left 14
ヽ(´∀｀ヽ)⠀Excited to the Left 15
ヽ(´ω｀○)ﾉ.+ﾟ*｡:ﾟ+⠀Excited to the Left 16
ヾ(≧∇≦*)ゝ⠀Excited to the Left 17
＼（＠￣∇￣＠）／⠀Both Arms Up 1
＼(^▽^＠)ノ⠀Both Arms Up 2
ヾ(@^▽^@)ノ⠀Both Arms Up 3
(((＼（＠v＠）／)))⠀Both Arms Up 4
＼(*T▽T*)／⠀Both Arms Up 5
＼（＾▽＾）／⠀Both Arms Up 6
＼（Ｔ∇Ｔ）／⠀Both Arms Up 7
ヽ( ★ω★)ノ⠀Both Arms Up 8
ヽ(；▽；)ノ⠀Both Arms Up 9
ヾ(。◕ฺ∀◕ฺ)ノ⠀Both Arms Up 10
ヾ(＠† ▽ †＠）ノ⠀Both Arms Up 11
ヾ(＠^∇^＠)ノ⠀Both Arms Up 12
ヾ(＠^▽^＠)ﾉ⠀Both Arms Up 13
ヾ（＠＾▽＾＠）ノ⠀Both Arms Up 14
ヾ(＠゜▽゜＠）ノ⠀Both Arms Up 15
ヾ(@°▽°@)ノ⠀Both Arms Up 16
ヾ(＠°▽°＠)ﾉ⠀Both Arms Up 17
ヽ(*≧ω≦)ﾉ⠀Both Arms Up 18
ヽ(*⌒∇⌒*)ﾉ⠀Both Arms Up 19
ヽ(^。^)丿⠀Both Arms Up 20
ヽ(＾Д＾)ﾉ⠀Both Arms Up 21
ヽ(=^･ω･^=)丿⠀Both Arms Up 22
⸂⸂⸜(രᴗര๑)⸝⸃⸃⠀Both Arms Up 23
⸜(ّᶿധّᶿ)⸝⠀Both Arms Up 24
ヽ(｡･ω･｡)ﾉ⠀Both Arms Up 25
╰(‘ω’ )╯⠀Both Arms Up 26
╰(°ㅂ°)╯⠀Both Arms Up 27
┗(＾∀＾)┛⠀Both Arms Up 28
ヾ(๑’౪`๑)ﾉﾞ⠀Both Arms Up 29
ヾ(*Őฺ∀Őฺ*)ﾉ⠀Both Arms Up 30
╰(✧∇✧)╯⠀Both Arms Up 31
ヾ(๑⃙⃘´ꇴ｀๑⃙⃘)ﾉ⠀Both Arms Up 32
✯⸜(ّᶿ̷ധّᶿ̷)⸝✯⠀Both Arms Up 33
◦°˚\(´°౪°`)/˚°◦⠀Both Arms Up 34
\(-ㅂ-)/⠀Both Arms Up 35
◦°˚\(*❛‿❛)/˚°◦⠀Both Arms Up 36
╰(◉ᾥ◉)╯⠀Both Arms Up 37
⌒°(ᴖ◡ᴖ)°⌒⠀Both Arms Up 38
ヾ(´∀｀○)ﾉ⠀Both Arms Up 39
｡ﾟ✶ฺ.ヽ(*´∀`*)ﾉ.✶ฺﾟ｡⠀Both Arms Up 40
＼(<ﾟ∇ﾟ)/⠀Both Arms Up 41
ヽ(*´∀`)ﾉﾞ⠀Both Arms Up 42
⸂⸂⸜(ೆ௰ೆ๑)⸝⸃⸃⠀Both Arms Up 43
✧⁺⸜(●′▾‵●)⸝⁺✧⠀Both Arms Up 44
ヾ(`ω`　)/⠀Both Arms Up 45
◦°˚\☻/˚°◦⠀Both Arms Up 46
ヾ(｡^ω^｡)ノ⠀Both Arms Up 47
⸜(ّᶿॕധّᶿॕ)⸝⠀Both Arms Up 48
⸜(ؔᶿധؔᶿ)⸝⠀Both Arms Up 49
╰( ･ ᗜ ･ )╯⠀Both Arms Up 50
┏○ ＼(ﾟ 0ﾟ <)/┓⠀Both Arms Up 51
҉*\( ‘ω’ )/*҉⠀Both Arms Up 52
ヽ(^◇^*)/⠀Both Arms Up 53
ヾ(≧∇≦)ゞ⠀Both Arms Up 54
*。ヾ(｡<><<ｖ<<<<｡)ﾉﾞ*。⠀Both Arms Up 55
☆*~ﾟ⌒(‘-‘*)⌒ﾟ~*☆⠀Both Arms Up 56
ヽ(ﾟ∀ﾟ)ﾉ⠀Both Arms Up 57
ヾ(o≧∀≦o)ﾉﾞ⠀Both Arms Up 58
.｡ﾟ+.ヽ| ゝ∀・*|ﾉ｡+.ﾟ⠀Both Arms Up 59
(ﾟ<<<<|＼(･ω･)／|<><<ﾟ)⠀Both Arms Up 60
╰| ° ◞౪◟ ° |╯⠀Both Arms Up 61
ヽ༼<><<ل͜<<<<༽ﾉ⠀Both Arms Up 62
ヽ[ヘ ل͟ ヘ]╯⠀Both Arms Up 63
＼(・ω・)/⠀Both Arms Up 64
ヽ（゜ω゜○）ノ⠀Both Arms Up 65
☆~~ヾ(<><<▽<<<<)ﾉ｡･☆⠀Both Arms Up 66
＼（*´･∀･｀*）／⠀Both Arms Up 67
＼（゜э゜）／⠀Both Arms Up 68
ヾ(￣◇￣)ノ⠀Both Arms Up 69
ヾ【*≧д≦】ノ⠀Both Arms Up 70
ヽ(^O^)ノ⠀Both Arms Up 71
ヾ(´▽｀*)ﾉ☆⠀Both Arms Up 72
ヾ(・∀・｀*)ﾉ☆⠀Both Arms Up 73
☆ヾ(*´▽｀)ﾉ⠀Both Arms Up 74
☆ヾ(*´・∀・)ﾉ⠀Both Arms Up 75
ヾ(*・ω・)ノ⠀Both Arms Up 76
ヾ(・ω・*)ノ⠀Both Arms Up 77
ヽ( ´￢`)ﾉ⠀Both Arms Up 78
ヾ(≧∪≦*)ノ〃⠀Both Arms Up 79
ヾ(*ゝω・*)ノ⠀Both Arms Up 80
＼（○＾ω＾○）／⠀Both Arms Up 81
╰(*´︶`*)╯⠀Both Arms Up 82
ヽ( ´ー`)ノ⠀Both Arms Up 83
┝＼( ‘∇^*)^☆／┥⠀Both Arms Up 84
ヽ(^o^)丿⠀Both Arms Up 85
┗|⌒O⌒|┛⠀Both Arms Up 86
┗|・o・|┛⠀Both Arms Up 87
ヾ(●・◇・●)ノ⠀Both Arms Up 88
ヽ( ‘ω’ )ﾉ⠀Both Arms Up 89
((ヾ(* ´∀｀)ノ))⠀Both Arms Up 90
ヽ(´∇｀)ﾉ⠀Both Arms Up 91
･:*+.\(( °ω° ))/.:+⠀Both Arms Up 92
ヽ(^□^｡)ノ⠀Both Arms Up 93
ヾ(o✪‿✪o)ｼ⠀Both Arms Up 94
＼(*ﾟ∀ﾟ*)／⠀Both Arms Up 95
＼(*^￢^*)／⠀Both Arms Up 96
Ψ(≧ω≦)Ψ⠀Both Arms Up 97
ヽ(*≧л≦)ﾉ⠀Both Arms Up 98
⸜₍ᕏ͜⁎₎⸝⠀Both Arms Up 99
୧☉□☉୨⠀Both Arms Up 100
(* <><<ω<<<<)⠀No Arms 1
(*≧▽≦)⠀No Arms 2
(๑<><<ᴗ<<<<๑)⠀No Arms 3
( ˃̶ω˂̶ ૃ)⠀No Arms 4
(٭°̧̧̧ω°̧̧̧٭)⠀No Arms 5
⸍⚙̥ꇴ⚙̥⸌⠀No Arms 6
(⊙ꇴ⊙)⠀No Arms 7
(*≧∀≦*)⠀No Arms 8
(≧∇≦*)⠀No Arms 9
（๑✧∀✧๑）⠀No Arms 10
(★^O^★)⠀No Arms 11
(ᗒᗨᗕ)⠀No Arms 12
(⌯꒪͒ ꌂ̇ ꒪͒)⠀No Arms 13
(≧∀≦)⠀No Arms 14
(⌬̀⌄⌬́)⠀No Arms 15
₊·*◟(˶╹̆ꇴ╹̆˵)◜‧*･⠀No Arms 16
(ᗒᏬᗕ) ˡ̵˖✮⃛⠀No Arms 17
(ؑ⸍⸍ᵕؑ̇⸍⸍)◞✧⠀No Arms 18
✮⃛( ◞´•௰•`)✮⃛⠀No Arms 19
(ؑᵒᵕؑ̇ᵒ)◞✧⠀No Arms 20
₍₍ ◝(●˙꒳˙●)◜ ₎₎⠀No Arms 21
(´｡✪ω✪｡｀)⠀No Arms 22
｡<+*(★`∪´☆)*+<｡⠀No Arms 23
(๑˃̶͈̀o˂̶͈́๑)⠀No Arms 24
≧ω≦⠀No Arms 25
(✧ ꒪◞౪◟꒪)⠀No Arms 26
٩(^ᴗ^)۶⠀٩ and ۶ Arms 1
٩(๑꒦ິȏ꒦ິ๑)۶⠀٩ and ۶ Arms 2
٩(●˙▿˙●)۶…⋆ฺ⠀٩ and ۶ Arms 3
٩(๑ơలơ)۶♡⠀٩ and ۶ Arms 4
୧(﹒︠ᴗ﹒︡)୨⠀٩ and ۶ Arms 5
٩(ó｡ò۶ ♡)))♬⠀٩ and ۶ Arms 6
ε٩( ºωº )۶з⠀٩ and ۶ Arms 7
٩(๑òωó๑)۶⠀٩ and ۶ Arms 8
٩( ๑^ ꇴ^)۶⠀٩ and ۶ Arms 9
٩(๑˃́ꇴ˂̀๑)۶⠀٩ and ۶ Arms 10
٩(๑∂▿∂๑)۶♡⠀٩ and ۶ Arms 11
٩(♡ε♡ )۶⠀٩ and ۶ Arms 12
۹(ÒہÓ)۶⠀٩ and ۶ Arms 13
٩(⚙ȏ⚙)۶⠀٩ and ۶ Arms 14
٩(✿∂‿∂✿)۶⠀٩ and ۶ Arms 15
୧⍢⃝୨⠀٩ and ۶ Arms 16
⁽⁽٩(๑˃̶͈̀ ᗨ ˂̶͈́)۶⁾⁾⠀٩ and ۶ Arms 17
(୨৩́ಐ৩̀੧)⠀٩ and ۶ Arms 18
٩(<ʘ¿ʘ<)۶⠀٩ and ۶ Arms 19
=。:.ﾟ٩(๑<><<ω<<<<๑)۶:.｡+ﾟ⠀٩ and ۶ Arms 20
٩(˘◊˘)۶⠀٩ and ۶ Arms 21
٩(*ゝڡゝ๑)۶♥⠀٩ and ۶ Arms 22
٩(｡θᗨθ｡)۶⠀٩ and ۶ Arms 23
٩(⚙ᴗ⚙)۶⠀٩ and ۶ Arms 24
୧(˃◡ु˂)୨⠀٩ and ۶ Arms 25
۹(˒௰˓)۶⠀٩ and ۶ Arms 26
٩(●ᴗ●)۶⠀٩ and ۶ Arms 27
♡〜٩( ˃́▿˂̀ )۶〜♡⠀٩ and ۶ Arms 28
٩(º౪º๑)۶⠀٩ and ۶ Arms 29
=。:.ﾟ٩(๑<><<◊<<<<๑)۶:.｡+ﾟ⠀٩ and ۶ Arms 30
٩(๑❛ᴗ❛๑)۶⠀٩ and ۶ Arms 31
୧| ͡ᵔ ﹏ ͡ᵔ |୨⠀٩ and ۶ Arms 32
୧〳 ” ʘ̆ ᗜ ʘ̆ ” 〵୨⠀٩ and ۶ Arms 33
٩(๑❛ʚ❛๑)۶⠀٩ and ۶ Arms 34
٩(இ ⌓ இ๑)۶⠀٩ and ۶ Arms 35
୧| ” •̀ ل͜ •́ ” |୨⠀٩ and ۶ Arms 36
୧( , ＾ 〰 ＾ , )୨⠀٩ and ۶ Arms 37
٩| ര ‿ ര |╯⠀٩ and ۶ Arms 38
୧〳 ＾ ౪ ＾ 〵୨⠀٩ and ۶ Arms 39
୧( ˵ ° ~ ° ˵ )୨⠀٩ and ۶ Arms 40
୧། ☉ ౪ ☉ །୨⠀٩ and ۶ Arms 41
୧༼ ヘ ᗜ ヘ ༽୨⠀٩ and ۶ Arms 42
❣࿌ིྀ྇°˚࿅୧( ॑ധ ॑)୨࿅˳०࿌ིྀ྇⠀٩ and ۶ Arms 43
٩(◦`꒳´◦)۶⠀٩ and ۶ Arms 44
٩(๑˃̌ۿ˂̌๑)۶⠀٩ and ۶ Arms 45
٩(θ‿θ)۶⠀٩ and ۶ Arms 46
˚₊*(ˊॢo̶̶̷̤◡ुo̴̶̷̤ˋॢ)*₊˚⁎⠀Elaborate Excitement 1
•ू(ᵒ̴̶̷ωᵒ̴̶̷*•ू) ​ )੭ु⁾⠀Elaborate Excitement 2
(❛ัॢᵕ❛ั ॢ)✩*ೃ.⋆⠀Elaborate Excitement 3
␟␏(ɲ˃ ˈ̫̮ ˂ɳ)␟␏ෆ⠀Elaborate Excitement 4
ෆ⃛(ٛ⌯ॢ˃ ɪ ˂ٛ⌯ॢ)⠀Elaborate Excitement 5
˚‧*♡ॢ˃̶̤̀◡˂̶̤́♡ॢ*‧˚⠀Elaborate Excitement 6
⁺✧.(˃̶ ॣ⌣ ॣ˂̶∗̀)ɞ⁾⠀Elaborate Excitement 7
₊*ˈ˚·(๑˃̶̡̢̥ ॣಐ ॣ˂̶̡̢̥๑)·˚ˈ*₊⠀Elaborate Excitement 8
\(●⁰౪⁰●\)(//●⁰౪⁰●)//⠀Looking back and forth 1
(´ ↂ⃙⃙⃚ꇴↂ⃙⃙⃚ `≡´ ↂ⃙⃙⃚ꇴↂ⃙⃙⃚ `)⠀Looking back and forth 2
✩⃛∗·⁽⁽◞(˃◟̵◞̵˂⁎=͟͟͞͞ ⁎˃◟̵◞̵˂)◟⁾⁾·∗✩⃛⠀Looking back and forth 3
o(^O^*=*^O^)o⠀Looking back and forth 4
✧(๑✪д✪)۶ㅂ٩(✪д✪๑)✧⠀Looking back and forth 5
⁽⁽◞(꒪ͦᴗ̵̍꒪ͦ=͟͟͞͞ ꒪ͦᴗ̵̍꒪ͦ)◟⁾⁾⠀Looking back and forth 6
ヾ(ﾟ∀ﾟ○)ﾂ三ヾ(●ﾟ∀ﾟ)ﾉ⠀Looking back and forth 7
✧*.◟(ˊᗨˋ)◞.*✧ᗯ੨~ɪ̊♪ْ˖⋆⠀Words 1
꒳ᵃ꒳ᵃ꒳ᵃ~(๑°ᗨૢ°๑)♡ӵᵉ੨ᑋ✧⠀Words 2
(⁼̴̀ૢ꒳​⁼̴́ૢ๑)⠀Fists or Grabby Hands 1
ෆු(*˃ர்˂*)ෆු⠀Fists or Grabby Hands 2
(ٛɲ˃ ˑ̣̮ ˂ٛɳ)⠀Fists or Grabby Hands 3
d(๑꒪່౪̮꒪່๑)b⠀Fists or Grabby Hands 4
( ˃̆ૢ௰˂̆ૢഃ )⠀Fists or Grabby Hands 5
ლ(*꒪ヮ꒪*)ლ⠀Fists or Grabby Hands 6
૮(ᶿ̴͈᷇ॢ௰ᶿ̴͈᷆ॢ)ა✧⠀Fists or Grabby Hands 7
∗˚(* ˃̤൬˂̤ *)˚∗⠀Fists or Grabby Hands 8
б（＞ε＜）∂⠀Fists or Grabby Hands 9
∩|*`・ρ・´|∩⠀Fists or Grabby Hands 10
(>Φ皿Φ)>〃⠀Fists or Grabby Hands 11
(༶ૢ˃̵̑◡˂̵̑༶ૢ)⠀Fists or Grabby Hands 12
о(ж＞▽＜)ｙ ☆⠀Miscellaneous 1
*＼( *ω*)┓⠀Miscellaneous 2
โ๏∀๏ใ⠀Miscellaneous 3
癶(癶✺౪✺ )癶⠀Miscellaneous 4
⊂((〃≧▽≦〃))⊃⠀Miscellaneous 5
~(≧◇≦)/ﾞﾞﾞﾞ⠀Miscellaneous 6
6((((≧▽≦))))9⠀Miscellaneous 7
☆*･゜ﾟ･*(^O^)/*･゜ﾟ･*☆⠀Giant Emoticons 1
☆*:.｡. o(≧▽≦)o .｡.:*☆⠀Giant Emoticons 2
*✲ﾟ*｡✧٩(･ิᴗ･ิ๑)۶*✲ﾟ*｡✧⠀Giant Emoticons 3
｡.ﾟ+:((ヾ(｡･ω･)ｼ)).:ﾟ+｡⠀Giant Emoticons 4
＼（　●　⌒　∇　⌒　●　）／⠀Giant Emoticons 5
☆ミヾ(∇≦((ヾ(≧∇≦)〃))≧∇)ノ彡☆⠀Giant Emoticons 6
ﾟ･✿ヾ╲(｡◕‿◕｡)╱✿･ﾟ⠀Giant Emoticons 7
＼＼(゜ロ＼＼)Ξ(／／ロ゜)／／⠀Giant Emoticons 8
o͡͡͡͡͡͡͡͡͡͡͡͡͡͡╮(^ ਊ ^)╭o͡͡͡͡͡͡͡͡͡͡͡͡͡͡⠀Giant Emoticons 9
ヽ( ･∀･)ﾉ┌┛Σ(ノ `Д´)ノ⠀Kicking 1
♪o(*´∇｀)┌θ☆(ﾉ<><<_<<<<)ﾉ⠀Kicking 2
(# ﾟ□)┌@≡@≡@)Д)ﾉﾉ☆⠀Kicking 3
ヽ( ￣∀￣)ﾉ┌┛Σ(ノ ・Д・)ノ⠀Kicking 4
!ヾ(▼皿▼ﾒ)┌θ☆(ﾉ □ )ﾉ ﾟ ﾟ⠀Kicking 5
≡≡ヾ(￣〇￣)┌ο⠀Kicking 6
ヽ(*´ｪ｀)ﾉ┌┛Σ(ﾉ´ｪ｀)ﾉ⠀Kicking 7
┗┐ヽ(･v･´o≡o`･v･)ﾉ┌┛⠀Kicking 8
ﾍ(●`,_っ´)┌θΣ(#´д`)⠀Kicking 9
ﾍ(*ﾟｰﾟ)┌θ)ﾟﾛﾟ)ﾉ⠀Kicking 10
( ･´Д｀･)┌θ☆(ﾉ´<><<ω<<<<)ﾉ⠀Kicking 11
ヽ( ￣∀￣)ﾉ┌┛三┌┛.∵(｡|⠀Kicking 12
ヽ( ･∀･)ﾉ┌┛三┌┛.∵(｡|⠀Kicking 13
(ｏﾟﾛﾟ)┌┛Σ(ﾉ´*ω*｀)ﾉ⠀Kicking 14
ヽ(#ﾟДﾟ)ﾉ┌┛(ﾉ´Д｀)ﾉ⠀Kicking 15
☆ﾍ(｀･ω･)ﾉ┌┛⠀Kicking 16
ヾ(･ω･)┌┛三三三⠀Kicking 17
ヘ(*ﾟ∀ﾟ)┌θ”)´Д｀●)ﾉ⠀Kicking 18
( ﾟДﾟ)┌┛Σ( ﾟ∀ﾟ)･∵⠀Kicking 19
ヽ( ．∀・)ﾉ┌┛⠀Kicking 20
☆ﾍ(○ゝз・)ﾉ┌┛⠀Kicking 21
ヾ(｡｀Д´｡)ﾉ┌┛⠀Kicking 22
ﾍ(　ﾟ益ﾟ)ﾉ┌┛Σ(ﾉ´ω`)ﾉ⠀Kicking 23
ヽ(╬☉Д⊙)ﾉ┌┛)๏д๏)ﾉ⠀Kicking 24
(乂∀◕ฺ)┌┛)`д)<∴⠀Kicking 25
（゜ε´（┗┓ヽ（ゝ∀・）ﾉ⠀Kicking 26
ヽ(#`Д´)ﾉ┌┛⠀Kicking 27
！( ･´Д｀･)┌θ☆(ﾉ´<><<ω<<<<)ﾉ⠀Kicking 28
ヽ(*´∀`)ﾉ┌┛⠀Kicking 29
三ヾ(ヽ*ω*)┌┛★⠀Kicking 30
Σ(ﾟ∀´(┗┐ヽ(.◕ฺˇд ˇ◕ฺ<)ﾉ⠀Kicking 31
(ﾟo´(┗┐ヽ(╰,╯ )ﾉ⠀Kicking 32
( #`⌂´)/┌┛⠀Kicking 33
Σ(ﾟ∀´(┗┐ヽ(･∀･ )ﾉ⠀Kicking 34
ヽ(#ﾟДﾟ)ﾉ┌┛Σ(ノ´Д`)ノ⠀Kicking 35
ヽ(＾▽＾)ﾉ┌┛Σ≡≡＝＝(*ﾟ□ﾟ:<’:┃⠀Kicking 36
ヽ(ヽ `д´)ヽ`д´)ヽ`д´)┌┛┌┛┌┛★)`з゜)y⠀Kicking 37
★┗┐ヽ(-ｃ＿´-,,≡,,-｀＿っ-)ﾉ┌┛★⠀Kicking 38
三ヾ(ヽ･┏x┓･)┌┛★)`3ﾟ)ﾟ:+｡⠀Kicking 39
＼＼(￢(OO)￢<)┌θ☆#)○(oo)●)~ﾉﾉ⠀Kicking 40
！(･∀･)┌┛”Σ　–==三三⊂´⌒つﾟ∀ﾟ)つ⠀Kicking 41
εε=====≡ﾞヽ(#｀Д´)っ┌┛))⠀Kicking 42
(･ω･人･ω･人･ω･)┌┛┌┛┌┛　ΣΣ((((ﾉﾟ x ﾟ):<*.’:<⠀Kicking 43
:<*.’:<(ﾟДﾟ｀(o=(´ｴ｀*)┌┛)´ﾟДﾟ）:<*.’:⠀Kicking 44
ヽ( ･∀･)ﾉ┌┛三┌┛.∵(|| ´(00)`)⠀Kicking 45
ヽ(#´Д｀)ﾉ┌┛☆　≡(；･∀･)っ⠀Kicking 46
εε=====≡ヾ(●’ｖ｀)ﾉ┌┛))…..○⠀Kicking 47
♪ヽ( ･益･)ﾉ┌┛ﾟ･*:.｡. .｡.:*･゜ﾟ･*⠀Kicking 48
(乂๑・‿・๑)┌┛)´ω`ﾟ)ﾟ｡､<’⠀Kicking 49
三ヾ(ヽ･┏x┓･)┌┛★)`3ﾟ)ﾟ:+｡｀ﾟ⠀Kicking 50
三ヾ(ヽ*ω*)┌┛★)◠‿◠)ﾟ: ｡｀ﾟ⠀Kicking 51
(((ง’ω’)و三 ง’ω’)ڡ≡⠀Punching 1
(๑و•̀ω•́)و⠀Punching 2
(ง •̀_•́)ง⠀Punching 3
‾͟͟͞(((ꎤˋ⁻̫ˊ)—̳͟͞͞o⠀Punching 4
꒰๑͒•̀ुꇵ͒•꒱و ̑̑⠀Punching 5
ʕง•ᴥ•ʔง⠀Punching 6
༼ ᓄºل͟º ༽ᓄ⠀Punching 7
(ง⌐□ل͜□)ง⠀Punching 8
(งಠل͜ಠ)ง⠀Punching 9
(ᓄಠ_ಠ)ᓄ⠀Punching 10
ᕙ(° ͜ಠ ͜ʖ ͜ಠ°)ᓄ⠀Punching 11
(ง ͡ʘ ͜ʖ ͡ʘ)ง⠀Punching 12
(งಠ_ಠ)ง⠀Punching 13
(ง ° ͜ ʖ °)ง⠀Punching 14
(ง’̀-‘́)ง⠀Punching 15
(́ง◉◞౪◟◉‵)ง⠀Punching 16
( ง ͡°╭ ͟ʖ╮͡° ) ง⠀Punching 17
(ง ͠° ͟ل͜ ͡°)ง⠀Punching 18
(ｏﾟﾛﾟ)=●)PC】･<’⠀Punching 19
(ง ͠° ͟ʖ ͡°)ง⠀Punching 20
Q(｀⌒´Q)⠀Punching 21
(ง ͠ ͠° ل͜ °)ง⠀Punching 22
(ง ͠° ͟ʖ #)ง⠀Punching 23
(ง •̀ゝ•́)ง⠀Punching 24
(⋆ˋ⑉̈ˊ)൭൭⁼³₌₃⠀Punching 25
(((ꎤ’ω’)و三 ꎤ’ω’)-o≡⠀Punching 26
(ง°ل͜°)ง⠀Punching 27
(૭ ఠ༬ఠ)૭⠀Punching 28
0( =^･_･^)=〇⠀Punching 29
༼ง=ಠ益ಠ=༽ง⠀Punching 30
Ｃ≡(・。・Ｃ≡)≡≡≡⠀Punching 31
(೨♛‿♛೨)⠀Punching 32
!!θ(　ﾟДﾟ)＝θ☆⠀Punching 33
(∩`ω´)⊃))⠀Punching 34
★o(･д´･+)９”⠀Punching 35
(((c=(ﾟﾛﾟ<q⠀Punching 36
(((c=(°ロ°<q⠀Punching 37
((งง •̀•̀__•́•́))งง⠀Punching 38
༼ง ◉_◉༽ง⠀Punching 39
༼ ᕤ◕◡◕ ༽ᕤ⠀Punching 40
༼ง’̀-‘́༽ง⠀Punching 41
༼ง ͠ຈ ͟ل͜ ͠ຈ༽ง⠀Punching 42
୧༼◔益◔୧ ༽⠀Punching 43
ᕙﾉ•̀ʖ•́ﾉ୨⠀Punching 44
୧▐ ್ ﹏ ್ ▐୨⠀Punching 45
=͟͟͞͞(งꏿ᷅॓৺ꏿ᷄॔)ง⁼³₌₃⠀Punching 46
((⊂(`ω´∩)⠀Punching 47
｡ﾟ+.*(+･｀ω･)９⠀Punching 48
‾͟͟͞(((ꎤ๑‾᷅༬‾᷄๑)̂—̳͟͞͞o⠀Punching 49
Q–(’̀-’̀Q )⠀Punching 50
ᕙ( ︡’︡益’︠)ง⠀Punching 51
ϱ(`ન̇´)⁼³̳⠀Punching 52
|ง།°╭͜ʖ╮°།|ง⠀Punching 53
((( งᵒ̴̶̷᷅ᐜᵒ̴̶̷᷄)ง三 ( งᵒ̴̶̷᷅ᐜᵒ̴̶̷᷄)ڡ≡⠀Punching 54
(҂‾ ▵‾)︻デ═一 (˚▽˚’!)/⠀Guns 1
̿’ ̿’\̵͇̿̿\з=(ಥДಥ)=ε/̵͇̿̿/’̿’̿⠀Guns 2
( う-´)づ︻╦̵̵̿╤── \(˚☐˚”)/⠀Guns 3
(⌐■_■)–︻╦╤─⠀Guns 4
̿̿ ̿̿ ̿’̿’̵͇̿̿з=༼ ▀̿̿Ĺ̯̿̿▀̿ ̿ ༽⠀Guns 5
━╤デ╦︻(▀̿̿Ĺ̯̿̿▀̿ ̿)⠀Guns 6
╾━╤デ╦︻⠀Guns 7
▄︻̷̿┻̿═━一⠀Guns 8
︻╦̵̵͇̿̿̿̿══╤─⠀Guns 9
༼ ಠل͟ಠ༽ ̿ ̿ ̿ ̿’̿’̵з=༼ຈل͜ຈ༽ﾉ⠀Guns 10
̿’ ̿’\̵͇̿̿\з=(ಡل͟ಡ)=ε/̵͇̿̿/’̿’̿⠀Guns 11
￢o(￣-￣ﾒ)⠀Guns 12
(҂`з´).っ︻デ═一⠀Guns 13
ᕕ╏ ͡ᵔ ‸ ͡ᵔ ╏و︻̷┻̿═━一⠀Guns 14
⌐╦╦═─⠀Guns 15
(ﾟ皿ﾟ)ｒ┏┳－－－＊⠀Guns 16
・-/(。□。</)—-┳┓y(-_・ )⠀Guns 17
(ﾒ▼▼)┏)ﾟoﾟ)⠀Guns 18
[ﾉಠೃಠ]︻̷┻̿═━一⠀Guns 19
……┳┓o(▼▼ｷ)⠀Guns 20
(ｷ▼▼)o┏┳……⠀Guns 21
(ﾒ▼皿▼)┳*–⠀Guns 22
̿̿’̿’\̵͇̿̿\=(•̪●)=/̵͇̿̿/’̿̿ ̿ ̿ ̿⠀Guns 23
】ﾟДﾟ)┳—-ﾟ~:<’:<ω*:<’<—-⠀Guns 24
ξ(✿ ❛‿❛)ξ▄︻┻┳═一⠀Guns 25
⁞ つ: •̀ ⌂ •́ : ⁞-︻╦̵̵͇̿̿̿̿══╤─⠀Guns 26
╾━╤デ╦︻ԅ། ･ิ _ʖ ･ิ །ง⠀Guns 27
……┳┓o(-｀Д´-ﾒ )⠀Guns 28
┌( ͝° ͜ʖ͡°)=ε/̵͇̿̿/’̿’̿ ̿ └། ๑ _ ๑ །┘⠀Guns 29
(‥)←￢~(▼▼#)~~⠀Guns 30
(ง⌐□ل͜□)︻̷┻̿═━一⠀Guns 31
‘̿’\̵͇̿̿\=( `◟ 、)=/̵͇̿̿/’̿̿ ̿⠀Guns 32
༼ ºل͟º ༽ ̿ ̿ ̿ ̿’̿’̵з=༼ ▀̿Ĺ̯▀̿ ̿ ༽⠀Guns 33
(キ▼▼)＿┏┳……⠀Guns 34
( ͝ಠ ʖ ಠ)=ε/̵͇̿̿/’̿’̿ ̿⠀Guns 35
ლ(~•̀︿•́~)つ︻̷┻̿═━一⠀Guns 36
(ง ͠° / ^ \ °)-/̵͇̿̿/’̿’̿ ̿⠀Guns 37
(‘ºل͟º)ノ⌒. ̿̿ ̿̿ ̿’̿’̵͇̿̿з=༼ ▀̿̿Ĺ̯̿̿▀̿ ̿ ༽⠀Guns 38
(▀̿̿Ĺ̯̿̿▀̿ ̿)•︻̷̿┻̿┻═━━ヽ༼ຈ益ຈ༽ﾉ⠀Guns 39
ー═┻┳︻▄ξ(✿ ❛‿❛)ξ▄︻┻┳═一⠀Guns 40
ﾍ(ToTﾍ)))　・　—　　ε￢(▼▼メ)凸⠀Guns 41
( ﾒ▼Д▼)┏☆====(((＿◇＿)======⊃⠀Guns 42
!! ( ﾒ▼Д▼)┏☆====(((＿◇＿)======⊃⠀Guns 43
!!(★▼▼)o┳*—————–●))<´ﾛ`))⠀Guns 44
!! ﾍ(ToTﾍ)))　・　—　　ε￢(▼▼メ)凸⠀Guns 45
ヽ༼ຈ益ຈ༽_•︻̷̿┻̿═━一|<<<<——— ҉ Ĺ̯̿̿▀̿ ̿)⠀Guns 46
ヽ༼xل͜x༽ﾉ <<<<===== ̿’ ̿’\̵͇̿̿\з༼ຈل͜ຈ༽ ε/̵͇̿̿/’̿’̿ =====<><< ヽ༼xل͜x༽ﾉ⠀Guns 47
ლ[☉︿۝)७)७︻̷┻̿═━一︻̷┻̿═━一⠀Guns 48
( φ_<<<<)r┬ ━━━━━━…=<><<⠀Guns 49
(∩ ͡ ° ʖ ͡ °) ⊃-(===<><<⠀Swords 1
ヽ༼ಥل͟ಥ༽¤=[]:::::<><<⠀Swords 2
¯\_( ͡° ͜ʖ ͡°)ง-]—-⠀Swords 3
(ง ͠ ᵒ̌ Дᵒ̌)¤=[]:::::<><<⠀Swords 4
(ง ͠° ͟ل͜ ͡°)¤=[]:::::<><<⠀Swords 5
ᗜಠ o ಠ)¤=[]:::::<><<⠀Swords 6
(ﾒ▼へ▼)ﾉ0=|⊃―⠀Swords 7
!( ｀皿´)o/)≡≡≡≡≡≡≡<><<十○⠀Swords 8
੧| ⊗ ▾ ⊗ |⊃¤=(————-⠀Swords 9
╰༼.◕ヮ◕.༽つ¤=[]————⠀Swords 10
———–[]=¤ԅ༼ ･ 〜 ･ ༽╯⠀Swords 11
ᕦ[ •́ ﹏ •̀ ]⊃¤=[]::::::::<><<⠀Swords 12
(*ﾟ∀ﾟ)つ＝<ニニフ⠀Swords 13
༼ง ͠ຈ ͟ل͜ ͠ຈ༽o:[]:::::::<><<⠀Swords 14
ᕙ༼◕ل͜◕༽つ¤=[]:::::<><<⠀Swords 15
<<<<:::::[]=¤༼ຈل͜ຈ༽ﾉ⠀Swords 16
╰༼⇀︿⇀༽つ-]═──⠀Swords 17
(つ･･)つ¤=[]:::::::<><<⠀Swords 18
༼ຈل͜ຈ༽ﾉ¤=[]:::::<><<⠀Swords 19
੧| ✿ ◔ ں ◔ ✿ |ᓄ¤=[]:::::::::::–⠀Swords 20
~~~~~~~[]=¤ԅ໒( ☯ ᗜ ☯ )७ᕗ⠀Swords 21
c:::::::::::::[]=¤ԅ╏ ˵ ⊚ ◡ ⊚ ˵ ╏┐⠀Swords 22
─=≡Σ((( つ◕ل͜◕)つ¤=[]:::::<><<⠀Swords 23
(　´,_ゝ｀)つ━╂──( ﾟ∀ﾟ)─⠀Swords 24
ᕙ╏✖۝✖╏⊃-(===<><<⠀Swords 25
∩༼˵☯‿☯˵༽つ¤=[]:::::<><<⠀Swords 26
༼ຈل͜ຈ༽▬▬ι═══════ﺤ⠀Swords 27
(っ ‘o’)ﾉ⌒ ~ ː̗̤̣̀̈̇ː̖́.•⠀Bombs 1
(╯°□°)ຈ҉̛༽̨҉҉ﾉ̨⠀Bombs 2
*~● ))))o(･.･<)⠀Bombs 3
!!(　’ ‘)ﾉﾉ⌒●~*⠀Bombs 4
( ･O･)ﾉ⌒●~*⠀Bombs 5
( ･_･)ﾉ⌒●~*⠀Bombs 6
(*,_,)ﾉ⌒●~*⠀Bombs 7
♪( ´ー｀)_●~*⠀Bombs 8
( ・_・)ノΞ●~*⠀Bombs 9
ヾ(<ﾟ⊿ﾟ)ﾉ *～●…⠀Bombs 10
(<°o°) *~●｡｡｡⠀Bombs 11
●～*°゜°。｡ヾ(≧∇≦o)⠀Bombs 12
*~●)ﾛﾟ)〃⠀Bombs 13
*~( ///// )ヽ(ﾟﾛﾟ)ﾉ⠀Bombs 14
~●)))　＼(･ｪ･^＼)⠀Bombs 15
~●)))　＼(-_＼)⠀Bombs 16
|ﾉｪ･)ﾉ (((●~*⠀Bombs 17
●~*＼(^o＼)⠀Bombs 18
●~*⌒☆＼_(–* )⠀Bombs 19
●~*⌒☆＼(-o- )⠀Bombs 20
●~* ε≡≡≡ﾍ(<￣▽￣)ﾉ⠀Bombs 21
|ﾉ_-)ﾉ 　(((●~⠀Bombs 22
(ﾉﾟДﾟ)ﾉ ))))))●~*⠀Bombs 23
●~*≡≡☆ヘ(｀ω´ )ミ⠀Bombs 24
ヽ(<´Д｀)ﾉ(((((((((●~*⠀Bombs 25
(メ▼ー▼)/●~*⠀Bombs 26
*~●＼(▼ー▼メ)⠀Bombs 27
(｀・ω・)つ ●~＊⠀Bombs 28
(￣、￣)ﾉ=――――――∞C●~*⠀Bombs 29
(o･_･)_……………………….●~*⠀Bombs 30
●~*⊃―(・_・ Ξ・_・)――――∞C●~*⠀Bombs 31
●~*⊃―(ﾟｰﾟ*Ξ*ﾟｰﾟ)―――∞C●~*⠀Bombs 32
（（（（（（BOMB）））））） ⌒⌒⌒⌒⌒／(x~x)＼⠀Bombs 33
●~*＼(-_＼)・・・ε=ε=ε=┏(<-_-)┛⠀Bombs 34
●~*●~*●~*ヽ(´ー｀ヽ)(ﾉ´ー｀)ﾉ*~●*~●*~●⠀Bombs 35
γ⌒γ⌒γﾟ･*:.●　⊂(ﾟﾛﾟ⊂≡≡===⠀Bombs 36
●~*●~*三ヾ( <><<o<<<<)ﾉ三*~●*~●⠀Bombs 37
ヽ(´ｰ`)ﾉ v⌒v⌒v⌒v⌒　●~*⠀Bombs 38
●~●~●~●~＼( <><<o<<<<)ﾉ⌒*~●　　～*~●　　～*~●⠀Bombs 39
(ﾉ-.-)ﾉ….((((((((((((●~* ( <><<_<<<<)⠀Bombs 40
!(￣o￣ )ﾉ v⌒v⌒v⌒v⌒ ミ●~*☆(((≪*☆*BOMB*☆*≫)))⠀Bombs 41
ﾍ(　・_・)ﾉ－－＝＝＝*~●☆●~*＝＝＝－－ヾ(・_・ )o⠀Bombs 42
－－－＝＝＝＝*~●ﾍ(ﾟρﾟ)ﾉ~⠀Bombs 43
(-.-)__ (((●～* (((●～* (((●～* (((●～*⠀Bombs 44
|ﾉ´ェ｀|)ﾉ)))))))))) ●~*●~*●~*●~*●~*⠀Bombs 45
(ノ^-^)ノ ⌒ ●~*●~*●~*●~*⠀Bombs 46
=͟͟͞͞➳ ͟ ͟ ͟ ͟╔̱॒⠀Arrows and Other Projectiles 1
=͟͟͞͞➳⠀Arrows and Other Projectiles 2
ヽ| ・∀・|ノ-=≡≡≡卍卍⠀Arrows and Other Projectiles 3
.∵･(ﾟДﾟ)　ー<(´　)⠀Arrows and Other Projectiles 4
⊂( ･∀･) 彡　=͟͟͞͞(✹)`Д´)⠀Arrows and Other Projectiles 5
⊂( ･∀･) 彡　=͟͟͞͞(●)`Д´)⠀Arrows and Other Projectiles 6
Σ<><<―(´･ω･`)→⠀Arrows and Other Projectiles 7
<<<<( ･ｪ-)<<<<}　　　　　　…………..⌒－( <ﾟ-ﾟ)→⠀Arrows and Other Projectiles 8
(ﾉ^-ﾟ)/|)‥‥…<><<<><<━→　 　<><<<><<-(◎)→⠀Arrows and Other Projectiles 9
( ･_･)ﾉ-≒≒≒≒≒≒≒≒≒≒卍ﾟoﾟ)⠀Arrows and Other Projectiles 10
/_･)/D･････—— →<ﾟoﾟ)⠀Arrows and Other Projectiles 11
!ヽ(ﾒ｀⌒´)θ☆===========(((旦~~⠀Arrows and Other Projectiles 12
(ﾉ-_･)/|)‥‥…<><<<><<━→　 　<><<<><<-(ﾟﾛﾟ)→⠀Arrows and Other Projectiles 13
<<<<( ・_・)。D -→ -→ -→ -→ (<><<_<<<<→⠀Arrows and Other Projectiles 14
!(。-ω-)_ ⌒　Σ<><<―(<=◇=)ﾉ→⠀Arrows and Other Projectiles 15
!( ･д･)_ ⌒ 　∑<><<―(<･◇･)ﾉ→⠀Arrows and Other Projectiles 16
!!(/_･)/D=============∋-(<><<<<<<)→⠀Arrows and Other Projectiles 17
∠( ･ｪ-)<<<<}　　　　　　　…－(=ﾟﾛﾟ=)→⠀Arrows and Other Projectiles 18
ヽ( ﾟｰﾟ)ﾉ}　　　–→　｡｡｡｡<<ﾉ<><<_<<<<)ﾉ⠀Arrows and Other Projectiles 19
ヽ( ^-^)ﾉ }—– → ｡｡｡｡｡(ﾉ<><<_<<<<)ﾉ⠀Arrows and Other Projectiles 20
／_・)/D・・・・・—— →ﾟ⊿ﾟ)ﾉ⠀Arrows and Other Projectiles 21
∠( -_)<<<<}･･･—–→－(´<ω<`)→⠀Arrows and Other Projectiles 22
( ・_・)D !———–―(<><<_<<<<→⠀Arrows and Other Projectiles 23
◎・———-‥…-o_(ﾟДﾟ ))⠀Arrows and Other Projectiles 24
(★´3｀)＝＝＝ミ○ミ○ミ○ミ○ミ○ミ○⠀Arrows and Other Projectiles 25
(★´Д｀)ﾉ －－－＝＝＝≡≡≡ 卍⠀Arrows and Other Projectiles 26
!!( ･_･)r鹵~<<<<巛巛巛⠀Spray 1
!!( ･_･)r鹵~<<<<巛巛巛(x_x)⠀Spray 2
!!( ･_･)r鹵~<<<<巛巛巛(ﾟoﾟ<⠀Spray 3
( ・∀・)ｒ鹵~<<<<≪巛<ﾟДﾟ)ﾉ⠀Spray 4
ヽ|・∀・|ｒ鹵～＜巛巛⠀Spray 5
（　＾）／占~~~~~⠀Spray 6
( ﾟДﾟ)ﾉ占~<<<<巛巛巛⠀Spray 7
( ▼▼)/鹵<<<<<<<<≪≪《《〈〈 巛 ( ◎_x)/⠀Spray 8
!!( ・_・)r鹵~<<<<炎炎炎炎炎炎(ﾟ■ﾟ<<)ﾉ⠀Spray 9
(○ゝ｀ω･)ｒ鹵~巛殺殺殺殺殺殺殺殺殺殺⠀Spray 10
ヾ((( ﾟ<<<<炎炎炎炎炎炎炎ﾉ<ﾟﾛﾟ)ﾉ炎炎炎⠀Spray 11
(〃’▽’)_中☆{{{Д}}}⠀Hammers 1
!!(｀･ω･)_中☆(　ﾟｪﾟ)・<’⠀Hammers 2
( ´∀｀)_中☆)<><<ω<<<<)⠀Hammers 3
(((´･ω･｀)_中☆{{{Д}}}⠀Hammers 4
⊂(ﾉ-(工)-)⊃ﾉ 中☆(o_ _)o ．ｚＺ⠀Hammers 5
( ►_◄ )-c<<<<*_*< )⠀Being a Jerk 1
(o≧ω≦)○))`ωﾟ)!⠀Being a Jerk 2
‾͟͟͞(((ꎤ°᷄д°᷅)و ̑̑༉☆))Д´)⠀Being a Jerk 3
(o￣∇￣)=◯)`ν゜)⠀Being a Jerk 4
(○ ｀ｰ´)○☆)ﾟoﾟ/⠀Being a Jerk 5
(●｀・ω・)=Ｏ)｀-д゜)⠀Being a Jerk 6
（。_°☆＼(- – )⠀Being a Jerk 7
╭ (o^o#)ᕗ-(-w-)⠀Being a Jerk 8
( ｀o´)_θ☆( <><<_<<<<)⠀Being a Jerk 9
!!(ﾒ￣ ￣)_θ☆ﾟ0ﾟ)/⠀Being a Jerk 10
ヾ(ﾟﾛﾟ((≡◯≠≠(￣(ｪ)￣ )⠀Being a Jerk 11
@(o･ｪ･)ﾉ☆@(*_ _)@⠀Being a Jerk 12
(￣ー￣〃)—-Ｃ＜T-T)ﾉ⠀Being a Jerk 13
(p –)=O=O))@⠀Being a Jerk 14
[emai<<#160<pro<ec<ed]⠀Being a Jerk 15
)/⠀Being a Jerk 16
☆(ﾟoﾟ(○=(-_-○⠀Being a Jerk 17
ﾍ(<ﾟﾛﾟ)o-(▼▼ﾒ)○⠀Being a Jerk 18
( ▼皿▼)=○)Д)゜゜⠀Being a Jerk 19
!! ( ･_･)_ …-=≡ξ<ﾟｏﾟ)⠀Being a Jerk 20
( ･･)-○))))))))))-○)ﾟoﾟ)⠀Being a Jerk 21
!!(*｀・д・)_／☆( ﾟωﾟ)⠀Being a Jerk 22
(　・д・)⊃)・O・)⠀Being a Jerk 23
┌(｀Д´)ノ)ﾟ∀ﾟ)⠀Being a Jerk 24
o( -ω-)ﾉ⊂■)ﾟ3ﾟ)⠀Being a Jerk 25
⊂(-(工)-)⊃ﾉ≡≡≡θ☆( ﾉ<_ _)ﾉ⠀Being a Jerk 26
(*・x・)っ-┷☆{{{Д}}}⠀Being a Jerk 27
(*･∀･)つ─━)ﾟдﾟ||)⠀Being a Jerk 28
(o｀･ω･)σ))Д｀<)⠀Being a Jerk 29
(´ε(○=(ﾟ∀ﾟ　)⠀Being a Jerk 30
(ﾒ▼皿▼)=○)Д)ﾟﾟ⠀Being a Jerk 31
(°Д°(☆○=(｀ω´*)o⠀Being a Jerk 32
(<｀Д´)≡⊃)｀Д)⠀Being a Jerk 33
( ･_･)_ …-=≡□Σﾟoﾟ)⠀Being a Jerk 34
(｡･д･)☞)´Д｀)⠀Being a Jerk 35
( ‘-‘)ﾉ)`-‘)⠀Being a Jerk 36
(´д｀(⊆≡(｀Д´⠀Being a Jerk 37
(^∀^)σ≡σ)┳_┳)⠀Being a Jerk 38
(•̀⌓•́)シ༼★ل͜★༽⠀Being a Jerk 39
༼ ಥل͟ಥ ༽シ(•̀⌓•́)⠀Being a Jerk 40
( ๑‾̀◡‾́)σ»⠀Being a Jerk 41
(*・)σσσ(*゜Д゜*)⠀Being a Jerk 42
( •̀ω•́ )σ ( . Y . )⠀Being a Jerk 43
┏┫*｀ｰ´┣━━━━━━━━━●)ﾟOﾟ).｡ﾟ⠀Being a Jerk 44
( ･_･)*――――――∞C<<<< /― _-)/⠀Being a Jerk 45
○＼( ・_・) !!( ・_・)＿ …-=≡○)<´д｀)⠀Being a Jerk 46
ヾ(ﾟOﾟ()○=(▼皿▼)=○()o×)/⠀Being a Jerk 47
(* ￣ ￣)ｃ――――――∞C<<<< /T_T)/⠀Being a Jerk 48
!(<￢_￢) ﾉ ～━━━∈☆)ﾟｏﾟ <)/⠀Being a Jerk 49
――==≡≡≪<<<<<<<<<<<<《(-_-)=○》≫≫()ﾟOﾟ)⠀Being a Jerk 50
(つ･∀･):･’.::･Σ====Σ≡つ)ﾟДﾟ):∵⠀Being a Jerk 51
┏┫*｀ ー ´┣━━━━━━━━━●)ﾟロﾟ)⠀Being a Jerk 52
o(*´Д｀)⊃☆三三三○))｀ω゜)・<’.、⠀Being a Jerk 53
━━( ´_ゝ｀)〓○<><<ﾟДﾟ<<<<○〓( ´ι_｀)━━!⠀Being a Jerk 54
!!!(つ´∀｀):･’.::･====≡つ)´Д｀):∵⠀Being a Jerk 55
(o･x･)/∝━━━━━━∈:<*.’:< ﾟДﾟ)⠀Being a Jerk 56
( ﾟ∀ﾟ)o──┫))ﾟдﾟ<((┣──ｏ(ﾟ∀ﾟ )⠀Being a Jerk 57
{{(*(エ)*)}} =D—o(-(エ)- )9″⠀Being a Jerk 58
!!(つ｀･ω･)つ三○　三○)ﾟдﾟ<)⠀Being a Jerk 59
!!!(*｀ω´)/――――― ●)´Дﾟ)⠀Being a Jerk 60
ーーーつ！！=͟͟͞͞ ( ・ω・)っ　=͟͟͞͞ ꒰__꒱ )’ω・)､<’.･⠀Being a Jerk 61
＜（‵□′）＞───Ｃε（┬＿┬）３⠀Being a Jerk 62
( `_)乂(_’ )⠀Two People Fighting 1
Ｏ( ｀_´)乂(｀_´ )Ｏ⠀Two People Fighting 2
(ó ì_í)=óò=(ì_í ò)⠀Two People Fighting 3
(=O*_*)=O Q(*_*Q)⠀Two People Fighting 4
(⸔⠊̥)ू (ृ⠑̥⸕ू)⠀Two People Fighting 5
( ◞•̀д•́)◞⚔◟(•̀д•́◟ )⠀Two People Fighting 6
१(ꐦꏿ᷅⺫ꏿ᷄)┈✷┈(ꏿ᷅﹏ੂꀛꐦ)ງ⠀Two People Fighting 7
(｀⌒*)O-(｀⌒´Q)⠀Two People Fighting 8
˛˛ꉂ ◞•̀д•́)◞⚔◟(•̀д•́◟ )⠀Two People Fighting 9
(θ｀＾´)θ　　○＝(-_-Ｏ)⠀Two People Fighting 10
６( -_-)ｏ ○(-_- )ｏ⠀Two People Fighting 11
(p－－)=O=O O=O=(－－ｑ)⠀Two People Fighting 12
ヾ(｡･o･)θ☆(*x_｡)/⠀Two People Fighting 13
(‘A`(爻)゜∀゜)⠀Two People Fighting 14
,,,((*≧∇)乂(∇≦*)),,,⠀Two People Fighting 15
┣o(･ω･｡)⠀Miscellaneous 1
━━o(･ω･｀)⠀Miscellaneous 2
(´･ω･)o━━⠀Miscellaneous 3
(⁎⚈ैꇴ⚈ै⁎⚑)⚐╒ⅰᵍһ৳ǁ͚⠀Words 1
કⁱᵍʰᵗᵎકⁱᵍʰᵗᵎ⚑⠀Words 2
¯\_( ͡° ͜ʖ ͡°)ง-]—- ᴇɴ ɢᴀʀᴅᴇ⠀Words 3
||☆FIGHT☆||´Д`*)9⠀Words 4
^(#｀∀´)_Ψ vs †_(ﾟｰﾟ*)β⠀Words 5
(*´∀｀*)ﾉ[☆ﾟ･*F i > h <*･ﾟ☆]ヽ(*´∀｀*)⠀Words 6
(゜))<<<<<<<<⠀Fish 1
(°))<<<<<<<<⠀Fish 2
(°)#))<<<<<<<<⠀Fish 3
(Q )) <><<⠀Fish 4
<><<_)))彡⠀Fish 5
<><<゜))))彡⠀Fish 6
ζ°)))彡⠀Fish 7
❥᷁)͜͡˒ ⋊⠀Fish 8
┣⠉❥᷁)͜͡˒ ⋊⠀Fish 9
<<<<º))))<><<<<<<⠀Fish 10
<<<<゜)))彡⠀Fish 11
<><<<<<<((((●ﾟ<<<<⠀Fish 12
<><<<<<<((((*ﾟ<<<< <><<ﾟ*)))<><<<<<<⠀Fish 13
ζ`))))))<<<<⠀Fish 14
♪ ε=<><<`)))<><<ﾟ)))彡~~⠀Fish 15
[<<<<+))<><<<<<<<<<< <<<<*))<><<=<<<<]⠀Fish 16
<><<ﾟ)##)彡⠀Fish 17
<><<ﾟ)))彡⠀Fish 18
<><<゜)))彡⠀Fish 19
゜~<><<゜))<><<<<<<⠀Fish 20
<><<゜)))<><<<<<<⠀Fish 21
<><<°))彡⠀Fish 22
<<<<・)))<><<<<<<<<<<⠀Fish 23
ミ．．ミ⠀Crabs 1
(/)(<,,<)(/)⠀Crabs 2
<><<=<<<<⠀Crabs 3
≧〔゜゜〕≦⠀Crabs 4
V=(° °)=V⠀Crabs 5
ミ(・・)ミ⠀Crabs 6
ミ[°°]ミ⠀Crabs 7
(V)oo<<(V)⠀Crabs 8
(*ꄱͦਵꄱͦ*)⠀Crabs 9
(V)(@,,,,@)(V)⠀Crabs 10
(V) (O ww O) (V)⠀Crabs 11
(V) (<,,,<) (V)⠀Crabs 12
＜コ：ミ⠀Squids 1
くコ:彡⠀Squids 2
くコ：彡⠀Squids 3
くコ：彡｡≠(￣～￣ )⠀Squids 4
くコ彡⠀Squids 5
（：。）ミ⠀Jellyfish 1
Ｃ：。ミ⠀Jellyfish 2
Ｃ：｡ミ⠀Jellyfish 3
@:≈⠀Jellyfish 4
. <><<<<<<{{{.______)⠀Whales 1
. <><<<<<<{{{o ______)⠀Whales 2
. <><<<<<<{{{x_______)⠀Whales 3
. <><<<<<<(((.______)⠀Whales 4
. <><<<<<<(((o ______)⠀Whales 5
. <><<<<<<(((x_______)⠀Whales 6
,=,e⠀Turtles 1
.=.e⠀Turtles 2
(◐ o ◑ )⠀Other Various Sea Creatures 1
<><<^)))<<<< ～～⠀Other Various Sea Creatures 2
(・8・)⠀Other Various Sea Creatures 3
☋⃘⠀Other Various Sea Creatures 4
<<<<コ:彡~~~~⠀Other Various Sea Creatures 5
ᗦ↞◃ 〜⠀Other Various Sea Creatures 6
(<`ー´)o/￣￣￣~<><<°)))彡⠀Fishing 1
ε-(￣(ｴ)￣*)/ ⌒<><<ﾟ)##)彡⠀Fishing 2
(　ﾟДﾟ)⊃⌒<><<゜)))彡⠀Fishing 3
(｡･ω･)o━<<<<コ：彡⠀Fishing 4
!(<｀-)/￣￣￣￣￣<><<ﾟ)))<><<彡⠀Fishing 5
(*^_^<)_o/━━━━━━<><<ﾟ)))≫彡 ~ ~ ~⠀Fishing 6
♪(oﾟｰﾟ)o＜爻爻爻爻爻爻爻爻<><<ﾟ)))彡爻爻爻爻爻⠀Fishing 7
∑(<￣(ｴ)￣)o/￣￣￣￣￣￣~ ゞ●)))彡⠀Fishing 8
<><<<<<<(((( ﾟ<<<<~￣￣￣＼o(￣(ｴ)￣)o/￣￣￣~<><<ﾟ ))))<><<<<<<⠀Fishing 9
<><<ﾟ<)))彡=3=3=3=3 ＼(￣(ｴ)￣＼))⠀Fishing 10
♪(*￣(ｴ)￣)o/￣￣￣￣￣￣~ <><<ﾟ )))<><<彡⠀Fishing 11
(“￣(ｴ)￣)o/￣￣￣￣~<><<ﾟ )++++<<<<<<<<⠀Fishing 12
,,,((／￣(ｴ)￣)／ ε=ε=ε=ε=ミ(((<ﾟ<<<<⠀Fishing 13
(｡´p｀)____¶⌒<><<゜)))333彡　★｡.::｡.::・’ﾟ⠀Fishing 14
(･ω･)ﾉ－－＝＝三三三 <><<ﾟ)))彡⠀Fishing 15
( ˘▽˘)っ♨⠀Food 1
◥█̆̈◤࿉∥⠀Food 2
♨(⋆‿⋆)♨⠀Food 3
ꊞ̩⁌•͡˻•⁍ᵒᵈᵃⁿᵍᵒ ⁿᵉ⠀Food 4
ℓ ❤ ϚϦοςӧԼձϮϵ❣⃛⠀Food 5
（￣ｗ￣）Ψ⠀Food 6
くコ：彡｡≠(￣～￣ )⠀Food 7
(●´з―━━━ε｀●)⠀Food 8
(▼д▼)o-{{[〃]}}⠀Food 9
( ・・)つ―{}@{}@{}-⠀Food 10
( ・・)つ-●●●⠀Food 11
―●○◎-⠀Food 12
( ・・)つ―●○◎-⠀Food 13
(　´∀｀)つ―●○◎-⠀Food 14
♪o<<<<( ´∀｀)っ┌iii┐⠀Food 15
(*･∀･)_Ω~⠀Food 16
(*ﾟДﾟ)つ-Oﾛ|<><<-⠀Food 17
ヽ|。´ェ｀|ﾉ ―■●▲⠀Food 18
(　・ω・)⊃-[二二]⠀Food 19
-●●●-ｃ(ω｀ｃ )⠀Food 20
―⊂ZZZ⊃⠀Food 21
─━━━━⠀Food 22
ʕ ಡ ﹏ ಡ ʔ⊃―{}@{}@{}-⠀Food 23
(　・ω・)⊃-[二<><< <><<二]-⊂(´∀｀ )⠀Food 24
<><<ﾟ)##)彡ｃ(｡･ェ･｡)っ━<<<<コ：彡━⠀Food 25
( -_-)旦~⠀Drink 1
(*^◇^)_旦⠀Drink 2
(＃´ー´)旦⠀Drink 3
(＾-＾)＿日⠀Drink 4
~(=^‥^)_旦~⠀Drink 5
~~旦_(･o･<)⠀Drink 6
(　 ゜Д゜)⊃旦⠀Drink 7
( ´･ω･`)_且~⠀Drink 8
( ^-^)_旦””⠀Drink 9
(； ｀ｪ´ ；)b三b⠀Drink 10
(。・・)_且⠀Drink 11
(*｀▽´)_旦~~⠀Drink 12
~旦_(^O^ )⠀Drink 13
ｏ口(・∀・ )⠀Drink 14
且_(・_・ )⠀Drink 15
且_(ﾟ◇ﾟ；)ノﾞ⠀Drink 16
ⅽ[ː̠̈ː̠̈ː̠̈] ͌⠀Drink 17
~(* ￣)-3旦ε-(￣ *)⠀Drink 18
((｡･”･)o自☆自o(･”･｡))⠀Drink 19
ｰ( ￣▽)_皿~~⠀Drink 20
( ^-)_旦~~ (ﾟoﾟ<)⠀Drink 21
(　ﾟДﾟ)⊃旦⠀Drink 22
((((´∀｀)＿旦～⠀Drink 23
(*´ｪ｀*)っ旦~⠀Drink 24
~~旦　ゝ(´-ω-｀ )⠀Drink 25
~~旦_(-ω-｀｡)⠀Drink 26
~~旦⊂(･∀･ )⠀Drink 27
(○^ω^)_旦~~♪⠀Drink 28
!!”(*<><<∀<<<<)o(酒)”⠀Drink 29
~~■P o(´・∀・｀ )⠀Drink 30
~~匸Pヽ(･ω･｀)⠀Drink 31
(*´・ω)o旦~┏┓⠀Drink 32
(*´-ω)o旦~┏┓⠀Drink 33
(　’ω’)旦~~┏━┓⠀Drink 34
( ͝° ͜ʖ͡°)つY⠀Drink 35
!(　・∀)つ且~~⊂(´∀｀ )⠀Drink 36
(●´▽｀●)_旦”☆”旦_(○´ー｀○)⠀Drink 37
ﾟ+｡:.(*･ω･)o旦　旦o(･ω･*).:｡+ﾟ⠀Drink 38
!(#ﾟДﾟ)ゞ‥･･━━━━━━旦~☆))｀ωﾟ)･<’.⠀Drink 39
(´・ω)ノ[|_|　|_|]ヽ(ω・｀)⠀Drink 40
( 。・_・。)人(。・_・。 )⠀High Five 1
( ⌒o⌒)人(⌒-⌒ )v⠀High Five 2
(･_･”)/＼(･_･”)⠀High Five 3
(*´∀｀*人*´∀｀*)⠀High Five 4
（*＾ω＾）人（＾ω＾*）⠀High Five 5
(°◇°人°◇°)⠀High Five 6
(=´∀`)人(´∀‘=)⠀High Five 7
(○｀ε´○)／＼(○｀ε´○)⠀High Five 8
ヘ( ^o^)ノ＼(^_^ )⠀High Five 9
( ｡･_･｡)人(｡･_･｡ )⠀High Five 10
（　＾＾）人（＾＾　）⠀High Five 11
(・_・”)／＼(・_・”)⠀High Five 12
(((＠°▽°＠)八(＠°▽°＠)))⠀High Five 13
(((*°▽°*)八(*°▽°*)))♪⠀High Five 14
(*･∀･)／＼(･∀･*)⠀High Five 15
（＾▽＾）／＼（＾▽＾）⠀High Five 16
(*^o^)人(^o^*)⠀High Five 17
(◎｀・ω・´)人(´・ω・｀*)⠀High Five 18
／(v x v｡)人(｡v x v)＼⠀High Five 19
＼（★´−｀）人（´▽｀★）／⠀High Five 20
☆-(ノﾟДﾟ)八(ﾟДﾟ )ノ⠀High Five 21
♡(*´∀｀*)人(*´∀｀*)♡⠀High Five 22
♪ヽ( ⌒o⌒)人(⌒-⌒ )v ♪⠀High Five 23
ヽ（　＾＾）人（＾＾　）ノ⠀High Five 24
ヽ(^ω^)人(^▽、^)ﾉ⠀High Five 25
ヽ(*^ｰ^)人(^ｰ^*)ノ⠀High Five 26
ヽ(∀゜ )人( ゜∀)ノ⠀High Five 27
♪(((#^-^)八(^_^*)))♪⠀High Five 28
(๑ ⁍̥̥̥᷅ ᴈ⁍̥̥̥᷅)人(⁌̥̥̥᷄ε ⁌̥̥̥᷄ ๑)ｰ⠀High Five 29
(｡• ̀д•́) 人 (•̀ω•́ )ﾊﾞ⠀High Five 30
ヾ(*⌒∇⌒)八(⌒∇⌒*)ツ⠀High Five 31
♪～(◔◡◔ิ)人(╹◡╹๑)～♪⠀High Five 32
ヾ(●･ｖ･人･ｖ･○)ﾉ⠀High Five 33
(▼▽▼)人(▼▽▼)⠀High Five 34
ヾ(●ﾟvﾟ)人(ﾟvﾟ○)ﾉ⠀High Five 35
(v´∀｀)ﾊ(´∀｀v)⠀High Five 36
(*●ω●)人(●ω●*)⠀High Five 37
(●゜□゜)人(゜□゜○)⠀High Five 38
(=゜ω゜)人(゜ω゜=)⠀High Five 39
ヽ(○｀･ェ･)人(･ェ･´●)ノ⠀High Five 40
|*゜ロ゜|人|゜ロ゜*|⠀High Five 41
♪(o=゜▽゜)人(゜▽゜=o)♪⠀High Five 42
(v〃∇〃)ハ(〃∇〃v)⠀High Five 43
ヾ(★´Д)人(Д｀☆)ノ゛⠀High Five 44
(♯ゝωσ♯)人(＋＞∀＜＋)ノ⠀High Five 45
(＊´ω｀人´∀｀＊)⠀High Five 46
(*・▽・)／＼(･▽･*）⠀High Five 47
┌|*゜ロ゜|人|゜ロ゜*|┐⠀High Five 48
ヽ（●´∀｀）人（´∀｀●）ノ⠀High Five 49
＼(#´▽｀)人(´▽｀#)ノ⠀High Five 50
＼(*｀∀´)人(｀∀´*)／⠀High Five 51
(*´∀｀)人(´∀｀*)⠀High Five 52
(ノ＾ω＾)ハ(＾ω＾ )ノ⠀High Five 53
(●ゝω)ノヽ(∀＜●)⠀High Five 54
!!(vﾟｰﾟ)ﾊ(ﾟ▽ﾟv)⠀High Five 55
｡*:★(´・ω・人・ω・`)｡:゜★｡⠀High Five 56
ヽ(　☸ ω ☸)人( ☸ ▽、 ☸ )ﾉ⠀High Five 57
♪♪♪ Ｕ・ｪ・Ｕ人(^･x･^=) ♪♪♪⠀High Five 58
（○・▽・○）人（●・▽・●）ノ⠀High Five 59
└(^o^ )Ｘ( ^o^)┘⠀Holding Hands 1
＼（＾∀＾）メ（＾∀＾）ノ⠀Holding Hands 2
ヾ(￣ー￣)X(^∇^)ゞ⠀Holding Hands 3
‹(⁽˙́ʷ˙̀⁾ )∨( ⁽˙́ʷ˙̀⁾)›⠀Holding Hands 4
(ી(΄◞ิ౪◟ิ‵)ʃ) (ી(΄◞ิ౪◟ิ‵)ʃ)⠀Holding Hands 5
(*◑∇◑)☞☜(◐∇◐*)⠀Holding Hands 6
ヽ(ﾟ▽ﾟ*)乂(*ﾟ▽ﾟ)ﾉ⠀Holding Hands 7
☆(*^o^)乂(^-^*)☆⠀Holding Hands 8
☆^v(*^∇’)乂(‘∇^*)v^☆⠀Holding Hands 9
(ﾉ*´･、<><<･)乂(・ι_・｀*)ﾉ⠀Holding Hands 10
━(p´･∀･)乂(･∀･｀q)━⠀Holding Hands 11
(ﾉ￣∇￣)乂(￣ｰ￣ )ﾉ⠀Holding Hands 12
♪(・∀・*)乂(*・∀・)ノ⠀Holding Hands 13
(*´･ω･)(･ω･`*)⠀Close Together 1
(Ɔ˘⌣˘)(˘⌣˘)˘⌣˘ C)⠀Close Together 2
＼(　^o)( ^ 0 ^ )(o^　)／⠀Close Together 3
(/^-^(^ ^*)/⠀Close Together 4
━(○´ｴ｀)(´ｴ｀●)━⠀Close Together 5
(<•͈́༚•͈̀)(•͈́༚•͈̀<)՞༘՞༘՞⠀Close Together 6
o(ﾟ益ﾟo)(oﾟ益ﾟ)o⠀Close Together 7
(٭′ᵕુ‵)ુ(ૂ′ᵕ‵ॢං)⠀Close Together 8
(*´ﾟд)(дﾟ｀*)⠀Close Together 9
⁽ ̇⌞.₎₍.⌟̇⁾⠀Close Together 10
(•′௰′)(‵௰‵•)⠀Close Together 11
(´･ω･`)(´-ω-`)⠀Close Together 12
(๑꒪▿꒪)*｡_｡)⠀Close Together 13
٩( ´◡` )( ´◡` )۶⠀Close Together 14
(๑´・‿・)(・‿・｀●)⠀Close Together 15
(⁎⁽⁰‸⁽⁰)(⁰⁾ˬ⁰⁾⁎)⠀Close Together 16
◟₍⁎꜇̈₎‸₍꜁̈⁎₎◞⠀Close Together 17
(⋆ु⁰ ̥̮⁽⁰)(⁰⁾ ̥̮⁰⋆ू)⠀Close Together 18
(❈ಥДಥ)(ಥДಥ❋)⠀Close Together 19
―(´￢O￢)(￢O￢｀)―⠀Close Together 20
(ؔؓؒؑؐ⁍◡ؔؓؒؑؐ⁍)(ؔؓؒؑؐ⁌◡ؔؓؒؑؐ⁌)⠀Close Together 21
(*´ω´(*｀ω｀)⠀Close Together 22
⑅❛⌔❛(❛ั▿ ❛ั ⋈⠀Close Together 23
(ｏ・_・)ノ”(ᴗ_ ᴗ。)⠀Cheering Up 1
(⁎·́௰·̀)◞ ͂͂(˒̩̩̥́௰˓̩̩̥̀⁎)⠀Cheering Up 2
( ‘́⌣’̀)/(˘̩̩ε˘̩ƪ)⠀Cheering Up 3
(*￣▽￣)ノ”(^ー^*)⠀Cheering Up 4
(*^ー^)ヾ(￣▽￣*)⠀Cheering Up 5
(*￣▽￣)ノ”(^∇^*)⠀Cheering Up 6
(*^∇^)ヾ(￣▽￣*)⠀Cheering Up 7
(*￣▽￣)ノ”(- -*)⠀Cheering Up 8
(*- -)ヾ(￣▽￣*)⠀Cheering Up 9
(*￣▽￣)ノ”(ﾟ∇ﾟ*)⠀Cheering Up 10
(*ﾟ∇ﾟ)ヾ(￣▽￣*)⠀Cheering Up 11
(*￣▽￣)ノ”(ﾟーﾟ*)⠀Cheering Up 12
(*ﾟーﾟ)ヾ(￣▽￣*)⠀Cheering Up 13
(*’-’)ノ”(^o^*)⠀Cheering Up 14
(*^o^)ヾ(‘-’*)⠀Cheering Up 15
(*´・ω・)ノ(-ω-｀*)⠀Cheering Up 16
(*~ρ~)ﾉ(ToTw)⠀Cheering Up 17
(^ｘ^<ヾ(^^ )⠀Cheering Up 18
(*-ω-)ヾ(・ω・*)⠀Cheering Up 19
( i_i)＼(^_^ )⠀Cheering Up 20
…ρ(..、)ヾ(^ー^<)⠀Cheering Up 21
…ρ(。。、)ヾ(^-^<)⠀Cheering Up 22
…ρ(｡｡､)ヾ(^-^<)⠀Cheering Up 23
(o・_・)ノ”(ノ_＜。)⠀Cheering Up 24
(o･_･)ﾉ”(ﾉ_＜。)⠀Cheering Up 25
(○ﾟωﾟ)(○｡_｡)ﾍﾟ⠀Cheering Up 26
(　ﾟωﾟ)/ (ﾉω`)ヽ(ﾟωﾟ　)⠀Cheering Up 27
(´._.`)\(‘́⌣’̀ )⠀Cheering Up 28
(๑*◡*๑)٩(❛ัᴗ❛ั⁎)ೄ⠀Cheering Up 29
( ￣▽￣)ﾉ”o(*・・*)oヾ(￣▽￣ )⠀Cheering Up 30
(＾○＾)オ(＾▽＾)ハ(＾０＾)ツ～⠀Lots of Friends 1
(〃￣д￣)八( ￣д￣ )八(￣д￣〃)⠀Lots of Friends 2
(〃⌒▽⌒)八(〃⌒▽⌒〃)八(⌒▽⌒〃)⠀Lots of Friends 3
(^^)-(^^)-(^^)-(^^)-(^^)⠀Lots of Friends 4
ヽ(´Д｀)人(´Д｀)人(´Д｀)ノ⠀Lots of Friends 5
ヽ(´Д｀)人(´Д｀)人(´Д｀)ノ〜♪⠀Lots of Friends 6
ヽ(＾▽＾)人(＾▽＾)人(＾▽＾)ﾉ⠀Lots of Friends 7
ヽ(○´∀)乂(*´∀`*）乂(∀`●)⠀Lots of Friends 8
(*σᴗσ)(ㅎᴗㅎ )　｜‸눈<)⠀Lots of Friends 9
̑⁽ᵕ̈⁾ ̆ ̀⁽ᵕ̈⁾ ́˂⁽ᵕ̈⁾˃˓⁽ᵕ̈⁾˒ ͑⁽ᵕ̈⁾ ͗ ̀⁽ᵕ̈⁾ ͛  ͗ ͗ᵞᵃᵞ⠀Lots of Friends 10
(•̴̑.̶̥•̴̑ (•̥̑.̮•̥̑) •̴̑.̶̥•̴̑)⠀Lots of Friends 11
╮(•́ω•̀)╭╮(•́ω•̀)╭╮(•́ω•̀)╭⠀Lots of Friends 12
( ･◡͐･)’◡͐’)`◡͐´)°◡͐°)^◡͐^)´◡͐`)⠀Lots of Friends 13
(‘౪’(`౪´(^౪^(´･౪･`)´౪`)°౪°)-౪-)⠀Lots of Friends 14
(*T_T)人(T^T)人(T_T*)⠀Lots of Friends 15
ꉂ (ˊଠୃˋꉧˊଠୄˋꉧˊଠୁˋ)ꋧ⠀Lots of Friends 16
ヽ(*ﾟ∀ﾟ)ﾉ||ヽ(･∀･)ﾉ||ヽ(ﾟ∀ﾟ*)ﾉ⠀Lots of Friends 17
ヾ｜*￣ー￣｜*￣ー￣｜/”　　ヾ｜*￣∇￣*｜⠀Lots of Friends 18
（・ω（・∀（・д・）３・）Λ・）⠀Lots of Friends 19
-(ﾉ｡･ω･)八(｡･ω･｡)八(･ω･｡)ﾉ-⠀Lots of Friends 20
( (￣ (ｰ￣( ｰ￣(￣ｰ￣(￣ｰ￣))⠀Lots of Friends 21
ヽ(゜∀゜)メ(゜∀゜)メ(゜∀゜)ノ⠀Lots of Friends 22
♪♪(((≧▽≦)八(≧▽≦)八(≧▽≦)))♪♪⠀Lots of Friends 23
(((￣(￣(￣(￣ー￣)￣)￣)￣)))⠀Lots of Friends 24
((≧(≧∇(≧∇≦(≧∇≦)≧∇≦)∇≦)≦)))⠀Lots of Friends 25
((((･ิ(･ิω(･ิω･ิ)ω･ิ)･ิ))))⠀Lots of Friends 26
＼(•̀.̫•)-(•̀.̫•)-(•̀.̫•)／⠀Lots of Friends 27
＼(⑅•̀.̫•)-(⑅•̀.̫•)-(⑅•̀.̫•)／⠀Lots of Friends 28
(・ω・`(・ω・`(・ω・`)⠀Lots of Friends 29
(∞’v`)◎’vﾟ)(∞’v`)◎’vﾟ)⠀Lots of Friends 30
ﾍ(ﾟ∀ﾟﾍ)ﾍ(ﾟ∀ﾟﾍ)ﾍ(ﾟ∀ﾟﾍ)⠀Lots of Friends 31
(ﾉ<><<ω<<<<)八(●´ω｀)八(′ω｀○)⠀Lots of Friends 32
꒰·͡ुˑ·ཻू꒱*̫ෆ๋*̫꒰•ི̫͡ુ•ྀૂ꒱*̫ෆ๋*̫꒰•̻̀ु•́ू໊꒱*̫ෆ๋*̫꒰•̹͡ु-ོू꒱*̫ෆ๋*̫꒰•̹͡ິु•ິू꒱⠀Lots of Friends 33
（￣(仝)￣）人（￣(仝)￣）人（￣(仝)￣）⠀Lots of Friends 34
（´ゝω・（´ゝω・（´ゝω・｀）´ゝω・）´ゝω・）⠀Lots of Friends 35
ヽ(ﾟ∇ﾟ(ﾟ∇ﾟ(ﾟ∇ﾟo(ﾟ∇ﾟ)oﾟ∇ﾟ)ﾟ∇ﾟ)ﾟ∇ﾟ)ﾉ⠀Lots of Friends 36
o┤*´Д｀*├oo┤*´Д｀*├oo┤*´Д｀*├oo┤*´Д｀*├o⠀Lots of Friends 37
(　´∀｀)・ω・) ゜Д゜)・∀・)￣ー￣)´_ゝ`)⠀Lots of Friends 38
(((￣(￣ｰ(￣ー(￣ー￣)ー￣)ｰ￣)￣)))⠀Lots of Friends 39
（(￣ー+(￣ー+(￣ー+(￣ー+(￣ー+￣)ー+￣)ー+￣)ー+￣)ー+￣)⠀Lots of Friends 40
(￣ー￣)ー￣)ー￣)ー￣）ー￣）ー￣）ー￣）⠀Lots of Friends 41
(´･(´･(´･(´･(´･(´･д･`) ･`)･`)･`)･`)･`)⠀Lots of Friends 42
＼(⌒∇⌒(⌒∇⌒(⌒∇⌒)⌒∇⌒)⌒∇⌒)／⠀Lots of Friends 43
ψ`ー´)ﾉψ`ー´)ﾉψ`ー´)ﾉψ`ー´)ﾉψ`ー´)ﾉψ`ー´)⠀Lots of Friends 44
(ﾟ艸ﾟ(｡艸｡(ﾟ艸ﾟ(｡艸｡(ﾟ艸ﾟ(｡艸｡(ﾟ艸ﾟ(｡艸｡(ﾟ艸ﾟ(｡艸｡ )⠀Lots of Friends 45
˹⁽ˆ˹⁽ˆ⁰˹⁽ˆ⁰ˆ˹⁽ˆ⁰ˆ˺ ⁾˺ʾʾʾʾ⠀Lots of Friends 46
⁽˙³˙⁾◟( ˘•ω•˘ )◞⁽˙³˙⁾⠀Lots of Friends 47
(ꈍεꈍ (ꈍ□ꈍ (ꈍㅿꈍ (ꈍ罒ꈍ﹡)⠀Lots of Friends 48
(꒪ꇴ꒪ (꒪ꇴ꒪ (꒪ꇴ꒪ <)⠀Lots of Friends 49
⁽⁽◝( ꒪͒∀꒪͒ )◜⁾⁾≡₍₍◞( ꒪͒∀꒪͒ )◟₎₎⁽⁽◝( ꒪͒∀꒪͒ )◜⁾⁾≡₍₍◞( ꒪͒∀꒪͒ )◟₎₎⠀Lots of Friends 50
┗(⌒)(╬◓ω◔╬)(⌒)┛⠀Lots of Friends 51
(人-ω-)｡o.ﾟ｡*･★Good Ni>h<★･*｡ﾟo｡(-ω-人)⠀Words 1
(人*´∪`)♪тнайк　чоц♪(´∪`*人)⠀Words 2
(人❛ᴗ❛)♪тнайк　чоц♪(❛ᴗ❛*人)⠀Words 3
˓˓(ृ　 ु ॑꒳’)ु(ृ’꒳ ॑ ृ　)ु˒˒˒⠀Complex 1
♬♩˂₍͔⁽ˆ⁰ˆ⁾₎͔˃ ͟͟͞͞≣͟ ͟͟͞͞˂₍͕⁽ˆ⁰ˆ⁾₎͕˃♪♫⠀Complex 2
(ृ ु ´͈ ᵕ `͈ )ु❀(ृˊ͈ ꒳ृ ˋ͈　)ु⠀Complex 3
(*´°̥̥̥̥̥̥̥̥﹏°̥̥̥̥̥̥̥̥ )人(´°̥̥̥̥̥̥̥̥ω°̥̥̥̥̥̥̥̥｀)⠀Complex 4
*✲ﾟ*｡✧٩(･ิᴗ･ิ๑)۶٩(･ิᴗ･ิ๑)۶*✲ﾟ*｡✧⠀Complex 5
✧( ु•⌄• )◞◟( •⌄• ू )✧⠀Miscellaneous 1
⁽⁽◝(๑꒪່౪̮꒪່๑)◜⁾⁾≡₍₍◞(๑꒪່౪̮꒪່๑)◟₎₎⠀Miscellaneous 2
＼(◑д◐)＞∠(◑д◐)⠀Miscellaneous 3
┌(｡°з ┐ )┘三└( ┌ ε°｡)┐┘⠀Miscellaneous 4
°˖✧⁽⁽◝(⁰▿⁰)◜◝(⁰▿⁰)◟₎₎✧˖°⠀Miscellaneous 5
\(●⁰౪⁰●\)(//●⁰౪⁰●)//⠀Miscellaneous 6
♫͙◟̊₍ꃓ₎◞◟₍ꃔ₎◞̊♫͙⠀Miscellaneous 7
\(ϋ)/\(ϋ)/♩⠀Miscellaneous 8
(✜ฺ’д’)从(‘д’✜ฺ)⠀Miscellaneous 9
✧(๑✪д✪)۶ㅂ٩(✪д✪๑)✧⠀Miscellaneous 10
◟(˓⸂⠊̮)◜◟(⠑̮⸃⸒)◜⠀Miscellaneous 11
(☞ﾟヮﾟ)☞ ☜(ﾟヮﾟ☜)⠀Miscellaneous 12
(っ´ω`)っ☂⊂(´ω`⊂ )⠀Miscellaneous 13
☆-(ﾉ●´∀)八(∀｀●)ﾉ⠀Miscellaneous 14
ﾍ(ﾟ∀ﾟ*)ﾉヽ(*ﾟ∀ﾟ)ﾉ⠀Miscellaneous 15
ヽ(･_･ ) (･_･)/⠀Miscellaneous 16
(( *~∇~)从(^-^*))⠀Miscellaneous 17
(*´ 艸`)(´艸 `*)⠀Miscellaneous 18
(*、｡艸｡)(ﾟ艸ﾟ`*)⠀Miscellaneous 19
（　◜◡‾）（‾◡◝　）⠀Miscellaneous 20
(・_・)〆＼(Ｔ＿Ｔ）⠀Miscellaneous 21
٩(⑅´◡` )۶٩( ´◡`⑅)۶ᵋᵎᵌ⁎४*✧⠀Miscellaneous 22
ヾ⊂((〃´⊥｀〃))⊃ノヾ⊂((〃´⊥｀〃))⊃ノ⠀Miscellaneous 23
($*’vﾟ)ﾉ【☆.｡.:*.ﾟ ﾟ.*:.｡.☆】ヽ(´v`*◇)⠀Miscellaneous 24
（三・o・）三☆三（｀ε´三）⠀Miscellaneous 25
∕∕ ∕ ∕∕˛₍˴◅ˋ)੭✧८(ˋ▻˴₎₇∖∖ ∖ ∖∖⠀Miscellaneous 26
(<-_-)/⠀Drops of Sweat 1
(一。一<<）⠀Drops of Sweat 2
（￣□￣；）⠀Drops of Sweat 3
（；￣д￣）⠀Drops of Sweat 4
（◎ー◎；）⠀Drops of Sweat 5
（ー△ー；）⠀Drops of Sweat 6
/(<-_-)⠀Drops of Sweat 7
ヾ(-_-<)⠀Drops of Sweat 8
o(-_-<*)⠀Drops of Sweat 9
y-(~。~；)⠀Drops of Sweat 10
彡(-_-<)彡⠀Drops of Sweat 11
o(- -<*)ゞ⠀Drops of Sweat 12
(/ _ < )⠀Drops of Sweat 13
(/ _ < )⠀Drops of Sweat 14
(<*´Д`)ﾉ⠀Drops of Sweat 15
(<-_-)ノ⠀Drops of Sweat 16
└(―_―；)_―；)―；)；))┐⠀Drops of Sweat 17
(oT-T)尸⠀Waving a Flag to Surrender 1
(￣^￣)尸⠀Waving a Flag to Surrender 2
ლ（ӨᆸӨ）۳⠀Waving a Flag to Surrender 3
˄̞⁽⁽⚑(꒪ͦᴗ̵̍꒪ͦ=͟͟͞͞ ꒪ͦ ˈ̫̮ ꒪ͦ)⚑⁾⁾˄̩̞⠀Waving a Flag to Surrender 4
(o尸’▽’)o尸⠀Waving a Flag to Surrender 5
(○p<><<ω<<<<)尸”⠀Waving a Flag to Surrender 6
!(*´∀｀*)尸”⠀Waving a Flag to Surrender 7
(oT-T)尸~~⠀Waving a Flag to Surrender 8
o-[･o･]-o尸⠀Waving a Flag to Surrender 9
(o_ _)o⠀Arms Up in a Minimal Effort Giving Up Sort of Way 1
(ﾉ_ _)ﾉ⠀Arms Up in a Minimal Effort Giving Up Sort of Way 2
(ノ#-_-)ノ⠀Arms Up in a Minimal Effort Giving Up Sort of Way 3
(ﾉ´ｰ`)ﾉ⠀Arms Up in a Minimal Effort Giving Up Sort of Way 4
(ﾉ￣д￣)ﾉ⠀Arms Up in a Minimal Effort Giving Up Sort of Way 5
<(-_-<)⠀Arms Up in a Minimal Effort Giving Up Sort of Way 6
ヘ(_ _ヘ)⠀Arms Up in a Minimal Effort Giving Up Sort of Way 7
ﾍ(<´Д｀ﾍ)⠀Arms Up in a Minimal Effort Giving Up Sort of Way 8
ヘ（´ｏ｀）ヘ⠀Arms Up in a Minimal Effort Giving Up Sort of Way 9
ﾍ(￣ ￣<ﾍ)⠀Arms Up in a Minimal Effort Giving Up Sort of Way 10
ヘ(￣ー￣ヘ)⠀Arms Up in a Minimal Effort Giving Up Sort of Way 11
<(-.-<)⠀Arms Up in a Minimal Effort Giving Up Sort of Way 12
Y(-.-Y)⠀Arms Up in a Minimal Effort Giving Up Sort of Way 13
ﾍ(-.-ﾍ<)…⠀Arms Up in a Minimal Effort Giving Up Sort of Way 14
੧(⸍⸓⸌੧)⠀Arms Up in a Minimal Effort Giving Up Sort of Way 15
{ﾉ｡⊍_⊍｡}ﾉ⠀Arms Up in a Minimal Effort Giving Up Sort of Way 16
|┘–|┘~⠀Arms Up in a Minimal Effort Giving Up Sort of Way 17
」（。。）L⠀Arms Up in a Minimal Effort Giving Up Sort of Way 18
＼( ｀.∀´)／⠀Arms Up with More Enthusiasm 1
＼(-___________-<)／⠀Arms Up with More Enthusiasm 2
＼（－－）／⠀Arms Up with More Enthusiasm 3
ヽ(｀◇´)/⠀Arms Up with More Enthusiasm 4
ƪ(‾_‾)ʃ⠀Arms Up with More Enthusiasm 5
\(-ㅂ-)/⠀Arms Up with More Enthusiasm 6
٩(-̃_̮̮̃-̃)۶⠀Arms Up with More Enthusiasm 7
┌（-.-)┐⠀Arms Down 1
╭✬⌢✬╮⠀Arms Down 2
……┌┤´д`├┐⠀Arms Down 3
o(╥﹏╥)o⠀Miscellaneous forms of Defeat 1
~(<><<_<<<<。)＼⠀Miscellaneous forms of Defeat 2
(-_＼)⠀Miscellaneous forms of Defeat 3
(。-ω-)ﾉ⠀Miscellaneous forms of Defeat 4
＼(-o- )⠀Miscellaneous forms of Defeat 5
（~～~）⠀Miscellaneous forms of Defeat 6
(@⠀Miscellaneous forms of Defeat 7
[emai<<#160<pro<ec<ed]⠀Miscellaneous forms of Defeat 8
)⠀Miscellaneous forms of Defeat 9
((-_-))⠀Miscellaneous forms of Defeat 10
(　-。-)⠀Miscellaneous forms of Defeat 11
( ͡° ͜ʖ ͡°)⠀Famous Happy Emoticons 1
∠( ᐛ 」∠)＿⠀Famous Happy Emoticons 2
(ﾟ⊿ﾟ)⠀Famous Happy Emoticons 3
ᕕ( ᐛ )ᕗ⠀Famous Happy Emoticons 4
_へ__(‾◡◝ )<><<⠀Famous Happy Emoticons 5
( ᐛ )و⠀Famous Happy Emoticons 6
( ◞･౪･)⠀Famous Happy Emoticons 7
( ´ ▽ ` )ﾉ⠀Triangle Mouths 1
(*^▽^*)⠀Triangle Mouths 2
(´∇ﾉ｀*)ノ⠀Triangle Mouths 3
(ノ^∇^)⠀Triangle Mouths 4
⊂((・▽・))⊃⠀Triangle Mouths 5
(　＾∇＾)⠀Triangle Mouths 6
( ﾟ▽ﾟ)/⠀Triangle Mouths 7
（‐＾▽＾‐）⠀Triangle Mouths 8
(“⌒∇⌒”)⠀Triangle Mouths 9
（*´▽｀*）⠀Triangle Mouths 10
(*＾▽＾)／⠀Triangle Mouths 11
(*^▽^*)⠀Triangle Mouths 12
(*~▽~)⠀Triangle Mouths 13
(*≧▽≦)⠀Triangle Mouths 14
(*⌒∇⌒*)⠀Triangle Mouths 15
(*⌒▽⌒*)θ～♪⠀Triangle Mouths 16
(/^▽^)/⠀Triangle Mouths 17
(^∇^)⠀Triangle Mouths 18
(＾▽＾)⠀Triangle Mouths 19
(￣▽￣)ノ⠀Triangle Mouths 20
(￣▽+￣*)⠀Triangle Mouths 21
(゜▽゜<)⠀Triangle Mouths 22
（=´∇｀=）⠀Triangle Mouths 23
(＝⌒▽⌒＝)⠀Triangle Mouths 24
(≡^∇^≡)⠀Triangle Mouths 25
(≧∇≦)/⠀Triangle Mouths 26
（⌒▽⌒）⠀Triangle Mouths 27
(⌒▽⌒)☆⠀Triangle Mouths 28
（⌒▽⌒ゞ⠀Triangle Mouths 29
(●⌒∇⌒●)⠀Triangle Mouths 30
(❁´▽`❁)*✲ﾟ*⠀Triangle Mouths 31
(ノ*゜▽゜*)⠀Triangle Mouths 32
°˖✧◝(⁰▿⁰)◜✧˖°⠀Triangle Mouths 33
~ヾ(＾∇＾)⠀Triangle Mouths 34
∩(︶▽︶)∩⠀Triangle Mouths 35
≧(´▽｀)≦⠀Triangle Mouths 36
ー( ´ ▽ ` )ﾉ⠀Triangle Mouths 37
ヾ(´▽｀<)ゝ⠀Triangle Mouths 38
ヾ(＾∇＾)⠀Triangle Mouths 39
d=(´▽｀)=b⠀Triangle Mouths 40
o(〃＾▽＾〃)o⠀Triangle Mouths 41
o(^▽^)o⠀Triangle Mouths 42
Ｏ(≧∇≦)Ｏ⠀Triangle Mouths 43
o(≧∇≦o)⠀Triangle Mouths 44
(๑꒪▿꒪)*⠀Triangle Mouths 45
(⁎⚈᷀᷁▿⚈᷀᷁⁎)⠀Triangle Mouths 46
(≧∇≦*)⠀Triangle Mouths 47
(=^▽^=)⠀Triangle Mouths 48
o(*^▽^*)o⠀Triangle Mouths 49
೭੧(❛▿❛✿)੭೨⠀Triangle Mouths 50
☜(⌒▽⌒)☞⠀Triangle Mouths 51
☜(˚▽˚)☞⠀Triangle Mouths 52
ɾ⚈▿⚈ɹ⠀Triangle Mouths 53
ﾍ(=￣∇￣)ﾉ⠀Triangle Mouths 54
φ(*⌒▽⌒)ﾉ⠀Triangle Mouths 55
(*･▽･*)⠀Triangle Mouths 56
(☆▽☆)⠀Triangle Mouths 57
≡(*′▽`)っ⠀Triangle Mouths 58
」(￣▽￣」)⠀Triangle Mouths 59
(〃⌒∇⌒)⠀Triangle Mouths 60
〔´∇｀〕⠀Triangle Mouths 61
(゜▼゜＊）⠀Triangle Mouths 62
໒( ͡ᵔ ▾ ͡ᵔ )७⠀Triangle Mouths 63
(｡´∀｀)ﾉ⠀Upside Down A Mouths 1
(　´∀｀)⠀Upside Down A Mouths 2
(・∀・)⠀Upside Down A Mouths 3
(´∀`)⠀Upside Down A Mouths 4
(°∀°)b⠀Upside Down A Mouths 5
(●´∀｀●)⠀Upside Down A Mouths 6
(✌ﾟ∀ﾟ)☞⠀Upside Down A Mouths 7
*(*´∀｀*)☆⠀Upside Down A Mouths 8
( ´ ∀ ` )⠀Upside Down A Mouths 9
ヽ(･∀･)ﾉ⠀Upside Down A Mouths 10
(。≖ˇ∀ˇ≖。)⠀Upside Down A Mouths 11
((o(´∀｀)o))⠀Upside Down A Mouths 12
o(´∀｀*)⠀Upside Down A Mouths 13
(ﾟ∀ﾟ　)⠀Upside Down A Mouths 14
(*≧∀≦*)⠀Upside Down A Mouths 15
(*ﾟ∀ﾟ*)⠀Upside Down A Mouths 16
ヾ(*´∀｀*)ﾉ⠀Upside Down A Mouths 17
(o^∀^o)⠀Upside Down A Mouths 18
ヾ(^ิ∀^ิ)⠀Upside Down A Mouths 19
o(｀・∀・´)○⠀Upside Down A Mouths 20
(ᗒᗊᗕ)⠀Upside Down A Mouths 21
(ノ・∀・)ノ⠀Upside Down A Mouths 22
o((◕ฺ∀ ◕✿ฺ))o⠀Upside Down A Mouths 23
～̎̎٩(⌒͡∀⌒͡⌯̊)̥̊◦⠀Upside Down A Mouths 24
(´･∀･`)⠀Upside Down A Mouths 25
∩(´∀｀∩)⠀Upside Down A Mouths 26
(ﾉ `･∀･)ﾉﾞ⠀Upside Down A Mouths 27
( ﾟ∀ ﾟ)⠀Upside Down A Mouths 28
Ψ(ﾟ∀ﾟ )Ψ⠀Upside Down A Mouths 29
Ψ(　ﾟ∀ﾟ)Ψ⠀Upside Down A Mouths 30
Ψ(ﾟ∀ﾟ)Ψ⠀Upside Down A Mouths 31
d┃･∀･┃b⠀Upside Down A Mouths 32
(*´･∀･)⠀Upside Down A Mouths 33
(･∀･○)⠀Upside Down A Mouths 34
【°∀°】⠀Upside Down A Mouths 35
（★￣∀￣★）⠀Upside Down A Mouths 36
(m*´∀`)m⠀Upside Down A Mouths 37
=͟͟͞͞( ✌°∀° )☛⠀Upside Down A Mouths 38
∩(´∀`∩)⠀Upside Down A Mouths 39
∩( ´∀` )∩⠀Upside Down A Mouths 40
(∩´∀`)∩⠀Upside Down A Mouths 41
⊂( ・ ̫・)⊃⠀Squiggly Mouths 1
(*′☉.̫☉)⠀Squiggly Mouths 2
((ඏ.̫ඏ*))⠀Squiggly Mouths 3
⁽͑˙ˆ˙̫ˆ˙⁾̉⠀Squiggly Mouths 4
(๑★ .̫ ★๑)⠀Squiggly Mouths 5
‧⁺◟( ᵒ̴̶̷̥́ ·̫ ᵒ̴̶̷̣̥̀ )⠀Squiggly Mouths 6
(^～^)⠀Squiggly Mouths 7
(⌯⚈ै〰̇⚈ै)⠀Squiggly Mouths 8
( ‾ʖ̫‾)⠀Squiggly Mouths 9
(̂ ˃̥̥̥ ˑ̫ ˂̥̥̥ )̂⠀Squiggly Mouths 10
⁽ˇ́˙̫ˇ̀˵⁾⠀Squiggly Mouths 11
( ᵕ̤ ‧̫̮ ᵕ̤ )⠀Squiggly Mouths 12
⁽͑΅ ˙̫ ῭⁾̉⠀Squiggly Mouths 13
(⋆ʾ ˙̫̮ ʿ⋆)⠀Squiggly Mouths 14
੭व(๑• .̫ •๑) ✧⠀Squiggly Mouths 15
(*′☉.̫☉)⠀Squiggly Mouths 16
⁽͑˙՞˙̫՞˙⁾̉⠀Squiggly Mouths 17
(´•.̫ • ⋈)⠀Squiggly Mouths 18
( ❝̆ ·̫̮ ❝̆ )✧⠀Squiggly Mouths 19
((⚆·̫⚆‧̣̥̇ ))⠀Squiggly Mouths 20
(⚭⃚⃙̛·̫⚭⃚⃙̛)⠀Squiggly Mouths 21
(*ꅔ ˙̫̮ ꅔ*)⠀Squiggly Mouths 22
₍꒵꒱ꂶ ˙̫ ꂶ꒰꒵₎⌕⠀Squiggly Mouths 23
(Θ̎Ͻ̫̥Θ̎)⠀Squiggly Mouths 24
⚈้̤͡ ˌ̫̮ ⚈้̤͡⠀Squiggly Mouths 25
ᗧʻ̑ ˙̫ ʻ̑ᗤ⠀Squiggly Mouths 26
( •́ .̫ •̀ )⠀Squiggly Mouths 27
(*´・ｖ・)⠀V Mouths 1
(*＾v＾*)⠀V Mouths 2
（＾ｖ＾）⠀V Mouths 3
(▰˘v˘▰)⠀V Mouths 4
(n˘v˘•)¬⠀V Mouths 5
(´｡･v･｡｀)⠀V Mouths 6
♡✧( ु•⌄• )⠀V Mouths 7
( •⌄• ू )✧⠀V Mouths 8
(⌯⌅⌄⌅)⠀V Mouths 9
῍̩̞(∗ɞ⌄ɞ∗)◞⠀V Mouths 10
(′ʘ⌄ʘ‵)⠀V Mouths 11
( ^_^)／⠀Simple Flat Mouths 1
(^ _ ^)/⠀Simple Flat Mouths 2
（＾_＾）⠀Simple Flat Mouths 3
(^-^*)/⠀Simple Flat Mouths 4
（￣ー￣）⠀Simple Flat Mouths 5
(∩_∩)⠀Simple Flat Mouths 6
(∩▂∩)⠀Simple Flat Mouths 7
(☆^ー^☆)⠀Simple Flat Mouths 8
（ｖ＾＿＾）ｖ⠀Simple Flat Mouths 9
p(*＾-＾*)q⠀Simple Flat Mouths 10
(^・ω・^ )⠀Squiggly W Mouth Emoticons 1
(=^-ω-^=)⠀Squiggly W Mouth Emoticons 2
(=^･ω･^)y＝⠀Squiggly W Mouth Emoticons 3
( ﾉ^ω^)ﾉﾟ⠀Squiggly W Mouth Emoticons 4
（＿´ω｀）⠀Squiggly W Mouth Emoticons 5
(｡･ω･｡)⠀Squiggly W Mouth Emoticons 6
(︶ω︶)⠀Squiggly W Mouth Emoticons 7
(｀・ω・´)”⠀Squiggly W Mouth Emoticons 8
(´ω｀★)⠀Squiggly W Mouth Emoticons 9
(＾ω＾)⠀Squiggly W Mouth Emoticons 10
(◐ω◑ )⠀Squiggly W Mouth Emoticons 11
∩( ・ω・)∩⠀Squiggly W Mouth Emoticons 12
ヾ(｡･ω･｡)⠀Squiggly W Mouth Emoticons 13
୧( ॑ധ ॑)୨⠀Squiggly W Mouth Emoticons 14
d(=^･ω･^=)b⠀Squiggly W Mouth Emoticons 15
ｏ（Ｕ・ω・）⊃⠀Squiggly W Mouth Emoticons 16
V(=^･ω･^=)v⠀Squiggly W Mouth Emoticons 17
川´･ω･`川⠀Squiggly W Mouth Emoticons 18
(*´꒳`*)⠀Squiggly W Mouth Emoticons 19
(*^ω^*)⠀Squiggly W Mouth Emoticons 20
(❁´ω`❁)⠀Squiggly W Mouth Emoticons 21
(´-ω-`)⠀Squiggly W Mouth Emoticons 22
ଘ(੭ˊ꒳ˋ)੭✧⠀Squiggly W Mouth Emoticons 23
(´へωへ`*)⠀Squiggly W Mouth Emoticons 24
(　^ω^）⠀Squiggly W Mouth Emoticons 25
（　＾ω＾）⠀Squiggly W Mouth Emoticons 26
(✌’ω’)✌⠀Squiggly W Mouth Emoticons 27
✌(‘ω’)✌⠀Squiggly W Mouth Emoticons 28
✌(‘ω’✌)⠀Squiggly W Mouth Emoticons 29
٩(ↁωↁ❀)⠀Squiggly W Mouth Emoticons 30
˚✧₊⁎( ˘ω˘ )⁎⁺˳✧༚⠀Squiggly W Mouth Emoticons 31
(◜௰◝)⠀Squiggly W Mouth Emoticons 32
✾(〜 ☌ω☌)〜✾⠀Squiggly W Mouth Emoticons 33
(´∩ω∩｀)⠀Squiggly W Mouth Emoticons 34
(¬‿¬)⠀Standard Smily Mouth Emoticons 1
( ⋂‿⋂’)⠀Standard Smily Mouth Emoticons 2
(-‿◦☀)⠀Standard Smily Mouth Emoticons 3
(*‿*✿)⠀Standard Smily Mouth Emoticons 4
(•‿•)⠀Standard Smily Mouth Emoticons 5
(•̀ᴗ•́)و ̑̑⠀Standard Smily Mouth Emoticons 6
(─‿─)⠀Standard Smily Mouth Emoticons 7
(◍•ᴗ•◍)❤⠀Standard Smily Mouth Emoticons 8
(◑‿◐)⠀Standard Smily Mouth Emoticons 9
(✿´‿`)⠀Standard Smily Mouth Emoticons 10
(❀◦‿◦)⠀Standard Smily Mouth Emoticons 11
(❁´‿`❁)*✲ﾟ*⠀Standard Smily Mouth Emoticons 12
(ᅌᴗᅌ* )⠀Standard Smily Mouth Emoticons 13
(•ˇ‿ˇ•)-→⠀Standard Smily Mouth Emoticons 14
♫꒰･‿･๑꒱⠀Standard Smily Mouth Emoticons 15
o (^‿^✿)⠀Standard Smily Mouth Emoticons 16
(◑‿◐✿)⠀Standard Smily Mouth Emoticons 17
(◡‿◡✿)⠀Standard Smily Mouth Emoticons 18
(✿◠‿◠)⠀Standard Smily Mouth Emoticons 19
(◕‿◕✿)⠀Standard Smily Mouth Emoticons 20
(๑<><<ᴗ<<<<๑)⠀Standard Smily Mouth Emoticons 21
(๑✧◡✧๑)⠀Standard Smily Mouth Emoticons 22
(๑<><<◡<<<<๑)⠀Standard Smily Mouth Emoticons 23
♪(๑ᴖ◡ᴖ๑)♪⠀Standard Smily Mouth Emoticons 24
(｡◝‿◜｡)⠀Standard Smily Mouth Emoticons 25
(๑^ں^๑)⠀Standard Smily Mouth Emoticons 26
( ்ͦˏ౦͜ˎ ்ͦ)⠀Standard Smily Mouth Emoticons 27
(ෆ ͒•∘̬• ͒)◞⠀Standard Smily Mouth Emoticons 28
(•⚗৺⚗•)⠀Standard Smily Mouth Emoticons 29
(ට˓˳̮ට๑)⠀Standard Smily Mouth Emoticons 30
(๑•͈ᴗ•͈)⠀Standard Smily Mouth Emoticons 31
₍՞◌′ᵕ‵ू◌₎♡⠀Standard Smily Mouth Emoticons 32
(੭ˊ͈ ꒵ˋ͈)੭̸*✧⁺˚⠀Standard Smily Mouth Emoticons 33
꒰⁎ᵉ̷͈ ॣ꒵ ॢᵉ̷͈⁎꒱໊⠀Standard Smily Mouth Emoticons 34
(⑅˘͈ ᵕ ˘͈ )⠀Standard Smily Mouth Emoticons 35
:: ೖ(⑅σ̑ᴗσ̑)ೖ ::⠀Standard Smily Mouth Emoticons 36
三⊂( っ⌒◡|⠀Standard Smily Mouth Emoticons 37
(ؑᵒᵕؑ̇ᵒ)◞✧⠀Standard Smily Mouth Emoticons 38
꒰•́ॢ৺•̀ॢ๑͒꒱⠀Standard Smily Mouth Emoticons 39
(｡≍ฺ‿ฺ≍ฺ)⠀Standard Smily Mouth Emoticons 40
(⚈᷁‿᷇⚈᷁)⠀Standard Smily Mouth Emoticons 41
(๑◕ฺ‿ฺ◕ฺ๑)⠀Standard Smily Mouth Emoticons 42
⁽(◍˃̵͈̑ᴗ˂̵͈̑)⠀Standard Smily Mouth Emoticons 43
(人 •͈ᴗ•͈)⠀Standard Smily Mouth Emoticons 44
(*˙︶˙*)☆*°⠀Standard Smily Mouth Emoticons 45
(୨୧ ❛ᴗ❛)✧⠀Standard Smily Mouth Emoticons 46
( ¨̮ )⠀Standard Smily Mouth Emoticons 47
(＊◕ᴗ◕＊)⠀Standard Smily Mouth Emoticons 48
(*´╰╯`๓)♬⠀Standard Smily Mouth Emoticons 49
(∗❛ัᴗ❛ั∗)⠀Standard Smily Mouth Emoticons 50
⊂(◉‿◉)つ⠀Standard Smily Mouth Emoticons 51
(人 •͈ᴗ•͈✿ฺ)⠀Standard Smily Mouth Emoticons 52
( ･ᴗ･̥̥̥ )⠀Standard Smily Mouth Emoticons 53
(≖ ‿ ≖)⠀Standard Smily Mouth Emoticons 54
(๑˃͈꒵˂͈๑)⠀Standard Smily Mouth Emoticons 55
(⑅‾̥̥̥̥̥̑⌣‾̥̥̥̥̥̑⑅)⠀Standard Smily Mouth Emoticons 56
(<><<̯-̮<<<<̯)⠀Standard Smily Mouth Emoticons 57
(⁎⚈᷀᷁ᴗ⚈᷀᷁⁎)⠀Standard Smily Mouth Emoticons 58
(⁰ੌ⌣⁰ੌ๑)⠀Standard Smily Mouth Emoticons 59
(⚈᷀᷁ᴗ⚈᷀᷁⁎)⠀Standard Smily Mouth Emoticons 60
✌(-‿-)✌⠀Standard Smily Mouth Emoticons 61
(⋓ื◡⋓ื)⠀Standard Smily Mouth Emoticons 62
（。≖ิ‿≖ิ）⠀Standard Smily Mouth Emoticons 63
(๑￫‿ฺ￩๑)⠀Standard Smily Mouth Emoticons 64
ˆ̭̭͙(๑ ົ̅ ͔৹͜ ົ̅๑)⠀Standard Smily Mouth Emoticons 65
(∗ᵕ̴᷄◡ᵕ̴᷅∗)՞⠀Standard Smily Mouth Emoticons 66
( •॒◞ ͜◟•॒ )⠀Standard Smily Mouth Emoticons 67
(ㆁᴗㆁ✿)⠀Standard Smily Mouth Emoticons 68
(๑’◡͐’๑)⠀Standard Smily Mouth Emoticons 69
(⌒⃝৺⌒⃝)⠀Standard Smily Mouth Emoticons 70
{´◕ ◡ ◕｀}⠀Standard Smily Mouth Emoticons 71
(ට ̥̆ ට)⠀Standard Smily Mouth Emoticons 72
⁽͑˙˚̀ᵕ˚́˙⁾̉⠀Standard Smily Mouth Emoticons 73
(*☌ᴗ☌)｡*ﾟ⠀Standard Smily Mouth Emoticons 74
( ´◡‿ゝ◡`)⠀Standard Smily Mouth Emoticons 75
(　◠ ◡ ◠　)⠀Standard Smily Mouth Emoticons 76
ల(*´= ◡ =｀*)⠀Standard Smily Mouth Emoticons 77
₊⚛⁺(ؔ꒨◡ؔ꒨)ᵌ⠀Standard Smily Mouth Emoticons 78
( ்ͧˏ౦͜ˎ ்ͧ)⠀Standard Smily Mouth Emoticons 79
꒰⁎❛⃘ੌ ᵕ ❛⃘ੌ⁎꒱⠀Standard Smily Mouth Emoticons 80
( ́⋅⃘ˬ̇⋅⃘ ̀ˋ)⠀Standard Smily Mouth Emoticons 81
(. ົ̅ ੭͜ ົ̅.)⠀Standard Smily Mouth Emoticons 82
( ᵘ ᵕ ᵘ ⁎)⠀Standard Smily Mouth Emoticons 83
( ᵘ ᵕ ᵘ ⁎)⠀Standard Smily Mouth Emoticons 84
(๑`･ᴗ･´๑)⠀Standard Smily Mouth Emoticons 85
❀.(*´◡`*)❀.⠀Standard Smily Mouth Emoticons 86
◟(๑•͈ᴗ•͈)◞⠀Standard Smily Mouth Emoticons 87
₍ఠ ͜ఠ₎⠀Standard Smily Mouth Emoticons 88
(•‾̑⌣‾̑•)⠀Standard Smily Mouth Emoticons 89
(∗ᒩ͜∗)⠀Standard Smily Mouth Emoticons 90
( ்ૂ౧͜ ்)⠀Standard Smily Mouth Emoticons 91
(⋈･◡･)✰⠀Standard Smily Mouth Emoticons 92
(⁝̥ꑦᴗꑦ)⠀Standard Smily Mouth Emoticons 93
(︶.̮︶✽)⠀Standard Smily Mouth Emoticons 94
(❍❛‿❛❍❋)⠀Standard Smily Mouth Emoticons 95
₍•͈ᴗ•͈₎⠀Standard Smily Mouth Emoticons 96
(ͼ ̥̆ ͽ)⠀Standard Smily Mouth Emoticons 97
(≖ᴗ≖๑)⠀Standard Smily Mouth Emoticons 98
( °̥̥̥̥̥̥̥̥◡͐°̥̥̥̥̥̥̥̥)⠀Standard Smily Mouth Emoticons 99
( ´͈ ◡ `͈ )⠀Standard Smily Mouth Emoticons 100
( ๑॔•◡ુ•๑॓)⠀Standard Smily Mouth Emoticons 101
(๑･`◡´･๑)⠀Standard Smily Mouth Emoticons 102
,､’`(((<ŏᴗŏ))),､’`’`,､⠀Standard Smily Mouth Emoticons 103
ෆ⃛(ට◡ට⁎)ფ⠀Standard Smily Mouth Emoticons 104
੬ჴ❛‿❛ჴჱ̒̒⠀Standard Smily Mouth Emoticons 105
৵( °͜ °৵)⠀Standard Smily Mouth Emoticons 106
(✿◕ ‿◕ฺ)ノ))。₀: *゜⠀Standard Smily Mouth Emoticons 107
☆(❁‿❁)☆⠀Standard Smily Mouth Emoticons 108
◃┆◉◡◉┆▷⠀Standard Smily Mouth Emoticons 109
q(❂‿❂)p⠀Standard Smily Mouth Emoticons 110
☆(◒‿◒)☆⠀Standard Smily Mouth Emoticons 111
⊂◉‿◉つ⠀Standard Smily Mouth Emoticons 112
(｡✿‿✿｡)⠀Standard Smily Mouth Emoticons 113
໒( ﹒ ͜ر ﹒ )७⠀Standard Smily Mouth Emoticons 114
( ‾̮‿͂‾̮ ꐦ)⠀Standard Smily Mouth Emoticons 115
(˘･ᴗ･˘)⠀Standard Smily Mouth Emoticons 116
(ό‿ὸ)ﾉ⠀Standard Smily Mouth Emoticons 117
ヾ|๑　╹　◡　╹　๑|ﾉ⠀Standard Smily Mouth Emoticons 118
(((<◔ᴗ◔<)))⠀Standard Smily Mouth Emoticons 119
໒( ” ¤ ‿ ¤ ” )७⠀Standard Smily Mouth Emoticons 120
✩*॰ ( ¨̮ ) ॰*✩⠀Standard Smily Mouth Emoticons 121
(✧≖‿ゝ≖)⠀Standard Smily Mouth Emoticons 122
☝( ◠‿◠ )☝⠀Standard Smily Mouth Emoticons 123
(*´◡｀​*)⠀Standard Smily Mouth Emoticons 124
(๑◔‿◔๑)⠀Standard Smily Mouth Emoticons 125
(◕‿‿◕｡)⠀Standard Smily Mouth Emoticons 126
(✿╹◡╹)⠀Standard Smily Mouth Emoticons 127
(◕ฺ ◡ฺ ◕ฺ)⠀Standard Smily Mouth Emoticons 128
(✿ฺ◡ฺ‿ฺ◡ฺ)⠀Standard Smily Mouth Emoticons 129
（◞‿◟）⠀Standard Smily Mouth Emoticons 130
(o˘◡˘o)⠀Standard Smily Mouth Emoticons 131
ꉂꉂ ( ˆᴗˆ )⠀Standard Smily Mouth Emoticons 132
₊·(ϱ॔⌄ᵕ๑॓)‧*⠀Standard Smily Mouth Emoticons 133
-(๑☆‿ ☆#)ᕗ⠀Standard Smily Mouth Emoticons 134
╭ (oㅇ‿ o#)ᕗ⠀Standard Smily Mouth Emoticons 135
／人◕ ‿‿ ◕人＼⠀Standard Smily Mouth Emoticons 136
(o◞ิ‿◟ิo)⠀Standard Smily Mouth Emoticons 137
(•_ ͜_•)⠀Standard Smily Mouth Emoticons 138
(´<><<‸⚲͜<<<<)⠀Standard Smily Mouth Emoticons 139
(๑❝᷀ົཽ ⁐̵ ❝᷀ົཽ)✧⠀Standard Smily Mouth Emoticons 140
(• ̥̆ •)⠀Standard Smily Mouth Emoticons 141
(o^^)o⠀Tiny or no Mouths 1
ヾ(^ ^ゞ⠀Tiny or no Mouths 2
o(^^o)⠀Tiny or no Mouths 3
(o^^o)♪⠀Tiny or no Mouths 4
(o⌒．⌒o)⠀Tiny or no Mouths 5
(=^･^=)⠀Tiny or no Mouths 6
。(⌒.⌒。)⠀Tiny or no Mouths 7
( ﾉ^.^)ﾉﾟ⠀Tiny or no Mouths 8
(“⌒.⌒”)⠀Tiny or no Mouths 9
(≧.≦*)⠀Tiny or no Mouths 10
(*^^*)⠀Tiny or no Mouths 11
(ꐦ ´͈ ᗨ `͈ )⠀Big Wide Open Mouths 1
( ´͈ ॢꇴ  `͈)੭ु⠀Big Wide Open Mouths 2
（ꉺᗜꉺ）⠀Big Wide Open Mouths 3
(･ัᗜ･ั)و⠀Big Wide Open Mouths 4
✌✌(➲ ᗜ ➲)✌✌⠀Big Wide Open Mouths 5
✌✌(˵¯̴͒ꇴ¯̴͒˵)✌✌⠀Big Wide Open Mouths 6
( ˙̣̣̣ↂ⃙⃙⃚᷄ᗨↂ⃙⃙⃚ )ꋧ⠀Big Wide Open Mouths 7
(ᗒᗨᗕ)⠀Big Wide Open Mouths 8
(๑’ᗢ’๑)ฅ⠀Big Wide Open Mouths 9
(✤❛⃘ͫ Ʉ̮ ❛⃘ͫ)⠀Big Wide Open Mouths 10
┌༼ ˵ ° ᗜ ° ˵ ༽┐⠀Big Wide Open Mouths 11
ˉ̶̡̭̭ ( ´͈ ᗨ `͈ ) ˉ̶̡̭̭⠀Big Wide Open Mouths 12
(□ᗜ□)⠀Big Wide Open Mouths 13
(:D)┼─┤⠀Big Wide Open Mouths 14
ヽ〳 ՞ ᗜ ՞ 〵ง⠀Big Wide Open Mouths 15
(-^〇^-)⠀Miscellaneous Mouths 1
(.=^・ェ・^=)⠀Miscellaneous Mouths 2
(・◇・)⠀Miscellaneous Mouths 3
(*＾ワ＾*)⠀Miscellaneous Mouths 4
(*¬*)⠀Miscellaneous Mouths 5
(´ヮ`)⠀Miscellaneous Mouths 6
(^(I)^)⠀Miscellaneous Mouths 7
(^(エ)^)⠀Miscellaneous Mouths 8
（＾⊆＾）⠀Miscellaneous Mouths 9
(๑^っ^๑)⠀Miscellaneous Mouths 10
（＞ｙ＜）⠀Miscellaneous Mouths 11
(⊙ヮ⊙)⠀Miscellaneous Mouths 12
(☆^O^☆)⠀Miscellaneous Mouths 13
°˖ ✧◝(○ ヮ ○)◜✧˖ °⠀Miscellaneous Mouths 14
⊂(^(工)^)⊃⠀Miscellaneous Mouths 15
ヾ（*⌒ヮ⌒*）ゞ⠀Miscellaneous Mouths 16
(ⓥꇳⓥ*)⠀Miscellaneous Mouths 17
((ꉺꈊꉺ)ꀢ༣⠀Miscellaneous Mouths 18
(๑❛ꆚ❛๑)⠀Miscellaneous Mouths 19
(ᵒ̴̶̷̤́◞౪◟ ᵒ̴̶̷̤̀ )⠀Miscellaneous Mouths 20
(^ワ^＝)⠀Miscellaneous Mouths 21
(*´ч ` *)⠀Miscellaneous Mouths 22
（｡◑ヮ◑｡）⠀Miscellaneous Mouths 23
（ꉺ౪ꉺ）⠀Miscellaneous Mouths 24
( ◑ٹ◐)⠀Miscellaneous Mouths 25
(´ёٹё)⠀Miscellaneous Mouths 26
(*^ิ益^ิ*)⠀Miscellaneous Mouths 27
(´◉◞౪◟◉)⠀Miscellaneous Mouths 28
(*^｡^*)⠀Miscellaneous Mouths 29
(๑*౪*๑)⠀Miscellaneous Mouths 30
（＾凹＾）⠀Miscellaneous Mouths 31
,､’`<<<<(❛ヮ❛✿)<><<,､’`’`,､⠀Miscellaneous Mouths 32
ೖ(σ̑˽σ̑)ೖ⠀Miscellaneous Mouths 33
(●⌃ٹ⌃)⠀Miscellaneous Mouths 34
(*꒩̐﹀꒩̐*)⠀Miscellaneous Mouths 35
(^◇^；)⠀Miscellaneous Mouths 36
(✿ ◜◒◝ )⠀Miscellaneous Mouths 37
(´◉◞౪◟◉｀)⠀Miscellaneous Mouths 38
(థฺˇ౪ˇథ)⠀Miscellaneous Mouths 39
(⁎ؔꇵ ˒̠̮ ؔꇵ)⠀Miscellaneous Mouths 40
( •˓◞•̀ )⠀Miscellaneous Mouths 41
(*ꄱͦ︺ꄱͦ*)⠀Miscellaneous Mouths 42
( ՞ٹ՞)⠀Miscellaneous Mouths 43
( ´•౪•`)⠀Miscellaneous Mouths 44
(*´∪`)⠀Miscellaneous Mouths 45
(◍ȋ ₎໐͜₍ ȋ◍)⠀Miscellaneous Mouths 46
♪~♪ d(⌒o⌒)b♪~♪⠀Miscellaneous Mouths 47
♪♪ｖ(⌒ｏ⌒)ｖ♪♪⠀Miscellaneous Mouths 48
∩`･◇･)⠀Miscellaneous Mouths 49
థ౪థ⠀Miscellaneous Mouths 50
₍‧ꀈ˙⁾՜⠀Miscellaneous Mouths 51
( θོثθོ )⠀Miscellaneous Mouths 52
ʿʿ˅⁽ˆ⁰ˆ˺ ⁾˺⠀Miscellaneous Mouths 53
(★^O^★)⠀High Energy Happiness 1
(((o(*ﾟ▽ﾟ*)o)))⠀High Energy Happiness 2
＼（＠￣∇￣＠）／⠀High Energy Happiness 3
ヽ(；▽；)ノ⠀High Energy Happiness 4
ヾ(@^▽^@)ノ⠀High Energy Happiness 5
o((*^▽^*))o⠀High Energy Happiness 6
Ｏ(≧▽≦)Ｏ⠀High Energy Happiness 7
– =͟͟͞͞ ( ꒪౪꒪)ฅ✧⠀High Energy Happiness 8
“ヽ(´▽｀)ノ”⠀High Energy Happiness 9
(((＼（＠v＠）／)))⠀High Energy Happiness 10
(ﾉ´ヮ´)ﾉ*:･ﾟ✧⠀High Energy Happiness 11
(ノ^_^)ノ⠀High Energy Happiness 12
(ノ＞▽＜。)ノ⠀High Energy Happiness 13
(ﾉﾟ▽ﾟ)ﾉ⠀High Energy Happiness 14
〈( ^.^)ノ⠀High Energy Happiness 15
＼(*T▽T*)／⠀High Energy Happiness 16
＼（＾▽＾）／⠀High Energy Happiness 17
＼(^ω^＼)⠀High Energy Happiness 18
＼（Ｔ∇Ｔ）／⠀High Energy Happiness 19
☆*:.｡. o(≧▽≦)o .｡.:*☆⠀High Energy Happiness 20
ヽ(<^o^ヽ)⠀High Energy Happiness 21
ヽ(；▽；)ノ⠀High Energy Happiness 22
ヽ(‘ ∇‘ )ノ⠀High Energy Happiness 23
ヾ(＠† ▽ †＠）ノ⠀High Energy Happiness 24
ヾ(＠^∇^＠)ノ⠀High Energy Happiness 25
ヾ(＠^▽^＠)ﾉ⠀High Energy Happiness 26
ヾ（＠＾▽＾＠）ノ⠀High Energy Happiness 27
ヾ(@゜∇゜@)ノ⠀High Energy Happiness 28
ヾ(＠゜▽゜＠）ノ⠀High Energy Happiness 29
ヾ(@°▽°@)ノ⠀High Energy Happiness 30
ヾ(＠⌒ー⌒＠)ノ⠀High Energy Happiness 31
ヽ(*≧ω≦)ﾉ⠀High Energy Happiness 32
ヽ(*・ω・)ﾉ⠀High Energy Happiness 33
ヽ(*⌒∇⌒*)ﾉ⠀High Energy Happiness 34
ヾ(＾-＾)ノ⠀High Energy Happiness 35
ヽ(^。^)丿⠀High Energy Happiness 36
ヽ(＾Д＾)ﾉ⠀High Energy Happiness 37
ヽ(=^･ω･^=)丿⠀High Energy Happiness 38
٩(^ᴗ^)۶⠀High Energy Happiness 39
о(ж＞▽＜)ｙ ☆⠀High Energy Happiness 40
ヘ(^_^ヘ)⠀High Energy Happiness 41
ヘ(^o^ヘ)⠀High Energy Happiness 42
へ(゜∇、°)へ⠀High Energy Happiness 43
＼＼\ ٩(`(エ)´ )و //／／⠀High Energy Happiness 44
(／・ω・)／⠀High Energy Happiness 45
୧(﹒︠ᴗ﹒︡)୨⠀High Energy Happiness 46
(☝ ՞ਊ ՞)☝⠀High Energy Happiness 47
⸂⸂⸜(രᴗര๑)⸝⸃⸃⠀High Energy Happiness 48
˛˛ƪ(⌾⃝ ౪ ⌾⃝ ๑)و ̉ ̉⠀High Energy Happiness 49
ヾ(๑╹ヮ╹๑)ﾉ”⠀High Energy Happiness 50
ヾ(๑╹ꇴ◠๑)ﾉ”⠀High Energy Happiness 51
ヾ(๑ㆁᗜㆁ๑)ﾉ”⠀High Energy Happiness 52
⁽⁽◞(꒪ͦᴗ̵̍꒪ͦ=͟͟͞͞ ꒪ͦᴗ̵̍꒪ͦ)◟⁾⁾⠀High Energy Happiness 53
ヾ(Ő∀Ő๑)ﾉ⠀High Energy Happiness 54
(੭ु｡╹▿╹｡)੭ु⁾⁾⠀High Energy Happiness 55
₍₍ (ง Ŏ౪Ŏ)ว ⁾⁾⠀High Energy Happiness 56
(ง •ૅ౪•᷄)ว⠀High Energy Happiness 57
₍₍⁽⁽(ી(^‿ゝ^)ʃ)₎₎⁾⁾⠀High Energy Happiness 58
(´ ↂ⃙⃙⃚ꇴↂ⃙⃙⃚ `≡´ ↂ⃙⃙⃚ꇴↂ⃙⃙⃚ `)⠀High Energy Happiness 59
(ﾉ^_^)ﾉ⠀High Energy Happiness 60
◦°˚\(*❛‿❛)/˚°◦⠀High Energy Happiness 61
⌒°(ᴖ◡ᴖ)°⌒⠀High Energy Happiness 62
⌒(o＾▽＾o)ノﾟ⠀High Energy Happiness 63
｡:.ﾟヽ(´∀`｡)ﾉﾟ.:｡+ﾟ⠀High Energy Happiness 64
ﾟ+｡:.ﾟヽ(*´∀`)ﾉﾟ.:｡+ﾟ⠀High Energy Happiness 65
ヾ(○･ω･)ﾉ☆⠀High Energy Happiness 66
୧( “̮ )୨✧⠀High Energy Happiness 67
✌(๑˃̶͈̀◡˂̶͈́๑)✌⠀High Energy Happiness 68
✩◝(◍⌣̎◍)◜✩⠀High Energy Happiness 69
∕∕∕ ∕ ∕∕˛₍˴◅ˋ)੭✧∕∕∕ ∕∕⠀High Energy Happiness 70
(◜▿‾ ≡‾▿◝)⠀High Energy Happiness 71
୧[ ˵ ͡ᵔ ͜ʟ ͡ᵔ ˵ ]୨⠀High Energy Happiness 72
ヾ( ~▽~)ﾂ⠀High Energy Happiness 73
(ﾉ*´▽)ﾉ⠀High Energy Happiness 74
ヽ(^◇^*)/⠀High Energy Happiness 75
ヾ（ ❀◕◡◕ฺฺ ）ノ⠀High Energy Happiness 76
ヽ（◕◡◕❀ฺ ）ノ⠀High Energy Happiness 77
ヾ(^▽^ヾ)⠀High Energy Happiness 78
୧〳 ＾ ౪ ＾ 〵୨⠀High Energy Happiness 79
=͟͟͞͞٩(๑☉ᴗ☉)੭ु⁾⁾⠀High Energy Happiness 80
ლ(⌒▽⌒ლ)⠀Grabby Hands 1
(ღ˘⌣˘ღ)⠀Grabby Hands 2
(ღ˘⌣˘ღ) ♫･*:.｡. .｡.:*･⠀Grabby Hands 3
(ॢ˘⌣˘ ॢ⑅)⠀Grabby Hands 4
꒰ღ˘‿˘ற꒱❤⃛⠀Grabby Hands 5
ლ(́◉◞౪◟◉‵ლ)⠀Grabby Hands 6
ლ(๏‿๏ ◝ლ)⠀Grabby Hands 7
(•ૢꆤ ˙̫̮ ꆤ•ૢ)⠀Grabby Hands 8
(๑ᵕॢ૩ᵕॢ)*౨˚ൗ⠀Grabby Hands 9
*.⋆( ˘̴͈́ ॢ꒵ॢ ˘̴͈̀ )⋆.*⠀Grabby Hands 10
῍̻̩✧(´͈ ૢᐜ `͈ૢ)˖῍̻̩⠀Grabby Hands 11
( ᵕ́ૢ‧̮ᵕ̀ૢ)‧̊·*⠀Grabby Hands 12
⁎⁙꒰⋓(༶∙ .̌ ∙༶ૢ)⋓꒱⁕⁛⠀Grabby Hands 13
꒰⌗´͈ ᵕ ॣ`͈⌗꒱৩⠀Grabby Hands 14
(•́ ॣ·̫ ॣ•̀,)՞⠀Grabby Hands 15
(*๓´╰╯`๓)⠀Grabby Hands 16
(ू• ౪•ू )⠀Grabby Hands 17
ლ(╹◡╹ლ)⠀Grabby Hands 18
ლ(o◡oლ)⠀Grabby Hands 19
(ღ′◡‵)⠀Grabby Hands 20
(*ฅ́˘ฅ̀*)⠀Grabby Hands 21
(⋆ॢʾ ˙̫̮ ʿ⋆ॢ)⠀Grabby Hands 22
*(Ü*ૢ)*⠀Grabby Hands 23
✿(′ॢᵕ‵*ॢ)⠀Grabby Hands 24
˓˓(๑ॢ₎ӧ ͜ ӧ₍๑ॢ)˒˒⠀Grabby Hands 25
(❝᷀ੌ ˙̮ ❝᷀ੌॢ●)✧⠀Grabby Hands 26
ღවꇳවღ⠀Grabby Hands 27
(•ૢ⚈͒⌄⚈͒•ૢ)⠀Grabby Hands 28
·◌̊ˈ*(⁰̶̶̷ ˙̮ ⁰̴̷̷๑ॢ॓).°◌̊⠀Grabby Hands 29
✧.*ධ̎ૢ ˒̫̮ ධ̎ૢ*·✧⠀Grabby Hands 30
ಞ(ల˙◡˙ల)ಞ⠀Grabby Hands 31
(ٛ⁎꒪̕ॢ ˙̫ ꒪ٛ̕ॢ⁎)⠀Grabby Hands 32
(◖̑◡ॢ◖̑⋆)⁎❀∗⠀Grabby Hands 33
( ღ’ᴗ’ღ )⠀Grabby Hands 34
(⋆ૢʾ ˙̫̮ ʿ⋆ૢ)⠀Grabby Hands 35
✧.*(⁎❝͋॔ ˙̫ॢ ॢ❝͋॓⁎)*·✧⠀Grabby Hands 36
(ლ◖◡◗ ლ)⠀Grabby Hands 37
ლↂ‿‿ↂლ⠀Grabby Hands 38
୨୧ •ॢ◡-ॢ⑅•ॢ◡-ॢ*｡.⠀Grabby Hands 39
(๑ॢ❛ꆚ❛๑ॢ)⠀Grabby Hands 40
ლ(- ◡ -ლ)⠀Grabby Hands 41
( ꒵͒◡ु꒵ ॣ)⠀Grabby Hands 42
( •ॢᴗ•ॢ⋈)⠀Grabby Hands 43
( •ॢ◡-ॢ)⠀Grabby Hands 44
ლ(❛◡❛✿)ლ⠀Grabby Hands 45
ლ(･ิω･ิლ)⠀Grabby Hands 46
ლ(＾ω＾ლ)⠀Grabby Hands 47
ლ(・∀・ )ლ⠀Grabby Hands 48
ლ（´∀`ლ）⠀Grabby Hands 49
(*ुම̤ᴗම̤*ू)꒭꒱꒹꒟✩⃛⠀Grabby Hands 50
(´⌣`ʃƪ)⠀Prayer Hands 1
(´▽`ʃƪ)⠀Prayer Hands 2
(º̩̩́⌣º̩̩̀ʃƪ)⠀Prayer Hands 3
(ʃƪ・∀・)⠀Prayer Hands 4
(＾ω＾ʃƪ)⠀Prayer Hands 5
(ʃƪ˘･ᴗ･˘)⠀Prayer Hands 6
(ʃƪ˘⌣˘)⠀Prayer Hands 7
(ʃƪ¬‿¬)⠀Prayer Hands 8
(＾▽＾ʃƪ)⠀Prayer Hands 9
(∩❛ڡ❛∩)⠀Tongues 1
(っ˘ڡ˘ς)⠀Tongues 2
(⁎⁍̴ڡ⁍̴⁎)⠀Tongues 3
(≧ڡ≦*)⠀Tongues 4
(*＾ڡ＾*)⠀Tongues 5
(∩ڡ∩)⠀Tongues 6
（〜^ڡ^)〜⠀Tongues 7
o((*^ڡ^*))o⠀Tongues 8
(・ڡ・)⠀Tongues 9
(　＾ڡ＾)⠀Tongues 10
(*⌒ڡ⌒*)⠀Tongues 11
∩(︶ڡ︶)∩⠀Tongues 12
〜(^∇^〜）⠀Happiness Dance 1
〜(￣▽￣〜)⠀Happiness Dance 2
。(⌒∇⌒。)⠀Happiness Dance 3
（〜^∇^)〜⠀Happiness Dance 4
(〜￣▽￣)〜⠀Happiness Dance 5
(。⌒∇⌒)。⠀Happiness Dance 6
((┌|o^▽^o|┘))♪⠀Happiness Dance 7
(~‾⌣‾)~⠀Happiness Dance 8
(~￣▽￣)~⠀Happiness Dance 9
(~˘▾˘)~⠀Happiness Dance 10
~(⁰▿⁰)~⠀Happiness Dance 11
~(‾⌣‾~)⠀Happiness Dance 12
~(˘▾˘)~⠀Happiness Dance 13
~(˘▾˘~)⠀Happiness Dance 14
┌(˘⌣˘)ʃ⠀Happiness Dance 15
ƪ(˘⌣˘)ʃ⠀Happiness Dance 16
ƪ(˘⌣˘)┐⠀Happiness Dance 17
♪((└|o^▽^o|┐))⠀Happiness Dance 18
｡^‿^｡⠀No Cheeks 1
｡◕‿◕｡⠀No Cheeks 2
´･ᴗ･`⠀No Cheeks 3
^ ͜• ^⠀No Cheeks 4
~ヾ ＾∇＾⠀No Cheeks 5
≖‿≖⠀No Cheeks 6
⊙▽⊙⠀No Cheeks 7
⊙ω⊙⠀No Cheeks 8
▽・ω・▽⠀No Cheeks 9
✖‿✖⠀No Cheeks 10
❣◕ ‿ ◕❣⠀No Cheeks 11
ʘ‿ʘ⠀No Cheeks 12
ಥ‿ಥ⠀No Cheeks 13
꒪̆౪̮꒪̆⠀No Cheeks 14
*✧₊✪͡◡ू✪͡⠀No Cheeks 15
ȏ.̮ȏ⠀No Cheeks 16
✾꒡ .̮ ꒡✾⠀No Cheeks 17
∩˙▿˙∩⠀No Cheeks 18
´͈ ᵕ `͈⠀No Cheeks 19
⚈້͈͡ ·̼̮ ⚈້͈͡⠀No Cheeks 20
´͈ ᵕ `͈ ♡°◌̊⠀No Cheeks 21
ヽﾐ ´∀｀ﾐノ⠀No Cheeks 22
◉‿◉⠀No Cheeks 23
˙ ͜ʟ˙⠀No Cheeks 24
ෆ╹ .̮ ╹ෆ⠀No Cheeks 25
⍣ঠৈ ◡ુ͐ ঠৈ⍣⠀No Cheeks 26
ҽ̑ӏ͜ ҽ̑⠀No Cheeks 27
☁മ◡മ☁⠀No Cheeks 28
꒡ꆚ꒡⠀No Cheeks 29
أ‿أ⠀No Cheeks 30
ರ ౪̮ ರ⠀No Cheeks 31
乂⍲‿⍲乂⠀No Cheeks 32
˙ᘧ ͜ ˙⠀No Cheeks 33
❝᷀ົ৺❝᷀ົ⠀No Cheeks 34
ɷ◡ɷ⠀No Cheeks 35
⋆•̵̑◡͐•̵̑⋆⠀No Cheeks 36
⋆′◡ु͐‵⋆⠀No Cheeks 37
⁙ὸ‿ό⁙⠀No Cheeks 38
ᴑ͝ᴗᴑ͝⠀No Cheeks 39
〤◕‿◕〤⠀No Cheeks 40
⋆ᘟ◡ुᘟ⋆⠀No Cheeks 41
⚆ꆚ⚆⠀No Cheeks 42
◙‿◙⠀No Cheeks 43
Ü⠀No Cheeks 44
❀◕ ‿ ◕❀⠀No Cheeks 45
<<<<【☯】‿【☯】<><<⠀No Cheeks 46
◉⃝ ˙̫̮ ◉⃝⠀No Cheeks 47
⁞ ᵕ ‿ ᵕ ⁞⠀No Cheeks 48
米＾－＾米⠀No Cheeks 49
റ്ധ ੭͜ റ്ധ⠀No Cheeks 50
⑅❛ั◡❛ั⑅⠀No Cheeks 51
(/•ิ_•ิ)/⠀Complex Emoticons 1
(•ิ_•ิ)⠀Complex Emoticons 2
(ી(΄◞ิ౪◟ิ‵)ʃ)♥⠀Complex Emoticons 3
(⁎⚈᷀᷁ᴗ⚈᷀᷁⁎)⠀Complex Emoticons 4
♝ཻ༨͜♝ཻ)✩⃛⠀Complex Emoticons 5
(•ؔʶ̷ ˡ̲̮ ؔʶ̷)✧⠀Complex Emoticons 6
*⃝̣◌◦°ᴑ̴̶̷̤◡ुᴑ̴̶̷̤ˋॢ°◦*⃝̣⠀Complex Emoticons 7
(ؔ♝ཻ༨͜♝ཻ)✩⃛⠀Complex Emoticons 8
⋆.*⃝̥◌ॱ꒰*ॢ˘̴͈́꒵˘̴͈̀*ॢ꒱ॱ◌̥*⃝̣ ⋆⠀Complex Emoticons 9
(´^ิ益^ิ｀ )⠀Complex Emoticons 10
˚ஐ₊✧(ؔ❝͋ ⍢ ؔ❝͋ೢ⁎)⁺˳ஐ༚⠀Complex Emoticons 11
(≖ิ(‿)≖ิ)⠀Complex Emoticons 12
˚ஐ₊✧(❝᷀ੌ ˙̮ ❝᷀ੌॢ●)⁺˳ஐ༚⠀Complex Emoticons 13
(◕ฺ‿◕ฺ✿ฺ)⠀Complex Emoticons 14
꒰๑˃͈꒵˂͈๑꒱୭̥*ﾞ̥♡⃛ Ɛn꒻öႸ⠀Happy Emotions with Words 1
ॱ॰⋆(˶ॢ‾᷄﹃‾᷅˵ॢ)ӵᵘᵐᵐᵞ♡♡♡⠀Happy Emotions with Words 2
(ˀ̢⋅⃘‧̮⋅⃘ˁ̡ી˂ᵒ͜͡ᵏᵎ⁾⠀Happy Emotions with Words 3
( ´͈ ॢꇴ  `͈)੭ु⁾⁾·°˖ᔆᵘᵗᵉᵏⁱ✧˖°⠀Happy Emotions with Words 4
Ⓗⓐⓟⓟⓨ❤ヾ(◍’౪`◍)ﾉﾞ⠀Happy Emotions with Words 5
(^▽^)/ ʸᵉᔆᵎ⠀Happy Emotions with Words 6
✧*.◟(ˊᗨˋ)◞.*✧ᗯ੨~ɪ̊♪ْ˖⋆⠀Happy Emotions with Words 7
(•ᵕᴗᵕ•)⁾⁾ᵖᵉᵏᵒ⠀Happy Emotions with Words 8
ପ(๑•̀ुᴗ•̀ु)* ॣ৳৸ᵃᵑᵏ Ꮍ৹੫ᵎ *ॣ⠀Happy Emotions with Words 9
｟❛◡❛ॣॣ｠*.･｡╟╢ᎯƤƤᎽ*.･｡⠀Happy Emotions with Words 10
▒▒▓█▇▅▂∩( ✧Д✧)∩▂▅▇█▓▒▒⠀Giant Emoticons 1
☆⌒Y⌒Y⌒Y⌒Y⌒ヾ(●´Ｕ｀●)ﾉ⠀Giant Emoticons 2
☆*･゜ﾟ･*(^O^)/*･゜ﾟ･*☆⠀Giant Emoticons 3
☆*✲ﾟ*｡(((´♡‿♡`+)))｡*ﾟ✲*☆⠀Giant Emoticons 4
✿♬ﾟ+.(｡◡‿◡)♪.+ﾟ♬✿。⠀Giant Emoticons 5
“:♡.•♬✧⁽⁽ଘ( ˊᵕˋ )ଓ⁾⁾*+:•*∴⠀Giant Emoticons 6
☆ﾟ･*:｡.:(ﾟ∀ﾟ)ﾟ･*:..:☆⠀Giant Emoticons 7
( ❀⃙⃕⃠⃝⃘⃚౪❀⃙⃕⃠⃝⃘⃚ )⠀Giant Emoticons 8
o͡͡͡͡͡͡͡͡͡͡͡͡͡͡╮(｡❛ᴗ❛｡)╭o͡͡͡͡͡͡͡͡͡͡͡͡͡͡⠀Giant Emoticons 9
|_・)⠀Hiding Behind a | 1
|･ω･｀)⠀Hiding Behind a | 2
｜−・<）⠀Hiding Behind a | 3
|ω・）⠀Hiding Behind a | 4
|ω･)و ̑̑༉⠀Hiding Behind a | 5
|д꒪ͧ)…⠀Hiding Behind a | 6
ﾍ(･_|⠀Hiding Behind a | 7
|₋ॢọ̶̶̷̥᷅๑)‧˚⁺⠀Hiding Behind a | 8
| ू*꒦ິ꒳꒦ີ)｡oO⠀Hiding Behind a | 9
( ͒•·̫|⠀Hiding Behind a | 10
| ू•ૅω•́)ᵎᵎᵎ⠀Hiding Behind a | 11
|ω`)⠀Hiding Behind a | 12
|ω･`)⠀Hiding Behind a | 13
| ू･᷄ω･᷅)｡oOஇo｡⠀Hiding Behind a | 14
|ʘ‿ʘ)╯⠀Hiding Behind a | 15
|ｮдﾟ)⠀Hiding Behind a | 16
｜ｏ゜）⠀Hiding Behind a | 17
|´ε ｀ゞ)*.。oO( )⠀Hiding Behind a | 18
|_-｡)⠀Hiding Behind a | 19
| 冫､)ｼﾞｰ⠀Hiding Behind a | 20
|Д´)/⠀Hiding Behind a | 21
|ｮз☆)⠀Hiding Behind a | 22
|ω´･<)⠀Hiding Behind a | 23
|๑˃ ॢ‧̫˂ॢ๑ ).*˚‧♡⠀Hiding Behind a | 24
|Д｀|┛⠀Hiding Behind a | 25
|･ω･`*)ッ⠀Hiding Behind a | 26
| ू´ᆺ`●)⠀Hiding Behind a | 27
|˄·͈༝·͈˄₎.｡oO⠀Hiding Behind a | 28
|ｴ)･)⊃⠀Hiding Behind a | 29
|*▼皿▼)⠀Hiding Behind a | 30
|ﾉｪ･)ﾉ (((●~*⠀Hiding Behind a | 31
|ﾉ_-)ﾉ 　(((●~⠀Hiding Behind a | 32
｜。・）⠀Hiding Behind a | 33
|∀･)ジ⠀Hiding Behind a | 34
|д･)⠀Hiding Behind a | 35
|x･`)⠀Hiding Behind a | 36
|´▽｀●)ﾉ⠀Hiding Behind a | 37
|*´Д｀|ﾉ⠀Hiding Behind a | 38
|*´ｪ｀ﾉ|ﾉ⠀Hiding Behind a | 39
|ｮ０ω０*)ﾉﾞ⠀Hiding Behind a | 40
|ω・｀)ノ⠀Hiding Behind a | 41
|Д´)ﾉ⠀Hiding Behind a | 42
ヽ(*｀Д´*||⠀Hiding Behind a | 43
||*｀Д´*)ﾉ⠀Hiding Behind a | 44
|ω-o)ﾟ⠀Hiding Behind a | 45
|´∀｀●)⠀Hiding Behind a | 46
| 、ン、)ﾉ⠀Hiding Behind a | 47
|*´・Д・)r))ﾟ⠀Hiding Behind a | 48
|´Ｕ｀●)r”⠀Hiding Behind a | 49
|〃´⊇｀)-3⠀Hiding Behind a | 50
｜д・´)　!!⠀Hiding Behind a | 51
|｡･益･)ﾉ⠀Hiding Behind a | 52
|⁰⊖⁰)⠀Hiding Behind a | 53
|⁰⊖⁰) |⊖⁰) |)⠀Hiding Behind a | 54
|･x･`)⠀Hiding Behind a | 55
三⊂( っ⌒◡|⠀Hiding Behind a | 56
|￣(ｴ)￣) |(ｴ)￣) |￣) |⠀Hiding Behind a | 57
|･ｪ･)@ |ｪ･)@ |･)@ |⠀Hiding Behind a | 58
│ω・)ノ~☆♡。*♠⠀Hiding Behind a | 59
┬┴┬┴┤(･_├┬┴┬┴⠀Hiding Behind a Big Wall 1
┻┳|･ω･)⠀Hiding Behind a Big Wall 2
┻┳|･ω･)ﾉ⠀Hiding Behind a Big Wall 3
(ʘ ل͟├┬┴┬┴⠀Hiding Behind a Big Wall 4
(☯‿├┬┴┬┴⠀Hiding Behind a Big Wall 5
( ͡°╭ ͟ʖ╮͡├┬┴┬┴⠀Hiding Behind a Big Wall 6
ԅ[ •́ ﹏├┬┴┬┴⠀Hiding Behind a Big Wall 7
ᕦ༼ ºººل͟ºº├┬┴┬┴⠀Hiding Behind a Big Wall 8
┬┴┬┴┤( ͡° ͜ʖ├┬┴┬┴⠀Hiding Behind a Big Wall 9
༼ຈل͜├┬┴┬┴⠀Hiding Behind a Big Wall 10
(*σᴗσ)(ㅎᴗㅎ )　｜‸눈<)⠀Hiding From People 1
(〃￣▽￣〃)_・)⠀Hiding From People 2
川o･-･)ﾉ⠀Miscellaneous Hiding 1
)Д⊙`)⠀Miscellaneous Hiding 2
)ु੭ु⁾⠀Miscellaneous Hiding 3
‾̠̠̠̠̠̠̠̄| ॣ•͈̀๑)⠀Miscellaneous Hiding 4
|　|д･)⠀Miscellaneous Hiding 5
|](ｴ)￣)⠀Miscellaneous Hiding 6
[wa<<]-；)⠀Miscellaneous Hiding 7
░ฺ|◕ฺΘ◕ฺ)ノ⠀Miscellaneous Hiding 8
┃(・ω┃⠀Miscellaneous Hiding 9
(⊃‿⊂)⠀Miscellaneous Hiding 10
ᒄ₍⁽ˆ⁰ˆ⁾₎ᒃ♪♬⠀Christmas or Winter Holidays 1
⁝⁝⸃₍⁽΄˙̥΄ ⁾₎⸜☂⠀Christmas or Winter Holidays 2
˭̡̞(◞⁎˃ᆺ˂)◞₎₎=͟͟͞͞˳˚॰°ₒ৹๐⠀Christmas or Winter Holidays 3
ʕ”̮ुॽु✚⃞ྉ*✲ﾟ*｡⋆⠀Christmas or Winter Holidays 4
ʕ”̮ुॽु✚⃞ྉ⠀Christmas or Winter Holidays 5
ʕ•̫͡•ॽु✚⃞ྉ*✲ﾟ*｡⋆⠀Christmas or Winter Holidays 6
(◞ꈍ∇ꈍ)◞⋆**✚⃞ྉ⠀Christmas or Winter Holidays 7
(ㆆᴗㆆ)*✲ﾟ*｡⋆⠀Christmas or Winter Holidays 8
◝₍⁽⁺⁰꒳⁰⁾₎◜❤✧⠀Christmas or Winter Holidays 9
(╬ᇂ..ᇂ)o彡°⠀Christmas or Winter Holidays 10
℺ຶཽྈ”⠀Christmas or Winter Holidays 11
⋆ᗰદ૨૨ʏ⋆ᐠ₍⁽˚⑅̆˚⁾₎ᐟ⋆ᘓમ૨ıડτന੨ડ⋆⠀Christmas or Winter Holidays 12
❄∘⁖⁎⋆ᶿ̴̤᷇ ˒̫ ᶿ̴̤᷆⋆ᶿ̤᷇ ˓̫ ᶿ̤᷆⋆✶⁎∘❄⠀Christmas or Winter Holidays 13
* . ` ✧*♡ᑕू∙ો ੍✧ ✶ * .⠀Christmas or Winter Holidays 14
*ଘ(੭*ˊᵕˋ)੭* ੈ✩‧₊˚⠀Christmas or Winter Holidays 15
⁷₍⁽՚ᵕ՝⁾₎₇⠀Christmas or Winter Holidays 16
༶･･ᗰદ૨૨ʏ ᘓમ૨ıડτന੨ડ･･༶⠀Christmas or Winter Holidays 17
✩*⋆ ⍋*☪⋆⍋⋆*✩⠀Christmas or Winter Holidays 18
₍⁽⁰꒫⁰⁾₎◞❢⠀Christmas or Winter Holidays 19
*☃∘ˁ†∘✭‿✭∘†ˀ∘☃*⠀Christmas or Winter Holidays 20
༝﹡˖˟ ⸜₍⁽ˊ꒳ˋ⁾₎⸝ ༝﹡˖˟⠀Christmas or Winter Holidays 21
꜂₍⁽ˆ⁰ˆ⁾₎꜄⠀Christmas or Winter Holidays 22
*̣̥☆·͙̥‧❄‧̩̥·‧•̥̩̥͙‧·‧̩̥˟͙☃˟͙‧̩̥·‧•̥̩̥͙‧·‧̩̥❄‧·͙̥̣☆*̣̥⠀Christmas or Winter Holidays 23
⁄⁄ ⁄‹₍⁽⁰⁻⁰⁺⁾₎◟⁄⁄ ⁄⁄⁄⠀Christmas or Winter Holidays 24
｡*ﾟ✲*☆(๑òᆺó๑)｡*ﾟ✲*☆⠀Christmas or Winter Holidays 25
✚⃞ ⸌̷̻( ᷇ॢ〰ॢ ᷆◍)⸌̷̻⠀Christmas or Winter Holidays 26
✩̣̣̣̣̣ͯ┄•͙✧⃝•͙┄✩ͯ•͙͙✧⃝•͙͙✩ͯ┄•͙✧⃝•͙┄✩̣̣̣̣̣ͯ⠀Christmas or Winter Holidays 27
⚨˝⠀Christmas or Winter Holidays 28
(੭ ◕㉨◕)੭ =͟͟͞͞=͟͟͞͞三❆)’дº)<,’:=͟͟͞͞⠀Christmas or Winter Holidays 29
῍̩̖̬ ̎=͟͟͞͞₍⁽̩̩̩͑*་˙̫༏*⁾̩̩̩̉₎⠀Christmas or Winter Holidays 30
(╯^□^)╯︵ ❄☃❄⠀Christmas or Winter Holidays 31
(　ﾟ∀ﾟ)っ由⠀Christmas or Winter Holidays 32
⸝₍̗⁽ˆ⁰ˆ⁾₎͕⸍∘˚˳°✧⠀Christmas or Winter Holidays 33
˓˓⌨◝₍⁽ˆ⁰ˆ⁾₎◟⌨˒˒⠀Christmas or Winter Holidays 34
(⑅ᵒ̴̶̷᷄ωᵒ̴̶̷᷅⊞ོॢ)fෆr yෆu⋆*⋆✩⠀Christmas or Winter Holidays 35
( ❅࿉❅)⠀Christmas or Winter Holidays 36
˳˚̊̊⌖∙◌˳⚛˳̊̊̊☃˚˳̊◌˚̊⌖♡⠀Christmas or Winter Holidays 37
♡*⑅୨୧*̩̩̩̥✼•⠀Christmas or Winter Holidays 38
₍₍꜂₍⁽ˆ⁰ˆ⁾₎꜄₎₎⠀Christmas or Winter Holidays 39
₍₍◞₍⁽⁰ॕᵋ⁰ॕ⁺⁾₎◟₎₎⌕⠀Christmas or Winter Holidays 40
◞₍⁽⁺⁰꒵⁰⁾₎◟❣⠀Christmas or Winter Holidays 41
¸.•.¸¸୨˚̣̣̣͙୧¨*✼*¨୨˚̣̣̣͙୧¸¸.•.¸⠀Christmas or Winter Holidays 42
༓❅⃝༓༓࿇⃝༓༓❅⃝༓⠀Christmas or Winter Holidays 43
❣࿌ིྀ྇°˚࿅୧( ॑ധ ॑)୨࿅˳०࿌ིྀ྇⠀Christmas or Winter Holidays 44
❆(੭ु ◜◡‾)੭ु⁾☃❆⠀Christmas or Winter Holidays 45
·͙⁺˚*•̩̩͙✩•̩̩͙*˚⁺‧͙⁺˚*•̩̩͙✩•̩̩͙*˚⁺‧͙⁺˚*•̩̩͙✩•̩̩͙*˚⁺‧͙⠀Christmas or Winter Holidays 46
*※*(。uωu)(uωu。)*※*　Мёγγч Х’мд∫⠀Christmas or Winter Holidays 47
ﾟ･:，｡★＼(*’v`*)♪merryXmas♪(*’v`*)/★，｡･:･ﾟ⠀Christmas or Winter Holidays 48
ﾟ･:*:･｡(〃･ω･)ﾉ由☆*:<<<:*Ｍｅｒｒｙ　Ｘ’ｍａｓ*:<<<:*☆由ヽ(･ω･〃)｡･:*:･ﾟ⠀Christmas or Winter Holidays 49
ﾟ･:*:･｡♪☆彡^･∋／[☆<:* Merry X<#8217<mas*:<☆ ]＼∈･^ミ☆♪｡･:*:･ﾟ⠀Christmas or Winter Holidays 50
･:★.．☆.<*≡ゝ(ﾟｖﾟ=)Merry( ﾟｖﾟ )X’mas(=ﾟ▽ﾟ)ﾉ`･:.☆．.<★*⠀Christmas or Winter Holidays 51
.｡+ﾟ*[o･ω･]ﾉ*мёЯЯЧ CнЯIsтмДs*.｡+ﾟ*⠀Christmas or Winter Holidays 52
。o○★ヾ(´ﾟ∀ﾟ`*)Ｍｅｒｒｙ☆ Ｘｍａｓ(*´ﾟ∀ﾟ`)★。o○⠀Christmas or Winter Holidays 53
(〃´ω)ﾉ『☆｡o○☆мёЯЯЧ χ<#8217<мдs☆○o｡☆』ヽ(ω`〃 )⠀Christmas or Winter Holidays 54
(☆`･Θ･)v[゜ﾟ*☆мёγγч Хмд∫☆*ﾟﾟ]v(･Θ･´★)⠀Christmas or Winter Holidays 55
(☆ﾟｖ｀)э【*:<:*мёяячｘ’мдｓ*:<:*】ε(´ｖ’☆)⠀Christmas or Winter Holidays 56
($’v｀d)･.｡*MёяячＸ’мдｓ*。.･(ｂ´ｖ’$)⠀Christmas or Winter Holidays 57
[｀+･ｖ･+]мёяяч　х’　мдs[+･ｖ･+´]⠀Christmas or Winter Holidays 58
｡.*:・’ﾟ:。'(((＋_＋)))｡.*:ﾟ･’ﾟﾟ:。’･ﾟ⠀Christmas or Winter Holidays 59
ヾ(☆ゝ∀・)ﾉ※ﾟﾟＳ｡*※Йﾟﾟ｡*※Оﾟﾟ｡※Ｗ*ヾ(ゝω・｀*)ﾉ⠀Christmas or Winter Holidays 60
゜｡*※Оﾟ｡※(*´-ω)个(ω-`*)ﾟ｡*※Оﾟ｡※⠀Christmas or Winter Holidays 61
(◎･ω･)っ〔ﾟ+｡ργё∫ёйт｡+ﾟ〕⠀Christmas or Winter Holidays 62
(yωy*) мёггу снгisтмдsﾟ･*:.｡. ☆⠀Christmas or Winter Holidays 63
o<<<<( ´∀｀)っ┌iii┐　Ｍｅｒｒｙ　Ｘ’ｍａｓ⠀Christmas or Winter Holidays 64
ヾ(uωu*[++мёггу снгisтмдs++]*uωu)ﾉ⠀Christmas or Winter Holidays 65
ヾ(*´Д｀*)ノ*+:.★МёЯЯУ　X’маs☆.:+*ヾ(*´Д｀*)ノ⠀Christmas or Winter Holidays 66
Σ(★´・ェ・)=C<<<<☆・゜:*мёяяу Ⅹмαδ*:゜・☆⠀Christmas or Winter Holidays 67
v(*´・ｖ・｀)φ…..|Мёγγё Х’мд∫☆|⠀Christmas or Winter Holidays 68
ཥ•̫͡•ཤ⠀Halloween 1
˓ ू༼ ்ͦ॔ཀ ்ͦ॓ू༽⠀Halloween 2
༼ ु ்ͦ॔ཫ ்ͦ॓༽ु˒˒⠀Halloween 3
(˼●̙̂ ̟ ̟̎ ̟ ̘●̂˻)⠀Halloween 4
[¬º-°]¬⠀Halloween 5
←～（o ｀▽´ )oΨ⠀Halloween 6
←~∋(｡Ψ▼ｰ▼)∈⠀Halloween 7
∋━━o(｀∀´oメ）～→⠀Halloween 8
(((༼•̫͡•༽)))⠀Halloween 9
ᕐ ̆̈͜͡ ᕐ ોु✩°｡⋆⠀Halloween 10
ヾ(◎o◎,,；)ﾉ⠀Halloween 11
(∴◎∀◎∴)⠀Halloween 12
(ﾉꐦ ◎曲◎)ﾉ⠀Halloween 13
( ⌒⃘ ◞⌓◟ ⌒⃘ )⠀Halloween 14
ヘ(◕。◕ヘ)⠀Halloween 15
↜(͛ ꒪͒৫͏̈́꒪͒)͛⌰⠀Halloween 16
ཥ•̬͡•ོཤ⠀Halloween 17
/╲/\╭ºoꍘoº╮/\╱\⠀Halloween 18
( ⌒⃘ ◞↭◟ ⌒⃘ )⠀Halloween 19
ʕ*̫͡*ʕ。oO⠀Halloween 20
/|\( <,<)/|\⠀Halloween 21
(┏ `● .̫ ●)┏⠀Halloween 22
/╲/\╭( ͡° ͡° ͜ʖ ͡° ͡°)╮/\╱\⠀Halloween 23
/╲/\(╭•̀ﮧ •́╮)/\╱\⠀Halloween 24
/╲/\ºo<88<oº/\╱\⠀Halloween 25
／/＼/＼( ə ゝ ə )／\／\＼⠀Halloween 26
へ(❍∠❍)へ⠀Halloween 27
へ(oゝo)へ⠀Halloween 28
ᄽὁȍ ̪ őὀᄿ⠀Halloween 29
へ(⚈益⚈)へ⠀Halloween 30
m(~ー~m)～⠀Halloween 31
～(m~ー~)m⠀Halloween 32
m(~ｰ~m)~⠀Halloween 33
(◎皿◎)⠀Halloween 34
ʔ•̫͡•ཻʕ⠀Halloween 35
ꐑ(*ꐌ◡ꐌꐐ*)࿐࿔࿓⠀Halloween 36
m(@益@m)～⠀Halloween 37
(m▼w▼)m[ ☆･ﾟ:*нαΙΙощёёй*:ﾟ･☆]m(▼w▼m)⠀Halloween 38
【ﾟ+｡τγιсκ★σγ★τγεατﾟ+｡】Ψ(oﾟ∀ﾟo)Ψ⠀Halloween 39
～(☆´∀｀っ)っ【。:+:†+Тяiск оя Тяёат+†:+:゜】q(ゝε・★)～⠀Halloween 40
～(m`･Å･´)m *†*Тяiск оя тяёат*†* Ψ(ゝc_･´☆)⠀Halloween 41
人*´∀｀)＜Тяiск оя тяёат♪＞(´∀｀*人⠀Halloween 42
~ m(￣_￣m)~†┏┛墓┗┓†~(m￣_￣)m ~⠀Halloween 43
・・・・・～～～～～～～(m￣ー￣)m⠀Halloween 44
~~(m´□｀)/ﾟ･:*†┏┛呪┗┓†*:･ﾟ＼(´□｀m)~~⠀Halloween 45
m(ﾟДﾟm)～【†】～(m´ρ`)m⠀Halloween 46
⠒̫⃝*｡೨⋆*✩⠀New Years and New Years Eve 1
:*:.｡.:*(´∀｀*)Д Ндррч Йёш Чёдя*:.｡.:*:⠀New Years and New Years Eve 2
(●´Д｀)＜Д Ндррч Йёш Чёдя♪＞(´Д｀●)⠀New Years and New Years Eve 3
(●´艸｀)｡ﾟ.o｡Д ＨДРРЧ ЙЁЩ ЧЁДЯ｡o.ﾟ｡(´艸｀●)⠀New Years and New Years Eve 4
(U´･ｪ･)ﾉ♪ﾟ+.Д нДρРч ЙёЩ чЁдЯ.+ﾟ♪ヾ(･ｪ･｀U)⠀New Years and New Years Eve 5
(σ^▽^)σﾟ･｡･ﾟ+｡+ﾟ*:<<:*ＨДРРЧ★ЙЁЩ★ЧЁДЯ*:<<:*ﾟ+｡+ﾟ･｡･⊂(^∀^⊂)⠀New Years and New Years Eve 6
*:<<<:*Д ＨДРРЧ ЙЁЩ ЧЁДЯ*:<<<:*Σ(ﾟ艸ﾟ*)⠀New Years and New Years Eve 7
ﾟ*｡☆ヾ(´∀｀)Д Ндррч Йёш Чёдя！(´∀｀)ノ☆｡*ﾟ⠀New Years and New Years Eve 8
★～*~*～☆ндρρч(+≧3≦)йёщ(≧ε≦+)чёдγ☆～*~*～★⠀New Years and New Years Eve 9
♪ﾟ+.ｏ(<#8216<v`★)Α ｈαρρψ ηεｗ ψεαγ (★<#8217<v`)♪ﾟ+.ｏ⠀New Years and New Years Eve 10
(●´∀｀)ノ*:<<<:*Д нДρРч ЙёЩ чЁдЯ*:<<<:*ヽ(´∀｀●)⠀New Years and New Years Eve 11
(●´艸｀)。゜.o。Д ＨДРРЧ ЙЁЩ ЧЁДЯ。o.゜。(´艸｀●)⠀New Years and New Years Eve 12
(●≧ノд≦)<<<<Д нДρРч ЙёЩ чЁдЯ゜゜*☆⠀New Years and New Years Eve 13
(U´・ェ・)ノ♪゜+.Д нДρРч ЙёЩ чЁдЯ.+゜♪ヾ(・ェ・｀U)⠀New Years and New Years Eve 14
(ノ´∀｀)ノ*.ﾟ･｡:*:．ﾟ・☆A HAPPY NEW YEAR☆・ﾟ．:*:｡･ﾟ.*ヽ(´∀｀ヽ)⠀New Years and New Years Eve 15
*:<<<:*Д ＨДРРЧ ЙЁЩ ЧЁДЯ*:<<<:*Σ(゜艸゜*)⠀New Years and New Years Eve 16
゜゜.:。+ ゜+。:.д ндρρч йёщ чγдγ.:。+゜ ゜+。:.゜⠀New Years and New Years Eve 17
.:。+゜ Д ＨДРРЧヽ(*´Д｀*)ノЙЁЩ ЧЁДЯ ゜+。:.゜⠀New Years and New Years Eve 18
゜+.*:<<<<<:* Α ｈαρρψ ηεｗ ψεαγ *:<<<<<:*ﾟ+.⠀New Years and New Years Eve 19
゜・。・゜+。+゜*:<<:*ＨДРРЧ★ЙЁЩ★ЧЁДЯ*:<<:*゜+。+゜・⠀New Years and New Years Eve 20
☆*ﾟ ゜ﾟ*☆Д нαρρy ЙёЩ ЧёαЯ!!☆*ﾟ ゜ﾟ*☆⠀New Years and New Years Eve 21
Д ＨДРРЧЙЁЩ ЧЁДЯ_φ(´ｪ｀*U⠀New Years and New Years Eve 22
୨୧ᕼᗩᑭᑭY ᗷIᖇTᕼᗞᗩY୨୧⠀Birthdays 1
♪ (｡´＿●`)ﾉ┌iiii┐ヾ(´○＿`*) ♪⠀Birthdays 2
✯ℋᵅᵖᵖᵞ ℬⁱʳᵗᑋᵈᵃᵞ✯⠀Birthdays 3
ℋ੨ppყ ᙖ ౹̊ণ৳hძ੨ყ·*⋆ฺ࿐♡⠀Birthdays 4
Ⓗ⃞ⓐ⃞ⓟ⃞ⓟ⃞ⓨ⃞ ᵕ̈*Ⓑ⃞ⓘ⃞ⓡ⃞ⓣ⃞ⓗ⃞ⓓ⃞ⓐ⃞ⓨ⃞⠀Birthdays 5
♫Happy☻໌*✰☻ັBir<hday☆+｡⠀Birthdays 6
(pq´∀`)┌iiiiii┐(´∀`pq)⠀Birthdays 7
畄_(*´Д｀*)_畄⠀Birthdays 8
(*’∀`)ﾊ┌iiiiii┐ﾊ(‘∀`*)⠀Birthdays 9
(*≧∀≦)ﾊ┏━iiiiii━┓ﾊ(≧∇≦*)⠀Birthdays 10
♪o<<<<( ´∀｀)っ┌iii┐⠀Birthdays 11
（●ＵωＵ*)ﾉ<#8221<┌iiii┐⠀Birthdays 12
(*･ω･)ﾉ<#8221<┌iii┐♡⠀Birthdays 13
.*･ﾟ☆Happyヾ(*∇*)ﾉBir<hday☆ﾟ･*.⠀Birthdays 14
.*･ﾟ☆Happyヾ(*ε*)ﾉBir<hday☆ﾟ･*.⠀Birthdays 15
.*･ﾟ☆ндрру(*⌒▽⌒*)b вiятнDду☆ﾟ･*⠀Birthdays 16
.*･ﾟ☆ндрруヾ(*＾-＾*)ﾉвiятнDду☆ﾟ･*.⠀Birthdays 17
.*･ﾟ☆ндрруヾ(*^▽^*)ﾉвiятнDду☆ﾟ･*.⠀Birthdays 18
ヾ(・∀・)ﾉ <<<<<<<< Happy Bir<hday♪⠀Birthdays 19
ヽ（≧ω≦）｛☆HAPPY★BIRTHDAY☆｝（≧ω≦）/⠀Birthdays 20
(*´p∀q｀*)ﾉ《*ﾟ:+.｡☆ＨДРРЧ ВＩЯтＨＤДЧ☆｡.+:ﾟ*》ヾ(*´p∀q｀*)⠀Birthdays 21
(*´uωu)Ｈдρρч☆Вiятнｄдч*+:｡.｡:+*⠀Birthdays 22
(●ﾟ∀ﾟ)ﾉ♭ﾟ’･:*♪:.ндρρч ьｉγтнｄдч.:♪*:･’ﾟ♭ヾ(ﾟ∀ﾟ○)⠀Birthdays 23
(☆-Ⅴ･)p||*:<<<:*ＨДРРЧ ВＩЯтＨ ＤДЧ*:<<<:*||q･Ⅴ-★)⠀Birthdays 24
(☆<><<∪<<<< b)b｡*†*｡★Ｈдρρч Вｉγтн Ｄдч☆｡*†*｡d(d<><<∪<<<<★)⠀Birthdays 25
*+:<нарру<<:+*(●´∀`人´∀`●)*+:<вiятнＤау<<:+*⠀Birthdays 26
∮(´･ω･)＜ндρρч ьдγтнｄдч∮⠀Birthdays 27
♪вiятнＤауヽ(´Д｀*)ﾉ ♪ヽ(*´Д｀)ﾉDайсё♪⠀Birthdays 28
o(★´∀｀★)o☆*:<<:*★ＨДРРЧ ВＩЯтＨＤДЧ★*:<<:*☆o(☆´∀｀☆)o⠀Birthdays 29
РЯЁＳЁЙТ　ＦОЯ　УОЦ・・・(*´∀｀*)σ[畄][畄][畄]⠀Birthdays 30
(。<><<∀<<<<)_畄q(<><<∀<<<< ｡)ТΗАЙΚУОЦ⠀Birthdays 31
◌⑅⃝ℋ⍲ᵖᴘᵞ ℬⁱᖇᐪમᵈ੨ყ♡ෆ ͙⁎♡⑅⃝◌⠀Birthdays 32
～ΒΙяΤΗDΑΥ LOVE❤(◍•ᴗ•◍)/⠀Birthdays 33
⋈‧̍̊·̊‧̥°̩̥˚̩̩̥͙°̩̥‧̥·̊‧̍̊наppעෆ⃛вiянтᏂᎴע‧̍̊·̊‧̥°̩̥˚̩̩̥͙°̩̥‧̥·̊‧̍̊⋈⠀Birthdays 34
ʕ•̫͡•ॽु✚⃞ྉ*✲ﾟ*｡⋆ ℳෆ<h ℯr’s ⅅ ੨Ꮍ⠀Other Holidays and Events 1
Мотнёя’δ Dαу:*:♪・゜’☆…((φ(‘ー’*)⠀Other Holidays and Events 2
*♡೫̥͙*:・ℋɑppყ Ϣәԁԁıɲɠﾟ･:* ೫̥͙♡*⠀Other Holidays and Events 3
d【☆＾∀＾】Ｃｏйｇядтμｌдтｉｏй【＾∀＾★】b⠀Other Holidays and Events 4
*.+(◇´v’σ【 ДρяiΙFооΙ 】ョ’v｀◆)+.*ﾟ⠀Other Holidays and Events 5
ヾ(*´・∀)ﾉ*:..｡o○∫μммёγ υдcдтioй○o｡..:*ヾ(∀・｀*)ﾉ⠀Other Holidays and Events 6
【☆･ﾟ:*сносоΙαтё*:ﾟ･☆ 】ｮω｀｡)⠀Other Holidays and Events 7
::.*゜:.。:.ⅤдＬ ёйтiйёＤду::.*゜:.。:.〆(uωu●)⠀Other Holidays and Events 8
☆ﾟ+｡(｀･ｪ´･+｡)b【Vд<ёйтiйё dду】d(｡+･｀ｪ･´)｡+ﾟ☆⠀Other Holidays and Events 9
☆ﾟ+o｡o｡o+ﾟ ⅤΑгЁЙтΙЙЁ ＤΑY ﾟ+o｡o｡o+ﾟ☆⠀Other Holidays and Events 10
★´・ω・ｐ≪*+｡ﾟ･ⅤД￡ЁЙТΙЙЁＤДЧ･ﾟ｡+*≫ｑ・ω・｀★⠀Other Holidays and Events 11
⊂((・▽・))⊃⠀Wide Open Hug Arms 1
＼(^o^)／⠀Wide Open Hug Arms 2
d=(´▽｀)=b⠀Wide Open Hug Arms 3
⊂(◉‿◉)つ⠀Wide Open Hug Arms 4
⊂（♡⌂♡）⊃⠀Wide Open Hug Arms 5
⊂( ◜◒◝ )⊃⠀Wide Open Hug Arms 6
(づ｡◕‿‿◕｡)づ⠀Hugging to the Right 1
(づ￣ ³￣)づ⠀Hugging to the Right 2
(っ˘̩╭╮˘̩)っ⠀Hugging to the Right 3
⁽₍੭ ՞̑◞ළ̫̉◟՞̑₎⁾੭⠀Hugging to the Right 4
(੭ु｡╹▿╹｡)੭ु⁾⁾⠀Hugging to the Right 5
(*´σЗ`)σ⠀Hugging to the Right 6
(っ´▽｀)っ⠀Hugging to the Right 7
(っ´∀｀)っ⠀Hugging to the Right 8
c⌒っ╹v╹ )っ⠀Hugging to the Right 9
(σ･з･)σ⠀Hugging to the Right 10
(੭ु´･ω･`)੭ु⁾⁾⠀Hugging to the Right 11
(oﾟ▽ﾟ)o⠀Hugging to the Right 12
༼つ ் ▽ ் ༽つ⠀Hugging to the Right 13
༼つ . •́ _ʖ •̀ . ༽つ⠀Hugging to the Right 14
╏つ ͜ಠ ‸ ͜ಠ ╏つ⠀Hugging to the Right 15
༼ つ ̥◕͙_̙◕͖ ͓༽つ⠀Hugging to the Right 16
༼ つ ◕o◕ ༽つ⠀Hugging to the Right 17
༼ つ ͡ ͡° ͜ ʖ ͡ ͡° ༽つ⠀Hugging to the Right 18
(っಠ‿ಠ)っ⠀Hugging to the Right 19
༼ つ ◕_◕ ༽つ⠀Hugging to the Right 20
ʕっ•ᴥ•ʔっ⠀Hugging to the Right 21
༼ つ ▀̿_▀̿ ༽つ⠀Hugging to the Right 22
ʕ ⊃･ ◡ ･ ʔ⊃⠀Hugging to the Right 23
╏つ” ⊡ 〜 ⊡ ” ╏つ⠀Hugging to the Right 24
(⊃｡•́‿•̀｡)⊃⠀Hugging to the Right 25
(っ⇀⑃↼)っ⠀Hugging to the Right 26
(.づ◡﹏◡)づ.⠀Hugging to the Right 27
(.づσ▿σ)づ.⠀Hugging to the Right 28
(っ⇀`皿′↼)っ⠀Hugging to the Right 29
(.づ▣ ͜ʖ▣)づ.⠀Hugging to the Right 30
(つ ͡° ͜ʖ ͡°)つ⠀Hugging to the Right 31
(⊃ • ʖ̫ • )⊃⠀Hugging to the Right 32
（っ・∀・）っ⠀Hugging to the Right 33
(つ´∀｀)つ⠀Hugging to the Right 34
(っ*´∀｀*)っ⠀Hugging to the Right 35
(つ▀¯▀)つ⠀Hugging to the Right 36
(つ◉益◉)つ⠀Hugging to the Right 37
(<><< ^_^ )<><<⠀Hugging to the Right 38
ლ(́◉◞౪◟◉‵ლ)⠀Hugging to the Left 1
ლ(◉◞⊖◟◉｀ლ)⠀Hugging to the Left 2
ლ(´ ❥ `ლ)⠀Hugging to the Left 3
⊂(´･◡･⊂ )∘˚˳°⠀Hugging to the Left 4
ヾ(‘c_’ヽ,,)⠀Hugging to the Left 5
⊂(・▽・⊂)⠀Hugging to the Left 6
⊂(・ヮ・⊂)⠀Hugging to the Left 7
⊂(・﹏・⊂)⠀Hugging to the Left 8
⊂(･ω･*⊂)⠀Hugging to the Left 9
⊂(´・ω・｀⊂)⠀Hugging to the Left 10
ლ(・ヮ・ლ)⠀Hugging to the Left 11
ლ(・﹏・ლ)⠀Hugging to the Left 12
ლ(･ω･*ლ)⠀Hugging to the Left 13
───==≡≡ΣΣ((( つºل͜º)つ⠀Running Hugs 1
─=≡Σ((( つ◕ل͜◕)つ⠀Running Hugs 2
─=≡Σ((( つ ◕o◕ )つ⠀Running Hugs 3
～～～～(/￣ｰ(･･｡)/⠀Running Hugs 4
───==≡≡ΣΣ(づ￣ ³￣)づ⠀Running Hugs 5
─=≡Σʕっ•ᴥ•ʔっ⠀Running Hugs 6
───==≡≡ΣΣ(<><< ^_^ )<><<⠀Running Hugs 7
─=≡Σ༼ つ ▀̿_▀̿ ༽つ⠀Running Hugs 8
───==≡≡ΣΣ(っ´▽｀)っ⠀Running Hugs 9
───==≡≡ΣΣ(っ´∀｀)っ⠀Running Hugs 10
～～(つˆДˆ)つﾉ<><<｡☆)ﾉ⠀Running Hugs 11
(<><<^_^)<><<<<<<(^o^<<<<)⠀Multiple People Hugging Each Other 1
(Ɔ˘⌣˘)(˘⌣˘)˘⌣˘ C)⠀Multiple People Hugging Each Other 2
(ღ˘⌣˘)❛ั◡❛ัღ)⠀Multiple People Hugging Each Other 3
(´◉◞౪◟◉)⊃))⊙ω⊙)⠀Multiple People Hugging Each Other 4
└(┐ﾞ’ωﾞ’ωﾞ`┘)┌⠀Multiple People Hugging Each Other 5
ღˇ◡ˇ(ᵕ꒶̮ᵕෆ⠀Multiple People Hugging Each Other 6
(￣ー￣(｡-_-｡*)ゝ⠀Multiple People Hugging Each Other 7
(_＾∇＾)･_･)η⠀Multiple People Hugging Each Other 8
(*´＾(^｀*∬o⠀Multiple People Hugging Each Other 9
(*￣-(-*)ゝ⠀Multiple People Hugging Each Other 10
(*-ｪ-(-ｪ-*)o⠀Multiple People Hugging Each Other 11
(*~ｰ(‘ー’*川o⠀Multiple People Hugging Each Other 12
(/´-(~。~*)/⠀Multiple People Hugging Each Other 13
(/^.^(^.^*)<><<⠀Multiple People Hugging Each Other 14
(●´Д｀)⊃⊂(´Д｀○)⠀Multiple People Hugging Each Other 15
｡ﾟ.(*♡´◡` 人´◡` ♡*)ﾟ °・⠀Multiple People Hugging Each Other 16
(٭′ᵕુ‵)ુ(ૂ′ᵕ‵ॢං)⠀Multiple People Hugging Each Other 17
(๑˃̶͈̀ ᵕ ॣ˂̶͈́)*｡̀ ̫ ｡́)ॢ)⠀Multiple People Hugging Each Other 18
(*• ुᴗ•ධ̢•͈ꄃ̑•͈ ධ̡੭ु⁾⁾·°♡⠀Multiple People Hugging Each Other 19
꒰๑*´ᗜ`*꒱*›◡‹꒱꒱⠀Multiple People Hugging Each Other 20
♪((●<><<ω<<<<)っ)))´、ゝ`)⠀Multiple People Hugging Each Other 21
(つ・▽・)つ⊂(・▽・⊂)⠀Multiple People Hugging Each Other 22
(つ≧▽≦)つ⊂(・ヮ・⊂)⠀Multiple People Hugging Each Other 23
(つˆ⌣ˆ)つ⊂(・﹏・⊂)⠀Multiple People Hugging Each Other 24
⊂´⌒つ ﾟ∀ﾟ)つ━⊂(ﾟ∀ﾟ⊂⌒｀つ⠀Multiple People Hugging Each Other 25
三 ( ◜◡‾)っ)⁰▿⁰)◜⠀Multiple People Hugging Each Other 26
(*･ω･)つ⊂(･ω･*)⠀Multiple People Hugging Each Other 27
（⊃≧ω≦(´ω｀*⊂)⠀Multiple People Hugging Each Other 28
((((／￣∇￣)／＼(￣∇￣＼))))⠀Multiple People Hugging Each Other 29
╰(*´︶`*)╯(´・ω・｀)⠀Multiple People Hugging Each Other 30
(/￣^￣)/￣ ＼(｡_｡＼)⠀Multiple People Hugging Each Other 31
(~˘▾˘)~ ~(˘▾˘~)⠀Multiple People Hugging Each Other 32
(ɔ ˘⌣˘)˘⌣˘ c)⠀Multiple People Hugging Each Other 33
(ﾉ*’ω’*)ﾉ~~~~) ◜◡‾)⠀Multiple People Hugging Each Other 34
（ノ´д｀ノ。・・。＼´д｀＼）⠀Multiple People Hugging Each Other 35
“8-( ●｀ε´●)爻(●｀ε´● )-8”⠀Grabbing Hands 1
(♥Ő‿Ő)爻(Ő‿Ő♥)⠀Grabbing Hands 2
(☆⊙∇⊙)爻(⊙∇⊙☆)⠀Grabbing Hands 3
(✿ʘ‿ʘ)爻(ʘ‿ʘ✿)⠀Grabbing Hands 4
(＾O＾)爻(◕▿◕✿)⠀Grabbing Hands 5
(˶′◡‵˶)爻(♥ O ♥)⠀Grabbing Hands 6
(　￣▽)爻(▽￣　)⠀Grabbing Hands 7
((／*~▽)乂(▽~*＼))⠀Grabbing Hands 8
(((●´Ｕ｀)爻(´Ｕ｀●))))⠀Grabbing Hands 9
(❀◕∇◕)爻(◕∇◕❀)⠀Grabbing Hands 10
(ﾉ^^)乂(^^ )ﾉ⠀Grabbing Hands 11
ヽ(*ﾟ｀∀´ﾟ)乂(´ﾟ∀ﾟ｀*)ﾉ⠀Grabbing Hands 12
(p´･∀･)乂(･∀･｀q)⠀Grabbing Hands 13
((( *~∇~)爻(~∇~* )))⠀Grabbing Hands 14
“8-(*･x･)爻(･x･*)-8”⠀Grabbing Hands 15
((( ^-^)爻(^-^ )))⠀Grabbing Hands 16
(*^^）爻（^^*)⠀Grabbing Hands 17
( <_<)爻(-“-<)⠀Grabbing Hands 18
((( ^^)爻(^^ )))⠀Grabbing Hands 19
“8-( ●｀・З・´)爻(｀・ε・´● )-8”⠀Grabbing Hands 20
٩꒰ ˘ ³˘꒱۶ⒽⓤⒼ♥♡̷♡̷⠀Words 1
٩(๑•◡-๑)۶ⒽⓤⒼ❤⠀Words 2
v(۝)v⠀Devouring Mouths 1
( ´◔ ۝ゝ◔`)⠀Devouring Mouths 2
(◉۝◉)⠀Devouring Mouths 3
╭〳 . ˘ ۝ ˘ . 〵╮⠀Devouring Mouths 4
ू꒰΄ ิ̤۝ ิ ̤꒱ु⠀Devouring Mouths 5
༼∗ღ۝ღ∗༽⠀Devouring Mouths 6
໒( ˵ ° ۝ ° ˵ )७⠀Devouring Mouths 7
(✧۝✧)/⠀Devouring Mouths 8
| ᴼ ۝ ᴼ |⠀Devouring Mouths 9
༼ ˘ ۝ ˘ ༽⠀Devouring Mouths 10
╰། ￣ ۝ ￣ །╯⠀Devouring Mouths 11
໒( ́ ۝ ́ )७⠀Devouring Mouths 12
╭། ” • ۝ • ” །╮⠀Devouring Mouths 13
┌[ ʘ̆ ۝ ʘ̆ ]┐⠀Devouring Mouths 14
╏ * ￣ ۝ ￣ * ╏⠀Devouring Mouths 15
(⸌۝⸍)⠀Devouring Mouths 16
╰(⊹◕۝◕ )╯⠀Devouring Mouths 17
⊱(*⁍ ڡ ⁍*)⊰⠀Licking Lips ڡ Style 1
(๑′ڡ‵๑)۶४४yϋᵐᵐӵ♡॰⋆̥⠀Licking Lips ڡ Style 2
٩(*ゝڡ◕๑)۶♥⠀Licking Lips ڡ Style 3
ꉨڡꉨ⠀Licking Lips ڡ Style 4
(*´ڡ`●)⠀Licking Lips ڡ Style 5
ʕ ∗ •́ ڡ •̀ ∗ ʔ⠀Licking Lips ڡ Style 6
╰། ❛ ڡ ❛ །╯⠀Licking Lips ڡ Style 7
ヽ(๑╹ڡ╹๑)ﾉ⠀Licking Lips ڡ Style 8
(ﾉ≧ڡ≦)⠀Licking Lips ڡ Style 9
(ˆ ڡ ˆ)⠀Licking Lips ڡ Style 10
ʕっ˘ڡ˘ςʔ⠀Licking Lips ڡ Style 11
(๑╹ڡ╹๑)⠀Licking Lips ڡ Style 12
ᕙ། – ڡ – །ᕗ⠀Licking Lips ڡ Style 13
(∩❛ڡ❛∩)⠀Licking Lips ڡ Style 14
(っ˘ڡ˘ς)⠀Licking Lips ڡ Style 15
ლ(´ڡ`ლ)⠀Licking Lips ڡ Style 16
(⁎⁍̴ڡ⁍̴⁎)⠀Licking Lips ڡ Style 17
(රڡර人)⠀Licking Lips ڡ Style 18
(ॢ◕ัڡ ◕ั ॢ)⠀Licking Lips ڡ Style 19
(≧ڡ≦*)⠀Licking Lips ڡ Style 20
ԅ[ ˵ ☯ ڡ ☯ ˵ ]凸⠀Licking Lips ڡ Style 21
୧〳 ” • ڡ • ” 〵୨⠀Licking Lips ڡ Style 22
ᕕ[ ˵ ☯ ڡ ☯ ˵ ]┐⠀Licking Lips ڡ Style 23
(๑╹ڡ╹)⠀Licking Lips ڡ Style 24
໒( = ▀ ڡ ▀ = )७⠀Licking Lips ڡ Style 25
| ⊘ ڡ ⊘ |⠀Licking Lips ڡ Style 26
ʕ ▀ ڡ ▀ ʔ⠀Licking Lips ڡ Style 27
ʕ ି ڡ ି ʔ⠀Licking Lips ڡ Style 28
╭〳 ° ڡ ° 〵╮⠀Licking Lips ڡ Style 29
ᕙ▐ ” ° ڡ ° ” ▐ᕗ⠀Licking Lips ڡ Style 30
ʕ ☯ ڡ ☯ ʔ⠀Licking Lips ڡ Style 31
 ᕦ〳 ⊙ ڡ ⊙ 〵ᕤ⠀Licking Lips ڡ Style 32
 ԅ| . ͡° ڡ ͡° . |ᕤ⠀Licking Lips ڡ Style 33
ᕕ[ ᓀ ڡ ᓂ ]ㄏ⠀Licking Lips ڡ Style 34
 〳 : ⊘ ڡ ⊘ : 〵⠀Licking Lips ڡ Style 35
(๑ゝڡ◕๑)⠀Licking Lips ڡ Style 36
(๑´ڡ`๑三๑´ڡ`๑)⠀Licking Lips ڡ Style 37
໒( ᓀ ڡ ᓂ )७⠀Licking Lips ڡ Style 38
[ ☉ ڡ ☉ ]⠀Licking Lips ڡ Style 39
( ๑ ❛ ڡ ❛ ๑ )❤⠀Licking Lips ڡ Style 40
 (๑´ڤ`๑)⠀Licking Lips ڡ Style 41
 ( ՞ ڡ ՞ )⠀Licking Lips ڡ Style 42
ԅ|.͡° ڡ ͡°.|ᕤ⠀Licking Lips ڡ Style 43
ʅ ﴾סּ ؂ סּ ʅ ﴿⠀Licking Lips ڡ Style 44
ತ ൧͑ ತ⠀Licking Lips ൧͑ Style 1
(๑ ˭̴̵̶᷄൧̑ ˭̴̵̶᷅๑)⠀Licking Lips ൧͑ Style 2
(ර൧ර☆)⠀Licking Lips ൧͑ Style 3
(ತ ൧͑ ತ)⠀Licking Lips ൧͑ Style 4
໒( ᓀ ൧̑ ᓂ )७⠀Licking Lips ൧͑ Style 5
[ ☉ ൧̑ ☉ ]⠀Licking Lips ൧͑ Style 6
ԅ|.͡° ൧͑ ͡°.|ᕤ⠀Licking Lips ൧͑ Style 7
ʕっ˘൧̑˘ςʔ⠀Licking Lips ൧͑ Style 8
╰། ❛ ൧̑ ❛ །╯⠀Licking Lips ൧͑ Style 9
(っ˘൧͑˘ς)⠀Licking Lips ൧͑ Style 10
(๑╹൧͑╹๑)⠀Licking Lips ൧͑ Style 11
ʕ ∗ •́ ൧͑ •̀ ∗ ʔ⠀Licking Lips ൧͑ Style 12
(∩❛൧͑❛∩)⠀Licking Lips ൧͑ Style 13
Σ_(꒪ཀ꒪」∠)_⠀Drooling with hunger 1
(⋅⃘﹎᷊⋅⃘)⠀Drooling with hunger 2
_:(´ཀ`」 ∠):_⠀Drooling with hunger 3
◟( ྃ༎͞ ྃ)◞⠀Drooling with hunger 4
(✽´ཫ`✽)⠀Drooling with hunger 5
˓˓ ू༼ ⠁⃘ཀ ⠁⃘ू༽⠀Drooling with hunger 6
༼ ु⠁⃘ཫ ⠁⃘༽ु˒˒⠀Drooling with hunger 7
 (´ q ` ” )⠀Drooling with hunger 8
(꒪ټ꒪☚)⠀Drooling with hunger 9
(๑ ิټ ิ)⠀Drooling with hunger 10
v(❆ڼ❆)v⠀Drooling with hunger 11
∗♞͂ ૂ ੭͜♞͂∗✩⃛⠀Drooling with hunger 12
(　 ิ౪ ิ )っ─∈⠀Forks ─∈ 1
ᕕ[ ᓀ ڡ ᓂ ]ㄏ─∈⠀Forks ─∈ 2
 ( ՞ ڡ ՞ )─∈⠀Forks ─∈ 3
໒( ́ ۝ ́ )७─∈⠀Forks ─∈ 4
(っ˘ڡ˘)っ─∈⠀Forks ─∈ 5
╭〳 ° ڡ ° 〵─∈⠀Forks ─∈ 6
ʕ ∗ •́ ڡ •̀ ∗ ʔ─∈⠀Forks ─∈ 7
ᕙ། – ڡ – །─∈⠀Forks ─∈ 8
╰། ❛ ڡ ❛ །─∈⠀Forks ─∈ 9
ʕっ˘ڡ˘ʔっ─∈⠀Forks ─∈ 10
ψ(・ω´・,,ψ⠀Forks ─∈ 11
ヘ（。□°）ヘ⠀General Pain and Injuries 1
(。_＋)＼⠀General Pain and Injuries 2
((((*｡_｡)_⠀General Pain and Injuries 3
(xLx)ヾ⠀General Pain and Injuries 4
｢(＝＞o≦＝)ﾉ⠀General Pain and Injuries 5
/(*ι*)ヾ⠀General Pain and Injuries 6
／(x~x)＼⠀General Pain and Injuries 7
~(<><<_<<<<~)⠀General Pain and Injuries 8
┗( ●-﹏ ｀｡)づ⠀General Pain and Injuries 9
☆￣(＞。☆)⠀General Pain and Injuries 10
☆⌒(＞。≪)⠀General Pain and Injuries 11
(‘﹏*๑)⠀General Pain and Injuries 12
.( ̵˃﹏˂̵ )⠀General Pain and Injuries 13
ლ(｡-﹏-｡ ლ)⠀General Pain and Injuries 14
(˃̶᷄︿๏）⠀General Pain and Injuries 15
(っ- ‸ – ς)⠀General Pain and Injuries 16
(ᗒᗩᗕ)՞⠀General Pain and Injuries 17
● ﹏☉⠀General Pain and Injuries 18
໒(⁄›˅̭‹∖)७⠀General Pain and Injuries 19
꒰⁎×﹏×⁎꒱՞༘✡⠀General Pain and Injuries 20
☆(　－o-)~~⠀General Pain and Injuries 21
(x_x☆⠀General Pain and Injuries 22
◟̽◞̽ ༘*⠀General Pain and Injuries 23
(≥_<<<<)⠀General Pain and Injuries 24
(⇀⼼_↼)*✲ﾟ*⠀General Pain and Injuries 25
꒰⋆ꆩ⌢̫ꆤ⋆ॢ꒱˚º✩⃛⠀General Pain and Injuries 26
(*<><<_<<<<*)⠀General Pain and Injuries 27
（＊о＊）≡☆⠀General Pain and Injuries 28
╰[✖Ĺ̯ಠ]╯⠀General Pain and Injuries 29
―(T_T)→⠀General Pain and Injuries 30
✧*。ヾ(｡<><<﹏<<<<｡)ﾉﾞ✧*。⠀General Pain and Injuries 31
（。_°☆＼(- – )⠀Inflicting Pain on Others 1
(☆⠀Inflicting Pain on Others 2
[emai<<#160<pro<ec<ed]⠀Inflicting Pain on Others 3
<)☆ ＼(｀-´ﾒ)⠀Inflicting Pain on Others 4
(._+ )☆＼(-.-メ)⠀Inflicting Pain on Others 5
!!( *д*):･’.::･(ｰｰ< )⠀Inflicting Pain on Others 6
(ノ<><<ノ)⠀Tripping or Falling Down 1
◎☆（♯××）┘⠀Tripping or Falling Down 2
(ｏ＿　＿)ｏ⠀Tripping or Falling Down 3
(o_□_)o⠀Tripping or Falling Down 4
(ヘ＿　＿)ヘ⠀Tripping or Falling Down 5
* ・・(o_ _)o⠀Tripping or Falling Down 6
ヽ(＿　＿ヽ)⠀Tripping or Falling Down 7
ヽ(_ _ヽ)彡⠀Tripping or Falling Down 8
(ノ_ _)ノ⠀Tripping or Falling Down 9
εミ(ο_ _)ο⠀Tripping or Falling Down 10
ο(_ _ο)彡3⠀Tripping or Falling Down 11
ミ(ノ_ _)ノ⠀Tripping or Falling Down 12
ヘ(＿　＿ヘ)⠀Tripping or Falling Down 13
ﾍ(｡｡ﾍ)☆⠀Tripping or Falling Down 14
┏|*＿ ＿|┓⠀Tripping or Falling Down 15
( っ_ _)っ)）⠀Tripping or Falling Down 16
⊂⌒~⊃｡Д｡)⊃⠀Tripping or Falling Down 17
((( ⊂⌒~⊃｡Д｡)⊃⠀Tripping or Falling Down 18
(o_ _)ﾉ彡☆⠀Tripping or Falling Down 19
☆ヽ(o_ _)o⠀Tripping or Falling Down 20
⊂´⌒∠；ﾟДﾟ)ゝつ⠀Tripping or Falling Down 21
(｡´<><<д<<<<)っ彡☆⠀Tripping or Falling Down 22
(o_ _)ｏ))⠀Tripping or Falling Down 23
！☆〓(ﾉ_ _)ﾉ⠀Tripping or Falling Down 24
┌(。Д。)┐⠀Tripping or Falling Down 25
(o_ _）ノ彡☆⠀Tripping or Falling Down 26
☆^(o≧∀≦)o⠀Tripping or Falling Down 27
=D—(o_　_)o⠀Tripping or Falling Down 28
ﾐ(ﾉ_ _)ﾉ=3⠀Tripping or Falling Down 29
☆ミ(+ωゞ)☆彡⠀Tripping or Falling Down 30
ミ☆(*._.)⠀Tripping or Falling Down 31
ヘ(<><<_<<<<ヘ)⠀Tripping or Falling Down 32
（<<￣Д￣）ノヾ((((；゜д゜))__⠀Tripping or Falling Down 33
[ ± _ ± ]⠀General Sickness 1
(๑-﹏-๑)⠀General Sickness 2
(˘̭⺫˘̭ <)⠀General Sickness 3
(-﹏-。)⠀General Sickness 4
(☍﹏⁰)｡⠀General Sickness 5
( ⁺⌓ॢ⁺<)՞⠀General Sickness 6
ෆ⃛(˃͈᷇◟̵◞̵˂͈᷆ ფ⠀General Sickness 7
◝(๑⁺᷄д⁺᷅๑)◞՞⠀General Sickness 8
බ͓⌢බ͓⠀General Sickness 9
ಸ , ໖⠀General Sickness 10
ಸ_ಸ⠀General Sickness 11
^(✹ཽ)﹏ु(✹ཽ)^⠀General Sickness 12
(°﹏｡υ)⠀General Sickness 13
༼ ಥ﹏لಥ ༽ ᵘ>ᵍʰ⠀General Sickness 14
⊂((° x。))⊃⠀General Sickness 15
｡.*:・’ﾟ:。'(((＋_＋)))｡.*:ﾟ･’ﾟﾟ:。’･ﾟ⠀General Sickness 16
(ﾟ×ﾟ<<<)⠀Throwing Up, Puking, or Barfing 1
( •́ ✖ •̀)⠀Throwing Up, Puking, or Barfing 2
(´ж｀<)⠀Throwing Up, Puking, or Barfing 3
(●’x`*)⌒％⠀Throwing Up, Puking, or Barfing 4
(ﾉ’x`｡ヽ)⠀Throwing Up, Puking, or Barfing 5
‧∘˳°∗˚(⁎›ˍູ‹) ∗.∘˚˳°⠀Throwing Up, Puking, or Barfing 6
( ╹✖╹)⠀Throwing Up, Puking, or Barfing 7
(<・ж<・<)⠀Throwing Up, Puking, or Barfing 8
(*<ﾟ<艸<ﾟ<)⠀Throwing Up, Puking, or Barfing 9
(；ﾟ；┏艸┓；ﾟ；)⠀Throwing Up, Puking, or Barfing 10
＿|￣|○､<’.･⠀Throwing Up, Puking, or Barfing 11
<｀<:ﾞ<｀(<ﾟ<ж<ﾟ< )⠀Throwing Up, Puking, or Barfing 12
˓˓( ॢ₎˔̈₍ ॢ)˒˒⠀Throwing Up, Puking, or Barfing 13
(。・艸・)⠀Throwing Up, Puking, or Barfing 14
(*U艸U*)⠀Throwing Up, Puking, or Barfing 15
((゜乂゜))⠀Throwing Up, Puking, or Barfing 16
⋆* ⁑⋆* (๑•﹏•)⋆* ⁑⋆*⠀Throwing Up, Puking, or Barfing 17
（＃´Ⅹ｀＃）⠀Throwing Up, Puking, or Barfing 18
┗┐(<<*<:´<艸<`:<*<<)┌┛⠀Throwing Up, Puking, or Barfing 19
ε≡ ε≡ ε≡ ε＝ （#・ж・）⠀Throwing Up, Puking, or Barfing 20
。゜+.(:.<゜<艸<゜<.:)゜+.゜⠀Throwing Up, Puking, or Barfing 21
ε-(≖д≖﹆)⠀Coughing 1
ε-(＞．＜<<⠀Coughing 2
ε=o(´ﾛ｀||)⠀Coughing 3
((( +д+)o=3=3⠀Coughing 4
ε-(<><<o<<<<)⠀Coughing 5
(；≧∇≦) =3⠀Coughing 6
（●｀□´）＝з⠀Coughing 7
人人人ヾ( <×o×)〃 人人人⠀Drowning 1
︵‿︵‿︵‿︵‿︵‿︵‿︵‿︵‿︵‿ヽ(゜□゜ )ノ︵‿︵‿︵‿︵‿︵‿⠀Drowning 2
(ू̯⋆̧ ͕⋆᷅ू̯ )  ༘˟⠀Complex Pain and Sickness 1
⁽⁽ƈ ͡ (ु ˲̥̥̥́ ˱̥̥̥̀) ु⁾⁾⠀Complex Pain and Sickness 2
₊·(ϱ॔﹏ᵕ๑॓)‧*⠀Complex Pain and Sickness 3
ₒ˛˚̣ (˃ᾓ˂⁎)₎₎⠀Complex Pain and Sickness 4
(﹡︠﹏ु﹡︡)⠀Complex Pain and Sickness 5
₍₍ (ृ˚͈ⅈ∘͈⁎৲ु₎₎՞⠀Complex Pain and Sickness 6
⁽⁽ƈ ͡ (ुŏ̥̥̥̥םŏ̥̥̥̥) ु⠀Complex Pain and Sickness 7
(ृˊ⌄˴⁎৲ु⠀Complex Pain and Sickness 8
⁽⁽ƈ ͡ (ु ˲̥̥̥́ ˱̥̥̥̀) ु⁾⁾⠀Complex Pain and Sickness 9
⁝ƈ ͡ (ुŏ̥̥̥̥םŏ̥̥̥̥) ु⁝⠀Complex Pain and Sickness 10
(╯3╰)⠀Kissing with Lips Aimed to the Right 1
( ˘ ³˘)♥⠀Kissing with Lips Aimed to the Right 2
( ˘ ³˘)❤⠀Kissing with Lips Aimed to the Right 3
（。ˇ ⊖ˇ）⠀Kissing with Lips Aimed to the Right 4
（*＾3＾）⠀Kissing with Lips Aimed to the Right 5
(○´3｀)ﾉ⠀Kissing with Lips Aimed to the Right 6
(☆´3｀)⠀Kissing with Lips Aimed to the Right 7
(ΦзΦ)⠀Kissing with Lips Aimed to the Right 8
|(￣3￣)|⠀Kissing with Lips Aimed to the Right 9
|°з°|⠀Kissing with Lips Aimed to the Right 10
～(^з^)-☆⠀Kissing with Lips Aimed to the Right 11
～(^з^)-♡⠀Kissing with Lips Aimed to the Right 12
ヽ(*´з｀*)ﾉ⠀Kissing with Lips Aimed to the Right 13
(。≖ˇ3ˇ≖｡)⠀Kissing with Lips Aimed to the Right 14
( ˘•૩•˘ ).｡oஇ⠀Kissing with Lips Aimed to the Right 15
⁽˙³˙⁾⠀Kissing with Lips Aimed to the Right 16
(๑•́ ₃ •̀๑)⠀Kissing with Lips Aimed to the Right 17
(๑ơ ₃ ơ)♥⠀Kissing with Lips Aimed to the Right 18
ฅ(♡ơ ₃ơ)ฅ⠀Kissing with Lips Aimed to the Right 19
(๛ ˘ ³˘)۶⠀Kissing with Lips Aimed to the Right 20
(๑•̑з•̑๑)੭ु⁾⁾ ༘⠀Kissing with Lips Aimed to the Right 21
(๑´• ₃ •̀๑)⠀Kissing with Lips Aimed to the Right 22
(*´σЗ`)σ⠀Kissing with Lips Aimed to the Right 23
(o˚̑̑̑̑̑ 3˚̑̑̑̑̑ o)⠀Kissing with Lips Aimed to the Right 24
( ੈჰ ੈ)⠀Kissing with Lips Aimed to the Right 25
( ^з^) y -☆⠀Kissing with Lips Aimed to the Right 26
( ´•₎౩•` )⠀Kissing with Lips Aimed to the Right 27
ᴓᴈᴓ⠀Kissing with Lips Aimed to the Right 28
ꉂ (๑ › ₃ ू‹)₋₃⠀Kissing with Lips Aimed to the Right 29
( ๑ ᴓ ᴈ ᴓ)⠀Kissing with Lips Aimed to the Right 30
|ｮз☆)⠀Kissing with Lips Aimed to the Right 31
(σ･з･)σ⠀Kissing with Lips Aimed to the Right 32
Ⴀ͡კႠ͡⠀Kissing with Lips Aimed to the Right 33
(；◔ิ з◔ิ)⠀Kissing with Lips Aimed to the Right 34
(๑♡3♡๑)⠀Kissing with Lips Aimed to the Right 35
꒰♡⌯́ॢ³⌯̀ॢ꒱⠀Kissing with Lips Aimed to the Right 36
(⁽ؔʽ⁾³⁽ؔʽ⁾)⠀Kissing with Lips Aimed to the Right 37
o┤*｀3´*├o⠀Kissing with Lips Aimed to the Right 38
(〃ﾟ3ﾟ〃)⠀Kissing with Lips Aimed to the Right 39
໒( ∗ ⇀ 3 ↼ ∗ )७⠀Kissing with Lips Aimed to the Right 40
(*´･з･)⠀Kissing with Lips Aimed to the Right 41
(〃бзб`)⠀Kissing with Lips Aimed to the Right 42
（๑・౩・๑）⠀Kissing with Lips Aimed to the Right 43
( ᵅั ᴈ ᵅั<)⠀Kissing with Lips Aimed to the Right 44
( ´з｀)ﾉ⌒☆⠀Kissing with Lips Aimed to the Right 45
(´з｀)⊃～⠀Kissing with Lips Aimed to the Right 46
(･´з`･)ゞ⠀Kissing with Lips Aimed to the Right 47
( *¯ ³¯*)♡⠀Kissing with Lips Aimed to the Right 48
❣ (●❛3❛●)⠀Kissing with Lips Aimed to the Right 49
(๑•з•)))⋆*♡*⋆ฺ=͟͟͞͞=͟͟͞͞⠀Kissing with Lips Aimed to the Right 50
(-ε- )⠀Kissing with Lips Aimed to the Left 1
(TεT)⠀Kissing with Lips Aimed to the Left 2
（＿ε＿）⠀Kissing with Lips Aimed to the Left 3
(｡・//ε//・｡)⠀Kissing with Lips Aimed to the Left 4
(‘ε’)⠀Kissing with Lips Aimed to the Left 5
（＠ーεー＠）⠀Kissing with Lips Aimed to the Left 6
(´ε｀ )♡⠀Kissing with Lips Aimed to the Left 7
(´ε｀*)⠀Kissing with Lips Aimed to the Left 8
（￣ε￣＠）⠀Kissing with Lips Aimed to the Left 9
（○゜ε＾○）⠀Kissing with Lips Aimed to the Left 10
(ΘεΘ<)⠀Kissing with Lips Aimed to the Left 11
(≡ε≡；)⠀Kissing with Lips Aimed to the Left 12
σ(≧ε≦ｏ)⠀Kissing with Lips Aimed to the Left 13
ヾ(❛ε❛“)ʃ⠀Kissing with Lips Aimed to the Left 14
✧˖°ˈ·*ε-(๑˃́ε˂̀๑ )⠀Kissing with Lips Aimed to the Left 15
(・ε・｀)⠀Kissing with Lips Aimed to the Left 16
(｡◕ฺˇε ˇ◕ฺ｡)⠀Kissing with Lips Aimed to the Left 17
(´. ॄ.｀)⠀Kissing with Lips Aimed to the Left 18
(๑ˇεˇ๑)⠀Kissing with Lips Aimed to the Left 19
(○ﾟεﾟ○)⠀Kissing with Lips Aimed to the Left 20
(´ε｀；)⠀Kissing with Lips Aimed to the Left 21
(^ε^)-☆⠀Kissing with Lips Aimed to the Left 22
•́ε•̀٥⠀Kissing with Lips Aimed to the Left 23
˶⚈Ɛ⚈˵⠀Kissing with Lips Aimed to the Left 24
(′• દ •‵)⠀Kissing with Lips Aimed to the Left 25
∵ゞ(´ε｀●) ﾌﾞ!!⠀Kissing with Lips Aimed to the Left 26
( ് દ ് )⠀Kissing with Lips Aimed to the Left 27
ෆ⃛(ˇᵋ ˇෆೄ⠀Kissing with Lips Aimed to the Left 28
(*̩̩̩ᵋ *̩̩̩ )⠀Kissing with Lips Aimed to the Left 29
(๑˙❥˙๑)⠀Kissing with Lips Aimed to the Left 30
(Ō̥̥̥̥̥̥̥ ԑ Ō̥̥̥̥̥̥̥ ૢ)⠀Kissing with Lips Aimed to the Left 31
(๑❛ั ॄ❛ั๑)⠀Kissing with Lips Aimed to the Left 32
┌║ ຈ ε ຈ ║┐⠀Kissing with Lips Aimed to the Left 33
♪(｡◕ฺˇε ˇ◕ฺ｡）♡⠀Kissing with Lips Aimed to the Left 34
ｰ(•̃͡ε•̃͡)∫⠀Kissing with Lips Aimed to the Left 35
₍₍୯ૃᵒ᷇ᵋᵒ᷆૨ુ⠀Kissing with Lips Aimed to the Left 36
(⁎⁍̴̆Ɛ⁍̴̆⁎)⠀Kissing with Lips Aimed to the Left 37
(○ﾟε^○)⠀Kissing with Lips Aimed to the Left 38
( ؔ⚈̫ ε ؔ⚈̫ ⁎)⠀Kissing with Lips Aimed to the Left 39
(≧ε≦)))⠀Kissing with Lips Aimed to the Left 40
(｀ε´#)⠀Kissing with Lips Aimed to the Left 41
★<><<d(,,･ε´-,,)⌒☆⠀Kissing with Lips Aimed to the Left 42
(・ε・`*)⠀Kissing with Lips Aimed to the Left 43
☆⌒ヽ(´ε｀ )⠀Kissing with Lips Aimed to the Left 44
ヾ(´ε｀*)ゝ⠀Kissing with Lips Aimed to the Left 45
ヾ(●ε●)ノ⠀Kissing with Lips Aimed to the Left 46
(´-ε-｀<)⠀Kissing with Lips Aimed to the Left 47
ㄖꏁㄖ⠀Kissing with Lips Aimed to the Left 48
(#^.^#)⠀Miscellaneous Mouths 1
（´・｀ ）♡⠀Miscellaneous Mouths 2
˓( ˶ ❛ ꁞ ❛ ˶ )˒˒⠀Miscellaneous Mouths 3
ϵ( ‘Θ’ )϶⠀Miscellaneous Mouths 4
(╯⊙ ⊱ ⊙╰ )⠀Miscellaneous Mouths 5
(✿ꈍ。 ꈍ✿)⠀Miscellaneous Mouths 6
(‘⁾ʚ’⁾*)ू⠀Miscellaneous Mouths 7
₍ ⁄⁄⁄ ຶᵦ ⁄⁄⁄ ຶ₎⠀Miscellaneous Mouths 8
(ﾉ￣〓￣)ﾉ⠀Miscellaneous Mouths 9
ヾ(￣〓￣ヾ)⠀Miscellaneous Mouths 10
ヾ(´〓｀)ﾉ⠀Miscellaneous Mouths 11
(ʃƪ ˘ ³˘)⠀Clasping Hands 1
(ʃƪ˘ﻬ˘)⠀Clasping Hands 2
(人´З`)⠀Clasping Hands 3
（ʃƪ＾3＾）⠀Clasping Hands 4
(ʃƪΦзΦ)⠀Clasping Hands 5
|人°з°|⠀Clasping Hands 6
(人^з^)-☆⠀Clasping Hands 7
(ʃƪ〃ﾟ3ﾟ〃)⠀Clasping Hands 8
（ʃƪ๑・౩・๑）⠀Clasping Hands 9
(´ε｀ ʃƪ)♡⠀Clasping Hands 10
（￣ε￣ʃƪ）⠀Clasping Hands 11
(ΘεΘʃƪ)⠀Clasping Hands 12
ლ(´◉❥◉｀ლ)⠀Grabby Hands 1
ლ(|||⌒εー|||)ლ⠀Grabby Hands 2
ლ(´ ❥ `ლ)⠀Grabby Hands 3
(~￣³￣)~⠀Grabby Hands 4
(づ￣ ³￣)づ⠀Grabby Hands 5
(ɔˆ ³(ˆ⌣ˆc)⠀One Person Kissing Another 1
(っ˘з(˘⌣˘ )⠀One Person Kissing Another 2
( ๑ ᴖ ᴈ ᴖ)ᴖ ᴑ ᴖ๑)❣⠀One Person Kissing Another 3
(っ˘зʕ•̫͡•ʔ⠀One Person Kissing Another 4
(◦˘ З(◦’ںˉ◦)♡⠀One Person Kissing Another 5
(ღ ･ิ◡･ิ)ε ･ิ ღ)⠀One Person Kissing Another 6
( ᵕ̤ɜ)ᵕ̤ૢᴗᵕ̤ૢ )⠀One Person Kissing Another 7
(-^3(//O//)<><<”⠀One Person Kissing Another 8
(´∀｀*)ε｀　)⠀One Person Kissing Another 9
(*^3(＃∀＃)⠀One Person Kissing Another 10
(*^3(*^o^*)⠀One Person Kissing Another 11
（^_^ ；)ε￣)⠀One Person Kissing Another 12
(*￣(^ *)⠀One Person Kissing Another 13
(((*☣ω☣(ε◕* )))⠀One Person Kissing Another 14
♡⑅⃝◌꒰ ˘̤ з꒰ ˃̶̤⌄˂̶̤ ` ू꒱◌⑅⃝♡⠀One Person Kissing Another 15
ｰ(･ω´･<<<))))　　ヽ(ﾟεﾟヽ)))))⠀One Person Kissing Another 16
☆⌒ヽ∞*´Зﾟ◆)∞*´зﾟ◆)ﾉ⌒★⠀One Person Kissing Another 17
ﾟ☆+.ﾟ☆+(〃´3(･艸･ 〃)+.☆ﾟ+.☆⠀One Person Kissing Another 18
((((@ﾉ´3｀)ﾉ　　･･･Σ(ﾟдﾟ<<ﾉ⠀One Person Kissing Another 19
( c//”-}{-*x)⠀Two People Kissing Each Other 1
(*◑З◑)爻(◐ε◐*)⠀Two People Kissing Each Other 2
(*-(　　)⠀Two People Kissing Each Other 3
˓˓ ˋ̩} ͢ {ˊ̩ ˒˒⠀Two People Kissing Each Other 4
(●´з(ε｀○)⠀Two People Kissing Each Other 5
❥( ◜3‾)(‾⊱◝ )⠀Two People Kissing Each Other 6
(●’3)♡(ε`●)⠀Two People Kissing Each Other 7
ღ꒡ ᴈ꒡)♡⃛(꒡ε ꒡ღ⠀Two People Kissing Each Other 8
│〇´3｀|人|´ε｀●|⠀Two People Kissing Each Other 9
(●´3`☆★´ε`●)⠀Two People Kissing Each Other 10
<><<<<<<((((*ﾟ<<<< <><<ﾟ*)))<><<<<<<⠀Two People Kissing Each Other 11
(ღ꒡ ᵌ꒡)⋆﹡♡⃛*⁎⋆(꒡ᵋ ꒡ღ)⠀Two People Kissing Each Other 12
“8-( ●｀ε´●)爻(●｀ε´● )-8”⠀Two People Kissing Each Other 13
～～～～～(／￣3)／ ＼(ε￣＼）～～～～～⠀Two People Kissing Each Other 14
━━━⊂´⌒つ ﾟзﾟ)ﾞ<☆<（ﾟεﾟ⊂⌒｀つ━━⠀Two People Kissing Each Other 15
⁽˙³˙⁾◟(๑•́ ₃ •̀๑)◞⁽˙³˙⁾⠀Three or More People Kissing 1
(Ɔ˘з˘)(ꈍヮꈍ)˘ε˘ C)⠀Three or More People Kissing 2
애❣⃛ღсμтёღ♡(˘ᵋ ˘ )⠀Words 1
(っ˘зʕ•̫͡•ʔcнϋෆ*⠀Words 2
(/ ᵒ̴̵̶̷౩ᵒ̴̵̶̷ )/ ᵏᴵˢઽ ❤⃛⠀Words 3
(*-(　　) cнϋ❤⠀Words 4
.+ﾟ*(●´ε`人)СНЦ｡:ﾟ+⠀Words 5
(^_^ ；)ε￣)ＣＨＵ★⠀Words 6
(*ﾟэﾟ)chu♪⠀Words 7
ιоνё(●´Å`)ε`○)снц♪⠀Words 8
˪৹⌵ೕෆ⃛(˃͈ દ ˂͈ )⠀Words 9
⁽͑˙˚̌ ᵌ˚̌˙⁾̉⁼ᵌ ᵇᵘᵎ⠀Words 10
(◦˘ З(◦’ںˉ◦)cнϋ♡⠀Words 11
L(*OεV*)E⠀Words 12
Ƭ ɧ ձ ƞ Ƙ ʂ❤ (◦˘ З(◦’ںˉ◦) Ȼ ɧ ư ♡⠀Words 13
Gооd Йi>h<(´ε｀*)ιον∈ Υου⠀Words 14
ﾟ･*:.｡. ☆κｉss мё(人uзu*)ρｌёдsё☆.｡.:*･ﾟ⠀Words 15
.+ﾟ*((人′3`))｡o(chu★)｡:ﾟ+⠀Words 16
(<<<:´<3<`:<<<)ﾉＣＨЦ*:ﾟ･☆*:ﾟ･☆*:ﾟ･☆⠀Words 17
((*´３｀)｡o○ﾟ･*:.｡. ☆κｉss мё☆ﾟ･*:.｡.⠀Words 18
( ⋆•ิ ᴈ-ิ(ᵕ❥ ᵕ⁎ ॢ)⠀Complex 1
( ु ॕ ӟ ॕ)ु⠀Complex 2
(ु*´З`)ू❣⠀Complex 3
*ଘ( ॢᵕ꒶̮ᵕ(꒡ᵋ ꒡ღ)⠀Complex 4
*ଘ( ॢᵕ꒶̮ᵕ(꒡ᵋ ꒡ღ)zZ‥⠀Complex 5
(。´✷ฺЗ✷ฺ)・<゛.:’<、⠀Complex 6
(๑ᵕॢ૩ᵕॢ)*౨˚ൗ⠀Complex 7
♡´͈ॢ ᵌˋ͈ॢꉧ´͈ॢᵋ ˋ͈ॢ♡⠀Complex 8
<<<<ब₍₍( ˃̗εू˂ )₎₎<<<<ब⠀Complex 9
(⌯˘̤ ॢᵌ ू˘̤)യෆ̈⠀Complex 10
⁽⁽(*꒪ั❥꒪ั*)⁾⁾⠀Complex 11
୧( ́⁰⃙⃘Ԑ⁰⃙ఁ̀ )୨⠀Complex 12
(ლ ۞ิ ჴ ۞ิ)ლ⠀Complex 13
(๑ᵕॢ₃ᵕू๑)⠀Complex 14
( ु ॕ ӟ ॕ)ुƾｭෆ⠀Complex 15
✧.*(⌯ⅉॕੰૈՅⅉॕੰૈ)⠀Complex 16
⁝(ृ°ۿ°ꐦ ृ　)ु⁝⠀Complex 17
(ෆ❛ัᵌ❛ัෆ)°⠀Complex 18
(●◦⃝⃚⃙⃘⃙⃚⃙⃚⃙⃘⃑з◦⃝⃚⃙⃘⃙⃐)⠀Complex 19
༼(*꒪ั❥꒪ั*༽༽⠀Complex 20
☻ू (ѳॅ ॄ ѳॆ ू )⠀Complex 21
(๑ʻัદʻั๑)⠀Complex 22
(՟ິͫઘ ՟ິͫ)⠀Complex 23
(ෆ❛ั ु³❛ัʕ•̫͡•ིʔྀ*✲ﾟ*｡⋆❤⃛ೄ⠀Complex 24
(*´艸`*)⠀Stifling Laughter 1
(●´艸`)⠀Stifling Laughter 2
( ´艸｀)⠀Stifling Laughter 3
(｡ <><<艸<<<<)⠀Stifling Laughter 4
(*・艸・)⠀Stifling Laughter 5
(*≧艸≦)⠀Stifling Laughter 6
(* ˚᷄ 艸 ˚᷅ *)⠀Stifling Laughter 7
(♡´艸`)⠀Stifling Laughter 8
(Ŏ艸Ŏ)⠀Stifling Laughter 9
(亝艸亝)⠀Stifling Laughter 10
(✿˘艸˘✿)⠀Stifling Laughter 11
(灬º 艸º灬)⠀Stifling Laughter 12
( ^ิ艸^ิﾟ)⠀Stifling Laughter 13
(ಡ艸ಡ)⠀Stifling Laughter 14
(｡ˇ艸ˇ)⠀Stifling Laughter 15
(*^ิ艸^ิ*)⠀Stifling Laughter 16
(o´艸`)⠀Stifling Laughter 17
( ❝ົཽ艸❝ົཽ)⠀Stifling Laughter 18
(❝ົཽ艸❝ົཽ )⠀Stifling Laughter 19
(≧艸≦*)⠀Stifling Laughter 20
(*<><<艸<<<<)⠀Stifling Laughter 21
((●≧艸≦)⠀Stifling Laughter 22
(´艸｀〃)⠀Stifling Laughter 23
(｡￫ˇ艸￩)⠀Stifling Laughter 24
( Ŏ艸Ŏ)(Ŏ艸Ŏ )⠀Stifling Laughter 25
(○v艸v*)⠀Stifling Laughter 26
(*´艸)(艸｀*)⠀Stifling Laughter 27
(○･艸)(艸･●)⠀Stifling Laughter 28
( 〃´艸｀)⠀Stifling Laughter 29
(*Q艸Q*）⠀Stifling Laughter 30
(o<><<艸<<<<)⠀Stifling Laughter 31
(+･艸･+)(+･艸･+)⠀Stifling Laughter 32
(*´艸｀)⠀Stifling Laughter 33
(๑ơ艸ơ๑)♡ฺ⠀Stifling Laughter 34
☆⌒(*’艸＾*)⠀Stifling Laughter 35
(。ｕ艸ｕ。)⠀Stifling Laughter 36
(*´ 艸`)(´艸 `*)⠀Stifling Laughter 37
(*、｡艸｡)(ﾟ艸ﾟ`*)⠀Stifling Laughter 38
(* ´<><<艸<<<<)゛⠀Stifling Laughter 39
(☆Θ艸Θ)⠀Stifling Laughter 40
（○´艸｀）⠀Stifling Laughter 41
((*´艸｀*))⠀Stifling Laughter 42
｡ﾟ(TヮT)ﾟ｡⠀Tears 1
。+゜(*´<><<艸<<<<｀*)。+゜⠀Tears 2
｡:+((*′艸`))+:｡⠀Tears 3
(○v艸v*).+ﾟ⠀Tears 4
・:*:・(*´艸｀*)・:*:・⠀Tears 5
゜+.(。´<><<艸<<<<)*.☆⠀Tears 6
∗˚(* ˃̤൬˂̤ *)˚∗⠀Tears 7
(*≧▽≦)ﾉｼ))⠀Waving arms 1
(ノ＞▽＜。)ノ⠀Waving arms 2
(੭ु˙꒳​˙)੭ु⁾⁾⠀Waving arms 3
꒰*⑅˃̶͈ ৺˂̶͈⑅꒱੭ु⁾⁾·°⠀Waving arms 4
((ꉺꈊꉺ)ꀢ༣⠀Waving arms 5
(੭ु ‾᷄ᗣ‾᷅ )੭ु⁾⁾⠀Waving arms 6
(੭ु´͈ ᐜ `͈)੭ु⁾⁾⠀Waving arms 7
(๑‾᷅⚰‾᷄๑)੭ु⁾⁾˞͛ ༘ؓ ︠³⠀Waving arms 8
౧(*മ് ധമ്)੭ु⁾⁾⠀Waving arms 9
(੭ु ´͈꒳​`͈)੭ु⁾⁾⠀Waving arms 10
(੭ु˙꒳˙)੭ु⁾⁾*✭⠀Waving arms 11
(੭ ˃̣̣̥ ω˂̣̣̥)੭ु⁾⁾⠀Waving arms 12
(˵¯̴͒ꇴ¯̴͒˵)⠀Big Wide Open Mouths 1
✧(σ๑˃̶̀ꇴ˂̶́)σ⠀Big Wide Open Mouths 2
٩̋(๑˃́ꇴ˂̀๑)⠀Big Wide Open Mouths 3
(ᗒᗜᗕ)՛̵̖⠀Big Wide Open Mouths 4
(ꐦ ´͈ ᗨ `͈ )⠀Big Wide Open Mouths 5
(◍˃̶ᗜ˂̶◍)ﾉ”⠀Big Wide Open Mouths 6
✧ꉂ(σ▰˃̶̀ꇴ˂̶́)σ✧⠀Big Wide Open Mouths 7
ꉂ(σ▰˃̶̀ꇴ˂̶́)σ⠀Big Wide Open Mouths 8
(●❛⃘ᗜ❛⃘●)੭ु⁾⁾⠀Big Wide Open Mouths 9
-(｡ﾉᗨ<<<<｡)ﾉ⠀Big Wide Open Mouths 10
°₊·ˈ∗(( ॣ<><<̶᷇ᗢ<<<<̶᷆ ॣ))∗ˈ‧⠀Big Wide Open Mouths 11
(੭ु˶˭̵̴⃙⃚⃘᷄ᗢ˭̴̵⃙⃚⃘᷅˶)੭ु⁾⁾~⠀Big Wide Open Mouths 12
ˉ̶̡̭̭ ( ´͈ ᗨ `͈ ) ˉ̶̡̭̭⠀Big Wide Open Mouths 13
(๐॔˃̶ᗜ˂̶๐॓)⠀Big Wide Open Mouths 14
(๑❛ꇳ❛๑)⠀Big Wide Open Mouths 15
ꉂ (′ ॢꇴ ॢ‵๑))⠀Big Wide Open Mouths 16
ꉂ ૮( ᵒ̌ૢꇴᵒ̌ૢ )ა｡*ﾟ✧⠀Big Wide Open Mouths 17
✧(˚ੌɄ̮˚ੌ◍)⠀Big Wide Open Mouths 18
(๑˃́ꇴ˂̀๑)⠀Big Wide Open Mouths 19
ꋧ(⋆ʾꇶʿ⋆)⠀Big Wide Open Mouths 20
(๑ ꒪̇ꌂ̇꒪̇๑)⠀Big Wide Open Mouths 21
ꉂ ꊚ(ꈍꇴꆧ )⠀Big Wide Open Mouths 22
ꉂ ฅ૮( ๑’ꇴ’๑)აฅ｡*ﾟ✧⠀Big Wide Open Mouths 23
(⌯꒪͒ ૢ∀ ૢ꒪͒) ੭ੇ⠀Little Hands 1
(⌯˃̶᷄ ᴗ̂ ॣ˂̶᷄⌯ั)⠀Little Hands 2
(˃̴̀ᄇॢ˂̴́ ∗)⠀Little Hands 3
ᵵ (ૢ˃ꌂ˂⁎)Շ^⠀Little Hands 4
✬̴⃛꒰⁍̴ꈊ ॢ⁍̴⌯꒱⠀Little Hands 5
(˃ॢ੪˂ू॓๑)‾̞̭̭⠀Little Hands 6
⁽⁽꒰๑•‧̮ૣ•ૣ๑꒱⁾⁾⠀Little Hands 7
(๑˃̶᷇⺫ॢ˂̶᷆๑)⠀Little Hands 8
(⌯꒪͒ ૢ◞◟ ૢ꒪͒)⠀Little Hands 9
ꉂ (˃̶᷄‧̫ॢ ˂̶᷅๑ )⠀Little Hands 10
ꉂ (ᵔ̴̶̤᷄ꇴ ॣᵔ̴̶̤᷅⌯))л̵ʱªʱª⁎*.＊⠀Words and Sounds 1
Σ(꒪ॢ∀꒪<)՞л̵ʱªʱª⠀Words and Sounds 2
ꉂ ꀞꀞꀞ(ᕑᗢूᓫ∗)˒˒⠀Words and Sounds 3
ꉂ (๑¯ਊ¯)σ л̵ʱªʱªʱª⠀Words and Sounds 4
ʱªʱªʱª (ᕑᗢूᓫ∗)⠀Words and Sounds 5
(๑ॢ˃̶͈̀ ꇴ ˂̶͈́๑ॢ) л̵ʱªʱªʱª⠀Words and Sounds 6
ｰΣ(꒪ॢ∀꒪<)՞л̵ʱªʱª⠀Words and Sounds 7
(˃̴̀ᄇॢ˂̴́ ∗)੭᷅ʊʊ⠀Words and Sounds 8
(‾͈̑ ◟  ॢ‾͈̑๑)ഽ̵ᵘഽ̵ᵘ४꒰ ꒱⠀Words and Sounds 9
(๑ ˃̵͈́∀˂̵͈̀ )ʊʊ⠀Words and Sounds 10
ꉂ (ᵔ̴̶̤᷄ꇴ ॣᵔ̴̶̤᷅⌯))л̵ʱªʱª⁎*.＊⠀Words and Sounds 11
ꉂ (๑¯ਊ¯)σ⠀ਊ Style Mouths 1
(灬㋭ ਊ ㋲灬)⠀ਊ Style Mouths 2
(<うਊ ՞)⠀ਊ Style Mouths 3
( ՞ਊ ՞)☞⠀ਊ Style Mouths 4
｡ﾟ(ﾟ＾ਊ＾ํ )ﾟ｡⠀ਊ Style Mouths 5
(☞ ՞ਊ ՞)☞⠀ਊ Style Mouths 6
( ՞ਊ՞)⠀ਊ Style Mouths 7
(⁙ູ՟ິͫ◞̴ਊ◟̴ູ՟ິͫ⁙ູ)⠀ਊ Style Mouths 8
(,, ՞ਊ ՞)=☞)՞ਊ ՞)⠀ਊ Style Mouths 9
(΄◞ิਊ◟ิ‵)⠀ਊ Style Mouths 10
(खਉख)⠀ਊ Style Mouths 11
v(＜°＞ਊ ＜°＞)v⠀ਊ Style Mouths 12
( ╹ਊ╹)⠀ਊ Style Mouths 13
(⁙ู꒪ู︠͒◞̴ਊ◟̴ู꒪︡͒⁙ู)⠀ਊ Style Mouths 14
(((< ఠ ਉ ఠ))⠀ਊ Style Mouths 15
┌( •́ ਊ •̀ )┐⠀ਊ Style Mouths 16
*･゜ﾟ･*:.｡.｡.:*･’(´◜◞ਊ◟◝｀)’･*:.｡.｡.:*･゜ﾟ･*⠀ਊ Style Mouths 17
（　´∀｀）⠀Simple or Miscellaneous Laughter 1
（・∀・）⠀Simple or Miscellaneous Laughter 2
(；-◞౪◟-)⠀Simple or Miscellaneous Laughter 3
（＾ｖ＾）⠀Simple or Miscellaneous Laughter 4
（＞ｙ＜）⠀Simple or Miscellaneous Laughter 5
（⌒▽⌒）⠀Simple or Miscellaneous Laughter 6
(◎ヮ◎)⠀Simple or Miscellaneous Laughter 7
(^ワ^＝)⠀Simple or Miscellaneous Laughter 8
(´つヮ⊂)⠀Simple or Miscellaneous Laughter 9
(๑´ㅂ`๑)⠀Simple or Miscellaneous Laughter 10
(｡￫∀￩｡)⠀Simple or Miscellaneous Laughter 11
(◍´͈ꈊ`͈◍)⠀Simple or Miscellaneous Laughter 12
☚(ﾟヮﾟ☚)⠀Simple or Miscellaneous Laughter 13
（＞Ц＜●）⠀Simple or Miscellaneous Laughter 14
(●＾曲＾●)⠀Simple or Miscellaneous Laughter 15
(*￣､ゝ￣)⠀Simple or Miscellaneous Laughter 16
“ψ(｀∇´)ψ⠀Simple or Miscellaneous Laughter 17
ಡ ੴಡ⠀Simple or Miscellaneous Laughter 18
( ਊдਊ)⠀Simple or Miscellaneous Laughter 19
(^ц^ )⠀Simple or Miscellaneous Laughter 20
(*˒ ̖˰̊ ̗˓*)⠀Simple or Miscellaneous Laughter 21
Σ (੭ु ຶਊ ຶ)੭ु⁾⁾⠀Complex Forms of Laughter 1
ꋧ(⁎ˊ̭ સˆ̀)◞₎̵₎⠀Complex Forms of Laughter 2
∗˚೫˳(●ᴖ͙̏ᴗॢᴖ͙̋●)˳೫˚∗⠀Complex Forms of Laughter 3
⸌̷̻ ( ᷇๑ॢ˃̶͈̀ ꇴ ˂̶͈́๑ॢ) ⸌̷̻⠀Complex Forms of Laughter 4
(੭ु റ̆ ˒̫̮ റ̥)੭ु⁾⁾⠀Complex Forms of Laughter 5
ꉂ ꋧ(⁎ˊ̭ સˆ̀)◞₎̵₎⠀Complex Forms of Laughter 6
ृ₍⁺ꇴ⁺᷅ ृ₎₎ ՞⠀Complex Forms of Laughter 7
ꆭ㐃(͛꒪͒ধृ꒪͒ॢ )͛↝꒱⠀Complex Forms of Laughter 8
ʕ̡̢̡̡̢̡̡̢♡ᵒ̴̷͈艸ᵒ̴̷͈॰ʔ̢̡̢̢̡̢̢̡̢✧⠀Complex Forms of Laughter 9
(●♡∀♡)⠀Love Eyes 1
(｡♥‿♥｡)⠀Love Eyes 2
(♥ω♥ ) ~♪⠀Love Eyes 3
(♥ω♥*)⠀Love Eyes 4
(✿ ♥‿♥)⠀Love Eyes 5
✿♥‿♥✿⠀Love Eyes 6
乂❤‿❤乂⠀Love Eyes 7
٩(♡ε♡ )۶⠀Love Eyes 8
ლζ*♡ε♡*ζლ⠀Love Eyes 9
⊂（♡⌂♡）⊃⠀Love Eyes 10
(๑♡3♡๑)⠀Love Eyes 11
(๑♡⌓♡๑)⠀Love Eyes 12
♱♡‿♡♰⠀Love Eyes 13
⊆♥_㇁♥⊇⠀Love Eyes 14
(●♡∀♡))ヾ☆*。⠀Love Eyes 15
໒( ♥ ◡ ♥ )७⠀Love Eyes 16
༼♥ل͜♥༽⠀Love Eyes 17
(灬♥ω♥灬)⠀Love Eyes 18
(‘∀’●)♡⠀Left Love 1
(´∀｀)♡⠀Left Love 2
（*´▽｀*）⠀Left Love 3
（´・｀ ）♡⠀Left Love 4
（´ω｀♡%）⠀Left Love 5
♥(ˆ⌣ˆԅ)⠀Left Love 6
꒰˘̩̩̩⌣˘̩̩̩๑꒱♡⠀Left Love 7
ლ(́◉◞౪◟◉‵ლ)⠀Left Love 8
⸌̷̻( ᷇ॢ〰ॢ ᷆◍)⸌̷̻♡⃛⠀Left Love 9
₍՞◌′ᵕ‵ू◌₎♡⠀Left Love 10
♡ฅ(ᐤˊ꒳ฅˋᐤ♪)⠀Left Love 11
ʚ♡⃛ɞ(ू•ᴗ•ू❁)⠀Left Love 12
❣⃛(❛ั◡˜๑)⠀Left Love 13
( ˭̵̵̵̵͈́◡ु͂˭̵̵̵͈̀ )ˉ̞̭♡⠀Left Love 14
♡(ŐωŐ人)⠀Left Love 15
❤⃛ヾ(๑❛ ▿ ◠๑ )⠀Left Love 16
（*’∀’人）♥⠀Left Love 17
(°◡°♡).:｡⠀Left Love 18
ʸ(➜◡ु⚈᷉)♡⃛⠀Left Love 19
ˉ̞̭(′͈∨‵͈♡)˄̻ ̊⠀Left Love 20
◟(◔ั₀◔ั )◞ ༘♡⠀Left Love 21
φ(ﾟ ωﾟ//）♡⠀Left Love 22
ʸ(ᴖ́◡ु⚈᷉)♡⃛⠀Left Love 23
ꉂ (′̤ॢ∀ ू‵̤๑))ˉ̞̭♡⠀Left Love 24
♡♡+.ﾟ(￫ε￩*)ﾟ+.ﾟ⠀Left Love 25
꒰✪ૢꇵ✪ૢ꒱ෆ⃛⠀Left Love 26
(●´□`)♡⠀Right Love 1
(｡･ω･｡)ﾉ♡⠀Right Love 2
(｡’▽’｡)♡⠀Right Love 3
（●´∀｀）ノ♡⠀Right Love 4
₍₍ ( ๑॔˃̶◡ ˂̶๑॓)◞♡⠀Right Love 5
(๑・ω-)～♥”⠀Right Love 6
(๑°꒵°๑)･*♡⠀Right Love 7
～(^з^)-♡⠀Right Love 8
(๑ˊ͈ ॢꇴ ˋ͈)〜♡॰ॱ⠀Right Love 9
(ෆ ͒•∘̬• ͒)◞⠀Right Love 10
♡(㋭ ਊ ㋲)♡⠀Right Love 11
( •ॢ◡-ॢ)-♡⠀Right Love 12
(●’ᴗ’σ)σணღ*⠀Right Love 13
(♡´͈༝`͈)ฅ˒˒⠀Right Love 14
(•‾⌣‾•)و ̑̑♡⠀Right Love 15
( ෆຶдෆຶ)⠀Right Love 16
(⁎⁍̴̛͂▿⁍̴̛͂⁎)*✲ﾟ*｡⋆♡ོ⠀Right Love 17
(*´o`*)ʖˋʖˋʖˋ～♡⠀Right Love 18
ღゝ◡╹)ノ♡⠀Right Love 19
⌓⌓⌕(˃̴◡ुؔ՞ઁ)♡⃛⠀Right Love 20
♡✧( ु•⌄• )⠀Right Love 21
(∗ᵒ̶̶̷̀ω˂̶́∗)੭₎₎̊₊♡⠀Right Love 22
(●මᴗමσ)σணღ*⠀Right Love 23
(๑╹ڡ╹)╭ ～ ♡⠀Right Love 24
(๑ Ỡ ◡͐ Ỡ๑)ﾉ♡⠀Right Love 25
(♡ ὅ ◡ ὅ )ʃ♡⠀Right Love 26
⁽⁽ପ( •ु﹃ •ु)​.⑅*♡⠀Right Love 27
꒰ ︠ु௰•꒱ु♡⠀Right Love 28
(⁎⁍̴̀﹃ ⁍̴́⁎)♡⠀Right Love 29
(๑ゝᴗම๑) ৷ਕკ~ෆ⠀Right Love 30
(⋈◍＞◡＜◍)。✧♡⠀Right Love 31
ε=(｡♡ˇд ˇ♡｡）⠀Right Love 32
(◍•ᴗ•◍)❤⠀Forward Love 1
(∩˃o˂∩)♡⠀Forward Love 2
♡(.◜ω◝.)♡⠀Forward Love 3
♡〜٩(^▿^)۶〜♡⠀Forward Love 4
♡´･ᴗ･`♡⠀Forward Love 5
♡＾▽＾♡⠀Forward Love 6
♥(✿ฺ´∀`✿ฺ)ﾉ⠀Forward Love 7
♥╣[-_-]╠♥⠀Forward Love 8
♡ლ(-༗‿༗-)ლ♡⠀Forward Love 9
(｡・‧̫・｡).*＊♡⠀Forward Love 10
(◍•ڡ•◍)❤⠀Forward Love 11
-ω(´•ω•｀)♡⠀Forward Love 12
(ෆˊ͈ ु꒳ ूˋ͈ෆ)⠀Forward Love 13
(♡´౪`♡)⠀Forward Love 14
ෆ╹ .̮ ╹ෆ⠀Forward Love 15
( ◜◒◝ )♡⠀Forward Love 16
♡〜ლ(๑癶ᴗ癶๑)ლ〜♡⠀Forward Love 17
(♡´❍`♡)*✧ ✰ ｡*⠀Forward Love 18
(´∩｡• ᵕ •｡∩`) ♡⠀Forward Love 19
( ˊᵕˋ )♡.°⑅⠀Forward Love 20
(♡ <><<ω<<<< ♡)⠀Forward Love 21
( ๑ ❛ ڡ ❛ ๑ )❤⠀Forward Love 22
（♥￫ｏ￩♥）⠀Forward Love 23
(◍•ᴗ•◍)♡ ✧*。⠀Forward Love 24
（〃・ω・〃）⠀Shy Love 1
(*°∀°)=3⠀Shy Love 2
♥（ﾉ´∀`）⠀Shy Love 3
(♡´艸`)⠀Shy Love 4
(´,,•ω•,,)♡⠀Shy Love 5
❤\(⸝⸝⸝°⁻̫° ⸝⸝⸝)⠀Shy Love 6
❣╰(⸝⸝⸝´꒳`⸝⸝⸝)╯❣⠀Shy Love 7
(⸝⸝⍢⸝⸝) ෆ⠀Shy Love 8
(⺣◡⺣)♡*⠀Shy Love 9
(๑´ლ`๑)ﾌﾌ♡⠀Shy Love 10
( ̧⸝⸝⍢⸝⸝)ི Շᐱෆ⠀Shy Love 11
( ⌯◞◟⌯)♡⠀Shy Love 12
♡(｡￫ˇ艸￩)⠀Shy Love 13
(灬ºωº灬)♡⠀Shy Love 14
꒰⁎˃ ॢꇴ ॢ˂⁎꒱➴ෆ⃛⠀Excited Love 1
ヽ(o♡o)/⠀Excited Love 2
♡✧。 (⋈◍＞◡＜◍)。✧♡⠀Excited Love 3
٩(ó｡ò۶ ♡)))♬⠀Excited Love 4
٩(*❛⊰❛)ʓਡ～❤⠀Excited Love 5
٩(๑ơలơ)۶♡⠀Excited Love 6
(੭ु ›ω‹ )੭ु⁾⁾♡⠀Excited Love 7
٩(๑∂▿∂๑)۶♡⠀Excited Love 8
\(-ㅂ-)/ ♥ ♥ ♥⠀Excited Love 9
ヾ(◍’౪`◍)ﾉﾞ♡⠀Excited Love 10
ヽ(愛´∀｀愛)ノ⠀Excited Love 11
♡٩(๑ö⊿ö๑)۶♡⠀Excited Love 12
٩(*ゝڡ◕๑)۶♥⠀Excited Love 13
♡〜٩( ╹▿╹ )۶〜♡⠀Excited Love 14
╰(✿´⌣`✿)╯♡⠀Excited Love 15
(´ ▽｀).。ｏ♡⠀Thinking about Love 1
( ´͈ ॢꇴ `͈ॢ)･*♡⠀Thinking about Love 2
(/∇＼*)｡o○♡⠀Thinking about Love 3
(´▽`ʃƪ)♡⠀Thinking about Love 4
(◞ꈍ∇ꈍ)◞⋆**✚⃞⠀Thinking about Love 5
(ღ˘⌣˘ღ)⠀Thinking about Love 6
（人´∀`*）⠀Thinking about Love 7
♡o｡.(✿ฺ｡ ✿ฺ)⠀Thinking about Love 8
♡o｡(๑๏‿ฺ๏๑)｡o♡⠀Thinking about Love 9
♥～(‘▽^人)⠀Thinking about Love 10
꒰♡ˊ͈ ु꒳ ूˋ͈꒱.⑅*♡⠀Thinking about Love 11
*ଯ( ॢᵕ꒶̮ᵕ)ॢഒ*♡⠀Thinking about Love 12
꒰⑅ᵕ༚ᵕ꒱˖♡⠀Thinking about Love 13
♡˖꒰ᵕ༚ᵕ⑅꒱⠀Thinking about Love 14
( ᵒ̴̶̷̤̀ुωᵒ̴̶̷̤́ू )❤”⠀Thinking about Love 15
(❃•̤ॢᗜ•̤ॢ)✲*｡♡⠀Thinking about Love 16
(๑॔˃̶ॢ◟◞ ˂̶ॢ๑॓)♡⠀Thinking about Love 17
(‾̴̴͡͡▿•‾̴̴͡͡ʃƪ)⠀Thinking about Love 18
( ´͈ ૢᐜ `͈ૢ)･*♡੭ੇ৸♡੭ੇ৸♡⠀Thinking about Love 19
꒰◍•̤ु௰•̤ु꒱* ∗◌+*♡⠀Thinking about Love 20
˚‧*♡ॢ˃̶̤̀◡˂̶̤́♡ॢ*‧˚⠀Thinking about Love 21
´͈ ᵕ `͈ ♡°◌̊⠀Thinking about Love 22
(*´ ˘ `*).｡oO ( ♡ )⠀Thinking about Love 23
(人 •͈ᴗ•͈)⠀Thinking about Love 24
(*˘︶˘*).｡.:*♡⠀Thinking about Love 25
(*ˊૢᵕˋૢ*)⠀Thinking about Love 26
❤⃛῍̻̩✧(´͈ ૢᐜ `͈ૢ)⠀Thinking about Love 27
❤︎⁄⁄꒰* ॢꈍ◡ꈍ ॢ꒱.*˚‧⠀Thinking about Love 28
♡( ૢ⁼̴̤̆ ꇴ ⁼̴̤̆ ૢ)~ෆ♡⠀Thinking about Love 29
°₊·ˈ∗♡( ˃̶᷇ ‧̫ ˂̶᷆ )♡∗ˈ‧₊°⠀Thinking about Love 30
°₊·ˈ∗♡( ˃̶᷇ ‧̫ ˂̶᷆ )♡∗ˈ‧₊°⠀Thinking about Love 31
ღ˘◡˘ற♡.｡oO⠀Thinking about Love 32
( ˘͈ ᵕ ˘͈♡)˚๐*˟ ♡⠀Thinking about Love 33
( ∩ˇωˇ∩)♡⠀Thinking about Love 34
|๑˃ ॢ‧̫˂ॢ๑ ).*˚‧♡⠀Thinking about Love 35
˞♡ฅ(ᐤˊ꒳ฅˋᐤ♪)⠀Thinking about Love 36
( ื▿ ืʃƪ)⠀Thinking about Love 37
(o´〰`o)♡*✲ﾟ*｡⠀Thinking about Love 38
(´⌣`ʃƪ)⠀Thinking about Love 39
(人*´∀｀)+ﾟ:｡*ﾟ+⠀Thinking about Love 40
(人´ω｀*)♡⠀Thinking about Love 41
❣‧✩͓̊(ᵕ̴̤‧̮ ॣᵕ̴̤∗)ɞ₎₎☽˟⠀Thinking about Love 42
(人´∀`)⠀Thinking about Love 43
（人*´∀｀）⠀Thinking about Love 44
ლ(´◉❥◉｀ლ)⠀Kissing Lips 1
( ˘ ³˘)♥⠀Kissing Lips 2
( ˘ ³˘)❤⠀Kissing Lips 3
（。ˇ ⊖ˇ）♡⠀Kissing Lips 4
（*＾3＾）/～♡⠀Kissing Lips 5
(｡・//ε//・｡)⠀Kissing Lips 6
(´ε｀ )♡⠀Kissing Lips 7
(ʃƪ ˘ ³˘)⠀Kissing Lips 8
(ʃƪ˘ﻬ˘)⠀Kissing Lips 9
(づ￣ ³￣)づ⠀Kissing Lips 10
♡(˃͈ દ ˂͈ ༶ )⠀Kissing Lips 11
٩꒰ ˘ ³˘꒱۶~♡⠀Kissing Lips 12
ƪ(♥ﻬ♥)ʃ⠀Kissing Lips 13
ლ(|||⌒εー|||)ლ⠀Kissing Lips 14
♡ლζ(♛ε♛*ζლ♡⠀Kissing Lips 15
†=”Ⴛ̸ ♡(˃͈ દ ˂͈ ༶ )⠀Kissing Lips 16
(⌯˘̤ ॢᵌ ू˘̤)യෆ̈⠀Kissing Lips 17
(๑ơ ₃ ơ)♥⠀Kissing Lips 18
ฅ(♡ơ ₃ơ)ฅ⠀Kissing Lips 19
(/ ᵒ̴̵̶̷౩ᵒ̴̵̶̷ )/ ᵏᴵˢઽ ❤⃛⠀Kissing Lips 20
৲( ᵒ ૩ᵕ )৴♡*৹⠀Kissing Lips 21
(ˊσ̴̶̷̤ ₋̮̑ σ̴̶̷̤ˋ)₊ෆ⃛⁺˚⠀Kissing Lips 22
ෆ⃛(ˇᵋ ˇෆೄ⠀Kissing Lips 23
꒰♡⌯́ॢ³⌯̀ॢ꒱⠀Kissing Lips 24
♪(｡◕ฺˇε ˇ◕ฺ｡）♡⠀Kissing Lips 25
( *¯ ³¯*)♡⠀Kissing Lips 26
❣ (●❛3❛●)⠀Kissing Lips 27
( c//”-}{-*x)⠀Couples 1
(｡-_-｡ )人( ｡-_-｡)⠀Couples 2
(*´∀｀*人*´∀｀*)⠀Couples 3
(/^-^(^ ^*)/⠀Couples 4
( ⋆•ิ ᴈ-ิ(ᵕ❥ ᵕ⁎ ॢ)⠀Couples 5
(・_・)❤(-_-)⠀Couples 6
(* ˘⌣˘)◞[_]♥[_]ヽ(•‿• )⠀Couples 7
(˘▼˘<><<ԅ( ˘⌣ƪ)⠀Couples 8
(ˆˇˆ)-c<<<<˘ˑ˘)⠀Couples 9
(<><<’o’)<><< ♥ <<<<(‘o'<<<<)⠀Couples 10
(<><<^_^)<><<<<<<(^o^<<<<)⠀Couples 11
(Ɔ ˘⌣˘)♥(˘⌣˘ C)⠀Couples 12
(ɔˆ ³(ˆ⌣ˆc)⠀Couples 13
(っ˘з(˘⌣˘ )⠀Couples 14
*ଘ( ॢᵕ꒶̮ᵕ(꒡ᵋ ꒡ღ)⠀Couples 15
♡(*´･ω･)(･ω･`*)♡⠀Couples 16
♡(*´∀｀*)人(*´∀｀*)♡⠀Couples 17
♡｡ﾟ.(*♡´‿` 人´‿` ♡*)ﾟ♡ °・⠀Couples 18
♡꒰*･ω･人･ω･*꒱♡⠀Couples 19
웃+웃=❤⠀Couples 20
*ଘ( ॢᵕ꒶̮ᵕ(꒡ᵋ ꒡ღ)zZ‥⠀Couples 21
◟( ˊ̱˂˃ˋ̱ )◞♡⃛◟( ˊ̱˂˃ˋ̱ )◞⠀Couples 22
❄∘⁖⁎⋆ᶿ̴̤᷇ ˒̫ ᶿ̴̤᷆⋆ᶿ̤᷇ ˓̫ ᶿ̤᷆⋆✶⁎∘❄⠀Couples 23
♡´͈ॢ ᵌˋ͈ॢꉧ´͈ॢᵋ ˋ͈ॢ♡⠀Couples 24
(ෆ❛ั ु▿❛ั੯ू❛ัू ໒꒱⁼³₌₃⠀Couples 25
♡⑅⃝◌꒰ ˘̤ з꒰ ˃̶̤⌄˂̶̤ ` ू꒱◌⑅⃝♡⠀Couples 26
(ღ˘⌣˘)❛ั◡❛ัღ)⠀Couples 27
( ๑ ᴖ ᴈ ᴖ)ᴖ ᴑ ᴖ๑)❣⠀Couples 28
✧˖°*॰ॱ(♡ˊ͈ ॢ꒳ˋ͈)ु(ूˊ͈꒳ ॢˋ͈♡)ʓ৸ʓ৸♪⠀Couples 29
(*• ुᴗ•ධ̢•͈ꄃ̑•͈ ධ̡੭ु⁾⁾·°♡⠀Couples 30
✩⃛*ෆʃᵕ ॢᴗ ॢᵕ)꒡◡꒡*ƪෆ*✩⃛⠀Couples 31
(۶•౪•)۶❤٩(•౪•٩)⠀Couples 32
(♥Ő‿Ő)爻(Ő‿Ő♥)⠀Couples 33
└(┐ﾞ’ωﾞ’ωﾞ`┘)┌⠀Couples 34
( ˘ω˘ )☞♡☜( ˘ω˘ )⠀Couples 35
꒰๑⃙⃘ϱ॔꒳˘͈( ˘͈꒳˘͈๑⃙⃘꒱♡⠀Couples 36
(ღ꒡ ᵌ꒡)⋆﹡♡⃛*⁎⋆(꒡ᵋ ꒡ღ)⠀Couples 37
♫(♡◖ฺ◡ฺ◗ฺ)♡(ฺ◖ฺ◡ฺ◗ฺ♡)♫⠀Couples 38
ღˇ◡ˇ(ᵕ꒶̮ᵕෆ⠀Couples 39
｡ﾟ.(*♡´◡` 人´◡` ♡*)ﾟ °・⠀Couples 40
(☞⁍ૈ৹॒̮⁍ૈ)☞♡⃛☜(⁌ૈ⍜̮⁌ૈ☜)⠀Couples 41
♡˖(⁎ᐙॢ*)ॢ(*ॢᐕॢ⁎)♡॰ॱ⠀Couples 42
ღƪ(ˆ◡ˆ)ʃ♡ƪ(ˆ◡ˆ)ʃ♪⠀Couples 43
( ´∀`)σ)∀`*)♡”⠀Couples 44
(۶•౪•)۶♡٩(•౪•٩)⠀Couples 45
⁽ ¨̮⁾⁽¨̮ ⁾*˚‧♡⠀Couples 46
(☞⁍ૈ৹॒̮⁍ૈ)☞♡⃛☜(⁌ૈ৹॒̮⁌ૈ☜)⠀Couples 47
(◦˘ З(◦’ںˉ◦)♡⠀Couples 48
(♧◑ω◑)☞♡☜(◐ω◐♧)⠀Couples 49
(｡••｡)⸝ෆ⃛⸜(｡••｡)⠀Couples 50
(ෆ❛ั ु³❛ัʕ•̫͡•ིʔྀ*✲ﾟ*｡⋆❤⃛ೄ⠀Couples 51
( ᵕ̤ɜ)ᵕ̤ૢᴗᵕ̤ૢ )⠀Couples 52
ღ꒡ ᴈ꒡)♡⃛(꒡ε ꒡ღ⠀Couples 53
(●’3)♡(ε`●)⠀Couples 54
(⋆◗̑◡◗̑)⸝♡⃛⸜(◖̑◡◖̑⋆)⠀Couples 55
_(┐「ε:)_❤_(:3 」∠)_⠀Couples 56
(-^3(//O//)<><<”⠀Couples 57
웃♥유⠀Couples 58
(*-ω-)ω-*)⠀Couples 59
–,–`–,{@⠀Objects of Love 1
( ° ᴗ°)~ð (/❛o❛\)⠀Objects of Love 2
˅ɞ♡⃛ʚ˅⠀Objects of Love 3
˖◛⁺⑅♡⠀Objects of Love 4
੯ूᵕ̤ू U॒॒॒॒॒୭ℒℴѵℯ❤⠀Animal Love 1
(♥ó㉨ò)ﾉ♡⠀Animal Love 2
Ϛ⃘๑•͡ .̫•๑꒜ℒℴѵℯ❤⠀Animal Love 3
(≚ᄌ≚)ℒℴѵℯ❤⠀Animal Love 4
ฅ ̳͒•ˑ̫• ̳͒ฅ♡⠀Animal Love 5
(͒ ॢ ›⚇‹ ॢ)͒୭♡⠀Animal Love 6
ʕ͙•̫͑͡•ʔͦʕͮ•̫ͤ͡•ʔ͙⠀Animal Love 7
* ི•̮͡ુ -ુ ྀෆ⃛* ི-̮͡ू -ू ྀ⠀Animal Love 8
ˁ̡̡̡∗⁎⃙ ̫⁎⃙ˀ̡̡̡ ̩˳♡⃝⠀Animal Love 9
♡ॢ₍⸍⸌̣ʷ̣̫⸍̣⸌₎⠀Animal Love 10
ෆ⃛(ٛ⌯ॢට ɪ ටٛ⌯ॢ)⠀Animal Love 11
♡͙♡͚₍⸉ॢ⸍͕͈ ˕̫ ⸌͔͈⸊ॢ₎♡͚♡͙⠀Animal Love 12
(人･㉨･)♡⠀Animal Love 13
♡ඩ⌔ඩ♡⠀Animal Love 14
•ू(ᵒ̴̶̷ωᵒ̴̶̷*•ू) ​ )੭ु⁾⠀Animal Love 15
(•ө•)♡⠀Animal Love 16
(ฅ’ω’ฅ)​♥⠀Animal Love 17
ʕ•̫͡•ʔ❤ʕ•̫͡•ʔ⠀Animal Love 18
(⁎⁍̴̛͂▿⁍̴̛͂⁎)*✲ﾟ*｡⋆♡⠀Complex 1
(♡ᵉ̷͈ัॢωᵉ̷͈ัॢ )‧₊°♡⠀Complex 2
(ી(΄◞ิ౪◟ิ‵)ʃ)♥⠀Complex 3
❤⃛(*ૂ❛ัᴗ❛ั*ૂ)⠀Complex 4
(ෆ❛ัᵌ❛ัෆ)°⠀Complex 5
(⁎ॢ˃᷄ ˙̫̮ ❝͋॓⁎)४ෆ⃛⠀Complex 6
˄̻ ̊σ(˃̴͈◡ुමੈॆ⋆)˄̻ ̊~♡⃛⠀Complex 7
❤(ꈍॢ ⁻̫ ꈍॢ)ʸº⠀Complex 8
(̂⁰̴̶̷ꇵ͒ॢ ⁰̴̶̷ૢෆ)̂⋆̥*̥̥⋆̥⠀Complex 9
ˉ̞̭̭̩(ૃˊ͕◡ु꒩ͩ ृ)❤⠀Complex 10
꒰♡˃̶̤́ ॢ꒳ ॢ˂̶̤̀ ꒱·◌*.♡⠀Complex 11
(♡ˊ͈ ॢ꒳ ॢˋ͈)♪⠀Complex 12
( ′ॢ◡̶͂‵ ॢ )♡*.⠀Complex 13
(ृˊ◡˴⁎৲ु॰∘♡⠀Complex 14
( ๑॔˃ ॢ‧̫˂)ॢ♡̷˚๐⠀Complex 15
(༘ ꒪ั̅ᴗ꒪ั̅ )༘≺ ̎৴〻৲♡⠀Complex 16
♡o｡(๑◕ฺ‿ฺ◕ฺ๑)｡o♡⠀Complex 17
♡( •ॢ◡-ॢ)✧˖° ♡⠀Complex 18
( ＾◡＾)っ✂❤⠀Love Hurts 1
(∿°○°)∿ ︵ ǝʌo<⠀Love Hurts 2
♡╰(*ﾟxﾟ​*)╯♡⠀Love Hurts 3
( ﾟ∀ﾟ)ﾉ【LOVE】⠀Love Hurts 4
( ﾟ∀ﾟ)ﾉ　　　　　～【LOVE】⠀Love Hurts 5
Σ(<ﾟ∀ﾟ)ﾉ　　　　　　　　　　　　三【LOVE:<*.’:|⠀Love Hurts 6
(⑅ ॣ•͈ᴗ•͈ ॣ)∟ᵒᵛᵉ૫૦∪⠀Words About Love 1
ପ(๑•̀ᴗ-♡ॢ)fෆr yෆu*೨⋆*✩⠀Words About Love 2
٩(๑•◡-๑)۶ⒽⓤⒼ❤⠀Words About Love 3
(๑′ᴗ‵๑)Ｉ Lᵒᵛᵉᵧₒᵤ♥⠀Words About Love 4
♡ℒฺℴฺνℯฺ♡⠀Words About Love 5
꒒ ০ ⌵ ୧ ♡⠀Words About Love 6
꒰♥︎꒱४ᵃʳⁱᵍᵅᵗᵒ꒰´͈ॢદॢˋ͈♡꒱⠀Words About Love 7
࿒ℓ࿆࿆࿆ෆ࿆౮࿆୧࿆♡࿆༝࿆༚࿆༝࿆༚࿆ ࿒⠀Words About Love 8
ॱ॰⋆(˶ॢ‾᷄﹃‾᷅˵ॢ)ӵᵘᵐᵐᵞ♡♡♡⠀Words About Love 9
♡+* Ɗɑɫë*+♡⠀Words About Love 10
♡+:｡.｡❣LﾛVЁ❣｡.｡:+♡⠀Words About Love 11
애❣⃛ღсμтёღ♡(˘ᵋ ˘ )⠀Words About Love 12
(୨୧•͈ᴗ•͈)◞ᵗʱᵃᵑᵏઽ*♡⠀Words About Love 13
(๑ᵉ̷͈◡ॢᵉ̷͈๑)Üfu♡⠀Words About Love 14
⋈˖⁺♡৹⑅♡˪৹⌵ೕ♡৹⑅♡⁺˖⋈⠀Words About Love 15
(ෆ`꒳´ෆ) ˡºᵛᵉ❤⃛⠀Words About Love 16
(๑′ڡ‵๑)۶४४yϋᵐᵐӵ♡॰⋆̥⠀Words About Love 17
˪৹⌵ೕ꒰๑•‧̮ૣ•ૣ๑꒱⠀Words About Love 18
(ෆˊ͈ ु꒳ ूˋ͈ෆ) ˡºᵛᵉ❤⃛⠀Words About Love 19
(ㅅꈍ﹃ꈍ)*>ᵒᵒᒄ ᵑⁱ>ᑋᵗ*(ꈍ﹃ꈍㅅ)♡⠀Words About Love 20
✧˖°(˶‾᷄ ॢ⁻̫ ‾᷅˵ॢ)◌⑅⃝*॰ॱᗪ੨ⅈઽᵘᵏⁱ✧˖°⠀Words About Love 21
(⑅ᵒ̴̶̷᷄ωᵒ̴̶̷᷅⊞ོॢ)fෆr yෆu⋆*⋆✩⠀Words About Love 22
ιоνё(●´Å`)ε`○)снц♪⠀Words About Love 23
Ꮭσνєஐ(๑´ლ`๑)♡⠀Words About Love 24
˻ᵒ♡ͮᵉ⸝⸝⑅⠀Words About Love 25
✨Lᵒᵛᵉᵧₒᵤ⠀Words About Love 26
(๑ˊ͈ ॢꇴ ˋ͈)ᵃʳⁱᵍᵃᵗᵒ〜♡॰ॱ⠀Words About Love 27
ⓛⓞⓥⓔ♡⠀Words About Love 28
˪৹⌵ೕෆ⃛(˃͈ દ ˂͈ )⠀Words About Love 29
Ⓜɨ ʂ ʂ Ⓨσư❤ (◡ε◡ฺ❤)⠀Words About Love 30
ℓօⓥɪɴ’ ϋ*॰¨̮ ♡➳♡ₓₒₓₒ⠀Words About Love 31
ʚ♡⃛ɞLᵒᵛᵉᵧₒᵤʚ♡⃛ɞ(ू•ᴗ•ू❁)⠀Words About Love 32
(ღˇ◡ˇ)♥ℒᵒᵛᵉᵧₒᵤ♥⠀Words About Love 33
ᎥᏝᵒᵛᵉϋෆ*⠀Words About Love 34
꒰๑͒•௰•๑͒꒱ℒℴѵℯ❤⠀Words About Love 35
ℓ ❤ ϚϦοςӧԼձϮϵ❣⃛⠀Words About Love 36
꒰♥︎꒱ઽᵘᵏⁱ♡ৎˊ͈ˣੰૢˋ͈ॢॽ∗｡⠀Words About Love 37
(๑′ᴗ‵๑)Ｉ Lᵒᵛᵉᵧₒᵤ♡⠀Words About Love 38
ℒℴѵℯ*¨*• ♡⠀Words About Love 39
￡ονё Υου…..φ(〃∇〃 ))⠀Words About Love 40
L(*OεV*)E⠀Words About Love 41
ℒℴѵℯℒᎥѵℯ⠀Words About Love 42
(人-ω-)｡o.ﾟ｡*･♡Good Ni>h<♡･*｡ﾟo｡(-ω-人)⠀Words About Love 43
*♡೫̥͙*:・ℋɑppყ Ϣәԁԁıɲɠﾟ･:* ೫̥͙♡*⠀Words About Love 44
Gооd Йi>h<(´ε｀*)ιον∈ Υου⠀Words About Love 45
*.･｡ヾ(◍ᄏᴗ))ﾉﾟ+.β੨ყ♡ β੨ყ+.°⠀Words About Love 46
•*ꑄೞᵉᵉ৳～❥˪৹⌵ೕ⋆.∗̥✩⁺˚⠀Words About Love 47
✿*ﾟ¨ﾟ✎･ ✿.｡.:* *.:｡✿*ﾟ¨ﾟ✎･✿.｡.:* ♡LOVE♡LOVE♡ ✿*ﾟ¨ﾟ✎･ ✿.｡.:*⠀Words About Love 48
Ｉ ￡ονё Υου…..φ┃*･ω･*┃⠀Words About Love 49
Ƭ ɧ ձ ƞ Ƙ ʂ❤ (◦˘ З(◦’ںˉ◦) Ȼ ɧ ư ♡⠀Words About Love 50
☆*✲ﾟ*｡(((´♡‿♡`+)))｡*ﾟ✲*☆⠀Giant 1
(๑•з•)))⋆*♡*⋆ฺ=͟͟͞͞=͟͟͞͞⠀Giant 2
◌⑅⃝●♡⋆♡⃝ ˻˳˯ₑ♡⃝⋆●♡⑅⃝◌⠀Giant 3
♡⑅*ॱ˖•. ·͙*̩̩͙˚̩̥̩̥*̩̩̥͙·̩̩̥͙*̩̩̥͙˚̩̥̩̥*̩̩͙‧͙ .•˖ॱ*⑅♡⠀Giant 4
♡⃛=͟͟͞͞꒰ˇ❝͋ुꈊ❝͋ुˇ꒱⁼³₌₃⠀Giant 5
(*’v`艸)ﾟ+｡.｡+ﾟ’ﾟ+｡.｡+ﾟ☆⠀Giant 6
(◦′ᆺ‵◦) ♬° ✧❥✧¸.•*¨*✧♡✧ ℒℴѵℯ ✧♡✧*¨*•.❥⠀Giant 7
*̥̻̥̻̥͙*̻̥̻̥͙*̥̻̥͙*̻̥͙*̥͙ ꒰ ˆ ॢ꒵ ॢˆ꒱♡꒰•ॢ◞•ॢ *꒱ *̻͙*̥̻͙*̻̥̻͙*̥̻̥̻͙*̻̥̻̥̻͙⠀Giant 8
♡⃛◟( ˊ̱˂˃ˋ̱ )◞⸜₍ ˍ́˱˲ˍ̀ ₎⸝◟( ˊ̱˂˃ˋ̱ )◞♡⃛⠀Giant 9
♡｡ﾟ.(*♡´◡` 人´◡` ♡*)ﾟ♡ °・⠀Giant 10
·̇·̣̇̇·̣̣̇·̣̇̇·̇ •❣•୨୧┈┈┈୨୧•❣• ·̇·̣̇̇·̣̣̇·̣̇̇·̇ •❣•୨୧┈┈┈୨୧•❣•⠀Giant 11
～♥（ﾉ´∀`）ﾉ田　ε=ε=ε=Γ（ｌｌｌ`Д´ｌｌｌ）」⠀Giant 12
゜*☆○o｡..:*･(*´-ω)(ω-`*)･*:..｡o○☆*ﾟ⠀Giant 13
୧(๑❛ั⌔❛ั๑)୨ ॢゕ̎Խ৷ਕ¨ ♡ॢ⠀Giant 14
ヘ（。□°）ヘ⠀General Pain and Injuries 1
(。_＋)＼⠀General Pain and Injuries 2
((((*｡_｡)_⠀General Pain and Injuries 3
(xLx)ヾ⠀General Pain and Injuries 4
｢(＝＞o≦＝)ﾉ⠀General Pain and Injuries 5
/(*ι*)ヾ⠀General Pain and Injuries 6
／(x~x)＼⠀General Pain and Injuries 7
~(<><<_<<<<~)⠀General Pain and Injuries 8
┗( ●-﹏ ｀｡)づ⠀General Pain and Injuries 9
☆￣(＞。☆)⠀General Pain and Injuries 10
☆⌒(＞。≪)⠀General Pain and Injuries 11
(‘﹏*๑)⠀General Pain and Injuries 12
.( ̵˃﹏˂̵ )⠀General Pain and Injuries 13
ლ(｡-﹏-｡ ლ)⠀General Pain and Injuries 14
(˃̶᷄︿๏）⠀General Pain and Injuries 15
(っ- ‸ – ς)⠀General Pain and Injuries 16
(ᗒᗩᗕ)՞⠀General Pain and Injuries 17
● ﹏☉⠀General Pain and Injuries 18
໒(⁄›˅̭‹∖)७⠀General Pain and Injuries 19
꒰⁎×﹏×⁎꒱՞༘✡⠀General Pain and Injuries 20
☆(　－o-)~~⠀General Pain and Injuries 21
(x_x☆⠀General Pain and Injuries 22
◟̽◞̽ ༘*⠀General Pain and Injuries 23
(≥_<<<<)⠀General Pain and Injuries 24
(⇀⼼_↼)*✲ﾟ*⠀General Pain and Injuries 25
꒰⋆ꆩ⌢̫ꆤ⋆ॢ꒱˚º✩⃛⠀General Pain and Injuries 26
(*<><<_<<<<*)⠀General Pain and Injuries 27
（＊о＊）≡☆⠀General Pain and Injuries 28
╰[✖Ĺ̯ಠ]╯⠀General Pain and Injuries 29
―(T_T)→⠀General Pain and Injuries 30
✧*。ヾ(｡<><<﹏<<<<｡)ﾉﾞ✧*。⠀General Pain and Injuries 31
（。_°☆＼(- – )⠀Inflicting Pain on Others 1
(☆⠀Inflicting Pain on Others 2
[emai<<#160<pro<ec<ed]⠀Inflicting Pain on Others 3
<)☆ ＼(｀-´ﾒ)⠀Inflicting Pain on Others 4
(._+ )☆＼(-.-メ)⠀Inflicting Pain on Others 5
!!( *д*):･’.::･(ｰｰ< )⠀Inflicting Pain on Others 6
(ノ<><<ノ)⠀Tripping or Falling Down 1
◎☆（♯××）┘⠀Tripping or Falling Down 2
(ｏ＿　＿)ｏ⠀Tripping or Falling Down 3
(o_□_)o⠀Tripping or Falling Down 4
(ヘ＿　＿)ヘ⠀Tripping or Falling Down 5
* ・・(o_ _)o⠀Tripping or Falling Down 6
ヽ(＿　＿ヽ)⠀Tripping or Falling Down 7
ヽ(_ _ヽ)彡⠀Tripping or Falling Down 8
(ノ_ _)ノ⠀Tripping or Falling Down 9
εミ(ο_ _)ο⠀Tripping or Falling Down 10
ο(_ _ο)彡3⠀Tripping or Falling Down 11
ミ(ノ_ _)ノ⠀Tripping or Falling Down 12
ヘ(＿　＿ヘ)⠀Tripping or Falling Down 13
ﾍ(｡｡ﾍ)☆⠀Tripping or Falling Down 14
┏|*＿ ＿|┓⠀Tripping or Falling Down 15
( っ_ _)っ)）⠀Tripping or Falling Down 16
⊂⌒~⊃｡Д｡)⊃⠀Tripping or Falling Down 17
((( ⊂⌒~⊃｡Д｡)⊃⠀Tripping or Falling Down 18
(o_ _)ﾉ彡☆⠀Tripping or Falling Down 19
☆ヽ(o_ _)o⠀Tripping or Falling Down 20
⊂´⌒∠；ﾟДﾟ)ゝつ⠀Tripping or Falling Down 21
(｡´<><<д<<<<)っ彡☆⠀Tripping or Falling Down 22
(o_ _)ｏ))⠀Tripping or Falling Down 23
！☆〓(ﾉ_ _)ﾉ⠀Tripping or Falling Down 24
┌(。Д。)┐⠀Tripping or Falling Down 25
(o_ _）ノ彡☆⠀Tripping or Falling Down 26
☆^(o≧∀≦)o⠀Tripping or Falling Down 27
=D—(o_　_)o⠀Tripping or Falling Down 28
ﾐ(ﾉ_ _)ﾉ=3⠀Tripping or Falling Down 29
☆ミ(+ωゞ)☆彡⠀Tripping or Falling Down 30
ミ☆(*._.)⠀Tripping or Falling Down 31
ヘ(<><<_<<<<ヘ)⠀Tripping or Falling Down 32
（<<￣Д￣）ノヾ((((；゜д゜))__⠀Tripping or Falling Down 33
[ ± _ ± ]⠀General Sickness 1
(๑-﹏-๑)⠀General Sickness 2
(˘̭⺫˘̭ <)⠀General Sickness 3
(-﹏-。)⠀General Sickness 4
(☍﹏⁰)｡⠀General Sickness 5
( ⁺⌓ॢ⁺<)՞⠀General Sickness 6
ෆ⃛(˃͈᷇◟̵◞̵˂͈᷆ ფ⠀General Sickness 7
◝(๑⁺᷄д⁺᷅๑)◞՞⠀General Sickness 8
බ͓⌢බ͓⠀General Sickness 9
ಸ , ໖⠀General Sickness 10
ಸ_ಸ⠀General Sickness 11
^(✹ཽ)﹏ु(✹ཽ)^⠀General Sickness 12
(°﹏｡υ)⠀General Sickness 13
༼ ಥ﹏لಥ ༽ ᵘ>ᵍʰ⠀General Sickness 14
⊂((° x。))⊃⠀General Sickness 15
｡.*:・’ﾟ:。'(((＋_＋)))｡.*:ﾟ･’ﾟﾟ:。’･ﾟ⠀General Sickness 16
(ﾟ×ﾟ<<<)⠀Throwing Up, Puking, or Barfing 1
( •́ ✖ •̀)⠀Throwing Up, Puking, or Barfing 2
(´ж｀<)⠀Throwing Up, Puking, or Barfing 3
(●’x`*)⌒％⠀Throwing Up, Puking, or Barfing 4
(ﾉ’x`｡ヽ)⠀Throwing Up, Puking, or Barfing 5
‧∘˳°∗˚(⁎›ˍູ‹) ∗.∘˚˳°⠀Throwing Up, Puking, or Barfing 6
( ╹✖╹)⠀Throwing Up, Puking, or Barfing 7
(<・ж<・<)⠀Throwing Up, Puking, or Barfing 8
(*<ﾟ<艸<ﾟ<)⠀Throwing Up, Puking, or Barfing 9
(；ﾟ；┏艸┓；ﾟ；)⠀Throwing Up, Puking, or Barfing 10
＿|￣|○､<’.･⠀Throwing Up, Puking, or Barfing 11
<｀<:ﾞ<｀(<ﾟ<ж<ﾟ< )⠀Throwing Up, Puking, or Barfing 12
˓˓( ॢ₎˔̈₍ ॢ)˒˒⠀Throwing Up, Puking, or Barfing 13
(。・艸・)⠀Throwing Up, Puking, or Barfing 14
(*U艸U*)⠀Throwing Up, Puking, or Barfing 15
((゜乂゜))⠀Throwing Up, Puking, or Barfing 16
⋆* ⁑⋆* (๑•﹏•)⋆* ⁑⋆*⠀Throwing Up, Puking, or Barfing 17
（＃´Ⅹ｀＃）⠀Throwing Up, Puking, or Barfing 18
┗┐(<<*<:´<艸<`:<*<<)┌┛⠀Throwing Up, Puking, or Barfing 19
ε≡ ε≡ ε≡ ε＝ （#・ж・）⠀Throwing Up, Puking, or Barfing 20
。゜+.(:.<゜<艸<゜<.:)゜+.゜⠀Throwing Up, Puking, or Barfing 21
ε-(≖д≖﹆)⠀Coughing 1
ε-(＞．＜<<⠀Coughing 2
ε=o(´ﾛ｀||)⠀Coughing 3
((( +д+)o=3=3⠀Coughing 4
ε-(<><<o<<<<)⠀Coughing 5
(；≧∇≦) =3⠀Coughing 6
（●｀□´）＝з⠀Coughing 7
人人人ヾ( <×o×)〃 人人人⠀Drowning 1
︵‿︵‿︵‿︵‿︵‿︵‿︵‿︵‿︵‿ヽ(゜□゜ )ノ︵‿︵‿︵‿︵‿︵‿⠀Drowning 2
(ू̯⋆̧ ͕⋆᷅ू̯ )  ༘˟⠀Complex Pain and Sickness 1
⁽⁽ƈ ͡ (ु ˲̥̥̥́ ˱̥̥̥̀) ु⁾⁾⠀Complex Pain and Sickness 2
₊·(ϱ॔﹏ᵕ๑॓)‧*⠀Complex Pain and Sickness 3
ₒ˛˚̣ (˃ᾓ˂⁎)₎₎⠀Complex Pain and Sickness 4
(﹡︠﹏ु﹡︡)⠀Complex Pain and Sickness 5
₍₍ (ृ˚͈ⅈ∘͈⁎৲ु₎₎՞⠀Complex Pain and Sickness 6
⁽⁽ƈ ͡ (ुŏ̥̥̥̥םŏ̥̥̥̥) ु⠀Complex Pain and Sickness 7
(ृˊ⌄˴⁎৲ु⠀Complex Pain and Sickness 8
⁽⁽ƈ ͡ (ु ˲̥̥̥́ ˱̥̥̥̀) ु⁾⁾⠀Complex Pain and Sickness 9
⁝ƈ ͡ (ुŏ̥̥̥̥םŏ̥̥̥̥) ु⁝⠀Complex Pain and Sickness 10
(╯3╰)⠀Kissing with Lips Aimed to the Right 1
( ˘ ³˘)♥⠀Kissing with Lips Aimed to the Right 2
( ˘ ³˘)❤⠀Kissing with Lips Aimed to the Right 3
（。ˇ ⊖ˇ）⠀Kissing with Lips Aimed to the Right 4
（*＾3＾）⠀Kissing with Lips Aimed to the Right 5
(○´3｀)ﾉ⠀Kissing with Lips Aimed to the Right 6
(☆´3｀)⠀Kissing with Lips Aimed to the Right 7
(ΦзΦ)⠀Kissing with Lips Aimed to the Right 8
|(￣3￣)|⠀Kissing with Lips Aimed to the Right 9
|°з°|⠀Kissing with Lips Aimed to the Right 10
～(^з^)-☆⠀Kissing with Lips Aimed to the Right 11
～(^з^)-♡⠀Kissing with Lips Aimed to the Right 12
ヽ(*´з｀*)ﾉ⠀Kissing with Lips Aimed to the Right 13
(。≖ˇ3ˇ≖｡)⠀Kissing with Lips Aimed to the Right 14
( ˘•૩•˘ ).｡oஇ⠀Kissing with Lips Aimed to the Right 15
⁽˙³˙⁾⠀Kissing with Lips Aimed to the Right 16
(๑•́ ₃ •̀๑)⠀Kissing with Lips Aimed to the Right 17
(๑ơ ₃ ơ)♥⠀Kissing with Lips Aimed to the Right 18
ฅ(♡ơ ₃ơ)ฅ⠀Kissing with Lips Aimed to the Right 19
(๛ ˘ ³˘)۶⠀Kissing with Lips Aimed to the Right 20
(๑•̑з•̑๑)੭ु⁾⁾ ༘⠀Kissing with Lips Aimed to the Right 21
(๑´• ₃ •̀๑)⠀Kissing with Lips Aimed to the Right 22
(*´σЗ`)σ⠀Kissing with Lips Aimed to the Right 23
(o˚̑̑̑̑̑ 3˚̑̑̑̑̑ o)⠀Kissing with Lips Aimed to the Right 24
( ੈჰ ੈ)⠀Kissing with Lips Aimed to the Right 25
( ^з^) y -☆⠀Kissing with Lips Aimed to the Right 26
( ´•₎౩•` )⠀Kissing with Lips Aimed to the Right 27
ᴓᴈᴓ⠀Kissing with Lips Aimed to the Right 28
ꉂ (๑ › ₃ ू‹)₋₃⠀Kissing with Lips Aimed to the Right 29
( ๑ ᴓ ᴈ ᴓ)⠀Kissing with Lips Aimed to the Right 30
|ｮз☆)⠀Kissing with Lips Aimed to the Right 31
(σ･з･)σ⠀Kissing with Lips Aimed to the Right 32
Ⴀ͡კႠ͡⠀Kissing with Lips Aimed to the Right 33
(；◔ิ з◔ิ)⠀Kissing with Lips Aimed to the Right 34
(๑♡3♡๑)⠀Kissing with Lips Aimed to the Right 35
꒰♡⌯́ॢ³⌯̀ॢ꒱⠀Kissing with Lips Aimed to the Right 36
(⁽ؔʽ⁾³⁽ؔʽ⁾)⠀Kissing with Lips Aimed to the Right 37
o┤*｀3´*├o⠀Kissing with Lips Aimed to the Right 38
(〃ﾟ3ﾟ〃)⠀Kissing with Lips Aimed to the Right 39
໒( ∗ ⇀ 3 ↼ ∗ )७⠀Kissing with Lips Aimed to the Right 40
(*´･з･)⠀Kissing with Lips Aimed to the Right 41
(〃бзб`)⠀Kissing with Lips Aimed to the Right 42
（๑・౩・๑）⠀Kissing with Lips Aimed to the Right 43
( ᵅั ᴈ ᵅั<)⠀Kissing with Lips Aimed to the Right 44
( ´з｀)ﾉ⌒☆⠀Kissing with Lips Aimed to the Right 45
(´з｀)⊃～⠀Kissing with Lips Aimed to the Right 46
(･´з`･)ゞ⠀Kissing with Lips Aimed to the Right 47
( *¯ ³¯*)♡⠀Kissing with Lips Aimed to the Right 48
❣ (●❛3❛●)⠀Kissing with Lips Aimed to the Right 49
(๑•з•)))⋆*♡*⋆ฺ=͟͟͞͞=͟͟͞͞⠀Kissing with Lips Aimed to the Right 50
(-ε- )⠀Kissing with Lips Aimed to the Left 1
(TεT)⠀Kissing with Lips Aimed to the Left 2
（＿ε＿）⠀Kissing with Lips Aimed to the Left 3
(｡・//ε//・｡)⠀Kissing with Lips Aimed to the Left 4
(‘ε’)⠀Kissing with Lips Aimed to the Left 5
（＠ーεー＠）⠀Kissing with Lips Aimed to the Left 6
(´ε｀ )♡⠀Kissing with Lips Aimed to the Left 7
(´ε｀*)⠀Kissing with Lips Aimed to the Left 8
（￣ε￣＠）⠀Kissing with Lips Aimed to the Left 9
（○゜ε＾○）⠀Kissing with Lips Aimed to the Left 10
(ΘεΘ<)⠀Kissing with Lips Aimed to the Left 11
(≡ε≡；)⠀Kissing with Lips Aimed to the Left 12
σ(≧ε≦ｏ)⠀Kissing with Lips Aimed to the Left 13
ヾ(❛ε❛“)ʃ⠀Kissing with Lips Aimed to the Left 14
✧˖°ˈ·*ε-(๑˃́ε˂̀๑ )⠀Kissing with Lips Aimed to the Left 15
(・ε・｀)⠀Kissing with Lips Aimed to the Left 16
(｡◕ฺˇε ˇ◕ฺ｡)⠀Kissing with Lips Aimed to the Left 17
(´. ॄ.｀)⠀Kissing with Lips Aimed to the Left 18
(๑ˇεˇ๑)⠀Kissing with Lips Aimed to the Left 19
(○ﾟεﾟ○)⠀Kissing with Lips Aimed to the Left 20
(´ε｀；)⠀Kissing with Lips Aimed to the Left 21
(^ε^)-☆⠀Kissing with Lips Aimed to the Left 22
•́ε•̀٥⠀Kissing with Lips Aimed to the Left 23
˶⚈Ɛ⚈˵⠀Kissing with Lips Aimed to the Left 24
(′• દ •‵)⠀Kissing with Lips Aimed to the Left 25
∵ゞ(´ε｀●) ﾌﾞ!!⠀Kissing with Lips Aimed to the Left 26
( ് દ ് )⠀Kissing with Lips Aimed to the Left 27
ෆ⃛(ˇᵋ ˇෆೄ⠀Kissing with Lips Aimed to the Left 28
(*̩̩̩ᵋ *̩̩̩ )⠀Kissing with Lips Aimed to the Left 29
(๑˙❥˙๑)⠀Kissing with Lips Aimed to the Left 30
(Ō̥̥̥̥̥̥̥ ԑ Ō̥̥̥̥̥̥̥ ૢ)⠀Kissing with Lips Aimed to the Left 31
(๑❛ั ॄ❛ั๑)⠀Kissing with Lips Aimed to the Left 32
┌║ ຈ ε ຈ ║┐⠀Kissing with Lips Aimed to the Left 33
♪(｡◕ฺˇε ˇ◕ฺ｡）♡⠀Kissing with Lips Aimed to the Left 34
ｰ(•̃͡ε•̃͡)∫⠀Kissing with Lips Aimed to the Left 35
₍₍୯ૃᵒ᷇ᵋᵒ᷆૨ુ⠀Kissing with Lips Aimed to the Left 36
(⁎⁍̴̆Ɛ⁍̴̆⁎)⠀Kissing with Lips Aimed to the Left 37
(○ﾟε^○)⠀Kissing with Lips Aimed to the Left 38
( ؔ⚈̫ ε ؔ⚈̫ ⁎)⠀Kissing with Lips Aimed to the Left 39
(≧ε≦)))⠀Kissing with Lips Aimed to the Left 40
(｀ε´#)⠀Kissing with Lips Aimed to the Left 41
★<><<d(,,･ε´-,,)⌒☆⠀Kissing with Lips Aimed to the Left 42
(・ε・`*)⠀Kissing with Lips Aimed to the Left 43
☆⌒ヽ(´ε｀ )⠀Kissing with Lips Aimed to the Left 44
ヾ(´ε｀*)ゝ⠀Kissing with Lips Aimed to the Left 45
ヾ(●ε●)ノ⠀Kissing with Lips Aimed to the Left 46
(´-ε-｀<)⠀Kissing with Lips Aimed to the Left 47
ㄖꏁㄖ⠀Kissing with Lips Aimed to the Left 48
(#^.^#)⠀Miscellaneous Mouths 1
（´・｀ ）♡⠀Miscellaneous Mouths 2
˓( ˶ ❛ ꁞ ❛ ˶ )˒˒⠀Miscellaneous Mouths 3
ϵ( ‘Θ’ )϶⠀Miscellaneous Mouths 4
(╯⊙ ⊱ ⊙╰ )⠀Miscellaneous Mouths 5
(✿ꈍ。 ꈍ✿)⠀Miscellaneous Mouths 6
(‘⁾ʚ’⁾*)ू⠀Miscellaneous Mouths 7
₍ ⁄⁄⁄ ຶᵦ ⁄⁄⁄ ຶ₎⠀Miscellaneous Mouths 8
(ﾉ￣〓￣)ﾉ⠀Miscellaneous Mouths 9
ヾ(￣〓￣ヾ)⠀Miscellaneous Mouths 10
ヾ(´〓｀)ﾉ⠀Miscellaneous Mouths 11
(ʃƪ ˘ ³˘)⠀Clasping Hands 1
(ʃƪ˘ﻬ˘)⠀Clasping Hands 2
(人´З`)⠀Clasping Hands 3
（ʃƪ＾3＾）⠀Clasping Hands 4
(ʃƪΦзΦ)⠀Clasping Hands 5
|人°з°|⠀Clasping Hands 6
(人^з^)-☆⠀Clasping Hands 7
(ʃƪ〃ﾟ3ﾟ〃)⠀Clasping Hands 8
（ʃƪ๑・౩・๑）⠀Clasping Hands 9
(´ε｀ ʃƪ)♡⠀Clasping Hands 10
（￣ε￣ʃƪ）⠀Clasping Hands 11
(ΘεΘʃƪ)⠀Clasping Hands 12
ლ(´◉❥◉｀ლ)⠀Grabby Hands 1
ლ(|||⌒εー|||)ლ⠀Grabby Hands 2
ლ(´ ❥ `ლ)⠀Grabby Hands 3
(~￣³￣)~⠀Grabby Hands 4
(づ￣ ³￣)づ⠀Grabby Hands 5
(ɔˆ ³(ˆ⌣ˆc)⠀One Person Kissing Another 1
(っ˘з(˘⌣˘ )⠀One Person Kissing Another 2
( ๑ ᴖ ᴈ ᴖ)ᴖ ᴑ ᴖ๑)❣⠀One Person Kissing Another 3
(っ˘зʕ•̫͡•ʔ⠀One Person Kissing Another 4
(◦˘ З(◦’ںˉ◦)♡⠀One Person Kissing Another 5
(ღ ･ิ◡･ิ)ε ･ิ ღ)⠀One Person Kissing Another 6
( ᵕ̤ɜ)ᵕ̤ૢᴗᵕ̤ૢ )⠀One Person Kissing Another 7
(-^3(//O//)<><<”⠀One Person Kissing Another 8
(´∀｀*)ε｀　)⠀One Person Kissing Another 9
(*^3(＃∀＃)⠀One Person Kissing Another 10
(*^3(*^o^*)⠀One Person Kissing Another 11
（^_^ ；)ε￣)⠀One Person Kissing Another 12
(*￣(^ *)⠀One Person Kissing Another 13
(((*☣ω☣(ε◕* )))⠀One Person Kissing Another 14
♡⑅⃝◌꒰ ˘̤ з꒰ ˃̶̤⌄˂̶̤ ` ू꒱◌⑅⃝♡⠀One Person Kissing Another 15
ｰ(･ω´･<<<))))　　ヽ(ﾟεﾟヽ)))))⠀One Person Kissing Another 16
☆⌒ヽ∞*´Зﾟ◆)∞*´зﾟ◆)ﾉ⌒★⠀One Person Kissing Another 17
ﾟ☆+.ﾟ☆+(〃´3(･艸･ 〃)+.☆ﾟ+.☆⠀One Person Kissing Another 18
((((@ﾉ´3｀)ﾉ　　･･･Σ(ﾟдﾟ<<ﾉ⠀One Person Kissing Another 19
( c//”-}{-*x)⠀Two People Kissing Each Other 1
(*◑З◑)爻(◐ε◐*)⠀Two People Kissing Each Other 2
(*-(　　)⠀Two People Kissing Each Other 3
˓˓ ˋ̩} ͢ {ˊ̩ ˒˒⠀Two People Kissing Each Other 4
(●´з(ε｀○)⠀Two People Kissing Each Other 5
❥( ◜3‾)(‾⊱◝ )⠀Two People Kissing Each Other 6
(●’3)♡(ε`●)⠀Two People Kissing Each Other 7
ღ꒡ ᴈ꒡)♡⃛(꒡ε ꒡ღ⠀Two People Kissing Each Other 8
│〇´3｀|人|´ε｀●|⠀Two People Kissing Each Other 9
(●´3`☆★´ε`●)⠀Two People Kissing Each Other 10
<><<<<<<((((*ﾟ<<<< <><<ﾟ*)))<><<<<<<⠀Two People Kissing Each Other 11
(ღ꒡ ᵌ꒡)⋆﹡♡⃛*⁎⋆(꒡ᵋ ꒡ღ)⠀Two People Kissing Each Other 12
“8-( ●｀ε´●)爻(●｀ε´● )-8”⠀Two People Kissing Each Other 13
～～～～～(／￣3)／ ＼(ε￣＼）～～～～～⠀Two People Kissing Each Other 14
━━━⊂´⌒つ ﾟзﾟ)ﾞ<☆<（ﾟεﾟ⊂⌒｀つ━━⠀Two People Kissing Each Other 15
⁽˙³˙⁾◟(๑•́ ₃ •̀๑)◞⁽˙³˙⁾⠀Three or More People Kissing 1
(Ɔ˘з˘)(ꈍヮꈍ)˘ε˘ C)⠀Three or More People Kissing 2
애❣⃛ღсμтёღ♡(˘ᵋ ˘ )⠀Words 1
(っ˘зʕ•̫͡•ʔcнϋෆ*⠀Words 2
(/ ᵒ̴̵̶̷౩ᵒ̴̵̶̷ )/ ᵏᴵˢઽ ❤⃛⠀Words 3
(*-(　　) cнϋ❤⠀Words 4
.+ﾟ*(●´ε`人)СНЦ｡:ﾟ+⠀Words 5
(^_^ ；)ε￣)ＣＨＵ★⠀Words 6
(*ﾟэﾟ)chu♪⠀Words 7
ιоνё(●´Å`)ε`○)снц♪⠀Words 8
˪৹⌵ೕෆ⃛(˃͈ દ ˂͈ )⠀Words 9
⁽͑˙˚̌ ᵌ˚̌˙⁾̉⁼ᵌ ᵇᵘᵎ⠀Words 10
(◦˘ З(◦’ںˉ◦)cнϋ♡⠀Words 11
L(*OεV*)E⠀Words 12
Ƭ ɧ ձ ƞ Ƙ ʂ❤ (◦˘ З(◦’ںˉ◦) Ȼ ɧ ư ♡⠀Words 13
Gооd Йi>h<(´ε｀*)ιον∈ Υου⠀Words 14
ﾟ･*:.｡. ☆κｉss мё(人uзu*)ρｌёдsё☆.｡.:*･ﾟ⠀Words 15
.+ﾟ*((人′3`))｡o(chu★)｡:ﾟ+⠀Words 16
(<<<:´<3<`:<<<)ﾉＣＨЦ*:ﾟ･☆*:ﾟ･☆*:ﾟ･☆⠀Words 17
((*´３｀)｡o○ﾟ･*:.｡. ☆κｉss мё☆ﾟ･*:.｡.⠀Words 18
( ⋆•ิ ᴈ-ิ(ᵕ❥ ᵕ⁎ ॢ)⠀Complex 1
( ु ॕ ӟ ॕ)ु⠀Complex 2
(ु*´З`)ू❣⠀Complex 3
*ଘ( ॢᵕ꒶̮ᵕ(꒡ᵋ ꒡ღ)⠀Complex 4
*ଘ( ॢᵕ꒶̮ᵕ(꒡ᵋ ꒡ღ)zZ‥⠀Complex 5
(。´✷ฺЗ✷ฺ)・<゛.:’<、⠀Complex 6
(๑ᵕॢ૩ᵕॢ)*౨˚ൗ⠀Complex 7
♡´͈ॢ ᵌˋ͈ॢꉧ´͈ॢᵋ ˋ͈ॢ♡⠀Complex 8
<<<<ब₍₍( ˃̗εू˂ )₎₎<<<<ब⠀Complex 9
(⌯˘̤ ॢᵌ ू˘̤)യෆ̈⠀Complex 10
⁽⁽(*꒪ั❥꒪ั*)⁾⁾⠀Complex 11
୧( ́⁰⃙⃘Ԑ⁰⃙ఁ̀ )୨⠀Complex 12
(ლ ۞ิ ჴ ۞ิ)ლ⠀Complex 13
(๑ᵕॢ₃ᵕू๑)⠀Complex 14
( ु ॕ ӟ ॕ)ुƾｭෆ⠀Complex 15
✧.*(⌯ⅉॕੰૈՅⅉॕੰૈ)⠀Complex 16
⁝(ृ°ۿ°ꐦ ृ　)ु⁝⠀Complex 17
(ෆ❛ัᵌ❛ัෆ)°⠀Complex 18
(●◦⃝⃚⃙⃘⃙⃚⃙⃚⃙⃘⃑з◦⃝⃚⃙⃘⃙⃐)⠀Complex 19
༼(*꒪ั❥꒪ั*༽༽⠀Complex 20
☻ू (ѳॅ ॄ ѳॆ ू )⠀Complex 21
(๑ʻัદʻั๑)⠀Complex 22
(՟ິͫઘ ՟ິͫ)⠀Complex 23
(ෆ❛ั ु³❛ัʕ•̫͡•ིʔྀ*✲ﾟ*｡⋆❤⃛ೄ⠀Complex 24
(*´艸`*)⠀Stifling Laughter 1
(●´艸`)⠀Stifling Laughter 2
( ´艸｀)⠀Stifling Laughter 3
(｡ <><<艸<<<<)⠀Stifling Laughter 4
(*・艸・)⠀Stifling Laughter 5
(*≧艸≦)⠀Stifling Laughter 6
(* ˚᷄ 艸 ˚᷅ *)⠀Stifling Laughter 7
(♡´艸`)⠀Stifling Laughter 8
(Ŏ艸Ŏ)⠀Stifling Laughter 9
(亝艸亝)⠀Stifling Laughter 10
(✿˘艸˘✿)⠀Stifling Laughter 11
(灬º 艸º灬)⠀Stifling Laughter 12
( ^ิ艸^ิﾟ)⠀Stifling Laughter 13
(ಡ艸ಡ)⠀Stifling Laughter 14
(｡ˇ艸ˇ)⠀Stifling Laughter 15
(*^ิ艸^ิ*)⠀Stifling Laughter 16
(o´艸`)⠀Stifling Laughter 17
( ❝ົཽ艸❝ົཽ)⠀Stifling Laughter 18
(❝ົཽ艸❝ົཽ )⠀Stifling Laughter 19
(≧艸≦*)⠀Stifling Laughter 20
(*<><<艸<<<<)⠀Stifling Laughter 21
((●≧艸≦)⠀Stifling Laughter 22
(´艸｀〃)⠀Stifling Laughter 23
(｡￫ˇ艸￩)⠀Stifling Laughter 24
( Ŏ艸Ŏ)(Ŏ艸Ŏ )⠀Stifling Laughter 25
(○v艸v*)⠀Stifling Laughter 26
(*´艸)(艸｀*)⠀Stifling Laughter 27
(○･艸)(艸･●)⠀Stifling Laughter 28
( 〃´艸｀)⠀Stifling Laughter 29
(*Q艸Q*）⠀Stifling Laughter 30
(o<><<艸<<<<)⠀Stifling Laughter 31
(+･艸･+)(+･艸･+)⠀Stifling Laughter 32
(*´艸｀)⠀Stifling Laughter 33
(๑ơ艸ơ๑)♡ฺ⠀Stifling Laughter 34
☆⌒(*’艸＾*)⠀Stifling Laughter 35
(。ｕ艸ｕ。)⠀Stifling Laughter 36
(*´ 艸`)(´艸 `*)⠀Stifling Laughter 37
(*、｡艸｡)(ﾟ艸ﾟ`*)⠀Stifling Laughter 38
(* ´<><<艸<<<<)゛⠀Stifling Laughter 39
(☆Θ艸Θ)⠀Stifling Laughter 40
（○´艸｀）⠀Stifling Laughter 41
((*´艸｀*))⠀Stifling Laughter 42
｡ﾟ(TヮT)ﾟ｡⠀Tears 1
。+゜(*´<><<艸<<<<｀*)。+゜⠀Tears 2
｡:+((*′艸`))+:｡⠀Tears 3
(○v艸v*).+ﾟ⠀Tears 4
・:*:・(*´艸｀*)・:*:・⠀Tears 5
゜+.(。´<><<艸<<<<)*.☆⠀Tears 6
∗˚(* ˃̤൬˂̤ *)˚∗⠀Tears 7
(*≧▽≦)ﾉｼ))⠀Waving arms 1
(ノ＞▽＜。)ノ⠀Waving arms 2
(੭ु˙꒳​˙)੭ु⁾⁾⠀Waving arms 3
꒰*⑅˃̶͈ ৺˂̶͈⑅꒱੭ु⁾⁾·°⠀Waving arms 4
((ꉺꈊꉺ)ꀢ༣⠀Waving arms 5
(੭ु ‾᷄ᗣ‾᷅ )੭ु⁾⁾⠀Waving arms 6
(੭ु´͈ ᐜ `͈)੭ु⁾⁾⠀Waving arms 7
(๑‾᷅⚰‾᷄๑)੭ु⁾⁾˞͛ ༘ؓ ︠³⠀Waving arms 8
౧(*മ് ധമ്)੭ु⁾⁾⠀Waving arms 9
(੭ु ´͈꒳​`͈)੭ु⁾⁾⠀Waving arms 10
(੭ु˙꒳˙)੭ु⁾⁾*✭⠀Waving arms 11
(੭ ˃̣̣̥ ω˂̣̣̥)੭ु⁾⁾⠀Waving arms 12
(˵¯̴͒ꇴ¯̴͒˵)⠀Big Wide Open Mouths 1
✧(σ๑˃̶̀ꇴ˂̶́)σ⠀Big Wide Open Mouths 2
٩̋(๑˃́ꇴ˂̀๑)⠀Big Wide Open Mouths 3
(ᗒᗜᗕ)՛̵̖⠀Big Wide Open Mouths 4
(ꐦ ´͈ ᗨ `͈ )⠀Big Wide Open Mouths 5
(◍˃̶ᗜ˂̶◍)ﾉ”⠀Big Wide Open Mouths 6
✧ꉂ(σ▰˃̶̀ꇴ˂̶́)σ✧⠀Big Wide Open Mouths 7
ꉂ(σ▰˃̶̀ꇴ˂̶́)σ⠀Big Wide Open Mouths 8
(●❛⃘ᗜ❛⃘●)੭ु⁾⁾⠀Big Wide Open Mouths 9
-(｡ﾉᗨ<<<<｡)ﾉ⠀Big Wide Open Mouths 10
°₊·ˈ∗(( ॣ<><<̶᷇ᗢ<<<<̶᷆ ॣ))∗ˈ‧⠀Big Wide Open Mouths 11
(੭ु˶˭̵̴⃙⃚⃘᷄ᗢ˭̴̵⃙⃚⃘᷅˶)੭ु⁾⁾~⠀Big Wide Open Mouths 12
ˉ̶̡̭̭ ( ´͈ ᗨ `͈ ) ˉ̶̡̭̭⠀Big Wide Open Mouths 13
(๐॔˃̶ᗜ˂̶๐॓)⠀Big Wide Open Mouths 14
(๑❛ꇳ❛๑)⠀Big Wide Open Mouths 15
ꉂ (′ ॢꇴ ॢ‵๑))⠀Big Wide Open Mouths 16
ꉂ ૮( ᵒ̌ૢꇴᵒ̌ૢ )ა｡*ﾟ✧⠀Big Wide Open Mouths 17
✧(˚ੌɄ̮˚ੌ◍)⠀Big Wide Open Mouths 18
(๑˃́ꇴ˂̀๑)⠀Big Wide Open Mouths 19
ꋧ(⋆ʾꇶʿ⋆)⠀Big Wide Open Mouths 20
(๑ ꒪̇ꌂ̇꒪̇๑)⠀Big Wide Open Mouths 21
ꉂ ꊚ(ꈍꇴꆧ )⠀Big Wide Open Mouths 22
ꉂ ฅ૮( ๑’ꇴ’๑)აฅ｡*ﾟ✧⠀Big Wide Open Mouths 23
(⌯꒪͒ ૢ∀ ૢ꒪͒) ੭ੇ⠀Little Hands 1
(⌯˃̶᷄ ᴗ̂ ॣ˂̶᷄⌯ั)⠀Little Hands 2
(˃̴̀ᄇॢ˂̴́ ∗)⠀Little Hands 3
ᵵ (ૢ˃ꌂ˂⁎)Շ^⠀Little Hands 4
✬̴⃛꒰⁍̴ꈊ ॢ⁍̴⌯꒱⠀Little Hands 5
(˃ॢ੪˂ू॓๑)‾̞̭̭⠀Little Hands 6
⁽⁽꒰๑•‧̮ૣ•ૣ๑꒱⁾⁾⠀Little Hands 7
(๑˃̶᷇⺫ॢ˂̶᷆๑)⠀Little Hands 8
(⌯꒪͒ ૢ◞◟ ૢ꒪͒)⠀Little Hands 9
ꉂ (˃̶᷄‧̫ॢ ˂̶᷅๑ )⠀Little Hands 10
ꉂ (ᵔ̴̶̤᷄ꇴ ॣᵔ̴̶̤᷅⌯))л̵ʱªʱª⁎*.＊⠀Words and Sounds 1
Σ(꒪ॢ∀꒪<)՞л̵ʱªʱª⠀Words and Sounds 2
ꉂ ꀞꀞꀞ(ᕑᗢूᓫ∗)˒˒⠀Words and Sounds 3
ꉂ (๑¯ਊ¯)σ л̵ʱªʱªʱª⠀Words and Sounds 4
ʱªʱªʱª (ᕑᗢूᓫ∗)⠀Words and Sounds 5
(๑ॢ˃̶͈̀ ꇴ ˂̶͈́๑ॢ) л̵ʱªʱªʱª⠀Words and Sounds 6
ｰΣ(꒪ॢ∀꒪<)՞л̵ʱªʱª⠀Words and Sounds 7
(˃̴̀ᄇॢ˂̴́ ∗)੭᷅ʊʊ⠀Words and Sounds 8
(‾͈̑ ◟  ॢ‾͈̑๑)ഽ̵ᵘഽ̵ᵘ४꒰ ꒱⠀Words and Sounds 9
(๑ ˃̵͈́∀˂̵͈̀ )ʊʊ⠀Words and Sounds 10
ꉂ (ᵔ̴̶̤᷄ꇴ ॣᵔ̴̶̤᷅⌯))л̵ʱªʱª⁎*.＊⠀Words and Sounds 11
ꉂ (๑¯ਊ¯)σ⠀ਊ Style Mouths 1
(灬㋭ ਊ ㋲灬)⠀ਊ Style Mouths 2
(<うਊ ՞)⠀ਊ Style Mouths 3
( ՞ਊ ՞)☞⠀ਊ Style Mouths 4
｡ﾟ(ﾟ＾ਊ＾ํ )ﾟ｡⠀ਊ Style Mouths 5
(☞ ՞ਊ ՞)☞⠀ਊ Style Mouths 6
( ՞ਊ՞)⠀ਊ Style Mouths 7
(⁙ູ՟ິͫ◞̴ਊ◟̴ູ՟ິͫ⁙ູ)⠀ਊ Style Mouths 8
(,, ՞ਊ ՞)=☞)՞ਊ ՞)⠀ਊ Style Mouths 9
(΄◞ิਊ◟ิ‵)⠀ਊ Style Mouths 10
(खਉख)⠀ਊ Style Mouths 11
v(＜°＞ਊ ＜°＞)v⠀ਊ Style Mouths 12
( ╹ਊ╹)⠀ਊ Style Mouths 13
(⁙ู꒪ู︠͒◞̴ਊ◟̴ู꒪︡͒⁙ู)⠀ਊ Style Mouths 14
(((< ఠ ਉ ఠ))⠀ਊ Style Mouths 15
┌( •́ ਊ •̀ )┐⠀ਊ Style Mouths 16
*･゜ﾟ･*:.｡.｡.:*･’(´◜◞ਊ◟◝｀)’･*:.｡.｡.:*･゜ﾟ･*⠀ਊ Style Mouths 17
（　´∀｀）⠀Simple or Miscellaneous Laughter 1
（・∀・）⠀Simple or Miscellaneous Laughter 2
(；-◞౪◟-)⠀Simple or Miscellaneous Laughter 3
（＾ｖ＾）⠀Simple or Miscellaneous Laughter 4
（＞ｙ＜）⠀Simple or Miscellaneous Laughter 5
（⌒▽⌒）⠀Simple or Miscellaneous Laughter 6
(◎ヮ◎)⠀Simple or Miscellaneous Laughter 7
(^ワ^＝)⠀Simple or Miscellaneous Laughter 8
(´つヮ⊂)⠀Simple or Miscellaneous Laughter 9
(๑´ㅂ`๑)⠀Simple or Miscellaneous Laughter 10
(｡￫∀￩｡)⠀Simple or Miscellaneous Laughter 11
(◍´͈ꈊ`͈◍)⠀Simple or Miscellaneous Laughter 12
☚(ﾟヮﾟ☚)⠀Simple or Miscellaneous Laughter 13
（＞Ц＜●）⠀Simple or Miscellaneous Laughter 14
(●＾曲＾●)⠀Simple or Miscellaneous Laughter 15
(*￣､ゝ￣)⠀Simple or Miscellaneous Laughter 16
“ψ(｀∇´)ψ⠀Simple or Miscellaneous Laughter 17
ಡ ੴಡ⠀Simple or Miscellaneous Laughter 18
( ਊдਊ)⠀Simple or Miscellaneous Laughter 19
(^ц^ )⠀Simple or Miscellaneous Laughter 20
(*˒ ̖˰̊ ̗˓*)⠀Simple or Miscellaneous Laughter 21
Σ (੭ु ຶਊ ຶ)੭ु⁾⁾⠀Complex Forms of Laughter 1
ꋧ(⁎ˊ̭ સˆ̀)◞₎̵₎⠀Complex Forms of Laughter 2
∗˚೫˳(●ᴖ͙̏ᴗॢᴖ͙̋●)˳೫˚∗⠀Complex Forms of Laughter 3
⸌̷̻ ( ᷇๑ॢ˃̶͈̀ ꇴ ˂̶͈́๑ॢ) ⸌̷̻⠀Complex Forms of Laughter 4
(੭ु റ̆ ˒̫̮ റ̥)੭ु⁾⁾⠀Complex Forms of Laughter 5
ꉂ ꋧ(⁎ˊ̭ સˆ̀)◞₎̵₎⠀Complex Forms of Laughter 6
ृ₍⁺ꇴ⁺᷅ ृ₎₎ ՞⠀Complex Forms of Laughter 7
ꆭ㐃(͛꒪͒ধृ꒪͒ॢ )͛↝꒱⠀Complex Forms of Laughter 8
ʕ̡̢̡̡̢̡̡̢♡ᵒ̴̷͈艸ᵒ̴̷͈॰ʔ̢̡̢̢̡̢̢̡̢✧⠀Complex Forms of Laughter 9
(●♡∀♡)⠀Love Eyes 1
(｡♥‿♥｡)⠀Love Eyes 2
(♥ω♥ ) ~♪⠀Love Eyes 3
(♥ω♥*)⠀Love Eyes 4
(✿ ♥‿♥)⠀Love Eyes 5
✿♥‿♥✿⠀Love Eyes 6
乂❤‿❤乂⠀Love Eyes 7
٩(♡ε♡ )۶⠀Love Eyes 8
ლζ*♡ε♡*ζლ⠀Love Eyes 9
⊂（♡⌂♡）⊃⠀Love Eyes 10
(๑♡3♡๑)⠀Love Eyes 11
(๑♡⌓♡๑)⠀Love Eyes 12
♱♡‿♡♰⠀Love Eyes 13
⊆♥_㇁♥⊇⠀Love Eyes 14
(●♡∀♡))ヾ☆*。⠀Love Eyes 15
໒( ♥ ◡ ♥ )७⠀Love Eyes 16
༼♥ل͜♥༽⠀Love Eyes 17
(灬♥ω♥灬)⠀Love Eyes 18
(‘∀’●)♡⠀Left Love 1
(´∀｀)♡⠀Left Love 2
（*´▽｀*）⠀Left Love 3
（´・｀ ）♡⠀Left Love 4
（´ω｀♡%）⠀Left Love 5
♥(ˆ⌣ˆԅ)⠀Left Love 6
꒰˘̩̩̩⌣˘̩̩̩๑꒱♡⠀Left Love 7
ლ(́◉◞౪◟◉‵ლ)⠀Left Love 8
⸌̷̻( ᷇ॢ〰ॢ ᷆◍)⸌̷̻♡⃛⠀Left Love 9
₍՞◌′ᵕ‵ू◌₎♡⠀Left Love 10
♡ฅ(ᐤˊ꒳ฅˋᐤ♪)⠀Left Love 11
ʚ♡⃛ɞ(ू•ᴗ•ू❁)⠀Left Love 12
❣⃛(❛ั◡˜๑)⠀Left Love 13
( ˭̵̵̵̵͈́◡ु͂˭̵̵̵͈̀ )ˉ̞̭♡⠀Left Love 14
♡(ŐωŐ人)⠀Left Love 15
❤⃛ヾ(๑❛ ▿ ◠๑ )⠀Left Love 16
（*’∀’人）♥⠀Left Love 17
(°◡°♡).:｡⠀Left Love 18
ʸ(➜◡ु⚈᷉)♡⃛⠀Left Love 19
ˉ̞̭(′͈∨‵͈♡)˄̻ ̊⠀Left Love 20
◟(◔ั₀◔ั )◞ ༘♡⠀Left Love 21
φ(ﾟ ωﾟ//）♡⠀Left Love 22
ʸ(ᴖ́◡ु⚈᷉)♡⃛⠀Left Love 23
ꉂ (′̤ॢ∀ ू‵̤๑))ˉ̞̭♡⠀Left Love 24
♡♡+.ﾟ(￫ε￩*)ﾟ+.ﾟ⠀Left Love 25
꒰✪ૢꇵ✪ૢ꒱ෆ⃛⠀Left Love 26
(●´□`)♡⠀Right Love 1
(｡･ω･｡)ﾉ♡⠀Right Love 2
(｡’▽’｡)♡⠀Right Love 3
（●´∀｀）ノ♡⠀Right Love 4
₍₍ ( ๑॔˃̶◡ ˂̶๑॓)◞♡⠀Right Love 5
(๑・ω-)～♥”⠀Right Love 6
(๑°꒵°๑)･*♡⠀Right Love 7
～(^з^)-♡⠀Right Love 8
(๑ˊ͈ ॢꇴ ˋ͈)〜♡॰ॱ⠀Right Love 9
(ෆ ͒•∘̬• ͒)◞⠀Right Love 10
♡(㋭ ਊ ㋲)♡⠀Right Love 11
( •ॢ◡-ॢ)-♡⠀Right Love 12
(●’ᴗ’σ)σணღ*⠀Right Love 13
(♡´͈༝`͈)ฅ˒˒⠀Right Love 14
(•‾⌣‾•)و ̑̑♡⠀Right Love 15
( ෆຶдෆຶ)⠀Right Love 16
(⁎⁍̴̛͂▿⁍̴̛͂⁎)*✲ﾟ*｡⋆♡ོ⠀Right Love 17
(*´o`*)ʖˋʖˋʖˋ～♡⠀Right Love 18
ღゝ◡╹)ノ♡⠀Right Love 19
⌓⌓⌕(˃̴◡ुؔ՞ઁ)♡⃛⠀Right Love 20
♡✧( ु•⌄• )⠀Right Love 21
(∗ᵒ̶̶̷̀ω˂̶́∗)੭₎₎̊₊♡⠀Right Love 22
(●මᴗමσ)σணღ*⠀Right Love 23
(๑╹ڡ╹)╭ ～ ♡⠀Right Love 24
(๑ Ỡ ◡͐ Ỡ๑)ﾉ♡⠀Right Love 25
(♡ ὅ ◡ ὅ )ʃ♡⠀Right Love 26
⁽⁽ପ( •ु﹃ •ु)​.⑅*♡⠀Right Love 27
꒰ ︠ु௰•꒱ु♡⠀Right Love 28
(⁎⁍̴̀﹃ ⁍̴́⁎)♡⠀Right Love 29
(๑ゝᴗම๑) ৷ਕკ~ෆ⠀Right Love 30
(⋈◍＞◡＜◍)。✧♡⠀Right Love 31
ε=(｡♡ˇд ˇ♡｡）⠀Right Love 32
(◍•ᴗ•◍)❤⠀Forward Love 1
(∩˃o˂∩)♡⠀Forward Love 2
♡(.◜ω◝.)♡⠀Forward Love 3
♡〜٩(^▿^)۶〜♡⠀Forward Love 4
♡´･ᴗ･`♡⠀Forward Love 5
♡＾▽＾♡⠀Forward Love 6
♥(✿ฺ´∀`✿ฺ)ﾉ⠀Forward Love 7
♥╣[-_-]╠♥⠀Forward Love 8
♡ლ(-༗‿༗-)ლ♡⠀Forward Love 9
(｡・‧̫・｡).*＊♡⠀Forward Love 10
(◍•ڡ•◍)❤⠀Forward Love 11
-ω(´•ω•｀)♡⠀Forward Love 12
(ෆˊ͈ ु꒳ ूˋ͈ෆ)⠀Forward Love 13
(♡´౪`♡)⠀Forward Love 14
ෆ╹ .̮ ╹ෆ⠀Forward Love 15
( ◜◒◝ )♡⠀Forward Love 16
♡〜ლ(๑癶ᴗ癶๑)ლ〜♡⠀Forward Love 17
(♡´❍`♡)*✧ ✰ ｡*⠀Forward Love 18
(´∩｡• ᵕ •｡∩`) ♡⠀Forward Love 19
( ˊᵕˋ )♡.°⑅⠀Forward Love 20
(♡ <><<ω<<<< ♡)⠀Forward Love 21
( ๑ ❛ ڡ ❛ ๑ )❤⠀Forward Love 22
（♥￫ｏ￩♥）⠀Forward Love 23
(◍•ᴗ•◍)♡ ✧*。⠀Forward Love 24
（〃・ω・〃）⠀Shy Love 1
(*°∀°)=3⠀Shy Love 2
♥（ﾉ´∀`）⠀Shy Love 3
(♡´艸`)⠀Shy Love 4
(´,,•ω•,,)♡⠀Shy Love 5
❤\(⸝⸝⸝°⁻̫° ⸝⸝⸝)⠀Shy Love 6
❣╰(⸝⸝⸝´꒳`⸝⸝⸝)╯❣⠀Shy Love 7
(⸝⸝⍢⸝⸝) ෆ⠀Shy Love 8
(⺣◡⺣)♡*⠀Shy Love 9
(๑´ლ`๑)ﾌﾌ♡⠀Shy Love 10
( ̧⸝⸝⍢⸝⸝)ི Շᐱෆ⠀Shy Love 11
( ⌯◞◟⌯)♡⠀Shy Love 12
♡(｡￫ˇ艸￩)⠀Shy Love 13
(灬ºωº灬)♡⠀Shy Love 14
꒰⁎˃ ॢꇴ ॢ˂⁎꒱➴ෆ⃛⠀Excited Love 1
ヽ(o♡o)/⠀Excited Love 2
♡✧。 (⋈◍＞◡＜◍)。✧♡⠀Excited Love 3
٩(ó｡ò۶ ♡)))♬⠀Excited Love 4
٩(*❛⊰❛)ʓਡ～❤⠀Excited Love 5
٩(๑ơలơ)۶♡⠀Excited Love 6
(੭ु ›ω‹ )੭ु⁾⁾♡⠀Excited Love 7
٩(๑∂▿∂๑)۶♡⠀Excited Love 8
\(-ㅂ-)/ ♥ ♥ ♥⠀Excited Love 9
ヾ(◍’౪`◍)ﾉﾞ♡⠀Excited Love 10
ヽ(愛´∀｀愛)ノ⠀Excited Love 11
♡٩(๑ö⊿ö๑)۶♡⠀Excited Love 12
٩(*ゝڡ◕๑)۶♥⠀Excited Love 13
♡〜٩( ╹▿╹ )۶〜♡⠀Excited Love 14
╰(✿´⌣`✿)╯♡⠀Excited Love 15
(´ ▽｀).。ｏ♡⠀Thinking about Love 1
( ´͈ ॢꇴ `͈ॢ)･*♡⠀Thinking about Love 2
(/∇＼*)｡o○♡⠀Thinking about Love 3
(´▽`ʃƪ)♡⠀Thinking about Love 4
(◞ꈍ∇ꈍ)◞⋆**✚⃞⠀Thinking about Love 5
(ღ˘⌣˘ღ)⠀Thinking about Love 6
（人´∀`*）⠀Thinking about Love 7
♡o｡.(✿ฺ｡ ✿ฺ)⠀Thinking about Love 8
♡o｡(๑๏‿ฺ๏๑)｡o♡⠀Thinking about Love 9
♥～(‘▽^人)⠀Thinking about Love 10
꒰♡ˊ͈ ु꒳ ूˋ͈꒱.⑅*♡⠀Thinking about Love 11
*ଯ( ॢᵕ꒶̮ᵕ)ॢഒ*♡⠀Thinking about Love 12
꒰⑅ᵕ༚ᵕ꒱˖♡⠀Thinking about Love 13
♡˖꒰ᵕ༚ᵕ⑅꒱⠀Thinking about Love 14
( ᵒ̴̶̷̤̀ुωᵒ̴̶̷̤́ू )❤”⠀Thinking about Love 15
(❃•̤ॢᗜ•̤ॢ)✲*｡♡⠀Thinking about Love 16
(๑॔˃̶ॢ◟◞ ˂̶ॢ๑॓)♡⠀Thinking about Love 17
(‾̴̴͡͡▿•‾̴̴͡͡ʃƪ)⠀Thinking about Love 18
( ´͈ ૢᐜ `͈ૢ)･*♡੭ੇ৸♡੭ੇ৸♡⠀Thinking about Love 19
꒰◍•̤ु௰•̤ु꒱* ∗◌+*♡⠀Thinking about Love 20
˚‧*♡ॢ˃̶̤̀◡˂̶̤́♡ॢ*‧˚⠀Thinking about Love 21
´͈ ᵕ `͈ ♡°◌̊⠀Thinking about Love 22
(*´ ˘ `*).｡oO ( ♡ )⠀Thinking about Love 23
(人 •͈ᴗ•͈)⠀Thinking about Love 24
(*˘︶˘*).｡.:*♡⠀Thinking about Love 25
(*ˊૢᵕˋૢ*)⠀Thinking about Love 26
❤⃛῍̻̩✧(´͈ ૢᐜ `͈ૢ)⠀Thinking about Love 27
❤︎⁄⁄꒰* ॢꈍ◡ꈍ ॢ꒱.*˚‧⠀Thinking about Love 28
♡( ૢ⁼̴̤̆ ꇴ ⁼̴̤̆ ૢ)~ෆ♡⠀Thinking about Love 29
°₊·ˈ∗♡( ˃̶᷇ ‧̫ ˂̶᷆ )♡∗ˈ‧₊°⠀Thinking about Love 30
°₊·ˈ∗♡( ˃̶᷇ ‧̫ ˂̶᷆ )♡∗ˈ‧₊°⠀Thinking about Love 31
ღ˘◡˘ற♡.｡oO⠀Thinking about Love 32
( ˘͈ ᵕ ˘͈♡)˚๐*˟ ♡⠀Thinking about Love 33
( ∩ˇωˇ∩)♡⠀Thinking about Love 34
|๑˃ ॢ‧̫˂ॢ๑ ).*˚‧♡⠀Thinking about Love 35
˞♡ฅ(ᐤˊ꒳ฅˋᐤ♪)⠀Thinking about Love 36
( ื▿ ืʃƪ)⠀Thinking about Love 37
(o´〰`o)♡*✲ﾟ*｡⠀Thinking about Love 38
(´⌣`ʃƪ)⠀Thinking about Love 39
(人*´∀｀)+ﾟ:｡*ﾟ+⠀Thinking about Love 40
(人´ω｀*)♡⠀Thinking about Love 41
❣‧✩͓̊(ᵕ̴̤‧̮ ॣᵕ̴̤∗)ɞ₎₎☽˟⠀Thinking about Love 42
(人´∀`)⠀Thinking about Love 43
（人*´∀｀）⠀Thinking about Love 44
ლ(´◉❥◉｀ლ)⠀Kissing Lips 1
( ˘ ³˘)♥⠀Kissing Lips 2
( ˘ ³˘)❤⠀Kissing Lips 3
（。ˇ ⊖ˇ）♡⠀Kissing Lips 4
（*＾3＾）/～♡⠀Kissing Lips 5
(｡・//ε//・｡)⠀Kissing Lips 6
(´ε｀ )♡⠀Kissing Lips 7
(ʃƪ ˘ ³˘)⠀Kissing Lips 8
(ʃƪ˘ﻬ˘)⠀Kissing Lips 9
(づ￣ ³￣)づ⠀Kissing Lips 10
♡(˃͈ દ ˂͈ ༶ )⠀Kissing Lips 11
٩꒰ ˘ ³˘꒱۶~♡⠀Kissing Lips 12
ƪ(♥ﻬ♥)ʃ⠀Kissing Lips 13
ლ(|||⌒εー|||)ლ⠀Kissing Lips 14
♡ლζ(♛ε♛*ζლ♡⠀Kissing Lips 15
†=”Ⴛ̸ ♡(˃͈ દ ˂͈ ༶ )⠀Kissing Lips 16
(⌯˘̤ ॢᵌ ू˘̤)യෆ̈⠀Kissing Lips 17
(๑ơ ₃ ơ)♥⠀Kissing Lips 18
ฅ(♡ơ ₃ơ)ฅ⠀Kissing Lips 19
(/ ᵒ̴̵̶̷౩ᵒ̴̵̶̷ )/ ᵏᴵˢઽ ❤⃛⠀Kissing Lips 20
৲( ᵒ ૩ᵕ )৴♡*৹⠀Kissing Lips 21
(ˊσ̴̶̷̤ ₋̮̑ σ̴̶̷̤ˋ)₊ෆ⃛⁺˚⠀Kissing Lips 22
ෆ⃛(ˇᵋ ˇෆೄ⠀Kissing Lips 23
꒰♡⌯́ॢ³⌯̀ॢ꒱⠀Kissing Lips 24
♪(｡◕ฺˇε ˇ◕ฺ｡）♡⠀Kissing Lips 25
( *¯ ³¯*)♡⠀Kissing Lips 26
❣ (●❛3❛●)⠀Kissing Lips 27
( c//”-}{-*x)⠀Couples 1
(｡-_-｡ )人( ｡-_-｡)⠀Couples 2
(*´∀｀*人*´∀｀*)⠀Couples 3
(/^-^(^ ^*)/⠀Couples 4
( ⋆•ิ ᴈ-ิ(ᵕ❥ ᵕ⁎ ॢ)⠀Couples 5
(・_・)❤(-_-)⠀Couples 6
(* ˘⌣˘)◞[_]♥[_]ヽ(•‿• )⠀Couples 7
(˘▼˘<><<ԅ( ˘⌣ƪ)⠀Couples 8
(ˆˇˆ)-c<<<<˘ˑ˘)⠀Couples 9
(<><<’o’)<><< ♥ <<<<(‘o'<<<<)⠀Couples 10
(<><<^_^)<><<<<<<(^o^<<<<)⠀Couples 11
(Ɔ ˘⌣˘)♥(˘⌣˘ C)⠀Couples 12
(ɔˆ ³(ˆ⌣ˆc)⠀Couples 13
(っ˘з(˘⌣˘ )⠀Couples 14
*ଘ( ॢᵕ꒶̮ᵕ(꒡ᵋ ꒡ღ)⠀Couples 15
♡(*´･ω･)(･ω･`*)♡⠀Couples 16
♡(*´∀｀*)人(*´∀｀*)♡⠀Couples 17
♡｡ﾟ.(*♡´‿` 人´‿` ♡*)ﾟ♡ °・⠀Couples 18
♡꒰*･ω･人･ω･*꒱♡⠀Couples 19
웃+웃=❤⠀Couples 20
*ଘ( ॢᵕ꒶̮ᵕ(꒡ᵋ ꒡ღ)zZ‥⠀Couples 21
◟( ˊ̱˂˃ˋ̱ )◞♡⃛◟( ˊ̱˂˃ˋ̱ )◞⠀Couples 22
❄∘⁖⁎⋆ᶿ̴̤᷇ ˒̫ ᶿ̴̤᷆⋆ᶿ̤᷇ ˓̫ ᶿ̤᷆⋆✶⁎∘❄⠀Couples 23
♡´͈ॢ ᵌˋ͈ॢꉧ´͈ॢᵋ ˋ͈ॢ♡⠀Couples 24
(ෆ❛ั ु▿❛ั੯ू❛ัू ໒꒱⁼³₌₃⠀Couples 25
♡⑅⃝◌꒰ ˘̤ з꒰ ˃̶̤⌄˂̶̤ ` ू꒱◌⑅⃝♡⠀Couples 26
(ღ˘⌣˘)❛ั◡❛ัღ)⠀Couples 27
( ๑ ᴖ ᴈ ᴖ)ᴖ ᴑ ᴖ๑)❣⠀Couples 28
✧˖°*॰ॱ(♡ˊ͈ ॢ꒳ˋ͈)ु(ूˊ͈꒳ ॢˋ͈♡)ʓ৸ʓ৸♪⠀Couples 29
(*• ुᴗ•ධ̢•͈ꄃ̑•͈ ධ̡੭ु⁾⁾·°♡⠀Couples 30
✩⃛*ෆʃᵕ ॢᴗ ॢᵕ)꒡◡꒡*ƪෆ*✩⃛⠀Couples 31
(۶•౪•)۶❤٩(•౪•٩)⠀Couples 32
(♥Ő‿Ő)爻(Ő‿Ő♥)⠀Couples 33
└(┐ﾞ’ωﾞ’ωﾞ`┘)┌⠀Couples 34
( ˘ω˘ )☞♡☜( ˘ω˘ )⠀Couples 35
꒰๑⃙⃘ϱ॔꒳˘͈( ˘͈꒳˘͈๑⃙⃘꒱♡⠀Couples 36
(ღ꒡ ᵌ꒡)⋆﹡♡⃛*⁎⋆(꒡ᵋ ꒡ღ)⠀Couples 37
♫(♡◖ฺ◡ฺ◗ฺ)♡(ฺ◖ฺ◡ฺ◗ฺ♡)♫⠀Couples 38
ღˇ◡ˇ(ᵕ꒶̮ᵕෆ⠀Couples 39
｡ﾟ.(*♡´◡` 人´◡` ♡*)ﾟ °・⠀Couples 40
(☞⁍ૈ৹॒̮⁍ૈ)☞♡⃛☜(⁌ૈ⍜̮⁌ૈ☜)⠀Couples 41
♡˖(⁎ᐙॢ*)ॢ(*ॢᐕॢ⁎)♡॰ॱ⠀Couples 42
ღƪ(ˆ◡ˆ)ʃ♡ƪ(ˆ◡ˆ)ʃ♪⠀Couples 43
( ´∀`)σ)∀`*)♡”⠀Couples 44
(۶•౪•)۶♡٩(•౪•٩)⠀Couples 45
⁽ ¨̮⁾⁽¨̮ ⁾*˚‧♡⠀Couples 46
(☞⁍ૈ৹॒̮⁍ૈ)☞♡⃛☜(⁌ૈ৹॒̮⁌ૈ☜)⠀Couples 47
(◦˘ З(◦’ںˉ◦)♡⠀Couples 48
(♧◑ω◑)☞♡☜(◐ω◐♧)⠀Couples 49
(｡••｡)⸝ෆ⃛⸜(｡••｡)⠀Couples 50
(ෆ❛ั ु³❛ัʕ•̫͡•ིʔྀ*✲ﾟ*｡⋆❤⃛ೄ⠀Couples 51
( ᵕ̤ɜ)ᵕ̤ૢᴗᵕ̤ૢ )⠀Couples 52
ღ꒡ ᴈ꒡)♡⃛(꒡ε ꒡ღ⠀Couples 53
(●’3)♡(ε`●)⠀Couples 54
(⋆◗̑◡◗̑)⸝♡⃛⸜(◖̑◡◖̑⋆)⠀Couples 55
_(┐「ε:)_❤_(:3 」∠)_⠀Couples 56
(-^3(//O//)<><<”⠀Couples 57
웃♥유⠀Couples 58
(*-ω-)ω-*)⠀Couples 59
–,–`–,{@⠀Objects of Love 1
( ° ᴗ°)~ð (/❛o❛\)⠀Objects of Love 2
˅ɞ♡⃛ʚ˅⠀Objects of Love 3
˖◛⁺⑅♡⠀Objects of Love 4
੯ूᵕ̤ू U॒॒॒॒॒୭ℒℴѵℯ❤⠀Animal Love 1
(♥ó㉨ò)ﾉ♡⠀Animal Love 2
Ϛ⃘๑•͡ .̫•๑꒜ℒℴѵℯ❤⠀Animal Love 3
(≚ᄌ≚)ℒℴѵℯ❤⠀Animal Love 4
ฅ ̳͒•ˑ̫• ̳͒ฅ♡⠀Animal Love 5
(͒ ॢ ›⚇‹ ॢ)͒୭♡⠀Animal Love 6
ʕ͙•̫͑͡•ʔͦʕͮ•̫ͤ͡•ʔ͙⠀Animal Love 7
* ི•̮͡ુ -ુ ྀෆ⃛* ི-̮͡ू -ू ྀ⠀Animal Love 8
ˁ̡̡̡∗⁎⃙ ̫⁎⃙ˀ̡̡̡ ̩˳♡⃝⠀Animal Love 9
♡ॢ₍⸍⸌̣ʷ̣̫⸍̣⸌₎⠀Animal Love 10
ෆ⃛(ٛ⌯ॢට ɪ ටٛ⌯ॢ)⠀Animal Love 11
♡͙♡͚₍⸉ॢ⸍͕͈ ˕̫ ⸌͔͈⸊ॢ₎♡͚♡͙⠀Animal Love 12
(人･㉨･)♡⠀Animal Love 13
♡ඩ⌔ඩ♡⠀Animal Love 14
•ू(ᵒ̴̶̷ωᵒ̴̶̷*•ू) ​ )੭ु⁾⠀Animal Love 15
(•ө•)♡⠀Animal Love 16
(ฅ’ω’ฅ)​♥⠀Animal Love 17
ʕ•̫͡•ʔ❤ʕ•̫͡•ʔ⠀Animal Love 18
(⁎⁍̴̛͂▿⁍̴̛͂⁎)*✲ﾟ*｡⋆♡⠀Complex 1
(♡ᵉ̷͈ัॢωᵉ̷͈ัॢ )‧₊°♡⠀Complex 2
(ી(΄◞ิ౪◟ิ‵)ʃ)♥⠀Complex 3
❤⃛(*ૂ❛ัᴗ❛ั*ૂ)⠀Complex 4
(ෆ❛ัᵌ❛ัෆ)°⠀Complex 5
(⁎ॢ˃᷄ ˙̫̮ ❝͋॓⁎)४ෆ⃛⠀Complex 6
˄̻ ̊σ(˃̴͈◡ुමੈॆ⋆)˄̻ ̊~♡⃛⠀Complex 7
❤(ꈍॢ ⁻̫ ꈍॢ)ʸº⠀Complex 8
(̂⁰̴̶̷ꇵ͒ॢ ⁰̴̶̷ૢෆ)̂⋆̥*̥̥⋆̥⠀Complex 9
ˉ̞̭̭̩(ૃˊ͕◡ु꒩ͩ ृ)❤⠀Complex 10
꒰♡˃̶̤́ ॢ꒳ ॢ˂̶̤̀ ꒱·◌*.♡⠀Complex 11
(♡ˊ͈ ॢ꒳ ॢˋ͈)♪⠀Complex 12
( ′ॢ◡̶͂‵ ॢ )♡*.⠀Complex 13
(ृˊ◡˴⁎৲ु॰∘♡⠀Complex 14
( ๑॔˃ ॢ‧̫˂)ॢ♡̷˚๐⠀Complex 15
(༘ ꒪ั̅ᴗ꒪ั̅ )༘≺ ̎৴〻৲♡⠀Complex 16
♡o｡(๑◕ฺ‿ฺ◕ฺ๑)｡o♡⠀Complex 17
♡( •ॢ◡-ॢ)✧˖° ♡⠀Complex 18
( ＾◡＾)っ✂❤⠀Love Hurts 1
(∿°○°)∿ ︵ ǝʌo<⠀Love Hurts 2
♡╰(*ﾟxﾟ​*)╯♡⠀Love Hurts 3
( ﾟ∀ﾟ)ﾉ【LOVE】⠀Love Hurts 4
( ﾟ∀ﾟ)ﾉ　　　　　～【LOVE】⠀Love Hurts 5
Σ(<ﾟ∀ﾟ)ﾉ　　　　　　　　　　　　三【LOVE:<*.’:|⠀Love Hurts 6
(⑅ ॣ•͈ᴗ•͈ ॣ)∟ᵒᵛᵉ૫૦∪⠀Words About Love 1
ପ(๑•̀ᴗ-♡ॢ)fෆr yෆu*೨⋆*✩⠀Words About Love 2
٩(๑•◡-๑)۶ⒽⓤⒼ❤⠀Words About Love 3
(๑′ᴗ‵๑)Ｉ Lᵒᵛᵉᵧₒᵤ♥⠀Words About Love 4
♡ℒฺℴฺνℯฺ♡⠀Words About Love 5
꒒ ০ ⌵ ୧ ♡⠀Words About Love 6
꒰♥︎꒱४ᵃʳⁱᵍᵅᵗᵒ꒰´͈ॢદॢˋ͈♡꒱⠀Words About Love 7
࿒ℓ࿆࿆࿆ෆ࿆౮࿆୧࿆♡࿆༝࿆༚࿆༝࿆༚࿆ ࿒⠀Words About Love 8
ॱ॰⋆(˶ॢ‾᷄﹃‾᷅˵ॢ)ӵᵘᵐᵐᵞ♡♡♡⠀Words About Love 9
♡+* Ɗɑɫë*+♡⠀Words About Love 10
♡+:｡.｡❣LﾛVЁ❣｡.｡:+♡⠀Words About Love 11
애❣⃛ღсμтёღ♡(˘ᵋ ˘ )⠀Words About Love 12
(୨୧•͈ᴗ•͈)◞ᵗʱᵃᵑᵏઽ*♡⠀Words About Love 13
(๑ᵉ̷͈◡ॢᵉ̷͈๑)Üfu♡⠀Words About Love 14
⋈˖⁺♡৹⑅♡˪৹⌵ೕ♡৹⑅♡⁺˖⋈⠀Words About Love 15
(ෆ`꒳´ෆ) ˡºᵛᵉ❤⃛⠀Words About Love 16
(๑′ڡ‵๑)۶४४yϋᵐᵐӵ♡॰⋆̥⠀Words About Love 17
˪৹⌵ೕ꒰๑•‧̮ૣ•ૣ๑꒱⠀Words About Love 18
(ෆˊ͈ ु꒳ ूˋ͈ෆ) ˡºᵛᵉ❤⃛⠀Words About Love 19
(ㅅꈍ﹃ꈍ)*>ᵒᵒᒄ ᵑⁱ>ᑋᵗ*(ꈍ﹃ꈍㅅ)♡⠀Words About Love 20
✧˖°(˶‾᷄ ॢ⁻̫ ‾᷅˵ॢ)◌⑅⃝*॰ॱᗪ੨ⅈઽᵘᵏⁱ✧˖°⠀Words About Love 21
(⑅ᵒ̴̶̷᷄ωᵒ̴̶̷᷅⊞ོॢ)fෆr yෆu⋆*⋆✩⠀Words About Love 22
ιоνё(●´Å`)ε`○)снц♪⠀Words About Love 23
Ꮭσνєஐ(๑´ლ`๑)♡⠀Words About Love 24
˻ᵒ♡ͮᵉ⸝⸝⑅⠀Words About Love 25
✨Lᵒᵛᵉᵧₒᵤ⠀Words About Love 26
(๑ˊ͈ ॢꇴ ˋ͈)ᵃʳⁱᵍᵃᵗᵒ〜♡॰ॱ⠀Words About Love 27
ⓛⓞⓥⓔ♡⠀Words About Love 28
˪৹⌵ೕෆ⃛(˃͈ દ ˂͈ )⠀Words About Love 29
Ⓜɨ ʂ ʂ Ⓨσư❤ (◡ε◡ฺ❤)⠀Words About Love 30
ℓօⓥɪɴ’ ϋ*॰¨̮ ♡➳♡ₓₒₓₒ⠀Words About Love 31
ʚ♡⃛ɞLᵒᵛᵉᵧₒᵤʚ♡⃛ɞ(ू•ᴗ•ू❁)⠀Words About Love 32
(ღˇ◡ˇ)♥ℒᵒᵛᵉᵧₒᵤ♥⠀Words About Love 33
ᎥᏝᵒᵛᵉϋෆ*⠀Words About Love 34
꒰๑͒•௰•๑͒꒱ℒℴѵℯ❤⠀Words About Love 35
ℓ ❤ ϚϦοςӧԼձϮϵ❣⃛⠀Words About Love 36
꒰♥︎꒱ઽᵘᵏⁱ♡ৎˊ͈ˣੰૢˋ͈ॢॽ∗｡⠀Words About Love 37
(๑′ᴗ‵๑)Ｉ Lᵒᵛᵉᵧₒᵤ♡⠀Words About Love 38
ℒℴѵℯ*¨*• ♡⠀Words About Love 39
￡ονё Υου…..φ(〃∇〃 ))⠀Words About Love 40
L(*OεV*)E⠀Words About Love 41
ℒℴѵℯℒᎥѵℯ⠀Words About Love 42
(人-ω-)｡o.ﾟ｡*･♡Good Ni>h<♡･*｡ﾟo｡(-ω-人)⠀Words About Love 43
*♡೫̥͙*:・ℋɑppყ Ϣәԁԁıɲɠﾟ･:* ೫̥͙♡*⠀Words About Love 44
Gооd Йi>h<(´ε｀*)ιον∈ Υου⠀Words About Love 45
*.･｡ヾ(◍ᄏᴗ))ﾉﾟ+.β੨ყ♡ β੨ყ+.°⠀Words About Love 46
•*ꑄೞᵉᵉ৳～❥˪৹⌵ೕ⋆.∗̥✩⁺˚⠀Words About Love 47
✿*ﾟ¨ﾟ✎･ ✿.｡.:* *.:｡✿*ﾟ¨ﾟ✎･✿.｡.:* ♡LOVE♡LOVE♡ ✿*ﾟ¨ﾟ✎･ ✿.｡.:*⠀Words About Love 48
Ｉ ￡ονё Υου…..φ┃*･ω･*┃⠀Words About Love 49
Ƭ ɧ ձ ƞ Ƙ ʂ❤ (◦˘ З(◦’ںˉ◦) Ȼ ɧ ư ♡⠀Words About Love 50
☆*✲ﾟ*｡(((´♡‿♡`+)))｡*ﾟ✲*☆⠀Giant 1
(๑•з•)))⋆*♡*⋆ฺ=͟͟͞͞=͟͟͞͞⠀Giant 2
◌⑅⃝●♡⋆♡⃝ ˻˳˯ₑ♡⃝⋆●♡⑅⃝◌⠀Giant 3
♡⑅*ॱ˖•. ·͙*̩̩͙˚̩̥̩̥*̩̩̥͙·̩̩̥͙*̩̩̥͙˚̩̥̩̥*̩̩͙‧͙ .•˖ॱ*⑅♡⠀Giant 4
♡⃛=͟͟͞͞꒰ˇ❝͋ुꈊ❝͋ुˇ꒱⁼³₌₃⠀Giant 5
(*’v`艸)ﾟ+｡.｡+ﾟ’ﾟ+｡.｡+ﾟ☆⠀Giant 6
(◦′ᆺ‵◦) ♬° ✧❥✧¸.•*¨*✧♡✧ ℒℴѵℯ ✧♡✧*¨*•.❥⠀Giant 7
*̥̻̥̻̥͙*̻̥̻̥͙*̥̻̥͙*̻̥͙*̥͙ ꒰ ˆ ॢ꒵ ॢˆ꒱♡꒰•ॢ◞•ॢ *꒱ *̻͙*̥̻͙*̻̥̻͙*̥̻̥̻͙*̻̥̻̥̻͙⠀Giant 8
♡⃛◟( ˊ̱˂˃ˋ̱ )◞⸜₍ ˍ́˱˲ˍ̀ ₎⸝◟( ˊ̱˂˃ˋ̱ )◞♡⃛⠀Giant 9
♡｡ﾟ.(*♡´◡` 人´◡` ♡*)ﾟ♡ °・⠀Giant 10
·̇·̣̇̇·̣̣̇·̣̇̇·̇ •❣•୨୧┈┈┈୨୧•❣• ·̇·̣̇̇·̣̣̇·̣̇̇·̇ •❣•୨୧┈┈┈୨୧•❣•⠀Giant 11
～♥（ﾉ´∀`）ﾉ田　ε=ε=ε=Γ（ｌｌｌ`Д´ｌｌｌ）」⠀Giant 12
゜*☆○o｡..:*･(*´-ω)(ω-`*)･*:..｡o○☆*ﾟ⠀Giant 13
୧(๑❛ั⌔❛ั๑)୨ ॢゕ̎Խ৷ਕ¨ ♡ॢ⠀Giant 14
(ﾉ≧∀≦)ﾉ・‥…━━━★⠀Star Magic 1
o͡͡͡╮༼ ಠДಠ ༽╭o͡͡͡━☆ﾟ.*･｡ﾟ⠀Star Magic 2
༼∩✿ل͜✿༽⊃━☆ﾟ. * ･ ｡ﾟ⠀Star Magic 3
༼(∩ ͡°╭͜ʖ╮͡ ͡°)༽⊃━☆ﾟ. * ･ ｡ﾟ⠀Star Magic 4
ᕦ( ✿ ⊙ ͜ʖ ⊙ ✿ )━☆ﾟ.*･｡ﾟ⠀Star Magic 5
(∩｀-´)⊃━☆ﾟ.*･｡ﾟ⠀Star Magic 6
༼∩☉ل͜☉༽⊃━☆ﾟ. * ･ ｡ﾟ⠀Star Magic 7
╰( ͡° ͜ʖ ͡° )つ──☆*:・ﾟ⠀Star Magic 8
(∩ ͡° ͜ʖ ͡°)⊃━☆ﾟ⠀Star Magic 9
੭•̀ω•́)੭̸*✩⁺˚⠀Star Magic 10
(੭ˊ͈ ꒵ˋ͈)੭̸*✧⁺˚⠀Star Magic 11
✩°｡⋆⸜(ू｡•ω•｡)⠀Star Magic 12
ヽ༼ຈل͜ຈ༽⊃─☆*:・ﾟ⠀Star Magic 13
╰(•̀ 3 •́)━☆ﾟ.*･｡ﾟ⠀Star Magic 14
(*’▽’)ノ＾—==ΞΞΞ☆⠀Star Magic 15
(੭•̀ω•́)੭̸*✩⁺˚⠀Star Magic 16
(っ・ω・）っ≡≡≡≡≡≡☆⠀Star Magic 17
. * ･ ｡ﾟ☆━੧༼ •́ ヮ •̀ ༽୨⠀Star Magic 18
༼∩ •́ ヮ •̀ ༽⊃━☆ﾟ. * ･ ｡ﾟ⠀Star Magic 19
(⊃｡•́‿•̀｡)⊃━☆ﾟ.*･｡ﾟ⠀Star Magic 20
(○´･∀･)o<<<<･。:*ﾟ<+．⠀Star Magic 21
＝＝＝＝☆┣o(´(００)｀ )⠀Star Magic 22
★≡≡＼（`△´＼）⠀Star Magic 23
( ◔ ౪◔)⊃━☆ﾟ.*・⠀Star Magic 24
彡ﾟ◉ω◉ )つー☆*⠀Star Magic 25
(☆_・)・‥…━━━★⠀Star Magic 26
(つ◕౪◕)つ━☆ﾟ.*･｡ﾟ⠀Star Magic 27
(つ˵•́ω•̀˵)つ━☆ﾟ.*･｡ﾟ҉̛༽̨҉҉ﾉ⠀Star Magic 28
✩°｡⋆⸜(ू˙꒳​˙ )⠀Star Magic 29
╰( ⁰ ਊ ⁰ )━☆ﾟ.*･｡ﾟ⠀Star Magic 30
(-_-)~~~○━━━━━☆)ﾟOﾟ)⠀Star Magic 31
(/￣ー￣)/‥∵:*:☆*゜★。：：＊☆⠀Star Magic 32
(*￣ー￣*)/~~☆’.･.･:★’.･.･:☆’.･.･:★⠀Star Magic 33
(ﾉ｀ゝ(ｪ)・)ﾉ･*:..｡o○☆*ﾟ+.☆｡+ﾟ⠀Star Magic 34
(ﾉ<><<ω<<<<)ﾉ :｡･:*:･ﾟ’★,｡･:*:♪･ﾟ’☆⠀Star Magic 35
!!(*ﾉ´∀｀)ﾉ‥‥…━━━━━☆⠀Star Magic 36
(┛｀Д´)┛・‥…━━━★)´∀｀ﾉ)ﾉ⠀Star Magic 37
(σ´Д｀)σ・・・・…━━━━☆⠀Star Magic 38
(∩,,◕◞౪◟◕)⊃━☆+ ﾟ .+ .ﾟ.ﾟ｡ ﾟ ｡. +ﾟ ｡ﾟ.ﾟ｡☆*｡｡ . ｡ o .｡ﾟ｡.o｡* ｡ .｡⠀Star Magic 39
(❀∩´◔‿ゝ◔`⑅)⊃―☆　*’“*:.｡. .｡.:*･゜ﾟ･♡♪+*.⠀Star Magic 40
(＠・｀ω・)v・・・．．．…━━━☆⠀Star Magic 41
＼_(￣、￣ 彡 ￣ー￣)_／ －☆・　・　・　‥……━━●⠀Star Magic 42
( ╹◡╹)っー’･*:.｡. .｡.:*･゜ﾟ･* ξ(╹-╹｡ζ⠀Star Magic 43
（＃￣□￣）＾ｏ―∈‥・・━━━━━━━☆⠀Star Magic 44
(ノﾟ∀ﾟ)ノ⌒･*:.｡. .｡.:*･゜ﾟ･*☆⠀Star Magic 45
(｀・ω・)メ＝＝＝＝＝＝＝＝＝＝＝*<’*’<☆⠀Star Magic 46
!!(ﾉﾟﾛﾟ)o･：*‥…━━━☆)ﾟ3ﾟ(★━━━…‥*：･o(ﾟﾛﾟヽ)⠀Star Magic 47
(´ﾉ･ω･｀)ﾉ・‥…━━━★ﾟ+.・‥…━━━★ﾟ+.・‥…━━━★ﾟ+⠀Star Magic 48
（ノ・＿・）．．．．．．━━━━━━━　☆－＼☆（・＿＼）⠀Star Magic 49
炎炎炎炎☆┣o(･ω･ )⠀Fire Magic 1
(*｀□)<<<<炎炎炎炎⠀Fire Magic 2
(∩｀-´)⊃━炎炎炎炎炎⠀Fire Magic 3
(ﾉ･ｪ･)ﾉ –==≡炎炎炎炎炎炎炎炎ヽ(ﾟД~ )ﾉ炎炎炎⠀Fire Magic 4
(ﾉ≧∀≦)ﾉ・‥…炎炎炎炎炎炎炎炎⠀Fire Magic 5
ᕦ( ✿ ⊙ ͜ʖ ⊙ ✿ )━炎炎炎炎炎炎炎炎⠀Fire Magic 6
(∩ ͡° ͜ʖ ͡°)⊃━炎炎炎炎炎炎炎炎⠀Fire Magic 7
ヽ༼ຈل͜ຈ༽⊃─炎炎炎炎炎炎炎炎⠀Fire Magic 8
(੭•̀ω•́)੭̸*炎炎炎炎炎炎炎⠀Fire Magic 9
(┛｀Д´)┛・‥…炎炎炎炎炎炎炎⠀Fire Magic 10
ପ(⚈᷉ʙ⚈᷉)੭̸୫炎炎炎炎炎炎炎⠀Fire Magic 11
╰( ´・ω・)つ──☆✿✿✿✿✿✿⠀Flower Magic 1
(∩｀-´)⊃━✿✿✿✿✿✿⠀Flower Magic 2
(*’▽’)ノ＾—==ΞΞΞ✿✿✿✿✿⠀Flower Magic 3
(∩ ͡° ͜ʖ ͡°)⊃━✿✿✿✿✿✿⠀Flower Magic 4
(⊃｡•́‿•̀｡)⊃━✿✿✿✿✿✿⠀Flower Magic 5
~●)))))☆Ю(￣ー￣*)⠀Bomb Magic 1
*~●))))☆O=(`_` )⠀Bomb Magic 2
＼_(-_- 彡 -_-)_／☆･ ･ ･ ‥……━━●~*⠀Bomb Magic 3
＼_(ﾟｰﾟ*彡*ﾟ▽ﾟ)_/☆･ ･･･‥…━（（●~*⠀Bomb Magic 4
(。・ω・)＝《《≠≠≠≠≠≠≠≠〇⠀Energy Balls 1
༼つಠ益ಠ༽つ ─=≡ΣO))⠀Energy Balls 2
<<<<(¬＿¬<<<<) o<<<<(¬＿¬<<<<) (<><<0o0)<><<==============O⠀Energy Balls 3
☆(ﾉ^ω^)ﾉ‥‥‥…━━━━〇　(^Ο^)⠀Energy Balls 4
(∩ ͡° ͜ʖ ͡°)⊃━☆─=≡Σ((( つ◕ل͜◕)つ⠀Miscellaneous Magic 1
(∩ᄑ_ᄑ)⊃━☆ﾟ*･｡*･:≡( ε:)⠀Miscellaneous Magic 2
ପ(⚈᷉ʙ⚈᷉)੭̸୫൦⃛⠀Miscellaneous Magic 3
∋(。・”・)_†:*.<”.*・<・⠀Miscellaneous Magic 4
☆ﾟ･*:.｡.☆†_(ﾟ▽ﾟ*)β⠀Miscellaneous Magic 5
☆━━━━━━…‥*：･†_(‘ｰ’*)β⠀Miscellaneous Magic 6
¯\_(ツ)_/¯⠀Shrug Faces 1
¯\(°_o)/¯⠀Shrug Faces 2
<(ツ)_/¯⠀Shrug Faces 3
¯\_ಠ_ಠ_/¯⠀Shrug Faces 4
¯\_(⌣̯̀⌣́)_/¯⠀Shrug Faces 5
˘\_( õ ‹3 ó)_/˘⠀Shrug Faces 6
¯\(◉‿◉)/¯⠀Shrug Faces 7
¯\_(☯෴☯)_/¯⠀Shrug Faces 8
乁[ᓀ˵▾˵ᓂ]ㄏ⠀Shrug Faces 9
¯\(©¿©) /¯⠀Shrug Faces 10
へ‿(ツ)‿ㄏ⠀Shrug Faces 11
¯\_▒ – ﹏ – ▒_/¯⠀Shrug Faces 12
¯\_( ◉ 3 ◉ )_/¯⠀Shrug Faces 13
¯\_〳 •̀ o •́ 〵_/¯⠀Shrug Faces 14
¯\_( ͠° ͟ʖ °͠ )_/¯⠀Shrug Faces 15
¯\_༼ᴼل͜ᴼ༽_/¯⠀Shrug Faces 16
¯\_༼ ି ~ ି ༽_/¯⠀Shrug Faces 17
¯\_༼ ಥ ‿ ಥ ༽_/¯⠀Shrug Faces 18
¯\_(⊙_ʖ⊙)_/¯⠀Shrug Faces 19
¯\_| ✖ 〜 ✖ |_/¯⠀Shrug Faces 20
¯\_▐ ☯ ︿ ☯ ▐_/¯⠀Shrug Faces 21
¯\_╏ ՞ ︿ ՞ ╏_/¯⠀Shrug Faces 22
¯\_(⊙︿⊙)_/¯⠀Shrug Faces 23
¯\_ȌᴥȌ_/¯⠀Shrug Faces 24
¯\_ʘᗜʘ_/¯⠀Shrug Faces 25
¯\_ȌᴥȌ_/¯⠀Shrug Faces 26
┻━┻ ︵ ¯\ (ツ)/¯ ︵ ┻━┻⠀Shrug Faces 27
＼(<´□｀)/⠀Straight Arms 1
＼（〇_ｏ）／⠀Straight Arms 2
＼⍩⃝／⠀Straight Arms 3
＼| ￣ヘ￣|／⠀Straight Arms 4
┐(‘～`；)┌⠀┐and ┌ Arms 1
┐(￣ー￣)┌⠀┐and ┌ Arms 2
┐(￣ヮ￣)┌⠀┐and ┌ Arms 3
┐(´-｀)┌⠀┐and ┌ Arms 4
┐( ˘_˘)┌⠀┐and ┌ Arms 5
┐( ∵ )┌⠀┐and ┌ Arms 6
┐(￣ヘ￣)┌⠀┐and ┌ Arms 7
┐(´∀｀)┌⠀┐and ┌ Arms 8
┐(´∇｀)┌⠀┐and ┌ Arms 9
┐(´д｀)┌⠀┐and ┌ Arms 10
┐(‘д’)┌⠀┐and ┌ Arms 11
┐(ﾟ～ﾟ)┌⠀┐and ┌ Arms 12
┐(~ー~<)┌⠀┐and ┌ Arms 13
┐(<Ծ⌓Ծ<)┌⠀┐and ┌ Arms 14
┐(･ิL_･ิ)┌⠀┐and ┌ Arms 15
(┐◎_◎┌)⠀┐and ┌ Arms 16
┐(´(エ)｀)┌⠀┐and ┌ Arms 17
┐(´･c_･｀ <)┌⠀┐and ┌ Arms 18
┐(●’v’)┌⠀┐and ┌ Arms 19
┐（´ー）┌⠀┐and ┌ Arms 20
┐(´Д｀┌⠀┐and ┌ Arms 21
┐(ﾟ⊇ﾟ)┌⠀┐and ┌ Arms 22
┐(‘～`<)┌⠀┐and ┌ Arms 23
┐|￣ρ￣✿|┌⠀┐and ┌ Arms 24
┐(；´・Д・`)┌⠀┐and ┌ Arms 25
┐(´ｰ｀)┌⠀┐and ┌ Arms 26
(「ఠωఠ)「⠀┐and ┌ Arms 27
┗(･ω･<)┛⠀Raised up 90 Degree Arms 1
┗┃・ ■ ・┃┛⠀Raised up 90 Degree Arms 2
┗┐ヽ(′Д、`*)ﾉ┌┛⠀Raised up 90 Degree Arms 3
└(・-・)┘⠀Raised up 90 Degree Arms 4
└(・。・)┘⠀Raised up 90 Degree Arms 5
≡└( ‘o’)┘≡⠀Raised up 90 Degree Arms 6
╚(•⌂•)╝⠀Raised up 90 Degree Arms 7
(┛ﾟΘﾟ)┛⠀Raised up 90 Degree Arms 8
┗(；´Д｀)┛⠀Raised up 90 Degree Arms 9
╚༼ ຈل͜ຈ༽╝⠀Raised up 90 Degree Arms 10
┗|*´Д｀|┛⠀Raised up 90 Degree Arms 11
└[ ◕ 〜 ◕ ]┘⠀Raised up 90 Degree Arms 12
╚═[ ˵ •̀ ﹏ •́ ˵ ]═╝⠀Raised up 90 Degree Arms 13
└(◉◞౪◟◉)┘⠀Raised up 90 Degree Arms 14
┗[~▿~]┛⠀Raised up 90 Degree Arms 15
┗[•͡˘◞౪◟•͡˘]┛⠀Raised up 90 Degree Arms 16
L(´▽｀L )⠀Raised up 90 Degree Arms 17
└((´э｀))┘⠀Raised up 90 Degree Arms 18
└( ͡° ︿ °͡ )┘⠀Raised up 90 Degree Arms 19
(」*´∇｀)」⠀Raised up 90 Degree Arms 20
└། ๑ _ ๑ །┘⠀Raised up 90 Degree Arms 21
L(ﾟ皿ﾟﾒ)」⠀Raised up 90 Degree Arms 22
└(ﾟ∀ﾟ└))⠀Raised up 90 Degree Arms 23
((┘ﾟ∀ﾟ)┘⠀Raised up 90 Degree Arms 24
┗|´Д｀*|┛⠀Raised up 90 Degree Arms 25
┗┐(*´Д｀*)┌┛⠀Raised up 90 Degree Arms 26
【┛ﾟ,_ゝﾟ】┛⠀Raised up 90 Degree Arms 27
L(ﾟ益ﾟL)⠀Raised up 90 Degree Arms 28
└|ﾟ益ﾟ└|⠀Raised up 90 Degree Arms 29
┗(´ι_,｀*<)┛⠀Raised up 90 Degree Arms 30
└(°ᴥ°)┘⠀Raised up 90 Degree Arms 31
└། : ᓀ ل͜ ᓂ : །┘⠀Raised up 90 Degree Arms 32
└╏ ʘ ▾ ʘ ╏┘⠀Raised up 90 Degree Arms 33
╚ |░▤﹏▤░|╝⠀Raised up 90 Degree Arms 34
└║ ՞ ౪ ՞ ║┘⠀Raised up 90 Degree Arms 35
└། – 〜 – །┘⠀Raised up 90 Degree Arms 36
└(՞▃՞ └)⠀Raised up 90 Degree Arms 37
└༼ •́ ͜ʖ •̀ ༽┘⠀Raised up 90 Degree Arms 38
└( * ᴼ ں ᴼ * )┘⠀Raised up 90 Degree Arms 39
└[ ☉ ل͟ ☉ ]┘⠀Raised up 90 Degree Arms 40
┗|´Д｀*||*´Д｀|┛⠀Raised up 90 Degree Arms 41
┗|｀O´|┛⠀Raised up 90 Degree Arms 42
┗(・o・)┛⠀Raised up 90 Degree Arms 43
└(oﾟ∀ﾟo)┘⠀Raised up 90 Degree Arms 44
(」*´ｪ｀)」⠀Raised up 90 Degree Arms 45
┗(｀皿´)┛⠀Raised up 90 Degree Arms 46
└(○｀ε´○)┘⠀Raised up 90 Degree Arms 47
└( ՞ ~ ՞ )┘⠀Raised up 90 Degree Arms 48
┗| ຶӫ ຶ|┛⠀Raised up 90 Degree Arms 49
╮ (. ❛ ᴗ ❛.) ╭⠀╮and╭ Style Arms 1
╮(＾▽＾)╭⠀╮and╭ Style Arms 2
╮(─▽─)╭⠀╮and╭ Style Arms 3
╮(•˘︿ ˘•)╭⠀╮and╭ Style Arms 4
╮(╯▽╰)╭⠀╮and╭ Style Arms 5
╮(╯-╰”)╭⠀╮and╭ Style Arms 6
╮(ਊ◞‸◟ਊ|||)╭⠀╮and╭ Style Arms 7
╮( ꒪౪꒪)╭⠀╮and╭ Style Arms 8
╮(╯ل͜╰)╭⠀╮and╭ Style Arms 9
╮(ﾟェﾟ*)╭⠀╮and╭ Style Arms 10
╮(▰´△`)╭⠀╮and╭ Style Arms 11
╰(　´◔　ω　◔ `)╯⠀╰ and ╯Style Arms 1
╰། ﹒ _ ﹒ །╯⠀╰ and ╯Style Arms 2
╰╏ ◉ 〜 ◉ ╏╯⠀╰ and ╯Style Arms 3
╰( ͡’◟◯ ͡’)╯⠀╰ and ╯Style Arms 4
╰▐ ◑ ‸ ◑ ▐╯⠀╰ and ╯Style Arms 5
╰| ⊡ _ ⊡ |╯⠀╰ and ╯Style Arms 6
ヽ( ´¬`)ノ⠀Curved Arms 1
ヽ(　￣д￣<)ノ⠀Curved Arms 2
ヽ（・＿・；)ノ⠀Curved Arms 3
ヽ(。_°)ノ⠀Curved Arms 4
ヽ(‘ー`)ノ⠀Curved Arms 5
ヾ(*´ー`)ノ⠀Curved Arms 6
ヽ（*ω。）ノ⠀Curved Arms 7
ヾ(´￢｀)ﾉ⠀Curved Arms 8
ヽ(´ー`)ﾉ⠀Curved Arms 9
ヾ(´A｀)ノﾟ⠀Curved Arms 10
ヽ(ー_ー )ノ⠀Curved Arms 11
ヾ(ｏ･ω･)ﾉ⠀Curved Arms 12
ヽ(｡･c_,･｡)ﾉﾞ⠀Curved Arms 13
ヽ(.◕ฺˇд ˇ◕ฺ<)ﾉ⠀Curved Arms 14
ヽ(´ー｀)ノ⠀Curved Arms 15
乁( ◔ ౪◔)ㄏ⠀乁 andㄏStyle Arms 1
乁༼ ͒ ╭͜ʖ╮ ͒ ༽ㄏ⠀乁 andㄏStyle Arms 2
乁▐ ˘ o ˘ ▐ㄏ⠀乁 andㄏStyle Arms 3
ㄟ( θ﹏θ)厂⠀乁 andㄏStyle Arms 4
乁║ ͡° ౪ °͡ ║ㄏ⠀乁 andㄏStyle Arms 5
乁༼☯‿☯✿༽ㄏ⠀乁 andㄏStyle Arms 6
乁( •_• )ㄏ⠀乁 andㄏStyle Arms 7
乁▐ * ◖ ‸ ◗ * ▐ㄏ⠀乁 andㄏStyle Arms 8
乁⁞ ි _ʖ ි ⁞ㄏ⠀乁 andㄏStyle Arms 9
乁⁞ ◑ ͜ر ◑ ⁞ㄏ⠀乁 andㄏStyle Arms 10
乁༼ ☯ ◯ ☯ ༽ㄏ⠀乁 andㄏStyle Arms 11
乁[ ୖ 〰 ୖ ]ㄏ⠀乁 andㄏStyle Arms 12
乁( . ര ʖ̯ ര . )ㄏ⠀乁 andㄏStyle Arms 13
乁░ ‾́ 〰 ‾́ ░ㄏ⠀乁 andㄏStyle Arms 14
乁║ ˙ 益 ˙ ║ㄏ⠀乁 andㄏStyle Arms 15
乁[ ◕ ᴥ ◕ ]ㄏ⠀乁 andㄏStyle Arms 16
乁╏ ಠ ┏ل͜┓ ಠ ╏ㄏ⠀乁 andㄏStyle Arms 17
乁( ⁰͡ Ĺ̯ ⁰͡ ) ㄏ⠀乁 andㄏStyle Arms 18
乁༼ Ɵ͆ ل͜ Ɵ͆ ༽ㄏ⠀乁 andㄏStyle Arms 19
乁| ･ 〰 ･ |ㄏ⠀乁 andㄏStyle Arms 20
ƪ(Ơ̴̴̴̴̴̴͡.̮Ơ̴̴͡)ʃ⠀ƪ and ʃ Style Arms 1
ƪ(‾ε‾“)ʃ⠀ƪ and ʃ Style Arms 2
ʅ(｡◔‸◔｡)ʃ⠀ƪ and ʃ Style Arms 3
ʅ(｡Ő౪Ő｡)ʃ⠀ƪ and ʃ Style Arms 4
ƪ(•̃͡ε•̃͡)∫ʃ⠀ƪ and ʃ Style Arms 5
ヾ(❛ε❛“)ʃ⠀ƪ and ʃ Style Arms 6
ƪ(“╰ _ ╯ )ʃ⠀ƪ and ʃ Style Arms 7
ʅ(´՞ਊ ՞ )ʃ⠀ƪ and ʃ Style Arms 8
ʅ(´⊙◞⊱◟⊙`)ʃ⠀ƪ and ʃ Style Arms 9
ƪ(‾(••)‾”)ʃ⠀ƪ and ʃ Style Arms 10
ʅ（‾◡◝）ʃ⠀ƪ and ʃ Style Arms 11
ʅ（‾‸◝）ʃ⠀ƪ and ʃ Style Arms 12
ƪ(~ε~“)ʃ⠀ƪ and ʃ Style Arms 13
ʅ（ ‾⊖◝）ʃ⠀ƪ and ʃ Style Arms 14
ʅʕ•ᴥ•ʔʃ⠀ƪ and ʃ Style Arms 15
ʅ（´◔౪◔）ʃ⠀ƪ and ʃ Style Arms 16
三三三ʅ(；◔౪◔)ʃ⠀ƪ and ʃ Style Arms 17
ʅ( ‾⊖◝)ʃ⠀ƪ and ʃ Style Arms 18
ʅ(‾◡◝)ʃ⠀ƪ and ʃ Style Arms 19
ʅ(◔౪◔ ) ʃ⠀ƪ and ʃ Style Arms 20
ƪƪ(•̃͡ε•̃͡)(•̃͡ε•̃͡)∫ʃ⠀ƪ and ʃ Style Arms 21
ʅฺ(・ω・。)ʃฺ⠀ƪ and ʃ Style Arms 22
ʅ(⑅*´◡`)ʃ⠀ƪ and ʃ Style Arms 23
ʅ(´-ω-`)ʃ⠀ƪ and ʃ Style Arms 24
ʅ(*´◡`)ʃ⠀ƪ and ʃ Style Arms 25
ƪ(΄◉◉‵<)))ʃ⠀ƪ and ʃ Style Arms 26
ʅ（ ◜‸‾）ʅ（‾‸◝）ʃ（‾‸◝ ）ʃ⠀ƪ and ʃ Style Arms 27
ɿ(｡･ɜ･)ɾⓌⓗⓨ?⠀Words 1
ɿ(｡･ɜ･)ɾⓌⓗⓐⓣ？⠀Words 2
(｢๑•₃•)｢ ʷʱʸ?⠀Words 3
o͡͡͡͡͡͡╮꒰♡∇♡*꒱╭o͡͡͡͡͡͡⠀Complex 1
o͡͡͡͡͡͡͡͡͡͡͡͡͡͡╮(๑θωθ๑)╭o͡͡͡͡͡͡͡͡͡͡͡͡͡͡⠀Complex 2
˚̑̑̑̑̑༾(-᷄◞८̻◟-᷅)༿˚̑̑̑̑̑⠀Complex 3
ʅ(◔.̸̸̸̸̸̸̸̸̸̸̸̸̸̸̸̸̸̸̸̸̸̸̸̸̨̨̨̨̨̨̨̨̨̨̨̨.̸̸̨̨◔)ʃ⠀Complex 4
Щ(´ω｀Щ)⠀Miscellaneous 1
（ｖ＾＿＾）ｖ⠀Miscellaneous 2
╮ (☆-_ ⊙<)ゞ⠀Miscellaneous 3
ヽ(´～｀；）⠀Miscellaneous 4
ヽ（´ー｀）┌⠀Miscellaneous 5
٩(-̮̮̃-̃)۶⠀Miscellaneous 6
٩(-̮̮̃•̃)۶⠀Miscellaneous 7
p(´⌒｀｡q)⠀Miscellaneous 8
༽΄◞ิ౪◟ิ‵༼⠀Miscellaneous 9
৲( ˃੭̴˂)৴⠀Miscellaneous 10
¶(⁄⁒∖)⁋⠀Miscellaneous 11
⸜₍⚛•⌣•⚛₎⸝⠀Miscellaneous 12
ᘛᐡᐤᐡᘚ⠀Miscellaneous 13
₍₍ ◟(•ૅ ॄ •ૅ๑)◞ ₎₎⠀Miscellaneous 14
⎩ ♨ᴥ♨ ⎭⠀Miscellaneous 15
༾(◉◞હ̱◟◉)༿⠀Miscellaneous 16
J( ‘ｰ`)し⠀Miscellaneous 17
⸂⸂⸜(ੱ௰ੱ๑)⸝⸃⸃⠀Miscellaneous 18
ɿ (•᷄દ•᷅)⠀Miscellaneous 19
✌⎦◜◦¬◦◝⎣✌⠀Miscellaneous 20
|´Ｕ｀●)r”⠀Miscellaneous 21
⋋〳 ᵕ _ʖ ᵕ 〵⋌⠀Miscellaneous 22
ᕕ| ͡■ ﹏ ■͡ |و⠀Miscellaneous 23
щ(´^｀щ)⠀Miscellaneous 24
￣(=＾ー＾=)￣⠀Miscellaneous 25
ી(⊙ு⊙)િ⠀Miscellaneous 26
（＾～＾）⠀Miscellaneous 27
( ᵌ ⍨ ᵌ )⠀Miscellaneous 28
⋋〳 ᵕ _ʖ ᵕ 〵⋌⠀Miscellaneous 29
( ͡ _ ͡°)ﾉ⚲⠀Miscellaneous 30
⋋| ◉ ͟ʖ ◉ |⋌⠀Miscellaneous 31
⋋|།<#8217<͡ᴼ╭͜ʖ╮͡ᴼ<#8217<།|⋌⠀Miscellaneous 32
@・ꈊ・@⠀@ Style Ears 1
@( o･ω･)@⠀@ Style Ears 2
@( o･ｪ･)@⠀@ Style Ears 3
@( o･ꎴ･)@⠀@ Style Ears 4
@( oóωò)@⠀@ Style Ears 5
@( oóꎴò)@⠀@ Style Ears 6
@(｡･o･)@⠀@ Style Ears 7
@(*^ｪ^)@⠀@ Style Ears 8
@(/o･ｪ･o)@/⠀@ Style Ears 9
@(o･ｪ･)@⠀@ Style Ears 10
@(o・ェ・)@ノ⠀@ Style Ears 11
@(o･ｪ･o)@⠀@ Style Ears 12
└@(･ｪ･)@┐⠀@ Style Ears 13
@(ᵕ.ᵕ)@⠀@ Style Ears 14
@(。・o・)@⠀@ Style Ears 15
@(。・0・)@⠀@ Style Ears 16
@(。・-・)@⠀@ Style Ears 17
@(。・。・)@⠀@ Style Ears 18
@(o･ｪ･)@ﾉ~”⠀@ Style Ears 19
@(｡･◇･)@⠀@ Style Ears 20
@(｡･｡･)@⠀@ Style Ears 21
@(｡･_･)@⠀@ Style Ears 22
@(･ｪ･｡)@⠀@ Style Ears 23
[emai<<#160<pro<ec<ed]⠀@ Style Ears 24
(･ｪ･ﾒ)@⠀@ Style Ears 25
@(<･ｪ･)@/⠀@ Style Ears 26
ヾ@(o･ｪ･o)@⠀@ Style Ears 27
@(´･ｪ･`)@⠀@ Style Ears 28
○Ｏo。⠀@ Style Ears 29
[emai<<#160<pro<ec<ed]⠀@ Style Ears 30
(-ェ-)@ノ⠀@ Style Ears 31
○Ｏo。⠀@ Style Ears 32
[emai<<#160<pro<ec<ed]⠀@ Style Ears 33
(-ェ-)@ノ~~~⠀@ Style Ears 34
@(<･ｪ･)@ﾉ⠀@ Style Ears 35
@(･o･)@⠀@ Style Ears 36
@(･0･)@⠀@ Style Ears 37
@(･ェ･)@⠀@ Style Ears 38
@(･-･)@⠀@ Style Ears 39
“(@･｡･@)/⠀@ Style Ears 40
@(・●・)@⠀@ Style Ears 41
@( ◕ x ◕ )@⠀@ Style Ears 42
ゞ@(o･ｪ･)@人@(･ｪ･o)@⠀@ Style Ears 43
ヽ@(*^ｪ^)@入@(･ｪ･o)@ﾉ⠀@ Style Ears 44
@(o･ｪ･)ﾉ☆@(*_ _)@⠀@ Style Ears 45
|･ｪ･)@ |ｪ･)@ |･)@ |⠀@ Style Ears 46
………..。。。ﾍ@( o･ｪ･)@￣[猿]￣@( o･ｪ･)@ﾉ⠀@ Style Ears 47
C= C= C= ⠀@ Style Ears 48
[emai<<#160<pro<ec<ed]⠀@ Style Ears 49
(/o･ｪ･o)@/⠀@ Style Ears 50
⊂((・⊥・))⊃⠀⊂ Style Ears 1
⊂((*＞⊥σ))⊃⠀⊂ Style Ears 2
⊂((*σ⊥σ*))⊃⠀⊂ Style Ears 3
⊂((〃￣⊥￣〃))⊃⠀⊂ Style Ears 4
⊂((∂⊥<<<<*))⊃⠀⊂ Style Ears 5
⊂((＞⊥＜))⊃⠀⊂ Style Ears 6
⊂((≧⊥≦))⊃⠀⊂ Style Ears 7
⊂((δ⊥δ))⊃⠀⊂ Style Ears 8
⊂((υ⊥υ))⊃⠀⊂ Style Ears 9
⊂((о∂⊥∂о))⊃⠀⊂ Style Ears 10
⊆ಠ ω ಠ⊇⠀⊂ Style Ears 11
⊆◍益◍⊇⠀⊂ Style Ears 12
⊂（（〃￣ー￣〃））⊃⠀⊂ Style Ears 13
⊂((o・ェ・))⊃ノ⠀⊂ Style Ears 14
⊂((。・o・))⊃⠀⊂ Style Ears 15
⊂((。・。・))⊃⠀⊂ Style Ears 16
⊂((･o･))⊃⠀⊂ Style Ears 17
⊂((｡･◇･))⊃⠀⊂ Style Ears 18
⊂((ᵕ.ᵕ))⊃⠀⊂ Style Ears 19
⊂((。・-・))⊃⠀⊂ Style Ears 20
⊂(( o･ω･))⊃⠀⊂ Style Ears 21
（⊂((・⊥・))⊃）⠀⊂ Style Ears 22
⊂((〃’⊥’〃))⊃⠀⊂ Style Ears 23
⊆（⌒◎⌒）⊇⠀⊂ Style Ears 24
Ϛ⃘๑•͡ .̫•๑꒜⠀Ϛ⃘๑•͡ .̫•๑꒜ Style Monkeys 1
Ϛ⃘๑•͡ .̫•๑꒜✧⠀Ϛ⃘๑•͡ .̫•๑꒜ Style Monkeys 2
Ϛ⃘<•͡ .̫•๑꒜྆྆⠀Ϛ⃘๑•͡ .̫•๑꒜ Style Monkeys 3
Ϛ⃘๑•͡ ི.ྀ̫•๑꒜⠀Ϛ⃘๑•͡ .̫•๑꒜ Style Monkeys 4
Ϛ⃘๑•͡ ི.ྀ̫•๑꒜✧⠀Ϛ⃘๑•͡ .̫•๑꒜ Style Monkeys 5
Ϛ⃘๑•͡ .̫•๑꒜ღ⃛⠀Ϛ⃘๑•͡ .̫•๑꒜ Style Monkeys 6
Ϛ⃘๑•͡ ི.ྀ̫•๑꒜ღ⃛⠀Ϛ⃘๑•͡ .̫•๑꒜ Style Monkeys 7
Ⴚტ◕‿◕ტჂ⠀Ϛ⃘๑•͡ .̫•๑꒜ Style Monkeys 8
Ϛ⃘๑•͡ .̫•๑꒜♬♫⠀Ϛ⃘๑•͡ .̫•๑꒜ Style Monkeys 9
Ϛ⃘๑•͡ .̫•๑꒜⠀Ϛ⃘๑•͡ .̫•๑꒜ Style Monkeys 10
Ϛ⃘๑•͡ .̫•๑꒜ℒℴѵℯ❤⠀Ϛ⃘๑•͡ .̫•๑꒜ Style Monkeys 11
⁝⁞⁝⁞Ϛ⃘๑•͡ .̫•๑꒜☂⁝⁞⁝⁝⠀Ϛ⃘๑•͡ .̫•๑꒜ Style Monkeys 12
⁝⁞⁝⁞Ϛ⃘๑•͡ ི.ྀ̫•๑꒜☂⁝⁞⁝⁝⠀Ϛ⃘๑•͡ .̫•๑꒜ Style Monkeys 13
Ϛ•͇ꇵ͒•ོ͇Ͻ⠀Ϛ⃘๑•͡ .̫•๑꒜ Style Monkeys 14
((๑✧ꈊ✧๑))⠀Miscellaneous Monkeys 1
✧.*◌·͡˔·ོ◌*·✧⠀Miscellaneous Monkeys 2
(((ლ(͏ ͒ • ꈊ • ͒)ლ)))♡⠀Miscellaneous Monkeys 3
¶(⁄•˅̭•∖)⁋⠀Miscellaneous Monkeys 4
(๑• .̫ •๑)⠀Miscellaneous Monkeys 5
– =͟͟͞͞(●⁰ꈊ⁰● |||)⠀Miscellaneous Monkeys 6
ධ̢•͙ꄃ̑•͙ຄ̏ධ̡⠀Miscellaneous Monkeys 7
☾ठ ੁठ☽⠀Miscellaneous Monkeys 8
((ᵒꈊᵒ᷅ ू‖))՞⠀Miscellaneous Monkeys 9
ᗧʻ̑ ˙̫ ʻ̑ᗤ⍝⠀Miscellaneous Monkeys 10
₢⦿͡ ˒̫̮ ⦿͡ꀣ⠀Miscellaneous Monkeys 11
₢ຈ▿ຈꀣ⠀Miscellaneous Monkeys 12
₢⦿͡㍕⦿͡ꀣ⠀Miscellaneous Monkeys 13
⸉ᘓ◎⃝ᆺ◎⃝ᘐ⸊⠀Miscellaneous Monkeys 14
♪( ･ｪ･)ﾂ彡(ﾟДﾟ?)⠀Miscellaneous Monkeys 15
“ヽ(´▽｀)ノ”⠀Singing 1
ヽ(´Д｀ヽ⠀Singing 2
（*´▽｀*）⠀Singing 3
(*￣0￣)θ～♪⠀Singing 4
(*゜▽゜ノノ゛☆⠀Singing 5
(*⌒▽⌒*)θ～♪⠀Singing 6
(´△｀)♪⠀Singing 7
(´▽｀)ノ♪⠀Singing 8
(´0ﾉ｀*)⠀Singing 9
（^[]＾）／♪⠀Singing 10
（＾Ｏ＾☆♪⠀Singing 11
(ﾉ´▽｀)ﾉ♪⠀Singing 12
(ﾉ<><< ◇ <<<<)ﾉ♪⠀Singing 13
｢(<´Σ ｀〃)ヘ⠀Singing 14
＼(^o^)／⠀Singing 15
≧(´▽｀)≦⠀Singing 16
┐(・。・┐) ♪⠀Singing 17
♪( ´θ｀)ノ⠀Singing 18
♪(o^0^)o♪⠀Singing 19
♪♪(o*゜∇゜)o～♪♪⠀Singing 20
ヽ(○´∀`)ﾉ♪⠀Singing 21
☆L(´▽｀L )♪⠀Singing 22
♬♫♪◖(●。●)◗♪♫♬⠀Singing 23
ヾ(・◇・)ﾉθ～♪⠀Singing 24
ヾ(´□｀* )ノ⠀Singing 25
ヽ(´▽｀；)/♪⠀Singing 26
ヾ(´▽｀<)ゝ⠀Singing 27
ヾ(´〇｀)ﾉ⠀Singing 28
ヾ(´ρ｀)〃⠀Singing 29
ᒄ₍⁽ˆ⁰ˆ⁾₎ᒃ♪♬⠀Singing 30
( ง ´◇｀)ง♪⠀Singing 31
♪(๑ᴖ◡ᴖ๑)♪⠀Singing 32
♪~♪ ヽ໒(⌒o⌒)७ﾉ ♪~♪⠀Singing 33
♪٩(✿′ᗜ‵✿)۶♪⠀Singing 34
꒰๑˃꒵˂꒱◞ ♪⋆ฺ｡⠀Singing 35
٩(ó｡ò۶ ♡)))♬⠀Singing 36
♪(o´▽｀o)ﾉ⠀Singing 37
♪!(^O^)y⠀Singing 38
♫ꉂ (๑¯ਊ¯)σ⠀Singing 39
♪ *ꈍ﹃ꈍ)ﾉ⠀Singing 40
(*’▽’*)♪⠀Singing 41
ヾ(＾。^*)♪～⠀Singing 42
(ฅˊ̱˂˃ˋ̱ฅ)♪⠀Singing 43
( ๑˃̶ ॣꇴ ॣ˂̶)♪⁺⠀Singing 44
(்͂ॢ⁰்͂ॢ)३३३∾♪⠀Singing 45
♪ꉂ ꊚ(ꈍꄱꆧ ) ♬♪⠀Singing 46
ヽ(≝∀≝)ﾉ ー♬⠀Singing 47
♪~♪ d(⌒o⌒)b♪~♪⠀Singing 48
♪♪ｖ(⌒ｏ⌒)ｖ♪♪⠀Singing 49
♪L(´▽｀L )♪⠀Singing 50
♪(ﾉ´∀｀*)ﾉ⠀Singing 51
♪(*´○｀)o¶~~♪⠀Singing 52
♪♪♪ ヽ(･ˇ∀ˇ･ゞ)⠀Singing 53
♪ヾ(＾Д＾*)ノ⠀Singing 54
ヾ（〃＾∇＾）ﾉ♪⠀Singing 55
♪|´∀｀)ノ⠀Singing 56
♬♪♫ ヾ(*・。・)ﾉ ♬♪♫⠀Singing 57
♬♩♫♪☻(●´∀｀●)☻♪♫♩♬⠀Singing 58
ヽ｀、ヽ｀ヽヽ｀、ヽ｀ヽ(*￣o￣*)<><<ヽ｀、ヽ｀ヽ｀、ヽ｀ヽ⠀Singing 59
(；◔ิз◔ิ)～♪♬⠀Whistling 1
(˳˘ ɜ˘)˳ ♬♪♫⠀Whistling 2
（＾3＾♪⠀Whistling 3
˳/(˘ε ˘)♬♪♫⠀Whistling 4
♪(´ε｀ )⠀Whistling 5
♪₊(˘ᵋॢ ˘ॢ⌯)*·♫⠀Whistling 6
♪～(´ε｀　)⠀Whistling 7
ヽ(*´з｀*)ﾉ⠀Whistling 8
ヽ(´・｀)ﾉ⠀Whistling 9
♬˚‧◟₍◌′ ॄ‵◌₎◞•˚♬⠀Whistling 10
(०՞კ՞)४♬♪⠀Whistling 11
(*´σ з｀) ～♪⠀Whistling 12
♪～(￣、￣ )⠀Whistling 13
( ˭̴̵̶᷅ ᑦॄ ˭̴̵̶᷅ )~♫⠀Whistling 14
(๑ › ₃ ू‹)₋₃ ♪⠀Whistling 15
◖ฺ|´ ՙˬ`˶|◗·˳♪⁎˚♫⠀Whistling 16
♪(ﾉε｀●)⠀Whistling 17
◖ฺ|⌯˃̶₎₃₍˂̶ ॣ|◗·˳♪⁎˚♫⠀Whistling 18
(๑ › ₃ ू‹)₋₃ ৴ડેং੭♪⠀Whistling 19
(๑ˇεˇ๑)•*¨*•.¸¸♪⠀Whistling 20
༼ つ ◕3◕ ༽つ ♫♪♫⠀Whistling 21
((< =ﾟ３ﾟ=))～♪⠀Whistling 22
♪(‘εﾟ人)*.+゜⠀Whistling 23
♪(*ﾟ 3ﾟ)/~♪⠀Whistling 24
ヽ(´Д｀)人(´Д｀)人(´Д｀)ノ⠀Multiple People Enjoying Music Together 1
(((*°▽°*)八(*°▽°*)))♪⠀Multiple People Enjoying Music Together 2
♪ヽ( ⌒o⌒)人(⌒-⌒ )v ♪⠀Multiple People Enjoying Music Together 3
♬♩˂₍͔⁽ˆ⁰ˆ⁾₎͔˃ ͟͟͞͞≣͟ ͟͟͞͞˂₍͕⁽ˆ⁰ˆ⁾₎͕˃♪♫⠀Multiple People Enjoying Music Together 4
( ︶⌢︶ ‘’) ⊰ ♬ ⊱ ( ⌣  ⌣)⠀Multiple People Enjoying Music Together 5
♫(♡◖ฺ◡ฺ◗ฺ)♡(ฺ◖ฺ◡ฺ◗ฺ♡)♫⠀Multiple People Enjoying Music Together 6
♪～(◔◡◔ิ)人(╹◡╹๑)～♪⠀Multiple People Enjoying Music Together 7
♪♪)<><<ш=(^。^ )⠀Musical Instruments and Devices 1
♪♫ ◟¶(⁄•˅̥•∖)⁋ ♪♬⠀Musical Instruments and Devices 2
₍₍¶(ू⁄›˅̮‹ू∖)⁋₎₎ ♪♬⠀Musical Instruments and Devices 3
◙▒◙♫♩♬⠀Musical Instruments and Devices 4
¶(⁄∘˅̻∘∖)⁋⠀Musical Instruments and Devices 5
˓˓▂▂⃔⃕ ू(⋅⃝ ௰͡ ⋅⃝⁎◗ू♪♬⠀Musical Instruments and Devices 6
(*´∀｀)ﾉ☊ฺ ▂ฺ ▃ฺ ▄ฺ ▅ฺ ▆ฺ ▇ฺ █⠀Musical Instruments and Devices 7
ʕ•̫͡•ʔ♬✧⠀Regular Emoticons with Musical Notes 1
Ϛ⃘๑•͡ .̫•๑꒜♬♫⠀Regular Emoticons with Musical Notes 2
♫✧.*◝(•❝͋꒳❝͋•)◟*·✧♫⠀Regular Emoticons with Musical Notes 3
✌♫♪˙❤‿❤˙♫♪✌⠀Regular Emoticons with Musical Notes 4
(*´╰╯`๓)♬⠀Regular Emoticons with Musical Notes 5
(o^^o)♪⠀Regular Emoticons with Musical Notes 6
(ෆ❛ั▿❛ัʃƪ)♩°:::⠀Regular Emoticons with Musical Notes 7
(♡ˊ͈ ॢ꒳ ॢˋ͈)♪⠀Regular Emoticons with Musical Notes 8
♡ฅ(ᐤˊ꒳ฅˋᐤ♪)⠀Regular Emoticons with Musical Notes 9
(◍ ͒•ಲ• ͒◍)♬⠀Regular Emoticons with Musical Notes 10
ต( ິᵒ̴̶̷̤ ﻌ ᵒ̴̶̷̤ )ິ ♬⠀Regular Emoticons with Musical Notes 11
ฅ( ̳͒•ಲ• ̳͒)♪⠀Regular Emoticons with Musical Notes 12
♪(∗ˊ ˂ॢ˃ ॢˋ∗)⠀Regular Emoticons with Musical Notes 13
◟(｡´௰`)◞३*¨♪⠀Regular Emoticons with Musical Notes 14
⊂(´ω｀｡) ♪⠀Regular Emoticons with Musical Notes 15
◖ฺ|´⌣`*|◗·˳♪⁎˚♫⠀Regular Emoticons with Musical Notes 16
( ‘́⌣’̀)/♫•*¨*•.¸¸♪⠀Regular Emoticons with Musical Notes 17
(^_^♪)⠀Regular Emoticons with Musical Notes 18
♪(´∪`●)ゝ⠀Regular Emoticons with Musical Notes 19
（＊＾ω＾）♪⠀Regular Emoticons with Musical Notes 20
♫꒰･◡･๑꒱⠀Regular Emoticons with Musical Notes 21
(◍ ͒•ಲ• ͒◍)♬⠀Regular Emoticons with Musical Notes 22
ʕु-̫͡-ʔु”♬⠀Regular Emoticons with Musical Notes 23
(ღ˘⌣˘ღ) ♫･*:.｡. .｡.:*･⠀Regular Emoticons with Musical Notes 24
(๑´▿｀๑)♫•*¨*•.¸¸♪✧⠀Regular Emoticons with Musical Notes 25
ŧ‹”ŧ‹”(⁎ᵒ̶̶̷ ̯ ̜ᵒ̴̶̷⁎).₊♪‧˚*⠀Regular Emoticons with Musical Notes 26
✿♬ﾟ+.(｡◡‿◡)♪.+ﾟ♬✿。⠀Regular Emoticons with Musical Notes 27
ლ(=σωσ=ლ)βﾟ｡.*゜♬♫⠀Regular Emoticons with Musical Notes 28
(◦′ᆺ‵◦) ♬° ✧❥✧¸.•*¨*✧♡✧ ℒℴѵℯ ✧♡✧*¨*•.❥⠀Regular Emoticons with Musical Notes 29
♬°⋆ɱUꑄյ͛ʗ⋆°♬⠀Miscellaneous 1
♪̊̈♪̆̈⠀Miscellaneous 2
( ￣┏＿┓￣)⠀┏ and ┓Style Moustaches 1
ヽ(◎´┏∀┓｀)ノ⠀┏ and ┓Style Moustaches 2
(￣┏Д┓￣°*)⠀┏ and ┓Style Moustaches 3
༼つ☉┏益┓⊙༽つ⠀┏ and ┓Style Moustaches 4
(ノ≧┏Д┓≦)ノ⠀┏ and ┓Style Moustaches 5
(*ﾟ┏∇┓ﾟ)⠀┏ and ┓Style Moustaches 6
(ﾟ┏∇┓ﾟ*)⠀┏ and ┓Style Moustaches 7
ヽ༼ຈ┏ل͜┓ຈ༽ﾉ⠀┏ and ┓Style Moustaches 8
⋋▐ ◔ ┏ل͜┓ ◔ ▐⋌⠀┏ and ┓Style Moustaches 9
w(′┏▽┓`●)w⠀┏ and ┓Style Moustaches 10
【●･´┏ω┓`･●】⠀┏ and ┓Style Moustaches 11
(￣┏Д┓￣ )⠀┏ and ┓Style Moustaches 12
ﾐ(´┏ω┓｀)/⠀┏ and ┓Style Moustaches 13
o(●′┏＿┓`)o⠀┏ and ┓Style Moustaches 14
ᕕ║ ˵ ᴼ ┏ل͜┓ ᴼ ˵ ║⊃⠀┏ and ┓Style Moustaches 15
o(ﾟ┏∀┓ﾟo)⠀┏ and ┓Style Moustaches 16
(´┏･┓｀)⠀┏ and ┓Style Moustaches 17
ヾ(ﾟ┏д┓ﾟ)ﾉ゛⠀┏ and ┓Style Moustaches 18
(oﾟ┏ω┓ﾟo)⠀┏ and ┓Style Moustaches 19
乁╏ ಠ ┏ل͜┓ ಠ ╏ㄏ⠀┏ and ┓Style Moustaches 20
┌〳 ՞ ┏ل͜┓ ՞ 〵┐⠀┏ and ┓Style Moustaches 21
(oﾟ┏Д┓ﾟ)o⠀┏ and ┓Style Moustaches 22
｡ﾟ(ﾟ´┏∀┓｀*ﾟ)ﾟ｡⠀┏ and ┓Style Moustaches 23
(*´┏ｴ┓｀*)⠀┏ and ┓Style Moustaches 24
～(´┏ω┓｀～)⠀┏ and ┓Style Moustaches 25
(´o・┏ω┓・o｀)⠀┏ and ┓Style Moustaches 26
(´┏o┓｀)⠀┏ and ┓Style Moustaches 27
(～´┏ω┓｀)～⠀┏ and ┓Style Moustaches 28
(￣┏∞┓￣)⠀┏ and ┓Style Moustaches 29
|*￣┏Д┓￣|┛⠀┏ and ┓Style Moustaches 30
(＾┌_̀┐＾)⠀┏ and ┓Style Moustaches 31
Σ(；ﾟ┏д┓ﾟ)_⠀┏ and ┓Style Moustaches 32
┗|￣┏Д┓￣*|⠀┏ and ┓Style Moustaches 33
( ˇ෴ˇ )⠀෴ Style Moustaches 1
(༎ຶ ෴ ༎ຶ)⠀෴ Style Moustaches 2
༼ ༎ຶ ෴ ༎ຶ༽⠀෴ Style Moustaches 3
(⚫ે෴ۜ⚫)⠀෴ Style Moustaches 4
ᕦ⊙෴⊙ᕤ⠀෴ Style Moustaches 5
◝₍⁽ֹ෴ֹ⁾₎◜⠀෴ Style Moustaches 6
[ ◯ ෴ ◯ ]⠀෴ Style Moustaches 7
| ・ ෴ ・ |⠀෴ Style Moustaches 8
ԅ(◉෴◉ԅ)⠀෴ Style Moustaches 9
┌། ิ ෴ ิ །┐⠀෴ Style Moustaches 10
(ಠ .̫.̫ ಠ)⠀Other Moustaches 1
(•̴̑⁎̵̭•̴̆)⠀Other Moustaches 2
✌(꒡͡ ો ̼̮ ꒡͡✌)⠀Other Moustaches 3
(　˙灬˙　)⠀Other Moustaches 4
❛ॕ̀ੇ≀ ̼❛ॕ̀ੇ˵⠀Other Moustaches 5
(⁰︻⁰)⠀Other Moustaches 6
(-◞८࿆◟࿆-)⠀Other Moustaches 7
(<><<̯-̮<<<<̯)⠀Other Moustaches 8
٩(-̃_̮̮̃-̃)۶⠀Other Moustaches 9
(˗̆ˍ̂˗)⠀Other Moustaches 10
(•˳̂•̆)⠀Other Moustaches 11
◟( ͡° ʃヮɭ ͡°)ﾉ⠀Other Moustaches 12
ᕙ། ¯ ~͜ʖ~ ¯ །ᕗ⠀Other Moustaches 13
ヽ(∴｀┗Д┛´)ﾉ⠀Other Moustaches 14
(⋆ʾ ˙̫̮ ʿ⋆)⠀Other Moustaches 15
σ(●ﾟ┏∀┛｡●)ﾉ⠀Other Moustaches 16
m(￣<<<<ス<><<￣)m⠀Other Moustaches 17
m(￣<<<<マ<><<￣)m⠀Other Moustaches 18
m(￣<<<<ン<><<￣)m⠀Other Moustaches 19
The Professor⠀Movember 2014 1
。(⌒෴⌒。)⠀Movember 2014 2
(｀ ┏ ∀ ┓ ´)⠀Movember 2014 3
且_(゜ ˒̫̮ ゜；)ノﾞ⠀Movember 2014 4
ᕙ(๏益๏)ᕗ⠀Movember 2014 5
ヽ(･ ˒̫̮･)ﾉ⠀Movember 2014 6
(⁎·́෴·̀)◞ ͂͂(˒̩̩̥́௰˓̩̩̥̀⁎)⠀Movember 2014 7
o(´~∀~｀*)⠀Movember 2014 8
٩(^෴^)۶⠀Movember 2014 9
o(^ 灬 ^)o⠀Movember 2014 10
(•̀ ⑉̈•́)و ̑̑⠀Movember 2014 11
ƪ(˘︷ ˘)و⠀Movember 2014 12
ԅ( ˘ ▂ ˘ ԅ)⠀Movember 2014 13
(¬ ₀̑ ¬)⠀Movember 2014 14
(っ˘ ˒̫̮ ˘ς)⠀Movember 2014 15
୧(﹒︠ ̫ ̫̊ ̫﹒︡)୨⠀Movember 2014 16
【・ ˡ̲̮ ・】⠀Movember 2014 17
꒰๑• ˳̫̬•๑꒱⠀Movember 2014 18
(⁰︻⁰)⠀Movember 2014 19
ಠ ~_~ ಠ⠀Movember 2014 20
| ू•ૅ •̫̮ •́)ᵎᵎᵎ⠀Movember 2014 21
(－ ˑ̭ ლ)⠀Movember 2014 22
˛˛ꉂ ◞•̀︷•́)੭̸⠀Movember 2014 23
┐(^▂ ^；)┌⠀Movember 2014 24
( ►┏_┓◄ )⠀Movember 2014 25
_(꒪ཀ꒪」∠)_⠀Single Line Nosebleeds 1
(ヾﾉ꒪ཫ꒪ )⠀Single Line Nosebleeds 2
(꒪ཀ꒪)⠀Single Line Nosebleeds 3
( °٢° )⠀Single Line Nosebleeds 4
ˉ̡̠̭̭”( ⑉¯ །། ¯⑉ )ˉ̡̠̭̭”⠀Single Line Nosebleeds 5
(＾་།＾)⠀Single Line Nosebleeds 6
(-́◞८͙༙◟-̀)⠀Single Line Nosebleeds 7
ᶘ○་།○ᶅ⠀Single Line Nosebleeds 8
(꒪ิཫ꒪ )ノิิิ ḟ৹ʳᵧ৹ᵤ⠀Single Line Nosebleeds 9
（´〃｀＊）⠀Single Line Nosebleeds 10
(´ii｀)⠀Single Line Nosebleeds 11
（￣ ¨ヽ￣ ）⠀Single Line Nosebleeds 12
(￣TT￣)⠀Single Line Nosebleeds 13
(´ノi｀)⠀Single Line Nosebleeds 14
(￣^<￣)⠀Single Line Nosebleeds 15
(￣ＴＴ￣)⠀Single Line Nosebleeds 16
(￣TT￣)⠀Single Line Nosebleeds 17
(￣ <￣)⠀Single Line Nosebleeds 18
(￣-<￣)⠀Single Line Nosebleeds 19
(￣￣ξ￣￣)⠀Single Line Nosebleeds 20
(￣ii￣)⠀Single Line Nosebleeds 21
(￣ii￣*)⠀Single Line Nosebleeds 22
(￣Γ￣)⠀Single Line Nosebleeds 23
(*￣ii￣)⠀Single Line Nosebleeds 24
{{{(￣ﾊ￣*)}}}⠀Single Line Nosebleeds 25
( ´ ii ｀ )⠀Single Line Nosebleeds 26
（￣￣ｉｉ￣￣）⠀Single Line Nosebleeds 27
⁽͑˙˚̀༎˚́˙⁾̉⠀Single Line Nosebleeds 28
ʅ(´◉◞.̸̸̸̸̸̸̸̸̸̸̸̸̸̸̸̸̸̸̸̸̸̸̸̸̨̨̨̨̨̨̨̨̨̨̨̨.̸̸̨̨◟◉) ʃ⠀Multiple Line Nosebleeds 1
(⁰₎₌̸̸̴̷̸̸̸̸̸̴̸̷̧̧̧̨̨ͨ₍⁰)⠀Multiple Line Nosebleeds 2
(꒪.̸̸̸̸̸̸̸̸̸̸̸̸̸̸̸̸̸̸̸̸̸̸̸̸̨̨̨̨̨̨̨̨̨̨̨̨.̸̸̨̨꒪ )⠀Multiple Line Nosebleeds 3
(｀･.̸̸̸̸̸̸̸̸̸̸̸̸̸̸̸̸̸̸̸̸̸̸̸̸̨̨̨̨̨̨̨̨̨̨̨̨.̸̸̨̨･´)⠀Multiple Line Nosebleeds 4
(๑◉.̸̸̸̸̸̸̸̸̸̸̸̸̸̸̸̸̸̸̸̸̸̸̸̸̨̨̨̨̨̨̨̨̨̨̨̨.̸̸̨̨◉๑）⠀Multiple Line Nosebleeds 5
(˶‾᷄.̸̸̸̸̸̸̸̸̸̸̸̸̸̸̸̸̸̸̸̸̸̸̸̸̨̨̨̨̨̨̨̨̨̨̨̨.̸̸̨̨ ‾᷅˵)⠀Multiple Line Nosebleeds 6
_(:.̸̸̸̸̸̸̸̸̸̸̸̸̸̸̸̸̸̸̸̸̸̸̸̸̨̨̨̨̨̨̨̨̨̨̨̨.̸̸̨̨ 」 ∠)_⠀Multiple Line Nosebleeds 7
Σ(꒪.̸̸̸̸̸̸̸̸̸̸̸̸̸̸̸̸̸̸̸̸̸̸̸̸̨̨̨̨̨̨̨̨̨̨̨̨.̸̸̨̨꒪ )ｴｪ!!⠀Multiple Line Nosebleeds 8
ʅ(◔.̸̸̸̸̸̸̸̸̸̸̸̸̸̸̸̸̸̸̸̸̸̸̸̸̨̨̨̨̨̨̨̨̨̨̨̨.̸̸̨̨◔)ʃ⠀Multiple Line Nosebleeds 9
（๑◉.̸̸̸̸̸̸̸̸̸̸̸̸̸̸̸̸̸̸̸̸̸̸̸̸̨̨̨̨̨̨̨̨̨̨̨̨.̸̸̨̨◉๑）⠀Multiple Line Nosebleeds 10
Σ(꒪.̸̸̸̸̸̸̸̸̸̸̸̸̸̸̸̸̸̸̸̸̸̸̸̸̨̨̨̨̨̨̨̨̨̨̨̨.̸̸̨̨꒪ )⠀Multiple Line Nosebleeds 11
(♡.̸̸̸̸̸̸̸̸̸̸̸̸̸̸̸̸̸̸̸̸̸̸̸̸̨̨̨̨̨̨̨̨̨̨̨̨.̸̸̨̨♡ )⠀Multiple Line Nosebleeds 12
｡ﾟ(ﾟ´.̸̸̸̸̸̸̸̸̸̸̸̸̸̸̸̸̸̸̸̸̸̸̸̸̨̨̨̨̨̨̨̨̨̨̨̨.̸̸̨̨｀ﾟ)ﾟ｡⠀Multiple Line Nosebleeds 13
ι(｀･.̸̸̸̸̸̸̸̸̸̸̸̸̸̸̸̸̸̸̸̸̸̸̸̸̨̨̨̨̨̨̨̨̨̨̨̨.̸̸̨̨･´)/⠀Multiple Line Nosebleeds 14
ʕ ㅎ.̸̸̸̸̸̸̸̸̸̸̸̸̸̸̸̸̸̸̸̸̸̸̸̸̨̨̨̨̨̨̨̨̨̨̨̨.̸̸̨̨ㅎʔ⠀Multiple Line Nosebleeds 15
(。≖ˇ.̸̸̸̸̸̸̸̸̸̸̸̸̸̸̸̸̸̸̸̸̸̸̸̸̨̨̨̨̨̨̨̨̨̨̨̨.̸̸̨̨ˇ≖｡)⠀Multiple Line Nosebleeds 16
(⑅*’.̸̸̸̸̸̸̸̸̸̸̸̸̸̸̸̸̸̸̸̸̸̸̸̸̨̨̨̨̨̨̨̨̨̨̨̨.̸̸̨̨’ *)⠀Multiple Line Nosebleeds 17
(๑´･.̸̸̸̸̸̸̸̸̸̸̸̸̸̸̸̸̸̸̸̸̸̸̸̸̨̨̨̨̨̨̨̨̨̨̨̨.̸̸̨̨･`)⠀Multiple Line Nosebleeds 18
(๑´.̸̸̸̸̸̸̸̸̸̸̸̸̸̸̸̸̸̸̸̸̸̸̸̸̨̨̨̨̨̨̨̨̨̨̨̨.̸̸̨̨`๑)⠀Multiple Line Nosebleeds 19
(இ.̸̸̸̸̸̸̸̸̸̸̸̸̸̸̸̸̸̸̸̸̸̸̸̸̨̨̨̨̨̨̨̨̨̨̨̨.̸̸̨̨இ`｡)⠀Multiple Line Nosebleeds 20
(σ｀.̸̸̸̸̸̸̸̸̸̸̸̸̸̸̸̸̸̸̸̸̸̸̸̸̨̨̨̨̨̨̨̨̨̨̨̨.̸̸̨̨´)σ⠀Multiple Line Nosebleeds 21
(<`.̸̸̸̸̸̸̸̸̸̸̸̸̸̸̸̸̸̸̸̸̸̸̸̸̨̨̨̨̨̨̨̨̨̨̨̨.̸̸̨̨´)⠀Multiple Line Nosebleeds 22
(:.̸̸̸̸̸̸̸̸̸̸̸̸̸̸̸̸̸̸̸̸̸̸̸̸̨̨̨̨̨̨̨̨̨̨̨̨.̸̸̨̨[_____]⠀Multiple Line Nosebleeds 23
(.̸̸̸̸̸̸̸̸̸̸̸̸̸̸̸̸̸̸̸̸̸̸̸̸̨̨̨̨̨̨̨̨̨̨̨̨.̸̸̨̨3[____]⠀Multiple Line Nosebleeds 24
(*‘.̸̸̸̸̸̸̸̸̸̸̸̸̸̸̸̸̸̸̸̸̸̸̸̸̨̨̨̨̨̨̨̨̨̨̨̨.̸̸̨̨‘*)⠀Multiple Line Nosebleeds 25
( •ॢ.̸̸̸̸̸̸̸̸̸̸̸̸̸̸̸̸̸̸̸̸̸̸̸̸̨̨̨̨̨̨̨̨̨̨̨̨.̸̸̨̨-ॢ)-♡⠀Multiple Line Nosebleeds 26
( ⊃・ω・)⊃☂⠀Multiple Line Nosebleeds 27
ヽ༼ຈل͜ຈ༽ﾉ☂⠀Multiple Line Nosebleeds 28
[+..••]⠀Multiple Line Nosebleeds 29
⊚⃝⸜(ू´•͈ω•͈⑅)⠀Multiple Line Nosebleeds 30
✎✐✎✐✎✐✎✐✎✐✎✐⠀Multiple Line Nosebleeds 31
( ˘ω˘ )ｼ ─=≡Σ((☎⠀Multiple Line Nosebleeds 32
(+[__]∙:∙)⠀Multiple Line Nosebleeds 33
|̲̅̅●̲̅̅|̲̅̅=̲̅̅|̲̅̅●̲̅̅|⠀Multiple Line Nosebleeds 34
⊚⃝⸜(ू｡∵｡) ⋆｡°✩⠀Multiple Line Nosebleeds 35
♧⃘⠀Multiple Line Nosebleeds 36
=͟͟͞͞ ⌧*Ժ⃒~ʓ⁂⠀Multiple Line Nosebleeds 37
☁ ☝ˆ~ˆ☂⠀Multiple Line Nosebleeds 38
（•☎_☎•）⠀Multiple Line Nosebleeds 39
[( o/)]|::|[( o/)]⠀Multiple Line Nosebleeds 40
⚀⚁⚂⚃⚄⚅⠀Multiple Line Nosebleeds 41
( ＾◡＾)っ✂⠀Multiple Line Nosebleeds 42
[-c°▥°]-c⠀Multiple Line Nosebleeds 43
✩⃛ ⁝⁞⁝⁞Ⴇ౿౿⁙⁞⁝⁝◟(˟ε˟ ◟)՞՞⠀Multiple Line Nosebleeds 44
⁝⁞⁝⁞ʕु•̫͡•ʔु☂⁝⁞⁝⁝⠀Multiple Line Nosebleeds 45
[̲̅$̲̅(̲̅5̲̅)̲̅$̲̅]⠀Multiple Line Nosebleeds 46
[̲̅$̲̅(̲̅ ͡° ͜ʖ ͡°̲̅)̲̅$̲̅]⠀Multiple Line Nosebleeds 47
[̲̅$̲̅(̲̅10)̲̅$̲̅]⠀Multiple Line Nosebleeds 48
[̲̅$̲̅(̲̅20)̲̅$̲̅]⠀Multiple Line Nosebleeds 49
[̲̅$̲̅(̲̅5̲̅0)̲̅$̲̅]⠀Multiple Line Nosebleeds 50
[̲̅$̲̅(̲̅100)̲̅$̲̅]⠀Multiple Line Nosebleeds 51
┫￣旦￣┣⠀Multiple Line Nosebleeds 52
(っ´ω`)っ☂⊂(´ω`⊂ )⠀Multiple Line Nosebleeds 53
< < <(*･ω･)o个< < <⠀Multiple Line Nosebleeds 54
☝(◔ิ_◔)☂⠀Multiple Line Nosebleeds 55
☎ヽ(◣д◢)⠀Multiple Line Nosebleeds 56
━[＼/]━a(´ω｀*)⠀Multiple Line Nosebleeds 57
⊂( ･∀･) 彡　=͟͟͞͞ ⌧⠀Multiple Line Nosebleeds 58
＼( *ω*)┓☎⠀Multiple Line Nosebleeds 59
☂｀(´ω｀u)⠀Multiple Line Nosebleeds 60
＜Σ三三三三三三三∃⠀Multiple Line Nosebleeds 61
☎Σ⊂⊂(☉ω☉∩)⠀Multiple Line Nosebleeds 62
( ・ ̫・)੭ु⁾⁾☎⠀Multiple Line Nosebleeds 63
( ^o^)Г☎⠀Multiple Line Nosebleeds 64
■━⊂(　・∀・) 彡⠀Multiple Line Nosebleeds 65
ʚ✟⃛ɞ⠀Multiple Line Nosebleeds 66
♳♴♵♶♷♸♹⠀Multiple Line Nosebleeds 67
ㄹㅁІㄹ⠀Multiple Line Nosebleeds 68
ヽ｀、、ヽ｀ヽ｀、ヽ｀、ヽ｀｀｀、ヽ｀｀、ヽ｀、ヽ｀ヽ｀、、ヽ｀ヽ｀、ヽ｀、ヽ｀｀、ヽ｀、ヽ｀ヽ｀、、ヽ｀ヽ｀、ヽ｀、ヽ｀｀、ヽ｀、ヽ｀ヽ｀、、ヽ｀ヽ｀、ヽ(ノ；Д；)ノ ｀、、ヽ｀☂ヽ｀、ヽ｀｀、ヽ｀、ヽ｀ヽ｀、｀、ヽ｀｀、ヽ｀、ヽ｀ヽ｀、、ヽ｀ヽ｀、ヽ｀、ヽ｀｀、ヽ｀、ヽ｀ヽ｀、、ヽ｀ヽヽ｀、ヽ｀｀、ヽ｀、ヽ｀ヽ｀、、ヽ｀ヽ⠀Multiple Line Nosebleeds 69
ヽ｀、、ヽ｀ヽ｀、、ヽ｀ヽ｀、、ヽ｀ヽ｀、ヽ｀｀、ヽ｀、ヽ｀ヽ｀、｀｀、ヽ｀、ヽ｀ヽ｀、、ヽ｀ヽ｀、ヽ、ヽ｀ヽ｀、ヽ｀｀、ヽ｀、ヽ｀ヽ｀((((( ( ⊃・ω・)⊃☂｀(´ω｀u)))ヽ｀、、ヽ｀ヽ｀、ヽ｀｀、ヽ｀、ヽ｀ヽ｀、、ヽ｀ヽ｀、ヽ｀｀、ヽ｀、ヽ｀ヽ｀、、ヽ、ヽ｀ヽ｀、ヽ｀、、ヽ｀ヽ｀、、ヽ｀ヽ｀、、ヽ｀ヽ｀、ヽ｀｀、ヽ｀、ヽ｀ヽ｀、⠀Multiple Line Nosebleeds 70
、ヽ｀、ヽ｀个o(･_･｡)｀ヽ、｀ヽ、⠀Multiple Line Nosebleeds 71
、ヽ｀、ヽ｀个c(ﾟ∀ﾟ∩)｀ヽ、｀ヽ、⠀Multiple Line Nosebleeds 72
。°。°。°。个o(-ω-｡)ﾟ。°。°。°。⠀Multiple Line Nosebleeds 73
【　TV　】　　　　-o(.￣　)⠀Multiple Line Nosebleeds 74
( • )( • )ԅ(‾⌣‾ԅ)⠀Touching Things 1
(˘▼˘<><<ԅ( ˘⌣ƪ)⠀Touching Things 2
ԅ╏ ˵ ⊚ ◡ ⊚ ˵ ╏┐⠀Touching Things 3
(¬_¬”)-cԅ(‾⌣‾ԅ)⠀Touching Things 4
♥(ˆ⌣ˆԅ)⠀Touching Things 5
ƪ(`▿▿▿▿´ƪ)⠀Touching Things 6
ԅ(≖‿≖ԅ)⠀Touching Things 7
ԅ(¯﹃¯ԅ)⠀Touching Things 8
ԅ( ˘ω˘ ԅ)⠀Touching Things 9
ԅ(‹o›Д‹o›ԅ)⠀Touching Things 10
√(￣‥￣√⠀Touching Things 11
ԅ། ຈ ◞౪◟ຈ །و⠀Touching Things 12
ԅ( ͒ ۝ ͒ )ᕤ⠀Touching Things 13
ԅ(´ڡ`ԅ)⠀Touching Things 14
ԅ(≖‿≖ <ԅ)⠀Touching Things 15
ƪ(ƪ꒪ৱ৹)ᵒʰ˵˵⠀The Slow Clap 1
(#´∞｀∫)∫⠀The Slow Clap 2
ƪƪ’▿’)⠀The Slow Clap 3
(‘▿’ʃʃ⠀The Slow Clap 4
(•’╻’• ۶)۶⠀The Slow Clap 5
(☞ﾟ∀ﾟ)☞⠀Pointing 1
( ´థ౪థ)σ’`ﾞ⠀Pointing 2
(σﾟ∀ﾟ)σ⠀Pointing 3
( •̀ω•́ )σ⠀Pointing 4
(*σ´益｀)σ⠀Pointing 5
(?・・)σ⠀Pointing 6
〈(•ˇ‿ˇ•)-→⠀Pointing 7
┗(•ˇ_ˇ•)―→⠀Pointing 8
（☝ ՞ਊ ՞）☝⠀Pointing 9
☞๏็ັཪ๏็๎☞⠀Pointing 10
☜Ҩↂ⼼ↂҨ☞⠀Pointing 11
☝(｀ط´≠)⠀Pointing 12
（☞´^ิ∀^ิ｀）☞⠀Pointing 13
[｀･⊆･´★]っ⠀Pointing 14
[★ ｀･⊇･´]っ⠀Pointing 15
[｀･⊆･´☆]っ⠀Pointing 16
[☆ ｀･⊇･´]っ⠀Pointing 17
(´∀｀σ)σ⠀Pointing 18
(╭☞•́⍛•̀)╭☞⠀Pointing 19
(՞ټ՞☝⠀Pointing 20
(☝ ՞՞)☝⠀Pointing 21
(╭☞´ิ∀´ิ)╭☞⠀Pointing 22
(☞^o^) ☞⠀Pointing 23
☜(⌒▽⌒)☞⠀Pointing 24
☞￣ᴥ￣☞⠀Pointing 25
( ━☞´◔‿ゝ◔`)━☞⠀Pointing 26
(☞三☞ ఠ ਉ ఠ))☞三☞⠀Pointing 27
＿|￣| ⍤⃝⠀Movement Related 1
＿|￣| ⍨⃝⠀Movement Related 2
＿|￣| ⍤⃝⠀Movement Related 3
_|￣|⑱⠀Movement Related 4
_|￣|⑬⠀Movement Related 5
_|￣|⑪⠀Movement Related 6
(._.) ( <: ) ( .-. ) ( :< ) (._.)⠀Movement Related 7
三(‘ω’)三( ε: )三(.ω.)三( :3 )三(‘ω’)三( ε: )三(.ω.)三( :3 )⠀Movement Related 8
ヽ(｀Д´)ノ　(д´ノ)　ヽ(　　　)ノ　(ヽ´△) ヽ(´△`)ﾉ⠀Movement Related 9
ヽ(´∇´)ノ　(∇´ノ)　ヽ(　　　)ノ　(ヽ´∇) ヽ(´∇`)ﾉ⠀Movement Related 10
Sneakin> Around⠀Movement Related 11
ू(･ิ ॄ･ิू๑)⠀Movement Related 12
(*ﾟﾉOﾟ)⠀Yelling 1
(ง ˙o˙)ว⠀Yelling 2
(ლ `Д ́)ლ⠀Yelling 3
ε=(｡◕ฺˇд ˇ◕ฺ｡）⠀Farting 1
○|￣|_ =3⠀Farting 2
ʸ(˃̴ꆚᵃ̷⁎)▁▂▃▅▆▓▒░✩⃛⠀Farting 3
(°༣°)༇༇⠀Blowing 1
ε-(´・｀) ﾌ⠀Blowing 2
ₒ₍₊˒₃˓₎ₒ▁▂▃▅▆▓▒░✩⃛⠀Blowing 3
d(-_^)⠀Thumbs Up or Down 1
(*＾-‘) 乃⠀Thumbs Up or Down 2
(*^▽^*)b⠀Thumbs Up or Down 3
(*＾▽＾)b⠀Thumbs Up or Down 4
d(´∀`)b⠀Thumbs Up or Down 5
d(ﾟ∀ﾟ )b⠀Thumbs Up or Down 6
d(･∀･○)⠀Thumbs Up or Down 7
d(^～^)⠀Thumbs Up or Down 8
(n˘v˘•)b⠀Thumbs Up or Down 9
(　^ω^）b⠀Thumbs Up or Down 10
d (^‿^✿)⠀Thumbs Up or Down 11
(。≖ˇｪˇ≖｡)b⠀Thumbs Up or Down 12
(｡^U^)b⠀Thumbs Up or Down 13
(*-凵-)b⠀Thumbs Up or Down 14
s( ^ ‿ ^)-b⠀Thumbs Up or Down 15
s( ^ ‸ ^)-p⠀Thumbs Up or Down 16
((“Ｑ(´▽｀｡)⠀Fanning 1
.:*ﾟ..:｡:.((“Ｑ(ω･´ｏ)⠀Fanning 2
(υ´-ω-)ゞ~~~”Q_(´ρ｀υ))))⠀Fanning 3
✌⎦ʘ_ゝʘ⎣✌⠀Peace Signs 1
v(｡-_-｡)v⠀Peace Signs 2
✌（◕ω◕）✌⠀Peace Signs 3
✌_‹(⊂•⊃¿⊂•⊃)›_✌⠀Peace Signs 4
✌(꒡͡ ો ̼̮ ꒡͡✌)⠀Peace Signs 5
✌( ་ེིོཻྀཽཾ⌓ ་ེིོཻྀཽཾ)⠀Peace Signs 6
(˘ʃƪ˘)⠀Various Other Actions 1
( ＾◡＾)っ✂╰⋃╯⠀Various Other Actions 2
( ु⚈᷁௰⚈᷁ ू)⠀Various Other Actions 3
(*・_・)ノ⌒*⠀Various Other Actions 4
(´･ω･)9))【dooя】⠀Various Other Actions 5
✩⃛ ⁝⁞⁝⁞Ⴇ౿౿⁙⁞⁝⁝◟(˟ε˟ ◟)՞՞⠀Various Other Actions 6
⁽͑˙ʾ́ ᵌʿ̀˙⁾̉⁼ᵌ ᵖᵘᵖᵘᵖᵘ˝ᵎ⠀Various Other Actions 7
(⊃‿⊂) ⊂(⋂ヮ⋂)⊃⠀Various Other Actions 8
( ﾟ∀(・－・)⠀Various Other Actions 9
【　TV　】　　　　-o(.￣　)⠀Various Other Actions 10
八(＾□＾*)⠀Various Other Actions 11
(๑•॒̀ ູ॒•́๑)⠀Various Other Actions 12
p■qω・´)⠀Various Other Actions 13
๏[-ิ_•ิ]๏⠀Various Other Actions 14
(੭ ˘•ω•˘)੭ु⁾⁾⠀Various Other Actions 15
ヽ｀、ヽ｀ヽ(*￣o￣*)<><<ヽ｀、ヽ｀⠀Various Other Actions 16
( ° ᴗ°)~ð (/❛o❛\)⠀Various Other Actions 17
\m/…(<><<.<<<<)…\m/⠀Various Other Actions 18
(*゜▽゜)*。_。)*゜▽゜)*。_。)⠀Various Other Actions 19
⁽⁽◟(˃◟̵◞̵˂⁎=͟͟͞͞ ⁎˃◟̵◞̵˂)◞⁾⁾⠀Various Other Actions 20
(*´σー｀)⠀Various Other Actions 21
( ≧ Д ≦) (✿☯.☯) (♥ω♥ ) ~♪⠀Various Other Actions 22
･*･:≡(　ε:)⠀Various Other Actions 23
(。-`ω´-)⠀Generic Animals with ω Mouths 1
(｡+･`ω･´)⠀Generic Animals with ω Mouths 2
(*´ω｀)o⠀Generic Animals with ω Mouths 3
(´・ω・)ﾉ⠀Generic Animals with ω Mouths 4
(=ﾟωﾟ)ノ⠀Generic Animals with ω Mouths 5
(ﾉ･ω･)ﾉﾞ⠀Generic Animals with ω Mouths 6
ヽ(･ω･｡)ﾉ⠀Generic Animals with ω Mouths 7
ヽ(･ω･ゞ)⠀Generic Animals with ω Mouths 8
ヽ(´･ω･`)､⠀Generic Animals with ω Mouths 9
Σ( ﾟωﾟ；≡⊃⠀Generic Animals with ω Mouths 10
( •̀ ω•́ )⠀Generic Animals with ω Mouths 11
(・ω・；)⠀Generic Animals with ω Mouths 12
(* <><<ω<<<<)⠀Generic Animals with ω Mouths 13
(*-ω-)⠀Generic Animals with ω Mouths 14
(*･ω･)⠀Generic Animals with ω Mouths 15
(•̀௰•́ )⠀Generic Animals with ω Mouths 16
(´-ω-｀)⠀Generic Animals with ω Mouths 17
(´・ω・`)⠀Generic Animals with ω Mouths 18
(´o・┏ω┓・o｀)⠀Generic Animals with ω Mouths 19
(=ﾟωﾟ)ﾉ⠀Generic Animals with ω Mouths 20
(○’ω’○)⠀Generic Animals with ω Mouths 21
[´・ω・`]⠀Generic Animals with ω Mouths 22
｛・ω-*}⠀Generic Animals with ω Mouths 23
┗(･ω･<)┛⠀Generic Animals with ω Mouths 24
ヾ(･ω･`｡)⠀Generic Animals with ω Mouths 25
ヾ(・ω・ｏ)⠀Generic Animals with ω Mouths 26
ヾ(｡･ω･｡)⠀Generic Animals with ω Mouths 27
ヽ(｡ゝω・｡)ﾉ⠀Generic Animals with ω Mouths 28
ヾ(ｏ･ω･)ﾉ⠀Generic Animals with ω Mouths 29
w(´･ω･`)w⠀Generic Animals with ω Mouths 30
Σ(・ω・`|||)⠀Generic Animals with ω Mouths 31
ฅ(ٛ•௰• ٛ )⠀Generic Animals with ω Mouths 32
(∗•ω•∗)⠀Generic Animals with ω Mouths 33
(›´ω`‹ )⠀Generic Animals with ω Mouths 34
( “･ω･ﾞ)⠀Generic Animals with ω Mouths 35
( ˘•ω•˘ )⠀Generic Animals with ω Mouths 36
( •̆௰•̆)⠀Generic Animals with ω Mouths 37
( •॔௰• ॓)⠀Generic Animals with ω Mouths 38
ต(ꏿ᷅௰ꏿ᷄)ต⠀Generic Animals with ω Mouths 39
ฅ(ٛ •௰•´ ٛ )꒭！⠀Generic Animals with ω Mouths 40
ต(ꏿ௰ꏿ)ต⠀Generic Animals with ω Mouths 41
(ό௰ὸ)⠀Generic Animals with ω Mouths 42
⁝ˊ ̤•௰⃜•ˋ ̤⁝˒˒˒⠀Generic Animals with ω Mouths 43
∩(｀・ω・´)∩⠀Generic Animals with ω Mouths 44
ε(*´･ω･)з⠀Generic Animals with ω Mouths 45
( ･ὢ･ )⠀Generic Animals with ω Mouths 46
=͟͟͞͞⊂( ’ω’ )=͟͟͞͞⊃⠀Generic Animals with ω Mouths 47
(<<<<●<><<ω<<<<●<><<)✧⠀Generic Animals with ω Mouths 48
◞(o꒪ͧω꒪ͧo)⠀Generic Animals with ω Mouths 49
(♦ŐωŐ♦)⠀Generic Animals with ω Mouths 50
•ू(ᵒ̴̶̷ωᵒ̴̶̷*•ू) )੭ु⁾⠀Generic Animals with ω Mouths 51
(⌯¤̴̶̷̀ω¤̴̶̷́)✧⠀Generic Animals with ω Mouths 52
(❛ω❛)⠀Generic Animals with ω Mouths 53
(　³ω³ )⠀Generic Animals with ω Mouths 54
(＝ω＝.)⠀Generic Animals with ω Mouths 55
:( •ᾥ•):⠀Generic Animals with ω Mouths 56
(ᵔᴥᵔ)⠀Seals 1
(◕ᴥ◕)⠀Seals 2
ᵔᴥᵔ⠀Seals 3
◕ᴥ◕⠀Seals 4
(^ᴥ^)⠀Seals 5
^ᴥ^⠀Seals 6
ᶘ ͡°ᴥ͡°ᶅ⠀Seals 7
(•̆ꈊ•̆<<)ꋧ⠀Porcupines 1
:: (•ᴥ• )́`́’́`́’⻍⠀Porcupines 2
⁽⁽꜀(:3꜂ ꜆)꜄⁾⁾⠀Otters 1
દ=๑๑( ੭ ε:)੭ु⁾⁾₍₍⠀Otters 2
_(﹚◜ ꒊः`)_⠀Otters 3
_(ר гꒊಃ)_⠀Otters 4
(:ᘌꇤ⁐ꃳ 三⠀Otters 5
_(:3 ⌒ﾞ)_⠀Otters 6
｡･*･:≡(　ε:)⠀Otters 7
( :3) ×)〆 ～～～⠀Otters 8
(ꏅꈯ )<<<<⠀Otters 9
]＾：山⠀Snakes 1
＞°）m～～～∈⠀Snakes 2
～<><<`)～～～⠀Snakes 3
～<><<゜）～～～～⠀Snakes 4
～＞°）mニニニニ＝～⠀Snakes 5
➰＞°）mニニニニ＝➰⠀Snakes 6
੯ू•́ू ໒꒱⁼³₌₃⠀Hedgehogs 1
੯ू❛ัू ໒꒱⠀Hedgehogs 2
੯ू❛ัू ໒⑅꒱⠀Hedgehogs 3
੯ू•́ू ໒وو꒱⠀Hedgehogs 4
੯ू•́ू ໒꒱Ꮅ⠀Hedgehogs 5
੯ू•́ूཻ ໒꒱Ꮅ”⠀Hedgehogs 6
੯ू‵ू ໒꒱⠀Hedgehogs 7
੯ूᵕू ໒꒱ƶƵ⠀Hedgehogs 8
੯ू•̀ ໒꒱⁼³₌₃⠀Hedgehogs 9
੯ू❛ัूཻ ໒꒱⁼³₌₃⠀Hedgehogs 10
੯ूᵕ̤ू U॒॒॒॒॒୭ℒℴѵℯ❤⠀Hedgehogs 11
੯”ړ ও͞=͟͟͞͞=͟͟͞͞=͟͟͞͞=͟͟͞͞=͟͟͞͞=͟͟͞͞⠀Hedgehogs 12
੯ूᵕ̤ू U॒॒॒॒॒୭ღ⃛⠀Hedgehogs 13
੯ू•̀ू ໒꒱٩(ε•́๑))⠀Hedgehogs 14
༼ (`・ㅅ ・´) ༽⠀Llamas or Alpacas 1
༼ (´・ω・`) ༽⠀Llamas or Alpacas 2
༼ (´・ｪ・`) ༽⠀Llamas or Alpacas 3
༼ (´◓ɷ◓`) ༽⠀Llamas or Alpacas 4
(◕(‘ 人 ‘) ◕)⠀Llamas or Alpacas 5
༼ (。-`ω´-) ༽⠀Llamas or Alpacas 6
༼ ( •̀ ω•́ ) ༽⠀Llamas or Alpacas 7
༼ (* <><<ω<<<<) ༽⠀Llamas or Alpacas 8
༼ (•̀௰•́ ) ༽⠀Llamas or Alpacas 9
༼ ( ˘•ω•˘ ) ༽⠀Llamas or Alpacas 10
༼ ( ˘•ㅅ•˘ ) ༽⠀Llamas or Alpacas 11
༼ (* <><<ㅅ<<<<) ༽⠀Llamas or Alpacas 12
༼ (›´ω`‹ ) ༽⠀Llamas or Alpacas 13
༼ (ό௰ὸ) ༽⠀Llamas or Alpacas 14
༼ (›´ㅅ`‹ ) ༽⠀Llamas or Alpacas 15
Ƹ̵̡Ӝ̵̨̄Ʒ⠀Insects 1
ᙙᙖ⠀Insects 2
* ूི-̭͡- ૂ ྀ⁎ꂚᴉᴉᴉ⠀Insects 3
ૂི•̮͡• ૂ ྀ⠀Insects 4
ᵋ* ूི-̭͡- ૂ ྀᵌ⠀Insects 5
ෆ͙⃛* ི•̮͡ુ -ુ ྀᵒᵏ❣⃛⠀Insects 6
* ूི×̺͡×ू ྀ⁎*☠⁎ꂚ*ᵎᵎᵎ⠀Insects 7
* ི•̮͡ુ -ુ ྀෆ⃛* ི-̮͡ू -ू ྀ⠀Insects 8
( ≖ଳ≖)⠀Insects 9
(ꂲଳꂲ)⠀Insects 10
ஞଲஞ⠀Insects 11
꒰ॱଳ͘꒱⠀Insects 12
(ଠୖ ଳି ଠୖ)՞⠀Insects 13
( ̊ଳ ̊)⠀Insects 14
ʢ்ꇵ்͒ʡ⠀Mice and or Rats 1
ʢ்́ꇵ்͒̀ʡ⠀Mice and or Rats 2
ʢ்̽ꇵ்͒̽ʡ⠀Mice and or Rats 3
ʢٛ•ꇵٛ•ʡ*✲ﾟ*｡ʚɞ⋆ྉ⠀Mice and or Rats 4
ʢ• ͡•ʢ• ͡•ʢ• ͡•ʡ⠀Mice and or Rats 5
…ᘛ⁐̤ᕐᐷ⠀Mice and or Rats 6
ᘛ⁐̤ᕐᐷ ◅⠀Mice and or Rats 7
၄ စ ౪ စ ၃⠀Mice and or Rats 8
٩ʕ◕౪◕ʔو⠀Mice and or Rats 9
ᑴ´⍘`ᑷ⠀Mice and or Rats 10
ʢ◉ᴥ◉ʡ⠀Mice and or Rats 11
ᕳ-⍘-ᕲ⠀Mice and or Rats 12
ᕳ•⍘•ᕲ⠀Mice and or Rats 13
ᕮ  _  ᕭ⠀Mice and or Rats 14
ᕮ´⍘`ᕭ⠀Mice and or Rats 15
q⊜ᨎ⊜p⠀Mice and or Rats 16
ᘳꝊ‿Ꝋᘰ⠀Mice and or Rats 17
ʢ´• ᴥ •`ʡ⠀Mice and or Rats 18
ʕ ・ Д ・ ʔ⠀Mice and or Rats 19
६ൠ͠३⠀Cows, Bison, Oxes or Maybe Wildebeests 1
( ఠൠఠ )⠀Cows, Bison, Oxes or Maybe Wildebeests 2
( ≖ิൠ≖ิ )⠀Cows, Bison, Oxes or Maybe Wildebeests 3
三|ლ(◉ืൠื◉)ლ|三⠀Cows, Bison, Oxes or Maybe Wildebeests 4
(☝ ◉ืൠ◉ื)⠀Cows, Bison, Oxes or Maybe Wildebeests 5
/╲/\╭( ͡° ͡° ͜ʖ ͡° ͡°)╮/\╱\⠀Spiders 1
/╲/\(╭•̀ﮧ •́╮)/\╱\⠀Spiders 2
ᄽὁȍ ̪ őὀᄿ⠀Spiders 3
/╲/\╭(ఠ్ఠఠ్ఠ˓̭ ఠ్ఠఠ్ఠ)╮/\╱\⠀Spiders 4
/╲/\╭[ ☯ _ ☯ ]╮/\╱\⠀Spiders 5
/╲/\〳 ᴼᴼ ౪ ᴼᴼ 〵/\╱\⠀Spiders 6
/╲/\╭⁞ ರರ ͜ʖ ರರ ⁞╮/\╱\⠀Spiders 7
/╲/\╭( . ರರ ل ರರ . )╮/\╱\⠀Spiders 8
/╲/\╭〳 . ˘ ۝ ˘ . 〵╮/\╱\⠀Spiders 9
/╲/\╭[ ☉ ﹏ ☉ ]╮/\╱\⠀Spiders 10
/╲/\╭༼ ººل͟ºº ༽╮/\╱\⠀Spiders 11
ᄽ῟｢❜ﭣ❜｣῏ᄿ⠀Spiders 12
(=˘ϖ˘=)⠀Buck Tooth Animals 1
( θ ϖ θ )⠀Buck Tooth Animals 2
(●´ϖ`●)⠀Buck Tooth Animals 3
ʃ͠ʘɷʘ͠ƪ⠀Buck Tooth Animals 4
(ꌷϖꌷ)⠀Buck Tooth Animals 5
( ・ϖ・)っ⠀Buck Tooth Animals 6
ヽ(･ϖ･｡)ﾉ⠀Buck Tooth Animals 7
ヽ(･ϖ･ゞ)⠀Buck Tooth Animals 8
(* <><<ϖ<<<<)⠀Buck Tooth Animals 9
(•̀ϖ•́ )⠀Buck Tooth Animals 10
( ˘•ϖ•˘ )⠀Buck Tooth Animals 11
(όϖὸ)⠀Buck Tooth Animals 12
(∵)⠀Other Miscellaneous Animal-like Emoticons 1
( ͒꒪̛ཅ꒪̛ ͒)⠀Other Miscellaneous Animal-like Emoticons 2
（-Φ-）⠀Other Miscellaneous Animal-like Emoticons 3
（’∽’）⠀Other Miscellaneous Animal-like Emoticons 4
(･｀ｪ´･)つ⠀Other Miscellaneous Animal-like Emoticons 5
(∩ё∩)⠀Other Miscellaneous Animal-like Emoticons 6
(͒⑅′࿉‵⑅)͒ෆ*⠀Other Miscellaneous Animal-like Emoticons 7
(͒●❛ੇ࿉❛̛●)͒⠀Other Miscellaneous Animal-like Emoticons 8
~(-仝-)~⠀Other Miscellaneous Animal-like Emoticons 9
≫(‘♀’)≪⠀Other Miscellaneous Animal-like Emoticons 10
≺⋏￣ㅅ￣⋏≻⠀Other Miscellaneous Animal-like Emoticons 11
⊂^j^⊃⠀Other Miscellaneous Animal-like Emoticons 12
ヾﾉ｡ÒㅅÓ)ﾉｼ⠀Other Miscellaneous Animal-like Emoticons 13
⍝◜῁●⌔⃝●῁◝⍝₌₃⠀Other Miscellaneous Animal-like Emoticons 14
(০გ০)⠀Other Miscellaneous Animal-like Emoticons 15
Ψ(●◜ ཅ ◝●)Ψ⠀Other Miscellaneous Animal-like Emoticons 16
૮(ꆚꁝꆚ)ა⠀Other Miscellaneous Animal-like Emoticons 17
(≖` _̆ ′≖⑉)⠀Other Miscellaneous Animal-like Emoticons 18
ᓷ⌽⏖⌽ᓸ⠀Other Miscellaneous Animal-like Emoticons 19
ᓷ᷆⌽⏡⌽᷇ᓸ⠀Other Miscellaneous Animal-like Emoticons 20
(・●・)⠀Other Miscellaneous Animal-like Emoticons 21
(●⁰8⁰●)⠀Other Miscellaneous Animal-like Emoticons 22
:(¦)⠀Other Miscellaneous Animal-like Emoticons 23
̊(̥̂̊♻̥⚉̥♻̥̊)̥̂⠀Other Miscellaneous Animal-like Emoticons 24
ต(●ิ ഠ്ധ ●ิ)ต⠀Other Miscellaneous Animal-like Emoticons 25
(⚭⃚⃙·̫⚭⃚⃙)⠀Other Miscellaneous Animal-like Emoticons 26
❝᷀ົཽꇵ͒❝᷀ົཽ⠀Other Miscellaneous Animal-like Emoticons 27
₍ᵋꏿ৺ꏿᵌ₎⠀Other Miscellaneous Animal-like Emoticons 28
ໂ‧͡‧̫ໃ⠀Other Miscellaneous Animal-like Emoticons 29
(*’ꉤ’*)⠀Other Miscellaneous Animal-like Emoticons 30
்ຶ ഠ്ധ ்ຶ⠀Other Miscellaneous Animal-like Emoticons 31
(͏ ͒ • ꇵ͒ • ͒)⠀Other Miscellaneous Animal-like Emoticons 32
ꇵ᷄ꆯꇵ̥᷅⠀Other Miscellaneous Animal-like Emoticons 33
°ꋣ°⠀Other Miscellaneous Animal-like Emoticons 34
ઇ(⊛த⊛)૬⠀Other Miscellaneous Animal-like Emoticons 35
ꏿѧꏿ⠀Other Miscellaneous Animal-like Emoticons 36
ต(ꇐːːːːꇐ)ต⠀Other Miscellaneous Animal-like Emoticons 37
ლ,ᔑ•ﺪ͟͠•ᔐ.ლ⠀Other Miscellaneous Animal-like Emoticons 38
ミ ﾟДﾟ彡⠀Other Miscellaneous Animal-like Emoticons 39
₍❜◖◟·◞◗❜₎⠀Other Miscellaneous Animal-like Emoticons 40
( മ്ന ഠ്ധ മ്ന )⠀Other Miscellaneous Animal-like Emoticons 41
(๑≧♉ฺ≦)⠀Other Miscellaneous Animal-like Emoticons 42
(((<꒪ꈊ꒪<)))⠀Other Miscellaneous Animal-like Emoticons 43
(//°ꈊ°//)⠀Other Miscellaneous Animal-like Emoticons 44
(° ꈊ °)⠀Other Miscellaneous Animal-like Emoticons 45
(((ლ(͏ ͒ • ꈊ • ͒)ლ)))⠀Other Miscellaneous Animal-like Emoticons 46
(꒪ॢ.̫.̫꒪ )⠀Other Miscellaneous Animal-like Emoticons 47
⊂⚥人⚥⊃⠀Other Miscellaneous Animal-like Emoticons 48
（Ｕ人Ｕ）⠀Other Miscellaneous Animal-like Emoticons 49
（´⑥｀）⠀Other Miscellaneous Animal-like Emoticons 50
(<ಥ<ω<ಥ<)⠀General Miscellaneous 1
ಥ಼ ர் ಥ಼⠀General Miscellaneous 2
❛ ੲ̆ ❛⠀General Miscellaneous 3
໒(•න꒶̰න•)७⠀General Miscellaneous 4
（´☣౪☣)⠀General Miscellaneous 5
⁽͑˙˚̀ⅈ˚́˙⁾̉⠀General Miscellaneous 6
꜏ˏˎ꜊⠀General Miscellaneous 7
*ꏨꉩꏨ*⠀General Miscellaneous 8
(⚈᷁₋̮₍⚈᷁)⠀General Miscellaneous 9
(⁙නₔන⁙)⠀General Miscellaneous 10
•̀رق•́✧⠀General Miscellaneous 11
━━☆＞＾）⠀General Miscellaneous 12
*~●＞＾）⠀General Miscellaneous 13
( ◎⃝⃘ .̫ ◎⃝⃘ )⠀General Miscellaneous 14
(*´◒`*)⠀General Miscellaneous 15
(炎ロ炎）⠀General Miscellaneous 16
(◐▂◑)⠀General Miscellaneous 17
（＄０＄）⠀General Miscellaneous 18
( ･ัω･ั< )⠀General Miscellaneous 19
(○´癶ω癶`○)⠀General Miscellaneous 20
(бвб)⠀General Miscellaneous 21
( ◐ω◐ )⠀General Miscellaneous 22
(০ᄇ০)⠀General Miscellaneous 23
( ﾟσωﾟ)⠀General Miscellaneous 24
⁽⁽ૢ(⁎❝ົཽω❝ົཽ⁎)✧⠀General Miscellaneous 25
⁽ˈ̂ʷˈ̂·⁾⠀General Miscellaneous 26
∩∵)∩★⠀General Miscellaneous 27
(  ்̋.̮˃ ்̋)⍝⠀General Miscellaneous 28
o(‧”’‧)⠀General Miscellaneous 29
(*б●б)⠀General Miscellaneous 30
ₒ˛˚̣⁽⁽(`ᾓू´⁎)⠀General Miscellaneous 31
໒(•න꒶̻න•)७⠀General Miscellaneous 32
(❛̌˴˷❛̌⁎੬৬⠀General Miscellaneous 33
(｀థ ౪ థ´)⠀General Miscellaneous 34
ლ(..ↁc_ↁ..)ლ⠀General Miscellaneous 35
애❣⃛(⌯･ิ느･ิ⌯)⠀General Miscellaneous 36
ପ( ຶཽ ˚̼̮ ຶཽ)ଓ✧⠀General Miscellaneous 37
(´≝◞⊖◟≝｀)⠀General Miscellaneous 38
ತಎತ⠀General Miscellaneous 39
(⑅╸▵╺⑅)ㆀ⠀General Miscellaneous 40
•✞_✞•⠀General Miscellaneous 41
ʿʿᒃ⁽⁰ᒼ ̵⁰⁾ᒄʾʾ⠀General Miscellaneous 42
(ꅔ∀ꅔ)⠀General Miscellaneous 43
( ΄◞ิ .̫.̫ ◟ิ‵)⠀General Miscellaneous 44
Σ(∩˃͈ ╻ ˂͈ ∩)‼︎⠀General Miscellaneous 45
(⚈ੌ๑⚈ੌ⋆ॢ)⠀General Miscellaneous 46
(ම᷄௰ම᷄)⠀General Miscellaneous 47
(•́✧•̀●)⠀General Miscellaneous 48
Ꮿ ౪ Ꮿ⠀General Miscellaneous 49
(*❦ω❦)⠀General Miscellaneous 50
(ಠ_ృ)⠀General Miscellaneous 51
⌈ ⚫▂▂⚫ ⌉⠀General Miscellaneous 52
ཁ ·̼̮ ག⠀General Miscellaneous 53
⑉ඕ⍹ඕ⑉⠀General Miscellaneous 54
(◞‸◟ㆀ)⠀General Miscellaneous 55
ˉ̞̭̭(˘̭⺫˘̭ㆀ)⠀General Miscellaneous 56
σ(ёωё*)⠀General Miscellaneous 57
ꆤѷꆤ⠀General Miscellaneous 58
☻྇˒˒⁔⌕⁔⌕⠀General Miscellaneous 59
∗ꉺ⃗ۈꉺ⃖∗⠀General Miscellaneous 60
(☸ω☸)✦⠀General Miscellaneous 61
(っ⌓☌✿)⠀General Miscellaneous 62
₍ꇪ̥༵ ₎=͟͟͞͞₍ꇪ̥༵₎⠀General Miscellaneous 63
( ꑵ _̆ ꑵ`﹡)⠀General Miscellaneous 64
( ∩ ՞ةڼ◔）⠀General Miscellaneous 65
(ට⸏ुට)⠀General Miscellaneous 66
ᵋ⁼⌙(ૢ•᷄ۿ•᷅╬)⠀General Miscellaneous 67
⋐(ల◕◡◕ల)⋑⠀General Miscellaneous 68
(υᇂνᇂ)⠀General Miscellaneous 69
( ´っ•ч•ｃ` )⠀General Miscellaneous 70
(ˈᕐ ̫ˈ⁎)⠀General Miscellaneous 71
(　‘ᾥ’　)⠀General Miscellaneous 72
⁽͑˙˚̀ⅉ˚́˙⁾̉⠀General Miscellaneous 73
(∂ω∂)⠀General Miscellaneous 74
ଞ(*∂ω∂*｀)ଞ⠀General Miscellaneous 75
(ꊳ٤ꊳ)⠀General Miscellaneous 76
(ΩθΩ)⠀General Miscellaneous 77
(* Ŏ∀Ŏ)･<ﾞ.:’<、⠀General Miscellaneous 78
(亝●亝)⠀General Miscellaneous 79
（ಠิ౪ಠิ*）⠀General Miscellaneous 80
( ͡↑ ͜ʖ ͡↑)⠀General Miscellaneous 81
〳 ◔ Ĺ̯ ◔ 〵⠀General Miscellaneous 82
(∩╹□╹∩)⠀General Miscellaneous 83
┌( ◕ 益 ◕ )ᓄ⠀General Miscellaneous 84
(◕⌂◕⊃⊃)⠀General Miscellaneous 85
ઈ(@̴̨̊̋̐̃̀̽̽ͅ❦@̴̨̊̋̐̃̀̽̽ͅ)ૐ⠀General Miscellaneous 86
*:･✧⃛(ཽ๑ඕัᴗඕั๑)✧⃛*:･⠀General Miscellaneous 87
=。:.ﾟ(●ö◡ö●):.｡+ﾟ⠀General Miscellaneous 88
₍ ⁄⁄⁄ ຶѧ ⁄⁄⁄ ຶ₎⁂⠀No Idea 1
(⁛න↭න⁛)⠀No Idea 2
ଘ(* ຫ࿆ꈲຫ࿆*)⠀No Idea 3
⁍ੈ٥॒̮⁍ੈ⠀No Idea 4
⁝₍˚į˚₎⁝⠀No Idea 5
⊍͝ ⸓̮ ⊍͝⠀No Idea 6
( ͒മ്ത ಷಿ മ്ത ͒)⠀No Idea 7
✧(❝ੌु ˙̬ ❝ੌू⋆)⠀No Idea 8
ʘੂඋ̈ੁʘੂ⠀No Idea 9
,,/(òÓ,),,/⠀No Idea 10
(ؔ❝ ˙̼̮ ؔ❝⁎)⠀No Idea 11
(⊚ຶັົ໋♜⊚ຶັົ໋)⠀No Idea 12
(໐ຶັົ໋≀ˍ໐ຶັົ໋๑)⠀No Idea 13
(⁕௹ۻ௹)⁎✧⠀No Idea 14
(⌯ຶັົ໌໋௰⌯ຶັົ໌໋⁎)⠀No Idea 15
૮( ْ۬۠ ⌣ັຶົ໋ ْ۬۠ ა⠀No Idea 16
(☣ฺ_,☣ฺ)⠀No Idea 17
( ँ ੬ هँ )⠀No Idea 18
(✖ฺ⋒ิ‸⋒ิฺ)ﾉ⠀No Idea 19
(∮UvU◆χ)⠀No Idea 20
(⋆ຶັົ໋௰⋆ຶັົ໋)⠀No Idea 21
(亝ω亝｡)⠀No Idea 22
〈 ●ˡ̑ ̫ ̫̊ ̫ˡ͂● 〉⠀No Idea 23
*✲ﾟ* (͏ ͒ ❛ัू ꇵ͒˘ ͒)⋆*:.⠀No Idea 24
(⁎❞⃘╼╾❞⃘⁎)⠀No Idea 25
(ृᓍृ∗◝੭ᐝ⠀No Idea 26
ˉ̞̭⋆›◡ु‹⋆˄̻̊⠀No Idea 27
‧˚*(¤̴̶̷́ॢω¤̴̶̷̀ॢ๑)₊.⠀No Idea 28
(✾ुӫू✾)⠀No Idea 29
༺‿༻⠀No Idea 30
ȍಷȍ⠀No Idea 31
(•ὴ̶•)⠀No Idea 32
ల(◕ ◠ ◕　)⠀No Idea 33
(✪ິັ໌໋໊ ꆚ ✪ິັ໌໋໊)⠀No Idea 34
⚕͙⚕ ⁎❛ั◡❛ั⁎⠀No Idea 35
˓˓(ค́ಐก̀⁎)՞⠀No Idea 36
˓˓(ꋁꎤुꋁ๑)˒˒՞⠀No Idea 37
(☉ິັ໌໋໊௰☉ິັ໌໋໊)⠀No Idea 38
(∘ິັ໌໋໊︽ੂ∘ິັ໌໋໊)⠀No Idea 39
(⚆ິັ໌໋໊௰⚆ິັ໌໋໊)⠀No Idea 40
₍₋ ู₋⠀No Idea 41
⁽⁽ૢ(⁎❝᷀ົཽω❝᷀ົཽ⁎)✧⠀No Idea 42
˓˓(ꋁꎤुꋁ๑)˒˒⠀No Idea 43
( ੱ ಒౢੱ)₹Ⱡ੭⠀No Idea 44
(●癶ᆺ癶●)⠀No Idea 45
⁺₊(తి̥॔ ˙̭̬̮ తి̥॓)₊⁺ɂ̀ೖ⠀No Idea 46
┏(<<<<：)⠀No Idea 47
(☽ৣˊ⚈̯ˋৣ☾)⠀No Idea 48
ꊢ⃜⃛ٹꊢ⃜⃛⠀No Idea 49
（ಷฺ♊ฺಷฺ)σ⠀No Idea 50
( ఢཻੋีۿఢཻੋี)۶⠀No Idea 51
ꀨଽ(ꍘꍱꆯꍱꍘ)ꀨ⠀No Idea 52
♡⃛˄̻ ̊⋆ට◡ुට⋆˄̻ ̊⠀No Idea 53
°˚(ृ´꒳ˁ　)ु˒˒⠀No Idea 54
∑∵∈◎]～｜⠀No Idea 55
(๑≖ิټ≖ิ)v⠀No Idea 56
ꀨଽ(ꍘꍱꁞꍱꍘ)⠀No Idea 57
(´ . .̫ . `) ༘ؓ ँั๊ྃ⠀No Idea 58
ₒ˛˚̣⁽⁽(`ᾓॢ´⁎)⠀No Idea 59
(　◔ิω◔ิ)⠀No Idea 60
*·✧( ऀืົཽ⸔ ͜⸕ ऀืົཽ*)✧.*⠀No Idea 61
૮( ऀืົཽु ˙̫̮ ऀืົཽू)ა✧⠀No Idea 62
(。☸ฺ⋌⋚⋛⋋☸ฺ。)⠀No Idea 63
₍₍ヾ͜(໐ຶັົ໋௰໐ຶັົ໋๑)ﾉｼ₎₎⠀No Idea 64
₍₍◟(໐ຶັົ໋௰໐ຶັົ໋๑)◞₎₎⠀No Idea 65
˚ஐ₊✧(ؔ❝͋ ˙̥̮ ؔ❝͋ೢ⁎)⁺˳ஐ༚⠀No Idea 66
ஐໍ༚೫*⌡⌡⌡ᕰ͠ ͛ ̼̮ ᕰ͠ ͛ற ෆ༚*ஐຸ⠀No Idea 67
(< ऀืົཽ ˙̫̮ ऀืົཽ)⠀No Idea 68
(⌯◎⃝⃘∀◎⃝⃘⌯)꒭¸ ∣ժ̅˚ʖˋ¸Ϯ ̵̲ ~⠀No Idea 69
੬͑३ુ͗ ᷅ ᷅ ᷆ ̑ ͡ ̑᷄ ̮̑͜ ̇ू ᷅͡ ̑ ̆ ̆३ુ͗⠀No Idea 70
✩̋·°✧̥͘*·˚⁺ˈ✩̋·°✧̥͘*·˚⁺ˈ✩̋·°✧̥͘*·˚⁺ˈ✩̋·°✧̥͘*·˚⁺ˈ⠀Decorations or Embellishments 1
☆彡　　★彡　　☆彡　　★彡 ☆彡　　★彡　　☆彡　　★彡⠀Decorations or Embellishments 2
☆彡★彡☆彡★彡☆彡★彡☆彡★彡⠀Decorations or Embellishments 3
`*:<,．★ ～☆・:.,<*`*:<,．★ ～☆・:.,<*⠀Decorations or Embellishments 4
˚̩͙⚛ ͙*̩̩̥˚̩͙⚛ ͙*̩̩̥˚̩͙⚛ ͙*̩̩̥˚̩͙⚛ ͙*̩̩̥⠀Decorations or Embellishments 5
⸄῁࿆⸅⸄῁̟࿆⸅ྃ⸄῁࿆⸅⸄῁̟࿆⸅ྃ⸄῁࿆⸅⸄῁̟࿆⸅ྃ⸄῁࿆⸅⸄῁̟࿆⸅ྃ⠀Decorations or Embellishments 6
* ੈ✩‧₊˚* ੈ✩‧₊˚* ੈ✩‧₊˚⠀Decorations or Embellishments 7
♡*+:•*∴”:♡.•♬✧♡*+:•*∴”:♡.•♬✧⠀Decorations or Embellishments 8
☆.。.:*・°☆.。.:*・°☆.。.:*・°☆.。.:*・°☆⠀Decorations or Embellishments 9
.₊̣̇.ෆ˟̑*̑˚̑*̑˟̑ෆ.₊̣̇.ෆ˟̑*̑˚̑*̑˟̑ෆ.₊̣̇.ෆ˟̑*̑˚̑*̑˟̑ෆ.₊̣̇.ෆ˟̑*̑˚̑*̑˟̑ෆ.₊̣̇.⠀Decorations or Embellishments 10
჻ღཾཿ༉ ༘჻ღཾཿ༉ ༘჻ღཾཿ༉ ༘჻ღཾཿ჻⠀Decorations or Embellishments 11
⋇⊶⊰❣⊱⊷⋇ ⋇⊶⊰❣⊱⊷⋇⠀Decorations or Embellishments 12
୨୧┄┈୨୧‧⁺̣˚̣̣*̣̩⋆̩·̩̩୨˚̣̣̣̣͙୧·̩̩⋆̩*̣̩˚̣̣⁺̣‧୨୧┈┈୨୧⠀Decorations or Embellishments 13
⋆⋆⃟⊱✪⃝⃞⃝⊰⋆⃟⋆ ⋆⋆⃟⊱✪⃝⃞⃝⊰⋆⃟⋆ ⋆⋆⃟⊱✪⃝⃞⃝⊰⋆⃟⋆⠀Decorations or Embellishments 14
✦͙͙͙*͙*❥⃝∗⁎.ʚɞ.⁎∗❥⃝**͙✦͙͙͙⠀Decorations or Embellishments 15
☮▁▂▃▄☾ ♛ ◡ ♛ ☽▄▃▂▁☮⠀Decorations or Embellishments 16
⠀Multiple Lines 1
｡ﾟ(ﾟ´(00)`ﾟ)ﾟ｡⠀Round Snout Holes 1
(；ﾟ(OO)ﾟ)⠀Round Snout Holes 2
(*´(00)`)’⠀Round Snout Holes 3
ヽ(*’(OO)’)ﾉﾟ⠀Round Snout Holes 4
q(￣(oo)￣)p⠀Round Snout Holes 5
( ´(00)`)⠀Round Snout Holes 6
(*’(OO)’*)⠀Round Snout Holes 7
(￣(oo)￣)ﾉ⠀Round Snout Holes 8
ヾ(；ﾟ(OO)ﾟ)ﾉ⠀Round Snout Holes 9
ヽ(*’(OO)’)ﾉ⠀Round Snout Holes 10
༼ つ◕(oo)◕༽つ⠀Round Snout Holes 11
[ ಠ (oo) ಠ ]⠀Round Snout Holes 12
། ~ ◕ (oo) ◕ ~ །⠀Round Snout Holes 13
| ˵ ･ (oo) ･ ˵ |⠀Round Snout Holes 14
▐ ᓀ (oo) ᓂ ▐⠀Round Snout Holes 15
(*ﾉ（○○）<<<<*)⠀Round Snout Holes 16
໒( ⊚ (oo) ⊚ )७⠀Round Snout Holes 17
（▼(00）▼ﾒ）⠀Round Snout Holes 18
ヽ(*'(OO)’)ﾉ⠀Round Snout Holes 19
_|￣|○ ○|￣|_⠀Round Snout Holes 20
(っﾟ（00）ﾟ；)っ⠀Round Snout Holes 21
(＞（00)＜）⠀Round Snout Holes 22
ᕕ〳 ் (oo) ் 〵╯⠀Round Snout Holes 23
| ~ ￣ (oo) ￣ ~ |⠀Round Snout Holes 24
―(´(００)｀ )→⠀Round Snout Holes 25
(ﾟ´(00)｀ﾟ)ﾟ⠀Round Snout Holes 26
╏ – (oo) – ╏⠀Round Snout Holes 27
▐ ˵ ͠° (oo) °͠ ˵ ▐⠀Round Snout Holes 28
ԅ〳 ᓀ (oo) ᓂ 〵ง⠀Round Snout Holes 29
( ´(00)`)y-~~⠀Round Snout Holes 30
(´･(00)･｀)⠀Round Snout Holes 31
(＞（00)＜）ﾉ⠀Round Snout Holes 32
＼＼(￢(OO)￢<)┌θ☆#)○(oo)●)~ﾉﾉ⠀Round Snout Holes 33
ε=ε=ε=ε=ε=ヾ(；ﾟ(OO)ﾟ)ﾉ⠀Round Snout Holes 34
＝＝＝＝☆┣o(´(００)｀ )⠀Round Snout Holes 35
((o( ´(００)｀)人(´(００)｀ )o))⠀Round Snout Holes 36
(￣（∞）￣)⠀Infinity Sign Snouts 1
(=｀(∞)´=)⠀Infinity Sign Snouts 2
ヾ(＠＾(∞)＾＠)ノ⠀Infinity Sign Snouts 3
(<´∞`)⠀Infinity Sign Snouts 4
(*’(∞)’*)⠀Infinity Sign Snouts 5
q(￣(∞)￣)p⠀Infinity Sign Snouts 6
( ´(∞)`)⠀Infinity Sign Snouts 7
(*’(∞)’*)⠀Infinity Sign Snouts 8
(￣(∞)￣)ﾉ⠀Infinity Sign Snouts 9
ヾ(；ﾟ(∞)ﾟ)ﾉ⠀Infinity Sign Snouts 10
ヽ(*’(∞)’)ﾉ⠀Infinity Sign Snouts 11
༼ つ◕(∞)◕༽つ⠀Infinity Sign Snouts 12
[ ಠ (∞) ಠ ]⠀Infinity Sign Snouts 13
། ~ ◕ (∞) ◕ ~ །⠀Infinity Sign Snouts 14
| ˵ ･ (∞) ･ ˵ |⠀Infinity Sign Snouts 15
▐ ᓀ (∞) ᓂ ▐⠀Infinity Sign Snouts 16
(*ﾉ（∞）<<<<*)⠀Infinity Sign Snouts 17
໒( ⊚ (∞) ⊚ )७⠀Infinity Sign Snouts 18
（▼(∞）▼ﾒ）⠀Infinity Sign Snouts 19
ヽ(*'(∞)’)ﾉ⠀Infinity Sign Snouts 20
(っﾟ（∞）ﾟ；)っ⠀Infinity Sign Snouts 21
(＞（∞)＜）⠀Infinity Sign Snouts 22
ᕕ〳 ் (∞) ் 〵╯⠀Infinity Sign Snouts 23
| ~ ￣ (∞) ￣ ~ |⠀Infinity Sign Snouts 24
―(´(∞)｀ )→⠀Infinity Sign Snouts 25
▐ ˵ ͠° (∞) °͠ ˵ ▐⠀Infinity Sign Snouts 26
ԅ〳 ᓀ (∞) ᓂ 〵ง⠀Infinity Sign Snouts 27
(´･(∞)･｀)⠀Infinity Sign Snouts 28
(｀(●●) ´)⠀Solid Circle Snouts 1
(○｀（●●）´○)ﾉ⠀Solid Circle Snouts 2
ƪ(‾(••)‾”)ʃ⠀Solid Circle Snouts 3
ヾ(￣(●●)￣)ノ⠀Solid Circle Snouts 4
(＝｀(●●)´＝)ﾉ⠀Solid Circle Snouts 5
φ(Ｕ（●●）Ｕｏ)⠀Solid Circle Snouts 6
((o(￣(●●)￣)o))⠀Solid Circle Snouts 7
o(T(●●)T)o⠀Solid Circle Snouts 8
^( ￣(●●)￣)^⠀Solid Circle Snouts 9
“v(￣￣(●●)￣￣)v”⠀Solid Circle Snouts 10
（Ф（●●）Ф）⠀Solid Circle Snouts 11
(#＞（●●）＜#)⠀Solid Circle Snouts 12
(T（●●）T)⠀Solid Circle Snouts 13
(<><<（●●）<<<<)⠀Solid Circle Snouts 14
(○（●●）○)⠀Solid Circle Snouts 15
（☆（●●）☆）⠀Solid Circle Snouts 16
(┬(●●)┬ )⠀Solid Circle Snouts 17
（＾(●●)＾）⠀Solid Circle Snouts 18
（Ф（●●）Ф）/⠀Solid Circle Snouts 19
<<<<(｀（●●）´)<><<⠀Solid Circle Snouts 20
▐ ˵ ͠° (●●) °͠ ˵ ▐⠀Solid Circle Snouts 21
| ˵ ･ (●●) ･ ˵ |⠀Solid Circle Snouts 22
q(￣(●●)￣)p⠀Solid Circle Snouts 23
▐ ᓀ (●●) ᓂ ▐⠀Solid Circle Snouts 24
ԅ〳 ᓀ (●●)) ᓂ 〵ง⠀Solid Circle Snouts 25
| ~ ￣ (●●)) ￣ ~ |⠀Solid Circle Snouts 26
ε＝ε＝ε＝ε＝ε＝┌┤￣￣（●●）￣￣├┘⠀Solid Circle Snouts 27
(￣(▽▽)￣)⠀Miscellaneous Pigs 1
૮⍝◜•⚇•◝⍝ა⠀Miscellaneous Pigs 2
(͒⚈ै⚇༵⚈ै)͒⠀Miscellaneous Pigs 3
( ఠ ⚇̭ ఠ )⠀Miscellaneous Pigs 4
(͒ ॢ ›⚇‹ ॢ)͒୭♡⠀Miscellaneous Pigs 5
(͒⚙⚇༵⚙)͒⠀Miscellaneous Pigs 6
(꒷ຶ⚇̯ ꒷ຶ)⠀Miscellaneous Pigs 7
ฒ(╹ྂ⚇̫╹ྂˇ͙)  ༘⁷̩ ̎⠀Miscellaneous Pigs 8
꒲⌯ ू(ꆧ⚇̭ꆧ ूˆ)⠀Miscellaneous Pigs 9
U・x・U⠀Big Floppy Ears 1
U｡･.･｡U⠀Big Floppy Ears 2
U=･ x ･=U⠀Big Floppy Ears 3
U=๏ x ๏=U⠀Big Floppy Ears 4
U ´꓃ ` U⠀Big Floppy Ears 5
U(,,๏ ⋏ ๏,,)U⠀Big Floppy Ears 6
U(•ㅅ•)U⠀Big Floppy Ears 7
U(ㅇㅅㅇ❀)U⠀Big Floppy Ears 8
U(⁎˃ᆺ˂)U⠀Big Floppy Ears 9
U(´･×･`)U⠀Big Floppy Ears 10
U(´・×・｀)U⠀Big Floppy Ears 11
U( ÒㅅÓ)U⠀Big Floppy Ears 12
U(,,Ő ｘ Ő,,)U⠀Big Floppy Ears 13
U(╹ૅ×╹ૅ)U⠀Big Floppy Ears 14
U( ´•̥×•̥` )U⠀Big Floppy Ears 15
／(･ × ･)＼⠀Straight Down Ears 1
／(^ x ^)＼⠀Straight Down Ears 2
／(^ x ^=)＼⠀Straight Down Ears 3
／(=๏ x ๏=)＼⠀Straight Down Ears 4
／(=´x`=)＼⠀Straight Down Ears 5
／(=∵=)＼⠀Straight Down Ears 6
／(=⌒x⌒=)＼⠀Straight Down Ears 7
／(=✪ x ✪=)＼⠀Straight Down Ears 8
／(≡・ x ・≡)＼⠀Straight Down Ears 9
／(≧ x ≦)＼⠀Straight Down Ears 10
／(v x v)＼⠀Straight Down Ears 11
／(=∵=)＼⠀Straight Down Ears 12
／(≡・ x ・≡)＼⠀Straight Down Ears 13
/ (,,๏ ⋏ ๏,,)＼⠀Straight Down Ears 14
／(￫ x ◕=)＼⠀Straight Down Ears 15
／(◕ x <<<< )＼⠀Straight Down Ears 16
／(◕ x ≦ )＼⠀Straight Down Ears 17
/ (ㅇㅅㅇ❀)＼⠀Straight Down Ears 18
/ (•ㅅ•)＼⠀Straight Down Ears 19
/ (´･×･`)＼⠀Straight Down Ears 20
/ (,,Ő ｘ Ő,,)＼⠀Straight Down Ears 21
/ (⁎˃ᆺ˂)＼⠀Straight Down Ears 22
/ (´・×・｀)＼⠀Straight Down Ears 23
/ (╹ૅ×╹ૅ)＼⠀Straight Down Ears 24
/ ( ÒㅅÓ)＼⠀Straight Down Ears 25
/ (⁎˃ᆺ˂)＼⠀Straight Down Ears 26
/ ( ´•̥×•̥` )＼⠀Straight Down Ears 27
⌒(・x・)⌒⠀Rounded Ears 1
⌒(｡･.･｡)⌒⠀Rounded Ears 2
⌒(=･ x ･=)⌒⠀Rounded Ears 3
⌒(=๏ x ๏=)⌒⠀Rounded Ears 4
⌒(=･ x ･=)⌒⠀Rounded Ears 5
⌒(=✪ x ✪=)⌒⠀Rounded Ears 6
⌒(=⌒x⌒=)⌒⠀Rounded Ears 7
⌒(≡・ x ・≡)⌒⠀Rounded Ears 8
⌒(≧ x ≦)⌒⠀Rounded Ears 9
⌒(=∵=)⌒⠀Rounded Ears 10
⌒(,,๏ ⋏ ๏,,)⌒⠀Rounded Ears 11
⌒ (⁎˃ᆺ˂)⌒⠀Rounded Ears 12
⌒(╹ૅ×╹ૅ)⌒⠀Rounded Ears 13
⌒( ÒㅅÓ)⌒⠀Rounded Ears 14
⌒(ㅇㅅㅇ❀)⌒⠀Rounded Ears 15
⌒(•ㅅ•)⌒⠀Rounded Ears 16
⌒(,,Ő ｘ Ő,,)⌒⠀Rounded Ears 17
⌒( ´•̥×•̥` )⌒⠀Rounded Ears 18
￣(〃ﾟｏ ﾟ〃)￣⠀Straight Out Ears 1
￣(=⌒・⌒=)￣⠀Straight Out Ears 2
￣( ´•̥×•̥` )￣⠀Straight Out Ears 3
￣(ㅇㅅㅇ❀)￣⠀Straight Out Ears 4
￣ (⁎˃ᆺ˂)￣⠀Straight Out Ears 5
￣(=✪ x ✪=)￣⠀Straight Out Ears 6
￣(=･ x ･=)￣⠀Straight Out Ears 7
￣(,,Ő ｘ Ő,,)￣⠀Straight Out Ears 8
￣( ÒㅅÓ)￣⠀Straight Out Ears 9
￣(,,๏ ⋏ ๏,,)￣⠀Straight Out Ears 10
￣(•ㅅ•)￣⠀Straight Out Ears 11
￣(╹ૅ×╹ૅ)￣⠀Straight Out Ears 12
￣(=⌒x⌒=)￣⠀Straight Out Ears 13
￣(=๏ x ๏=)￣⠀Straight Out Ears 14
(,,๏ ⋏ ๏,,)⠀No Ears 1
(•ㅅ•)⠀No Ears 2
(ㅇㅅㅇ❀)⠀No Ears 3
(๏ᆺ๏υ)⠀No Ears 4
(⁎˃ᆺ˂)⠀No Ears 5
(๑òᆺó๑)⠀No Ears 6
(｡´•ㅅ•｡)⠀No Ears 7
( ´•̥×•̥` )⠀No Ears 8
(´･×･`)⠀No Ears 9
(´・×・｀)⠀No Ears 10
( ¯•ω•¯ )⠀No Ears 11
（ ÒㅅÓ)⠀No Ears 12
(=‘ｘ‘=)⠀No Ears 13
(,,Ő ｘ Ő,,)⠀No Ears 14
(′⅄‵)⠀No Ears 15
(๑╹ᆺ╹)⠀No Ears 16
(,,◕ ⋏ ◕,,)⠀No Ears 17
(╹ૅ×╹ૅ)⠀No Ears 18
˚ᆺ˚⠀No Ears 19
(乂☉ｪ☉=)⠀No Ears 20
（≡・　x　・≡）⠀No Ears 21
○(・x・)⠀No Ears 22
⁽⁽˙˟˙⁾⁾⠀Tiny Rabbits 1
( °̥̥̥̥̥̥̥̥˟°̥̥̥̥̥̥̥̥ )⠀Tiny Rabbits 2
⁽˙̄˟˙̄⁾⠀Tiny Rabbits 3
､., ⌒ ､., ⌒ ､., ⌒ ､., ⌒ ､., ⌒ ､., ⌒ ／( =ﾟｪﾟ=)ヽ⠀Hopping Rabbits 1
､., ⌒ ､., ⌒ ､., ⌒ ､., ⌒ ､., ⌒ ､., ⌒￣(=∵=)￣⠀Hopping Rabbits 2
､., ⌒ ､., ⌒ ､., ⌒ ､., ⌒ ､., ⌒ ､., ⌒／(・ x ･)＼⠀Hopping Rabbits 3
૮⍝◜•˕̮•◝⍝ა⠀Miscellaneous Rabbits 1
૮( ᵒ̌ૢ௰ᵒ̌ૢ )ა⠀Miscellaneous Rabbits 2
૮(⋆❛ہ❛⋆)ა⠀Miscellaneous Rabbits 3
( ்̓˟்̓)⠀Miscellaneous Rabbits 4
⊂((・x・))⊃⠀Miscellaneous Rabbits 5
ヾ( ´｡ •x• ｡` )ﾉ”⠀Miscellaneous Rabbits 6
(/(°∞°)\)⠀Miscellaneous Rabbits 7
ଽ ฅ૮( ꒪〰꒪)აฅ⠀Miscellaneous Rabbits 8
○(･x･)○⠀Miscellaneous Rabbits 9
₍ᐢ ›̥̥̥ ༝ ‹̥̥̥ ᐢ₎⠀Miscellaneous Rabbits 10
(๑་ ༝ ༌๑)ෆ*⠀Miscellaneous Rabbits 11
(*´･x･`)ゞ⠀Miscellaneous Rabbits 12
／(v x v｡)人(｡v x v)＼⠀Miscellaneous Rabbits 13
<(〃⊙౪ ∩＝)/⠀Miscellaneous Rabbits 14
-(๑☆‿ ☆#)ᕗ⠀Miscellaneous Rabbits 15
((☆＾⌓ ＾☆)╭⠀Miscellaneous Rabbits 16
((o⊙Σ ⊙｡)m⠀Miscellaneous Rabbits 17
｢(<´Σ ｀〃)ヘ⠀Miscellaneous Rabbits 18
｢(#Φ益 Φo)∩⠀Miscellaneous Rabbits 19
｢(＝＞o≦＝)ﾉ⠀Miscellaneous Rabbits 20
~(｡☉︵ ಠ@)<><<⠀Miscellaneous Rabbits 21
~(๑ñ﹏ ⊙☆)ノ⠀Miscellaneous Rabbits 22
⊂(o•ิ▂ ñ*)づ⠀Miscellaneous Rabbits 23
┗( ●-﹏ ｀｡)づ⠀Miscellaneous Rabbits 24
╭ (oㅇ‿ o#)ᕗ⠀Miscellaneous Rabbits 25
╮ (☆-_ ⊙<)ゞ⠀Miscellaneous Rabbits 26
╰(๑＾⌓ ＾＝)ᕗ⠀Miscellaneous Rabbits 27
ヾ (<・﹏ •̀☆)b⠀Miscellaneous Rabbits 28
ヾ (✿＞﹏ ⊙〃)ノ⠀Miscellaneous Rabbits 29
ヽ(♡≧m´｡)っ⠀Miscellaneous Rabbits 30
m(★⊙¬ ㅇ ●)ლ⠀Miscellaneous Rabbits 31
Ｏ(*＠д o#)づ⠀Miscellaneous Rabbits 32
Ｏ(o＾O ｀<)人⠀Miscellaneous Rabbits 33
Σ(@°xº♡)/⠀Miscellaneous Rabbits 34
Σ(♡＠﹏ ＠☆)ﾉ”⠀Miscellaneous Rabbits 35
Σ(๑+⌓ o｡)シ⠀Miscellaneous Rabbits 36
φ( ●⌒へ ⌒〃)o⠀Miscellaneous Rabbits 37
ψ(๑∩⌓ ∩ ●)y⠀Miscellaneous Rabbits 38
щ (*ㅇ△ Φ☆)ノ⠀Miscellaneous Rabbits 39
ლ (#｀ﾛ＾<)<><<⠀Miscellaneous Rabbits 40
ᕙ (<｀⊥ ＾★)┐⠀Miscellaneous Rabbits 41
ᕙ (✿⊙へ ⊙〃)⠀Miscellaneous Rabbits 42
ᕙ (❁^д ^*)っ⠀Miscellaneous Rabbits 43
ᕦ(<*Σ ⌒❁)ᕗ⠀Miscellaneous Rabbits 44
へ( ●｀ㅅ ｀☆)ლ⠀Miscellaneous Rabbits 45
へ(｡•ิ‿ -〃)⠀Miscellaneous Rabbits 46
┗(•̀へ •́ ╮ )⠀Miscellaneous Rabbits 47
╭( ✖_✖ )╮⠀Miscellaneous Rabbits 48
ε=ε=ε=ε=ε=┌(；　・＿・)┘⠀Running with One Arm Up and One Arm Down 1
ε=ε=┏( <><<_<<<<)┛⠀Running with One Arm Up and One Arm Down 2
ε=ε=ε=┌(๑ʘ∀ʘ)┘⠀Running with One Arm Up and One Arm Down 3
ε=ε=ε=ε=┏(<￣▽￣)┛⠀Running with One Arm Up and One Arm Down 4
ε=ε=ε=ε=ε=ε=┌(๑ʘ∀ʘ)┘⠀Running with One Arm Up and One Arm Down 5
ε＝┏(･ω･)┛⠀Running with One Arm Up and One Arm Down 6
ε=ε=ε=ε=ε=ε=┌(<￣◇￣)┘⠀Running with One Arm Up and One Arm Down 7
三┏ ( ˘ω˘ )┛⠀Running with One Arm Up and One Arm Down 8
₍₍ ᕕ(´◓⌓◔)ᕗ⁾⁾⠀Running with One Arm Up and One Arm Down 9
ε=┌(<･_･)┘⠀Running with One Arm Up and One Arm Down 10
ε=ε=ε=ε=ε=ε=┌(￣ー￣)┘⠀Running with One Arm Up and One Arm Down 11
└(<><<ω<<<<。)┐-=≡⠀Running with One Arm Up and One Arm Down 12
ε=ε=ε=ε┏(●´Д｀●)┛⠀Running with One Arm Up and One Arm Down 13
ε=ε=┏( ・＿・)┛⠀Running with One Arm Up and One Arm Down 14
ᕕ( ◎_◎)ᕗ⠀Running with One Arm Up and One Arm Down 15
ε=ε=ε=ε=ε=ε=┏(*´∀｀)┛⠀Running with One Arm Up and One Arm Down 16
=ε=ε=ε=ε=┌(`<@@)┘⠀Running with One Arm Up and One Arm Down 17
┏( ゜)ਊ゜)┛⠀Running with One Arm Up and One Arm Down 18
ᕕ(╯°□°)ᕗ⠀Running with One Arm Up and One Arm Down 19
・・・・・・・┌|*´∀｀|┘⠀Running with One Arm Up and One Arm Down 20
ε=┏(*`＞ω<<<<)┛⠀Running with One Arm Up and One Arm Down 21
===≡≡≡｡ﾟ┌(ﾟ´Д`ﾟ)┘ﾟ｡⠀Running with One Arm Up and One Arm Down 22
┏┃*･д┃┛⠀Running with One Arm Up and One Arm Down 23
┗(^o^　)┓三⠀Running with One Arm Up and One Arm Down 24
┌（・Σ・）┘≡З⠀Running with One Arm Up and One Arm Down 25
ᕕ༼✿•̀︿•́༽ᕗ⠀Running with One Arm Up and One Arm Down 26
C= C= C= C= C= C= C= C= C= ┌(<・ω・)┘⠀Running with One Arm Up and One Arm Down 27
ε＝ε＝ε＝ε＝ε＝┌┤￣￣（●●）￣￣├┘⠀Running with One Arm Up and One Arm Down 28
C= C= C= C= C= C= ┌(<･_･)┘ ））●⠀Running with One Arm Up and One Arm Down 29
ε===(っ≧ω≦)っ⠀Running with Arms Out Going for a Hug 1
─=≡Σ((( つ•̀ω•́)つ⠀Running with Arms Out Going for a Hug 2
ε=ε=(っ*´□`)っ⠀Running with Arms Out Going for a Hug 3
─=≡Σ(([ ⊐•̀⌂•́]⊐⠀Running with Arms Out Going for a Hug 4
ε=ε=(⊃≧□≦)⊃⠀Running with Arms Out Going for a Hug 5
─=≡Σ((( つ◕ل͜◕)つ⠀Running with Arms Out Going for a Hug 6
───==≡≡ΣΣ((( つºل͜º)つ⠀Running with Arms Out Going for a Hug 7
─=≡Σ((( つ ◕o◕ )つ⠀Running with Arms Out Going for a Hug 8
……..(((((￢￣▽￣)￢⠀Running with Arms Out Going for a Hug 9
～(((((っ*´_⊃｀)っ⠀Running with Arms Out Going for a Hug 10
-=≡Σ(((⊃ﾟ∀ﾟ)つ⠀Running with Arms Out Going for a Hug 11
!!Σ≡≡≡((っ`･Å･)っ⠀Running with Arms Out Going for a Hug 12
!!((((((っ<ﾟ∀ﾟ)っ⠀Running with Arms Out Going for a Hug 13
ε==ε==(っ*｀oЗo*)っ⠀Running with Arms Out Going for a Hug 14
≡≡≡(⊃´･Δ･`)⊃⠀Running with Arms Out Going for a Hug 15
(((((っ－＿－)っ⠀Running with Arms Out Going for a Hug 16
⊂(‘ω’⊂ )))Σ≡=─༄༅༄༅༄༅༄༅༄༅⠀Running with Arms Out Going for a Hug 17
ε=ε=ε=ε=ε=ε=ε=ε= ━( ^O^)━⠀Running with Arms Out Going for a Hug 18
⌒⌒　　　⌒ “⊂(　っ☉ω☉)っ⠀Running with Arms Out Going for a Hug 19
！(∩ω)⊃ —==三 ⊂⌒っ´ㅅ)っ⠀Running with Arms Out Going for a Hug 20
⊂＝⊂＝⊂(┛ﾟΘﾟ)┛⠀Running with Arms Up for No Particular Reason 1
ε-ε-ヾ(o´∀)ノ⠀Running with Arms Up for No Particular Reason 2
ε=(｡ﾉ･ω･)ﾉ⠀Running with Arms Up for No Particular Reason 3
ε=ε=ε=(#`・д・)/⠀Running with Arms Up for No Particular Reason 4
ε=ε=(ノ≧∇≦）ノ⠀Running with Arms Up for No Particular Reason 5
ε＝ε＝ヾ（（●・ω・）ﾉ⠀Running with Arms Up for No Particular Reason 6
٩(•౪•٩)三⠀Running with Arms Up for No Particular Reason 7
☆ヾ(･ε･*)ﾉﾞ =з=з=з⠀Running with Arms Up for No Particular Reason 8
ε=(ﾉo`･∀･)ﾉ⠀Running with Arms Up for No Particular Reason 9
ヾ(･c_,･｡) ﾉ =з =з= з⠀Running with Arms Up for No Particular Reason 10
♪ε=ε=ε=ﾍ(*≧∇)ﾉ~⠀Running with Arms Up for No Particular Reason 11
ε=ε=ε=(ﾉ≧∀)ﾉ⠀Running with Arms Up for No Particular Reason 12
ε=ε=ε=ε=ε” “(/*’-‘*)/⠀Running with Arms Up for No Particular Reason 13
(=(=(=(=(=(／(ｴ)￣)／⠀Running with Arms Up for No Particular Reason 14
C= C= C= ⠀Running with Arms Up for No Particular Reason 15
[emai<<#160<pro<ec<ed]⠀Running with Arms Up for No Particular Reason 16
(/o･ｪ･o)@/⠀Running with Arms Up for No Particular Reason 17
ε≡(ノ´＿ゝ｀）ノ⠀Running with Arms Up for No Particular Reason 18
☆ﾐ(o*･ω･)ﾉ⠀Running with Arms Up for No Particular Reason 19
～(((((((っ´Ι`)ﾉ⠀Running with Arms Up for No Particular Reason 20
!!≡≡≡ﾍ(*-ω-)ﾉ⠀Running with Arms Up for No Particular Reason 21
ε=ε=ε=(#ﾉ~ω~)ﾉ⠀Running with Arms Up for No Particular Reason 22
☆⌒v⌒v⌒ヾ((｀･∀･´)ﾉ⠀Running with Arms Up for No Particular Reason 23
ε＝ε＝(((((○´3`)ﾉ⠀Running with Arms Up for No Particular Reason 24
ヾ(Ô‿Ô✾)ﾉ=з =з⠀Running with Arms Up for No Particular Reason 25
– =͟͟͞͞ =͟͟͞͞ ﾍ( ´Д`)ﾉ⠀Running Away in Fear 1
ε=ε=(怒ﾟДﾟ)ﾉ⠀Running Away in Fear 2
ヽ(￣д￣<)ノ=3=3=3⠀Running Away in Fear 3
ε=ε=ε=(۶•̀Д•́)۶⠀Running Away in Fear 4
ε＝ε＝ε＝(((((ﾉ｀･Д･)ﾉ⠀Running Away in Fear 5
(◞º❒º)◞₎₎(◟º❑º)◟⁾⁾➟➠➨⠀Running Away in Fear 6
ε=٩(●❛ö❛)۶⠀Running Away in Fear 7
≡≡≡=(ﾉTдT)ﾉ⠀Running Away in Fear 8
..･ヾ(。￣□￣)ﾂ⠀Running Away in Fear 9
⊂(ﾟДﾟ<⊂⌒`つ⠀Running Away in Fear 10
(c=(c=(c=(c=(ﾟﾛﾟ<c=⠀Running Away in Fear 11
ε=ε=ε=ε=ε=(o- -)o⠀Running Away in Fear 12
!!Σ(ﾟДﾟ<≡≡≡≡≡ヾ(<ﾟдﾟ)/⠀Running Away in Fear 13
ε＝ε＝ε＝┌(<ﾟдﾟ)┘⠀Running Away in Fear 14
≡┏|*´･Д･|┛⠀Running Away in Fear 15
ε=ε=εε=ε=ε=（　┯_┯）⠀Running Away in Fear 16
ε=ε=ε=(ﾉTдT)ﾉ⠀Running Away in Fear 17
～ε～ε～┌(|||´Д｀)ノ⠀Running Away in Fear 18
ε=ε=ε=┏(ﾟロﾟ<)┛⠀Running Away in Fear 19
ε=ε=ε=ε=＼(<´□｀)/⠀Running Away in Fear 20
C= C= C= C=(o<><<ﾛ)o⠀Running Away in Fear 21
ヽ(￣д￣<)ﾉ=3=3=3⠀Running Away in Fear 22
ε=ε=ε=ε=(ノ*´Д｀)ノ⠀Running Away in Fear 23
ε=ε=ε=ε=ε=ヾ(<ﾟﾛﾟ)ﾉ⠀Running Away in Fear 24
ε=ε=ε=ε=ε=(；ﾟロﾟ)⠀Running Away in Fear 25
⊂(ﾟДﾟ⊂⌒｀つ≡≡≡⠀Running Away in Fear 26
⌒Ｙ⌒Ｙ⌒ ヾ(ｏ´Д｀)ﾉ⠀Running Away in Fear 27
ε==ε==(ﾉ゜д゜)ﾂ⠀Running Away in Fear 28
ε=ε=ε=ε=ε=ヾ(；ﾟ(OO)ﾟ)ﾉ⠀Running Away in Fear 29
ε=ε=ε=(((怒ﾟДﾟ)ﾉﾉ⠀Running Away in Fear 30
ε=ε=ε=(*ﾉ´Д｀)ﾉﾟ⠀Running Away in Fear 31
ε=ε=(*ﾉ´Д`)ﾉ⠀Running Away in Fear 32
ヾ(￣Q￣ヾ))))ミ～～⠀Running Away in Fear 33
ε=ε=ε=ﾍ(* – -)ﾉ⠀Running Away in Fear 34
｡｡゛(ﾉ<><<<<<<)ﾉ⠀Running Away in Fear 35
ﾚ(ﾟ∀ﾟ<)ﾍ=З=З=З⠀Running Away in Fear 36
ε≡Ξ≡Ξ≡ヽ( <￣〇￣)ﾉ⠀Running Away in Fear 37
ε＝（ﾉﾟдﾟ）ﾉ⠀Running Away in Fear 38
ε=ε=ε=┌(；´ﾟｪﾟ)┘⠀Running Away in Fear 39
γ⌒γ⌒γﾟ･*:.●　⊂(ﾟﾛﾟ⊂≡≡===⠀Running Away in Fear 40
C= C= C= C= C= C= 。・゜゜ヽ| ；∀；|ノ⠀Running Away in Fear 41
★⌒Ｙ⌒Ｙ⌒Ｙ⌒Ｙ⌒ ヾ(oﾟДﾟ)ﾉ⠀Running Away in Fear 42
===≡≡≡。゜┌(゜☣ฺД☣ฺ)┘゜。⠀Running Away in Fear 43
=͟͟͞͞( ∩ ‘ヮ’=͟͟͞͞) ੭ु⁾⁾⠀Lines of Speed 1
=͟͟͞͞=͟͟͞͞ ⊂(=͟͟͞͞=͟͟͞͞っ☉ω=͟͟͞͞☉)っ=͟͟͞͞⠀Lines of Speed 2
=͟͟͞͞(꒪ᗜ꒪ ‧̣̥̇)!!!!=͟͟͞͞⠀Lines of Speed 3
=͟͟͞͞( ๑⃙⃘°◊°๑⃙⃘ )⠀Lines of Speed 4
῍̩̖̬ ̎ ̎=͟͟͞͞(꒪ͦ॓ ˈ̫̮ ꒪ͦ॔)=͟͟͞͞८ಯು✧⠀Lines of Speed 5
=͟͟͞͞(๑•̀ㅁ•́ฅ✧⠀Lines of Speed 6
┗=͟͟͞͞( ˙∀˙)=͟͟͞͞┛⠀Lines of Speed 7
(ृ°͈꒳​°͈ ृ =͟͟͞͞)ु≡:*・.*⠀Lines of Speed 8
=͟͟͞͞( •̀д•́)))⠀Lines of Speed 9
ਭ३౽=͟͟͞͞(((ഽʻ⁸ʻ)ഽ⠀Lines of Speed 10
=͟͟͞͞(　 ω )=͟͟͞͞　³ ³⠀Lines of Speed 11
三=͟͟͞͞( ∩ ‘ヮ’=͟͟͞͞) ੭ु⁾⁾⠀Lines of Speed 12
=͟͟͞͞ (০͂ ̵̻০͂)ԓ⠀Lines of Speed 13
=͟͟͞͞≠⌓̈⃝\ᵒᵐᵍ⠀Lines of Speed 14
一二三☞ ´◔‿ゝ◔ `)☞⠀Running with Lines Behind 1
─=≡Σ((((͡◔ ͜ʖ ͡◔)⠀Running with Lines Behind 2
─=≡Σ((((ó ì_í)=ó⠀Running with Lines Behind 3
三三三ʅ(；◔౪◔)ʃ⠀Running with Lines Behind 4
૮(”ړ ა)͞=͟͟͞͞=͟͟͞͞=͟͟͞͞=͟͟͞͞=͟͟͞͞=͟͟͞͞ #⠀Running with Lines Behind 5
ΣΣ≡≡≡ｰ(ｰ・ω･)ｰ⠀Running with Lines Behind 6
｢(◔ω◔「)三⠀Running with Lines Behind 7
｢(⑅◔ω◔「)三⠀Running with Lines Behind 8
(’ω’ ⊃)⊃三二一⠀Running with Lines Behind 9
●~*＼(-_＼)・・・ε=ε=ε=┏(<-_-)┛⠀Running Because of Reasons 1
●~* ε≡≡≡ﾍ(<￣▽￣)ﾉ⠀Running Because of Reasons 2
εε===(⊃$∀$)⊃ーーーーー[ $ $ $ ]⠀Running Because of Reasons 3
εε===(⊃$∀$)⊃ーーーーー[￥￥￥]⠀Running Because of Reasons 4
。。°°┏┓。。ﾍ( ^0^)ﾉ┏┓　　┏┓　　┏┓⠀Running Because of Reasons 5
ヾ(<ﾟ皿ﾟ)ﾉ･･･ ⊆￣U)┬┬ﾉ~”　=3 =3⠀Running Because of Reasons 6
○～　　　　　　　　　　 ＼(゜口゜｜｜＼)⠀Running Because of Reasons 7
(￣ー￣〃)ﾉヽ(･_･、))))))))⠀Running Because of Reasons 8
(*ﾉД｀)ﾉ:.*:.｡.:ﾟ..:*.:ヾ(´Дヽ*)⠀Running Because of Reasons 9
ε≡ ε≡ ε≡ ε＝ （#・ж・）⠀Running Because of Reasons 10
⊂(( っ☉ω☉)っ　　～εїз⠀Running Because of Reasons 11
(/´Д｀)/Heeeeeeee<p!!!!!　!!Σ(ﾟДﾟ<≡≡≡≡≡ヾ(<ﾟдﾟ)/⠀Running Because of Reasons 12
～♥（ﾉ´∀`）ﾉ田　ε=ε=ε=Γ（ｌｌｌ`Д´ｌｌｌ）」⠀Running Because of Reasons 13
੯ू•́ू ໒꒱⁼³₌₃⠀Hedgehogs 1
੯”ړ ও͞=͟͟͞͞=͟͟͞͞=͟͟͞͞=͟͟͞͞=͟͟͞͞=͟͟͞͞⠀Hedgehogs 2
੯”ཻړ ა͞=͟͟͞͞=͟͟͞͞=͟͟͞͞=͟͟͞͞=͟͟͞͞=͟͟͞͞⠀Hedgehogs 3
=͟͟͞͞ʕ•̫͡•ʔ=͟͟͞͞ʕ•̫͡•ʔ=͟͟͞͞ʕ•̫͡•ʔ⠀Bears 1
°◦=͟͟͞͞ʕ̡̢̡ु•̫͡•ʔ̡̢̡ु ☏⠀Bears 2
=͟͟͞͞ʕ•̀=͟͟͞͞ʕ•̀▿•́=͟͟͞͞ʕ•̀▿•́ʔ=͟͟͞͞ʕ•̀▿•⠀Bears 3
=͟͟͞͞ʕ•̫͡•ʔ =͟͟͞͞ʕ•̫͡•ʔ =͟͟͞͞ʕ•̫͡•ʔ =͟͟͞͞ʕ•̫͡•ʔ =͟͟͞͞ʕ•̫͡•ʔ⠀Bears 4
=͟͟͞͞(๑•̀=͟͟͞͞(๑•̀д•́=͟͟͞͞(๑•̀д•́๑)=͟͟͞͞(๑•̀д•́)))⠀In a Blur 1
=͟͟͞͞(๑•̀д•́๑=͟͟͞͞(๑•̀д•́๑=͟͟͞͞(๑•̀д•́๑)⠀In a Blur 2
٩(ﾟ∀三ﾟ三∀ﾟ)⠀Running Back and Forth 1
(´×д×`三꒪д꒪ <)⠀Running Back and Forth 2
=͟͟͞͞ ➵=͟͟͞͞⁽⁽◞(꒪ͦ ˈ̫̮ ꒪ͦ=͟͟͞͞ ꒪ͦ ˈ̫̮ ꒪ͦ)◟⁾⁾➴⠀Running Back and Forth 3
˓˓◟(˃◟̵◞̵˂⁎=͟͟͞͞ ⁎˃◟̵◞̵˂)◞˒˒⠀Running Back and Forth 4
ヾ(ﾟ∀ﾟ○)ﾂ三ヾ(●ﾟ∀ﾟ)ﾉ⠀Running Back and Forth 5
ε=ε=ε= (э^✪ｪ✪^)э⠀Running with Large Clouds of Dust Behind 1
ε=ε=ε=ε=ε=(ｏ゜―゜)ｏ⠀Running with Large Clouds of Dust Behind 2
ε＝ε＝ε＝ε＝ε＝(ｏ・・)ｏ⠀Running with Large Clouds of Dust Behind 3
o(▼Д▼ﾒo)=3 =3 =3⠀Running with Large Clouds of Dust Behind 4
ε=ε=((( ^-x-^)ﾉ⠀Running with Large Clouds of Dust Behind 5
ε=ε=ε=ε=ε=ε= ◟( ⚫͈ω⚫̤)◞⠀Running with Large Clouds of Dust Behind 6
(･ω･｡)ﾉ=з=з=з⠀Running with Large Clouds of Dust Behind 7
ε=ε=ε=ヾ(э^・ｪ・^)э⠀Running with Large Clouds of Dust Behind 8
ε＝o(*’◡͐’)o⠀Running with Large Clouds of Dust Behind 9
（´□｀；）=З=З=З=З=З=З⠀Running with Large Clouds of Dust Behind 10
o(￣･･￣o)))=3⠀Running with Large Clouds of Dust Behind 11
뮻⁼³₌₃⠀Running with Small Clouds of Dust Behind 1
٩뮹۶⁼³₌₃⠀Running with Small Clouds of Dust Behind 2
(`ન̇´) ⁼³₌₃⠀Running with Small Clouds of Dust Behind 3
(ↀДↀ)⁼³₌₃⠀Running with Small Clouds of Dust Behind 4
٩(ै ̀ ๔ิ ́ )۶༴ ⁼³₌₃⠀Running with Small Clouds of Dust Behind 5
٩(•ི̛ᵋ•̛)ྀ۶⁼³₌₃⠀Running with Small Clouds of Dust Behind 6
ૃ(ó˳ò ૃ)՞⌯ɜɜɜ⠀Miscellaneous Running Emoticons 1
へ( ʘ͡ ₒ ʘ͡ )╮/\╱\⠀Miscellaneous Running Emoticons 2
三(卍 ˘ω˘))卍⠀Miscellaneous Running Emoticons 3
ღ(◔ڼ◔ღ)ミ⠀Miscellaneous Running Emoticons 4
৫(”ړ৫)˒˒˒˒⠀Miscellaneous Running Emoticons 5
Σ(゜ワﾟ⊂)≡≡≡ззз⠀Miscellaneous Running Emoticons 6
!!Σ(゜ワﾟ⊂)≡≡≡ззз⠀Miscellaneous Running Emoticons 7
=͟͟͞͞◎(◎ ^o^)◎⠀Miscellaneous Running Emoticons 8
˹⁽ˆ⁰ˆ˺ ⁾˺ʾʾʾʾ⠀Miscellaneous Running Emoticons 9
ʿʿʿʿ˹⁽ ˹ˆ⁰ˆ⁾˺⠀Miscellaneous Running Emoticons 10
<<<<!– (‘<<<<_｀)⊃ )⊃ –<><<⠀Miscellaneous Running Emoticons 11
（（（（（（（（　゜□゜）ノ⠀Miscellaneous Running Emoticons 12
͛꒰ू ऀ•̥́ꈊ͒ੁ•ૅू॰˳ऀ꒱ ͟͟͞ ̊ ̥ ̥⠀Complex Running Emoticons 1
٩꒰´·⌢•｀꒱۶⁼³₌₃⠀Complex Running Emoticons 2
━ =͟͟͞͞(๏้♓๏้)⠀Complex Running Emoticons 3
** =͟͟͞͞(งꏿ᷅૩ꏿ᷄)ง⁼³₌₃⠀Complex Running Emoticons 4
(ꏿ᷄౪ ꏿ᷄ ̨ )͞˭̳̳̳˭̳̳̳ˍ̿̿ˍ̿ˌ˳ˏ̇⋅∴༣⠀Complex Running Emoticons 5
٩̋٩̋(ꄬຶȏ ꄬຶ=͟͟͞͞)⠀Complex Running Emoticons 6
̨(༎ິ῀̫ ༎ິ ̨ )͞˭̳̳̳˭̳̳̳ˍ̿̿ˍ̿ˌ˳ˏ̇⋅∴༣⠀Complex Running Emoticons 7
̨(༠౪༠ ̨ )͞˭̳̳̳˭̳̳̳ˍ̿̿ˍ̿ˌ˳ˏ̇⋅∴༣⠀Complex Running Emoticons 8
( ≧Д≦)⠀No tears 1
((´д｀))⠀No tears 2
(∩︵∩)⠀No tears 3
(▰˘︹˘▰)⠀No tears 4
(✖╭╮✖)⠀No tears 5
(‘A`)⠀No tears 6
(︶︹︺)⠀No tears 7
(＠´＿｀＠)⠀No tears 8
（´＿｀）⠀No tears 9
(⊙︿⊙✿)⠀No tears 10
(⌣_⌣”)⠀No tears 11
(▰︶︹︺▰)⠀No tears 12
~(｡☉︵ ಠ@)<><<⠀No tears 13
⊙︿⊙⠀No tears 14
ヽ(●ﾟ´Д｀ﾟ●)ﾉﾟ⠀No tears 15
(.﹒︣︿﹒︣.)⠀No tears 16
(Θ︹Θ)ს⠀No tears 17
٩꒰´·⌢•｀꒱۶⁼³₌₃⠀No tears 18
:: ˓(ᑊᘩᑊ⁎) ::⠀No tears 19
˓˓(ᑊᘩᑊ⁎)⠀No tears 20
(๑◕︵◕๑)⠀No tears 21
( .. )⠀No tears 22
(｡•́︿•̀｡)⠀No tears 23
(´°ω°`)⠀No tears 24
੨( ･᷄ ︵･᷅ )ｼ⠀No tears 25
꒰๑˃͈꒳˂͈๑꒱ﾉ*ﾞ̥⠀No tears 26
(⌯˃̶᷄ ﹏ ˂̶᷄⌯)ﾟ⠀No tears 27
(っ- ‸ – ς)⠀No tears 28
(๑′°︿°๑)⠀No tears 29
⊛ठ̯⊛⠀No tears 30
ಠ╭╮ಠ⠀No tears 31
( ◞᷄દ◟᷅ )⠀No tears 32
(oꆤ︵ꆤo)⠀No tears 33
ಗಾ ﹏ ಗಾ⠀No tears 34
ᵟຶᴖ ᵟຶ⠀No tears 35
(⋅⃘˕̭⋅⃘)⠀No tears 36
ōۃō⠀No tears 37
( ⁍᷄⌢̻⁍᷅ )⠀No tears 38
(.﹒︠₋﹒︡.)⠀No tears 39
(˵¯͒⌢͗¯͒˵)⠀No tears 40
☹ै⠀No tears 41
(　´_ﾉ` )⠀No tears 42
ʕ ಡ ﹏ ಡ ʔ⠀No tears 43
●︿●⠀No tears 44
(◕︿◕✿)⠀No tears 45
ਉ_ਉ⠀No tears 46
༶ඬ༝ඬ༶⠀No tears 47
໒( •́ ∧ •̀ )७⠀No tears 48
へ[ •́ ‸ •̀ ]ʋ⠀No tears 49
┏༼ ◉ ╭╮ ◉༽┓⠀No tears 50
▐ ﹒︣ Ĺ̯ ﹒︣ ▐⠀No tears 51
( ˃̶͈ ̯ ̜ ˂̶͈ˊ ) ︠³⠀No tears 52
(๑´╹‸╹`๑)⠀No tears 53
(⌯˃̶᷄ ﹏ ˂̶᷄⌯)⠀No tears 54
（（●´∧｀●））⠀No tears 55
(｡-人-｡)⠀No tears 56
、ヽ｀(~д~*)、ヽ｀⠀No tears 57
(<*△*<)⠀Vertical Tears 1
（ < < ）⠀Vertical Tears 2
(っ˘̩╭╮˘̩)っ⠀Vertical Tears 3
(个_个)⠀Vertical Tears 4
（；へ：）⠀Vertical Tears 5
o(；△；)o⠀Vertical Tears 6
((o(<△<)o))⠀Vertical Tears 7
ͼ(ݓ_ݓ)ͽ⠀Vertical Tears 8
(*´；ェ；`*)⠀Vertical Tears 9
(´；ω；`)⠀Vertical Tears 10
(´；д；`)⠀Vertical Tears 11
(´；Д；｀)⠀Vertical Tears 12
(゜´Д｀゜)⠀Vertical Tears 13
ಥ_ಥ⠀Vertical Tears 14
(ఠ్ఠ ˓̭ ఠ్ఠ)⠀Vertical Tears 15
(๑′̥̥̥▵‵̥̥̥ ૂ๑)⠀Vertical Tears 16
(٭°̧̧̧꒳°̧̧̧٭)⠀Vertical Tears 17
（ｉДｉ）⠀Vertical Tears 18
( ´•̥×•̥` )⠀Vertical Tears 19
( ᵒ̴̶̷̥́ _ᵒ̴̶̷̣̥̀ )⠀Vertical Tears 20
( ˃̣̣̥ω˂̣̣̥ )⠀Vertical Tears 21
꒰๑•̥﹏•̥๑꒱⠀Vertical Tears 22
(੭ ˃̣̣̥ ㅂ˂̣̣̥)੭ु⠀Vertical Tears 23
( ɵ̥̥ ˑ̫ ɵ̥̥)⠀Vertical Tears 24
(´<︵<`)⠀Vertical Tears 25
( ´•̥̥̥ω•̥̥̥` )⠀Vertical Tears 26
(ˊ̥̥̥̥̥ ³ ˋ̥̥̥̥̥)⠀Vertical Tears 27
(⌯͒⁍̩̩᷄ ɪ ⁍̩̩᷄ฅ͒)⠀Vertical Tears 28
(๑ १д१)⠀Vertical Tears 29
(๑⃙⃘°̧̧̧ㅿ°̧̧̧๑⃙⃘)⠀Vertical Tears 30
(῭̩̩̩̥ꄗ΅̩̩̩̥)⠀Vertical Tears 31
(̥ ̥এ́ ̼ এ̥̀)̥̥⠀Vertical Tears 32
(̥ ̥এ́ ̼ এ̥̀)̥̥੭ੇʓ ੭ੇʓ⠀Vertical Tears 33
⁝(˚͈͈͈͈̥̆₍₎˚͈͈͈͈̥̆⁎)⁝⠀Vertical Tears 34
(<﹏<)⠀Vertical Tears 35
(˃̥̥ω˂̥̥̥)⠀Vertical Tears 36
( ͒˃̩̩⌂˂̩̩ ͒)⠀Vertical Tears 37
(ᵕ̣̣̣̣̣̣﹏ᵕ̣̣̣̣̣̣)⠀Vertical Tears 38
(˃̩̩̥ɷ˂̩̩̥)⠀Vertical Tears 39
( -̩̩̩͡˛ -̩̩̩͡ )⠀Vertical Tears 40
(﹡ᵗ ᵔ ᵗ ﹡)⠀Vertical Tears 41
( ب_ب )⠀Vertical Tears 42
c〳 ݓ ﹏ ݓ 〵੭⠀Vertical Tears 43
( Ĭ ^ Ĭ )⠀Vertical Tears 44
(´<ω<｀)⠀Vertical Tears 45
(<•͈́༚•͈̀)⠀Vertical Tears 46
＼（＠；◇；＠）／⠀Vertical Tears 47
(ﾟ´Д｀ﾟ)ﾟ⠀Flying Tears 1
・(/Д`)・⠀Flying Tears 2
・゜・(ノД`)⠀Flying Tears 3
.·´¯`(<><<▂<<<<)´¯`·.⠀Flying Tears 4
｡：ﾟ(｡ﾉω＼｡)ﾟ･｡⠀Flying Tears 5
。：゜(；´∩｀；)゜：。⠀Flying Tears 6
｡ﾟ( ﾟஇ‸இﾟ)ﾟ｡⠀Flying Tears 7
。ﾟ(ﾟﾉД｀ﾟ)ﾟ｡⠀Flying Tears 8
｡゜(｀Д´)゜｡⠀Flying Tears 9
(ノД`)・゜・。⠀Flying Tears 10
˚‧º·(˚ ˃̣̣̥᷄⌓˂̣̣̥᷅ )‧º·˚⠀Flying Tears 11
°(ಗдಗ。)°.⠀Flying Tears 12
(/□＼*)・゜⠀Flying Tears 13
.°(ಗдಗ。)°.⠀Flying Tears 14
｡ﾟ(ﾟ∩´﹏`∩ﾟ)ﾟ｡⠀Flying Tears 15
｡ﾟ(ﾟ´Д｀ﾟ)ﾟ｡⠀Flying Tears 16
‧º·(˚ ˃̣̣̥⌓˂̣̣̥ )‧º·˚⠀Flying Tears 17
๐·°(৹˃̵﹏˂̵৹)°·๐⠀Flying Tears 18
⋆*:.｡. (-᷄◞८ૄ◟-᷅) .｡.:*⋆⠀Flying Tears 19
｡･+ﾟﾟ(うд´｡)ﾟﾟ+･｡⠀Flying Tears 20
｡･ﾟ(ﾟ⊃ω⊂ﾟ)ﾟ･｡⠀Flying Tears 21
｡･ﾟ･(*ﾉД`*)･ﾟ･。⠀Flying Tears 22
ﾟ｡･ﾟヾ(ﾟ｀ｪ´ﾟ)ﾉ｡ﾟ･｡⠀Flying Tears 23
｡ﾟヽ(ﾟ´Д｀)ﾉﾟ｡⠀Flying Tears 24
｡･ﾟ’(*/益＼*) ‘ﾟ･｡⠀Flying Tears 25
｡ﾟ(ﾟ`⊿゜)ﾟ｡⠀Flying Tears 26
˚‧º·(˚ ˃̣̣̥⌓˂̣̣̥ )‧º·˚⠀Flying Tears 27
｡ﾟ(ﾟ´Д`ﾟ)ﾟ｡⠀Flying Tears 28
｡ﾟ(ﾟ∩´﹏`∩ﾟ)ﾟ｡⠀Flying Tears 29
゜．(つx･｡`*)゜．・⠀Flying Tears 30
｡ﾟ( ﾟஇ‸இﾟ+)ﾟ｡⠀Flying Tears 31
(つ﹏<<<<)･ﾟ｡⠀Flying Tears 32
｡ﾟ･（<><<﹏<<<<）･ﾟ｡⠀Flying Tears 33
｡ﾟ(*´□`)ﾟ｡⠀Flying Tears 34
｡:ﾟ(<´∩`<)ﾟ:｡⠀Flying Tears 35
。･゜･(｡´ﾉω･`)⠀Flying Tears 36
.・゜゜・（／。＼）・゜゜・．⠀Flying Tears 37
｡･ﾟﾟ･(<><<д<<<<)･ﾟﾟ･｡⠀Flying Tears 38
｡･ﾟﾟ･o（ｉДｉ）o･ﾟﾟ･｡⠀Flying Tears 39
(╯︵╰,)⠀A Single Tear 1
ヽ(´□｀。)ﾉ⠀A Single Tear 2
( p′︵‵。)⠀A Single Tear 3
（；_・）⠀A Single Tear 4
（；￣д￣）⠀A Single Tear 5
(/ _ < )⠀A Single Tear 6
(′︿‵｡)⠀A Single Tear 7
(´＿｀。)⠀A Single Tear 8
(´∩｀。)⠀A Single Tear 9
(´Ａ｀。)⠀A Single Tear 10
(´Д｀。)⠀A Single Tear 11
(|||❛︵❛.)⠀A Single Tear 12
(இ﹏இ`｡)⠀A Single Tear 13
p(´⌒｀｡q)⠀A Single Tear 14
(ᗒᗣᗕ)՞⠀A Single Tear 15
(≖͞_≖̥)⠀A Single Tear 16
(๑•́₋•̩̥̀๑)⠀A Single Tear 17
(˃ ⌑ ˂ഃ )⠀A Single Tear 18
(´•ω•̥`)⠀A Single Tear 19
(<•͈́༚•͈̀)⠀A Single Tear 20
(◞‸◟；)⠀A Single Tear 21
(•̥́_•ૅू˳)⠀A Single Tear 22
(-人-。)⠀A Single Tear 23
(T＿T)⠀T Style Tears 1
(o<TωT)o⠀T Style Tears 2
(━┳━ _ ━┳━)⠀T Style Tears 3
(┳◇┳)⠀T Style Tears 4
(┳Д┳)⠀T Style Tears 5
(╥_╥)⠀T Style Tears 6
(。┰ω┰。)⠀T Style Tears 7
(； T.T))⠀T Style Tears 8
（ ＴДＴ）⠀T Style Tears 9
((T.T； )⠀T Style Tears 10
(T_T)⠀T Style Tears 11
(T⌓T)⠀T Style Tears 12
(Ｔ▽Ｔ)⠀T Style Tears 13
(ToT)⠀T Style Tears 14
（πーπ）⠀T Style Tears 15
(ㄒoㄒ)⠀T Style Tears 16
╥﹏╥⠀T Style Tears 17
o(╥﹏╥)o⠀T Style Tears 18
o(TヘTo)⠀T Style Tears 19
(╥_╥)⠀T Style Tears 20
(╥╯θ╰╥)⠀T Style Tears 21
Σ(ＴωＴ)⠀T Style Tears 22
(╥ᆺ╥；)⠀T Style Tears 23
【T__T】⠀T Style Tears 24
o(TﾍTo)⠀T Style Tears 25
ヽ(T-T )ノ⠀T Style Tears 26
ヽ( T-T)ノ⠀T Style Tears 27
(T～T；。)⠀T Style Tears 28
(╥︣﹏᷅╥᷅)⠀T Style Tears 29
(━━━┳━━━○━━━┳━━━)⠀T Style Tears 30
૮( ꒦ິ⍣꒦ີ)ა⠀꒦ິ Style Tears 1
(๑꒦ິ ̼ ꒦ິ๑)⠀꒦ິ Style Tears 2
૮(꒦ິཅ꒦ິ)ა⠀꒦ິ Style Tears 3
(꒦ິ⍸꒦ິ)⠀꒦ິ Style Tears 4
(*꒦ິ⌓꒦ີ)⠀꒦ິ Style Tears 5
(*꒦ິ꒦ີ)⠀꒦ິ Style Tears 6
(*꒦ິ³꒦ີ)⠀꒦ິ Style Tears 7
(*꒦ິ꒳꒦ີ)⠀꒦ິ Style Tears 8
(*꒦ິㅂ꒦ີ)⠀꒦ິ Style Tears 9
(*꒦ິㅿ꒦ີ)⠀꒦ິ Style Tears 10
| ू*꒦ິ꒳꒦ີ)｡oO⠀꒦ິ Style Tears 11
(꒦໊ྀʚ꒦໊ི )⠀꒦ິ Style Tears 12
༼ ༎ຶ ෴ ༎ຶ༽⠀Tears that Freak Me Out 1
(༎ຶ⌑༎ຶ)⠀Tears that Freak Me Out 2
(༎ຶ ෴ ༎ຶ)⠀Tears that Freak Me Out 3
( ´༎ຶㅂ༎ຶ`)⠀Tears that Freak Me Out 4
(༎ຶ ෴ ༎ຶ)⠀Tears that Freak Me Out 5
( ´༎ຶㅂ༎ຶ`)⠀Tears that Freak Me Out 6
( ཀ͝ ∧ ཀ͝ )⠀Tears that Freak Me Out 7
( p_q)⠀Rubbing Eyes 1
{{p´Д｀q}}⠀Rubbing Eyes 2
( /)u(\ )⠀Rubbing Eyes 3
(ʃ⌣́,⌣́ƪ)⠀Rubbing Eyes 4
(｡•́-ก̀｡)⠀Rubbing Eyes 5
(,,•́ω ก̀,,)⠀Rubbing Eyes 6
(っ◞‸◟c)⠀Rubbing Eyes 7
( つ᷄.̯σ̣̥᷅ )⠀Rubbing Eyes 8
(˘̩̩̩ε˘̩ƪ)⠀Rubbing Eyes 9
(ρﾟ∩ﾟ)⠀Rubbing Eyes 10
．(つx･｡`*)゜．・⠀Rubbing Eyes 11
(つ﹏<<<<。)⠀Rubbing Eyes 12
(ノ﹏ヽ)⠀Rubbing Eyes 13
(＊ρω-*)⠀Rubbing Eyes 14
(⁎•̛̣̣꒶̯•̛̣̣⁎)⠀Complex 1
ू(ʚ̴̶̷́ .̠ ʚ̴̶̷̥̀ ू)⠀Complex 2
(๑´• .̫ •ू`๑)⠀Complex 3
ଘ(੭*◕ฺω◕ฺ)੭⠀Complex 4
(๑⃙⃘ ˃̶͈̀ロ˂̶͈́)੭ु⁾⁾⠀Complex 5
(๑•̥̥̥́ω•̀ू๑)⠀Complex 6
⁝(ृ•ˇ‸ˇ•。 ृ　)ु⁝⠀Complex 7
(⁎ְְ⁍̴ ॄְְ⁍̴⁎)⠀Complex 8
(-̩̩̩-̩̩̩-̩̩-̩̩̩_-̩̩̩-̩-̩̩̩-̩̩̩)⠀Complex 9
(⌯͒⁍̩̩᷄ ɪ ⁍̩̩᷄ฅ͒)⠀Complex 10
(๑මั‸මั๑)⠀Complex 11
˞̣̣̣̀ ᶿ᷄ ˈ̯̥̮ ᶿ᷅⠀Complex 12
☎*⁎ά⁎́ ॄཻ͡⁎̀ूॽ⠀Complex 13
ₒ˛˚̣⁽⁽(˃ᾓॄ˂⁎)⠀Complex 14
(๑ ⁍̥̥̥᷅ ᴈ⁍̥̥̥᷅)人(⁌̥̥̥᷄ε ⁌̥̥̥᷄ ๑)ｰ⠀Two People 1
( ‘́⌣’̀)/(˘̩̩ε˘̩ƪ)⠀Two People 2
(*~ρ~)ﾉ(ToTw)⠀Two People 3
(´._.`)\(‘́⌣’̀ )⠀Two People 4
Ⓜɨ ʂ ʂ Ⓨσư (̥ ̥এ́ ̼ এ̥̀)̥̥⠀Words 1
(´°̥̥̥̥̥̥̥̥ω°̥̥̥̥̥̥̥̥｀)⠀Crazy and or Broken 1
(-̩̩-̩̩͡_-̩̩-̩̩͡)⠀Crazy and or Broken 2
(-̩̩̩-̩̩̩-̩̩̩-̩̩̩-̩̩̩___-̩̩̩-̩̩̩-̩̩̩-̩̩̩-̩̩̩)⠀Crazy and or Broken 3
(*´°̥̥̥̥̥̥̥̥﹏°̥̥̥̥̥̥̥̥ )人(´°̥̥̥̥̥̥̥̥ω°̥̥̥̥̥̥̥̥｀)⠀Crazy and or Broken 4
(∘⁼̴⃙̀˘︷˘⁼̴⃙́∘)⠀Crazy and or Broken 5
(　-̥̥̥̥̥̥̥̥̥̥̥̥̥̥̥̥̥̥̥̥̥̥̥̥̥᷄◞ω◟-̥̥̥̥̥̥̥̥̥̥̥̥̥̥̥̥̥̥̥̥̥̥̥̥̥᷅ )⠀Crazy and or Broken 6
(づ-̩̩̩-̩̩̩_-̩̩̩-̩̩̩)づ⠀Crazy and or Broken 7
( °̥̥̥̥̥̥̥̥˟°̥̥̥̥̥̥̥̥ )⠀Crazy and or Broken 8
…(•̩̩̩̩＿•̩̩̩̩)⠀Crazy and or Broken 9
ৎ｡ ॄཻ͡⁎̥̥̥̥̥̥ૂॽ⠀Crazy and or Broken 10
⁽⁽ƈ ͡ (ु ˲̥̥̥́ ˱̥̥̥̀) ु⁾⁾⠀Crazy and or Broken 11
ৎ⁎́ ॄཻ͡⁎̀ूॽ྆྆⠀Crazy and or Broken 12
(๑˃̥̩̥̥̥̥̆ಐ˂̩̩̥̥̩̥̆৭)⠀Crazy and or Broken 13
ƈ ͡ (ुŏ̥̥̥̥ ‸ ŏ̥̥̥̥) ु⠀Crazy and or Broken 14
(<̦̦̦̦̦̦̦̦ↂ⃝⃓⃙⃚⃘дↂ⃝⃓⃙⃚⃘<̦̦̦̦̦̦̦̦)⠀Crazy and or Broken 15
(◍°̧̧̧o°̧̧̧◍)⠀Crazy and or Broken 16
(͡͡͡͡T̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̤̤̤̤̤AT̼̼̼̼̼̼̼̼̼̼̼̼̼̼̼̤̤̤̤̤̤͡͡͡͡͡)⠀Crazy and or Broken 17
( ´•̥̥̥ω•̥̥̥` )⠀Crazy and or Broken 18
|||᷇᷇˃⁻᷄⁻̦̦̦̦̦̦̦̦̦̦̦̦̦υ͜⁻⁻̦̦̦̦̦̦̦̦̦̦̦̦̦̦᷅˂|᷆᷆||⠀Crazy and or Broken 19
(๑•̥̥̥́ω•̀ू๑)⠀Crazy and or Broken 20
( ⚈̥̥̥̥̥́⌢⚈̥̥̥̥̥̀)⠀Crazy and or Broken 21
(´•̥̥̥д•̥̥̥`̀ू๑)‧º·˚⠀Crazy and or Broken 22
(⊙̥◞८͙◟⊙̥ ̥̥̥̥̥̥)⠀Crazy and or Broken 23
(´•̥̥̥д•̥̥̥`̀ू๑)⠀Crazy and or Broken 24
⁽͑*ˀ́˙̭˚̣̣̣̣̀*⁾̉ ˀ̀ˈˈˈ⠀Crazy and or Broken 25
(　-̥̥̥̥̥̥̥̥̥̥̥̥̥̥̥̥̥̥̥̥̥̥̥̥̥᷄◞ω◟-̥̥̥̥̥̥̥̥̥̥̥̥̥̥̥̥̥̥̥̥̥̥̥̥̥᷅ )⠀Crazy and or Broken 26
(ˊ̥̥̥̥̥ ³ ˋ̥̥̥̥̥)⠀Crazy and or Broken 27
(-ω-ゞ⠀ω Mouths 1
(*´ﾟωﾟﾉ⠀ω Mouths 2
(〃´・ω・`)ゝ⠀ω Mouths 3
(≧ω≦)ゞ⠀ω Mouths 4
(◎｀・ω・´)ゞ⠀ω Mouths 5
(★｀･ω･)ゞ⠀ω Mouths 6
(★´ω｀★)ゞ⠀ω Mouths 7
(ο´ω｀ο)ゝ⠀ω Mouths 8
(｀･ω･´)ゞ⠀ω Mouths 9
(′σω`)ﾉ⠀ω Mouths 10
(*゜ω゜)ゞ⠀ω Mouths 11
☆(･ω･*)ゞ⠀ω Mouths 12
ヾ|*ﾟωﾟ|ゞ⠀ω Mouths 13
(`･ω･´)ゞ⠀ω Mouths 14
(｡･ω･)ゞ⠀ω Mouths 15
∠(｀･ω･´)⠀ω Mouths 16
( ゜ω゜)ゝ⠀ω Mouths 17
（｀・ω・）ゞ⠀ω Mouths 18
(-ω-)ゝ⠀ω Mouths 19
ヽ|･ω･|ゞ⠀ω Mouths 20
┏( ﾟωﾟ)ゝ⠀ω Mouths 21
〆(´ω`●)ゞ⠀ω Mouths 22
(●´ω｀●)ゞ⠀ω Mouths 23
|；´・ω･｀|ゞ⠀ω Mouths 24
(。・ω・)ゞ⠀ω Mouths 25
ヽ( ˘ω˘ )ゝ⠀ω Mouths 26
（＊´ω｀）ゞ⠀ω Mouths 27
ヾ(☆´･ω･)ゞ⠀ω Mouths 28
ヾ(･ω･｀★)ゞ⠀ω Mouths 29
(･ω´-ゞ)^☆⠀ω Mouths 30
（´ω｀◎）ゞ⠀ω Mouths 31
ヽ(￣ω￣(￣ω￣〃)ゝ⠀ω Mouths 32
(o｀･ω･)ゞ⠀ω Mouths 33
（*｀・ω・*）ゞ⠀ω Mouths 34
(*<><<ω<<<<)ゞ⠀ω Mouths 35
（○｀ω´）ゞ⠀ω Mouths 36
(●｀･ω･)ゞ＜ok！⠀ω Mouths 37
(*｀･ω･)ゞ⠀ω Mouths 38
(・ω・｀=)ゞ⠀ω Mouths 39
c(＞ω＜)ゞ⠀ω Mouths 40
(`･ω･)ゞ⠀ω Mouths 41
(。・ω・。)ゞ⠀ω Mouths 42
(；・ε・)ゝ”⠀ε Mouths 1
(★ゝз･)ﾉ~*⠀ε Mouths 2
*~ヽ(ゝз･☆)⠀ε Mouths 3
(`･ε´-ゞ)⠀ε Mouths 4
(〃´3′〃)ゞ⠀ε Mouths 5
ヾ(´ε｀*)ゝ⠀ε Mouths 6
(･´з`･)ゞ⠀ε Mouths 7
ヽ|･з･|ゞ⠀ε Mouths 8
(｡･з･)ゞ⠀ε Mouths 9
ヽ( ˘з˘ )ゝ⠀ε Mouths 10
(；´・∀・)ゝ”⠀∀ Mouths 1
(；●∀●)ゝ”⠀∀ Mouths 2
(‘∀`)ゝ”⠀∀ Mouths 3
(｀∀´)ゝ”⠀∀ Mouths 4
(°∀°)ゝ”⠀∀ Mouths 5
(≧∀≦ゞ⠀∀ Mouths 6
(○$´∀`)ゞ⠀∀ Mouths 7
( ・∀・ )ゞ⠀∀ Mouths 8
/(‘∀’*⠀∀ Mouths 9
(｡ゝ∀･)ゞ⠀∀ Mouths 10
(*°∀°)ゞ⠀∀ Mouths 11
（・∀・）ゞ⠀∀ Mouths 12
(oゝ∀・o)ゞ⠀∀ Mouths 13
(*´∀｀*)ゞ⠀∀ Mouths 14
―(≧∀≦)ゞ⠀∀ Mouths 15
(*・∀・)ゞ⠀∀ Mouths 16
（＾∀＾）ゞ⠀∀ Mouths 17
*＜( ・∀・)ノ⠀∀ Mouths 18
ヽ(・∀・ )＞*⠀∀ Mouths 19
(〃＾∀ﾟ ゞ⠀∀ Mouths 20
(´∀｀ゞ⠀∀ Mouths 21
（─∀─）ゞ⠀∀ Mouths 22
(｀∀´*)ゞ⠀∀ Mouths 23
(‘∀`)ゞ⠀∀ Mouths 24
ヾ(*｀∀´*)ゞ⠀∀ Mouths 25
(゜∀´)ゞ=☆⠀∀ Mouths 26
(∀｀*ゞ)⠀∀ Mouths 27
(･∀･´*)ゞ⠀∀ Mouths 28
(〃⌒▽⌒〃)ゝ⠀Sharp Triangle Mouths 1
(*<><<▽<<<<*)ゞ⠀Sharp Triangle Mouths 2
(=´▽｀)ゞ⠀Sharp Triangle Mouths 3
ヾ(≧∇≦)ゞ⠀Sharp Triangle Mouths 4
！(@＾▽＾@）ゞ⠀Sharp Triangle Mouths 5
（≧▽≦）ゝ⠀Sharp Triangle Mouths 6
*＜( ≧▽≦)／⠀Sharp Triangle Mouths 7
＼(≧▽≦ )＞*⠀Sharp Triangle Mouths 8
v(ﾟ∇^*)＞o⌒☆⠀Sharp Triangle Mouths 9
<<<<(￣∇￣)ゞ⠀Sharp Triangle Mouths 10
(￣▽￣)ゞ⠀Sharp Triangle Mouths 11
!!(･∇･｀ゞ⠀Sharp Triangle Mouths 12
（≧▽≦）ゞ⠀Sharp Triangle Mouths 13
(｀∇´ゞ⠀Sharp Triangle Mouths 14
ヾ(●｀･△･´●)ゞ⠀Sharp Triangle Mouths 15
∠(*ﾟ∇ﾟ*)⠀Sharp Triangle Mouths 16
(´▽｀；)ゞ⠀Sharp Triangle Mouths 17
(￣∇￣*)ゞ⠀Sharp Triangle Mouths 18
(・∧‐)ゞ⠀Sharp Triangle Mouths 19
(￣^￣)ゞ⠀Sharp Triangle Mouths 20
( ’v`*)ゞ⠀Sharp Triangle Mouths 21
(`Д´)ゞ⠀Д Mouths 1
(｀д´)ゝ⠀Д Mouths 2
ｏ(･д´･+)ゞ⠀Д Mouths 3
(＞Д＜)ゝ⠀Д Mouths 4
（・д・ゝ）⠀Д Mouths 5
∠(´д｀)⠀Д Mouths 6
(`Д´)ゞ⠀Д Mouths 7
(｀ﾟДﾟ´)ゞ⠀Д Mouths 8
(●<><<д<<<<●)ゞ⠀Д Mouths 9
く（＠Д＠）⠀Д Mouths 10
( *๑•̀д•́๑)」⠀Д Mouths 11
＼|*≧Д≦|<><<⠀Д Mouths 12
(｀・д・´)ゝ⠀Д Mouths 13
(`-д-；)ゞ⠀Д Mouths 14
∠( ﾟдﾟ)/⠀Д Mouths 15
(｀･д´･ゞ)-☆⠀Д Mouths 16
(＞Д＜)ゝ”⠀Д Mouths 17
( ﾟДﾟ)ゞ⠀Д Mouths 18
<<<<|๑⊙Д⊙|/⠀Д Mouths 19
(｡･Д･)ゞ⠀Д Mouths 20
(´･Д･<<<)ゞ⠀Д Mouths 21
(*゜－＾)ゞ⠀Flat Mouths 1
(^-^)ゝ⠀Flat Mouths 2
(‘-‘*ゞ⠀Flat Mouths 3
∠(･`_´･ )⠀Flat Mouths 4
(‘ー’*)ゞ⠀Flat Mouths 5
∠(^ー^)⠀Flat Mouths 6
(‾-ƪ‾)⠀Flat Mouths 7
(*^-^*)ゞ⠀Flat Mouths 8
( ´_ゝ｀)ゞ⠀Flat Mouths 9
v(*’-^*)ゞ・’ﾟ☆⠀Flat Mouths 10
ヾ(≧ー≦)ゞ⠀Flat Mouths 11
(*ﾟｰﾟ)ゞ⌒☆⠀Flat Mouths 12
（￣ー￣)ゞ⠀Flat Mouths 13
(*゜ー゜)ゞ⌒☆⠀Flat Mouths 14
(＊･_･＊)ゞ⠀Flat Mouths 15
(*´-｀*)ゞ⠀Flat Mouths 16
(＊･_･＊)ゞ⠀Flat Mouths 17
(*´-｀*)ゞ⠀Flat Mouths 18
(‘ – ‘ *)ゞ⠀Flat Mouths 19
く(^ｰﾟ)ﾉ⠀Flat Mouths 20
(‘ー’*)ゞ⠀Flat Mouths 21
ヽ(⌒‐⌒)ゝ⠀Flat Mouths 22
(￣ー￣)ゞ⠀Flat Mouths 23
(゜◇゜)ゞ⠀Diamond Mouths 1
ｏ(〃･◇･〃)ゞ⠀Diamond Mouths 2
（’◇’）ゞ⠀Diamond Mouths 3
ｏ(〃・◇・〃)ゞ⠀Diamond Mouths 4
ヽ|･◇･|ゞ⠀Diamond Mouths 5
(｡･◇･)ゞ⠀Diamond Mouths 6
(⑅･◇･)ゞ⠀Diamond Mouths 7
ヽ( ˘◇˘ )ゝ⠀Diamond Mouths 8
(*｀･益･´)ゞ⠀益 Mouths 1
┏( ﾟ益ﾟ)ゞ⠀益 Mouths 2
(｡･益･)ゞ⠀益 Mouths 3
ヽ|･益･|ゞ⠀益 Mouths 4
(｡･益･)ゞ⠀益 Mouths 5
ヽ( ˘益˘ )ゝ⠀益 Mouths 6
（〃・ロ・〃）ゞ⠀Square Mouths 1
(*´□`)ゞ⠀Square Mouths 2
ヽ|･ロ･|ゞ⠀Square Mouths 3
( *๑•̀ロ•́๑)」⠀Square Mouths 4
( ゜ロ゜)ゝ⠀Square Mouths 5
(･´□`･)ゞ⠀Square Mouths 6
(｡･□･)ゞ⠀Square Mouths 7
ヽ( ˘□˘ )ゝ⠀Square Mouths 8
(＞ロ＜)ゝ⠀Square Mouths 9
(U･× ･´)ゞ⠀X Mouths 1
(。・ｘ・)ゞ⠀X Mouths 2
(*･×･*)ゞ⠀X Mouths 3
(*´･x･`)ゞ⠀X Mouths 4
ヽ|･x･|ゞ⠀X Mouths 5
(｡･x･)ゞ⠀X Mouths 6
ヽ( ˘x˘ )ゝ⠀X Mouths 7
(〇´∪`●ゞ）⠀U Mouths 1
(*｀∪´*)ゞ⠀U Mouths 2
ヽ|･u･|ゞ⠀U Mouths 3
(｡･u･)ゞ⠀U Mouths 4
ヽ( ˘∪˘ )ゝ⠀U Mouths 5
ヽ(⌒∪⌒)ゝ⠀U Mouths 6
<<<<|๑⊙∪⊙|/⠀U Mouths 7
(●￣(ｴ)￣●)ゞ⠀Saluting Bears 1
(〓￣(∵エ∵)￣〓)ゞ⠀Saluting Bears 2
( -(ｴ)-)ゞ⠀Saluting Bears 3
ヾ(´(ｴ)｀ﾉﾞ⠀Saluting Bears 4
(=`ｪ´=；)ゞ⠀Miscellaneous Saluting Emoticons 1
(「꒪౪꒪)」⠀Miscellaneous Saluting Emoticons 2
(･`◡´･)ゝ⠀Miscellaneous Saluting Emoticons 3
∠꒰’౪’꒱✧⠀Miscellaneous Saluting Emoticons 4
◞(⚭⃚⃙͐·̫⚭⃚⃙͐)˩✧⠀Miscellaneous Saluting Emoticons 5
|･｀ヘ´･<|ゞ⠀Miscellaneous Saluting Emoticons 6
☆( ´ ਊ ՞ )ゞ⠀Miscellaneous Saluting Emoticons 7
o(*￣○￣)ゝ⠀Miscellaneous Saluting Emoticons 8
（*＾～＾*）ゝ⠀Miscellaneous Saluting Emoticons 9
s(●｀ヘ´●<)ゞ⠀Miscellaneous Saluting Emoticons 10
(；°ρ°)ゝ”⠀Miscellaneous Saluting Emoticons 11
☆(*･ｪ･*)＞｡⠀Miscellaneous Saluting Emoticons 12
＼(^O^ )＞*⠀Miscellaneous Saluting Emoticons 13
*＜( ^O^)／⠀Miscellaneous Saluting Emoticons 14
（｀・ゝ・´）ゞ⠀Miscellaneous Saluting Emoticons 15
（*￣‥￣*）ゝ⠀Miscellaneous Saluting Emoticons 16
♪(´∪`●)ゝ⠀Miscellaneous Saluting Emoticons 17
（★・л・★）ゝ⠀Miscellaneous Saluting Emoticons 18
o(- -<*)ゞ⠀Miscellaneous Saluting Emoticons 19
([]-[]-“ゝ⠀Miscellaneous Saluting Emoticons 20
(/-(ｴ)-＼)⠀Covering Your Eyes and or Face in Fear 1
( /)u(\ )⠀Covering Your Eyes and or Face in Fear 2
（*/∇＼*）⠀Covering Your Eyes and or Face in Fear 3
(*/ω＼*)⠀Covering Your Eyes and or Face in Fear 4
（／_＼）⠀Covering Your Eyes and or Face in Fear 5
（／．＼）⠀Covering Your Eyes and or Face in Fear 6
（/｡＼)⠀Covering Your Eyes and or Face in Fear 7
(／。＼)⠀Covering Your Eyes and or Face in Fear 8
(／(ｴ)＼)⠀Covering Your Eyes and or Face in Fear 9
(/ω＼)⠀Covering Your Eyes and or Face in Fear 10
(⊃‿⊂)⠀Covering Your Eyes and or Face in Fear 11
(ノдヽ)⠀Covering Your Eyes and or Face in Fear 12
(⊃д⊂)⠀Covering Your Eyes and or Face in Fear 13
(*/∇＼*)⠀Covering Your Eyes and or Face in Fear 14
(`･/д＼･)⠀Covering Your Eyes and or Face in Fear 15
◑.◑⠀Big Wide Open Eyes of Fear 1
( ⚆ _ ⚆ )⠀Big Wide Open Eyes of Fear 2
━(◯Δ◯∥)━ン⠀Big Wide Open Eyes of Fear 3
(　〇□〇）⠀Big Wide Open Eyes of Fear 4
(((φ(◎ロ◎<)φ)))⠀Big Wide Open Eyes of Fear 5
ゞ◎Д◎ヾ⠀Big Wide Open Eyes of Fear 6
（｀〇Д〇）⠀Big Wide Open Eyes of Fear 7
（ΟΔΟ；；）⠀Big Wide Open Eyes of Fear 8
(O∆O)⠀Big Wide Open Eyes of Fear 9
（　(≪●≫)　）Д（　(≪●≫)　）⠀Big Wide Open Eyes of Fear 10
ヽ(ﾟДﾟ)ﾉ⠀Scared Д Mouths 1
(((╹д╹<)))⠀Scared Д Mouths 2
(╬⁽⁽ ⁰ ⁾⁾ Д ⁽⁽ ⁰ ⁾⁾)⠀Scared Д Mouths 3
ヾ( •́д•̀ <)ﾉ⠀Scared Д Mouths 4
ヽ ( ꒪д꒪ )ﾉ⠀Scared Д Mouths 5
ヾ( ๑´д`๑)ﾂ⠀Scared Д Mouths 6
џ(ºДºџ)⠀Scared Д Mouths 7
( ⁰д⁰)⠀Scared Д Mouths 8
(ﾟДﾟ；)ゞ⠀Scared Д Mouths 9
－(゜Д゜<)-ン!⠀Scared Д Mouths 10
(ﾟДﾟ<)⠀Scared Д Mouths 11
(ﾟдﾟ；)⠀Scared Д Mouths 12
∠(ﾟДﾟ)/⠀Scared Д Mouths 13
‘`( ꒪Д꒪),､⠀Scared Д Mouths 14
(╬☉д⊙)⠀Scared Д Mouths 15
σ(ｏдｏ<<<)⠀Scared Д Mouths 16
(ﾟДﾟ?)⠀Scared Д Mouths 17
ヾ(´ﾟДﾟ｀<)ゝ⠀Scared Д Mouths 18
(#｀ﾟд´)ﾉ⠀Scared Д Mouths 19
゛(●ﾉ´・Д・｀)ﾉ⠀Scared Д Mouths 20
╰། ᵒ̌ д ᵒ̌ །╯⠀Scared Д Mouths 21
ヽ(○´Д｀)ﾉ⠀Scared Д Mouths 22
(゜Д゜*)⠀Scared Д Mouths 23
⊃゜Д゜）⊃⠀Scared Д Mouths 24
⊂（゜Д゜⊂⠀Scared Д Mouths 25
┗|*´ﾟДﾟ｀|┛⠀Scared Д Mouths 26
(ｼ<ﾟДﾟ)ｼ⠀Scared Д Mouths 27
ヾ(ﾟДﾟ<ヾ)⠀Scared Д Mouths 28
ヾ(<ﾟДﾟ<)ｼ⠀Scared Д Mouths 29
（ΩДΩ）⠀Scared Д Mouths 30
ヽ(#ﾟДﾟ)ﾉ⠀Scared Д Mouths 31
!!(ﾉ*ﾟДﾟ)ﾉ⠀Scared Д Mouths 32
,､’`( ꒪Д꒪),､’`’`,､⠀Scared Д Mouths 33
◝(๑⁺д⁺๑)◞՞⠀Scared Д Mouths 34
(⠀Scared Д Mouths 35
[emai<<#160<pro<ec<ed]⠀Scared Д Mouths 36
Д@)⠀Scared Д Mouths 37
(｢⊙Д⊙)｢⠀Scared Д Mouths 38
<<<<|๑⊙Д⊙|/⠀Scared Д Mouths 39
ლ|’Д’ლ|⠀Scared Д Mouths 40
（┛〃°　Д°）┛⠀Scared Д Mouths 41
ヽ〔ﾟДﾟ〕丿⠀Scared Д Mouths 42
)Д⊙`)⠀Scared Д Mouths 43
ฺ(☼Д☼)⠀Scared Д Mouths 44
工ｴｴｪｪ(<╹⌓╹)ｪｪｴｴ工⠀Surrounded by Fear 1
エｴｪｪｪ(●’Д’●)ｪｪｪｴエ⠀Surrounded by Fear 2
エエェェェェ（/×＼）ェェｴｴエエ⠀Surrounded by Fear 3
ε=ε=(っ*´□`)っ⠀Running Away in Fear 1
ε=ε=(怒ﾟДﾟ)ﾉ⠀Running Away in Fear 2
=͟͟͞͞ =͟͟͞͞ ﾍ( ´Д`)ﾉ⠀Running Away in Fear 3
ヽ(￣д￣<)ノ=3=3=3⠀Running Away in Fear 4
٩(´Д` <)۶:.*⠀Running Away in Fear 5
(´×д×`三꒪д꒪ <)⠀Running Away in Fear 6
– =͟͟͞͞ =͟͟͞͞ ﾍ( ´Д`)ﾉ⠀Running Away in Fear 7
ε＝ε＝ε＝(((((ﾉ｀･Д･)ﾉ⠀Running Away in Fear 8
(◞º❒º)◞₎₎(◟º❑º)◟⁾⁾➟➠➨⠀Running Away in Fear 9
ε=٩(●❛ö❛)۶⠀Running Away in Fear 10
Σ(ﾟДﾟ；≡；ﾟдﾟ)⠀Running Away in Fear 11
(c=(c=(c=(c=(ﾟﾛﾟ<c=⠀Running Away in Fear 12
⊂(ﾟДﾟ<⊂⌒`つ⠀Running Away in Fear 13
..･ヾ(。￣□￣)ﾂ⠀Running Away in Fear 14
≡≡≡=(ﾉTдT)ﾉ⠀Running Away in Fear 15
ε=ε=(⊃≧□≦)⊃⠀Running Away in Fear 16
!!Σ(ﾟДﾟ<≡≡≡≡≡ヾ(<ﾟдﾟ)/⠀Running Away in Fear 17
┃ ु ⠁⃘ ⠁⃘ू┃⁼³₌₃⠀Running Away in Fear 18
༻(〃ຶ⌂〃ຶ)⠀Running Away in Fear 19
ਭ३౽=͟͟͞͞(((ഽʻ⁸ʻ)ഽ⠀Running Away in Fear 20
ε=ε=ε=(ﾉ≧∀)ﾉ⠀Running Away in Fear 21
(❛ӧ❛三❛ӧ❛)⠀Running Away in Fear 22
Σ(°Д°；≡；°д°)⠀Running Away in Fear 23
ε=ε=ε=(ﾉTдT)ﾉ⠀Running Away in Fear 24
～ε～ε～┌(|||´Д｀)ノ⠀Running Away in Fear 25
゛(ﾉ~o~)ﾉ⠀Running Away in Fear 26
ε=ε=ε=┏(ﾟロﾟ<)┛⠀Running Away in Fear 27
ε==ε==(ﾉ゜д゜)ﾂ⠀Running Away in Fear 28
ヽ(д`ヽ)｡｡⠀Running Away in Fear 29
｡｡(ﾉ´д)ﾉ⠀Running Away in Fear 30
ヽ(´Д｀<≡<´Д｀)丿⠀Running Away in Fear 31
((ヽ(´Д`<ゞ=ヾ<´Д`)ﾉ))⠀Running Away in Fear 32
ヽ(ω；`ヽ))…((ﾉ´；ω)ﾉ⠀Running Away in Fear 33
ヽ(д｀ヽ彡ﾉ´д)ﾉ⠀Running Away in Fear 34
ε=ε=ε=(((怒ﾟДﾟ)ﾉﾉ⠀Running Away in Fear 35
ε=ε=ε=(*ﾉ´Д｀)ﾉﾟ⠀Running Away in Fear 36
ヾ(*゜、ω゜*)ﾉﾟ⠀Running Away in Fear 37
!!((((((っ<ﾟ∀ﾟ)っ⠀Running Away in Fear 38
へ( ʘ͡ ₒ ʘ͡ )╮/\╱\⠀Running Away in Fear 39
（（（（（（（（　゜□゜）ノ⠀Running Away in Fear 40
ヾ(･c_,･｡) ﾉ =з =з= з⠀Running Away in Fear 41
｡｡゛(ﾉ<><<<<<<)ﾉ⠀Running Away in Fear 42
ε≡Ξ≡Ξ≡ヽ( <￣〇￣)ﾉ⠀Running Away in Fear 43
ヽ(ﾟ□ﾟ＼*≡*／ﾟ□ﾟ)ﾉ⠀Running Away in Fear 44
ε＝（ﾉﾟдﾟ）ﾉ⠀Running Away in Fear 45
(＾ω＾ ≡ °д°)⠀Running Away in Fear 46
ヾ(((<ꈡ▱ꈡ<)))ﾉ⠀Running Away in Fear 47
✧.*(⌯ⅉॕੰૈ▱ⅉॕੰૈ)⠀Running Away in Fear 48
★⌒Ｙ⌒Ｙ⌒Ｙ⌒Ｙ⌒ ヾ(oﾟДﾟ)ﾉ⠀Running Away in Fear 49
へ(~Д~*へ))))… …((((ノ*~З~)ノ⠀Running Away in Fear 50
（´□｀；）=З=З=З=З=З=З⠀Running Away in Fear 51
(꒪ȏ꒪<)⠀Miscellaneous Fear 1
(˵¯͒ བ¯͒˵)⠀Miscellaneous Fear 2
ヽ(<ﾟ<∀<ﾟ< )ﾉ⠀Miscellaneous Fear 3
ヽ( <ﾟ<ж<ﾟ<)ﾉ⠀Miscellaneous Fear 4
y( ꒪◊꒪)y⠀Miscellaneous Fear 5
ヽ(≡ω≡<ヽ)⠀Miscellaneous Fear 6
(ﾉ<≡ω≡)ﾉ⠀Miscellaneous Fear 7
((ﾟ□ﾟ<))⠀Miscellaneous Fear 8
(●゜□゜)人(゜□゜○)⠀Miscellaneous Fear 9
§<ﾟﾛﾟ§⠀Miscellaneous Fear 10
(ノ´ロ`)ノ⠀Miscellaneous Fear 11
(ノ ゜口゜)ノ⠀Miscellaneous Fear 12
!!!!!!(ﾟﾛﾟ屮)屮⠀Miscellaneous Fear 13
ヾ(´囗｀｡)ﾉ⠀Miscellaneous Fear 14
(/<◇<)/⠀Miscellaneous Fear 15
ﾍ(<´o｀)ﾍ⠀Miscellaneous Fear 16
(°□°)⊅⠀Miscellaneous Fear 17
Σ(°□°)⊃⠀Miscellaneous Fear 18
…(ﾟⅩﾟ)…。⠀Miscellaneous Fear 19
(＠O＠<)⠀Miscellaneous Fear 20
〣( ºΔº )〣⠀Miscellaneous Fear 21
˓⁽͑ʺˀ́˙̻ˁ̀ʺ⁾̉ʾʾ ᵏᵞᵅ˞ᵎ⠀Words 1
=͟͟͞͞≠⌓̈⃝\ᵒᵐᵍ⠀Words 2
Ꮚˊ•⌔•ˋᏊ⠀Ꮚ Ꮚ Style Sheep 1
Ꮚᵒ̴̶̷ꈊ˂̤Ꮚ⠀Ꮚ Ꮚ Style Sheep 2
ᏊºัꈊºัᏊ⠀Ꮚ Ꮚ Style Sheep 3
Ꮚ˘̴͈́ꈊ˘̴͈̀Ꮚ⋆✩⠀Ꮚ Ꮚ Style Sheep 4
Ꮚᵒ̴̶̷ꈊᵒ̴̶̷Ꮚ⠀Ꮚ Ꮚ Style Sheep 5
Ꮚ¯ꈊ¯Ꮚ⠀Ꮚ Ꮚ Style Sheep 6
ᏊˊꍓˋᏊ⠀Ꮚ Ꮚ Style Sheep 7
Ꮚ꒵͒ꈊ꒵͒Ꮚ⠀Ꮚ Ꮚ Style Sheep 8
Ꮚ˃̶͈ꈊ˂̶͈Ꮚ⠀Ꮚ Ꮚ Style Sheep 9
Ꮚ˘ꈊ˘Ꮚ⠀Ꮚ Ꮚ Style Sheep 10
Ꮚ˘̩̩̩ꈊ˘̩̩̩Ꮚ⠀Ꮚ Ꮚ Style Sheep 11
ᏊʻัꈊʻัᏊ⠀Ꮚ Ꮚ Style Sheep 12
Ꮚ•ꈊ•Ꮚ⠀Ꮚ Ꮚ Style Sheep 13
Ꮚ°ꈊ°<Ꮚ⠀Ꮚ Ꮚ Style Sheep 14
Ꮚ☻̴̶̷̤ꈊ☻̴̶̷̤Ꮚ⠀Ꮚ Ꮚ Style Sheep 15
Ꮚ˘ꍓ˘Ꮚ⠀Ꮚ Ꮚ Style Sheep 16
ᏊꈍꈊꈍᏊ⠀Ꮚ Ꮚ Style Sheep 17
ᏊᵋꈊᵋᏊ⠀Ꮚ Ꮚ Style Sheep 18
Ꮚ❛ꈊ❛Ꮚ⠀Ꮚ Ꮚ Style Sheep 19
Ꮚ⌀֊̫⍉Ꮚ⠀Ꮚ Ꮚ Style Sheep 20
Ꮚᵔꈊ<#8217<Ꮚෆ⠀Ꮚ Ꮚ Style Sheep 21
Ꮚ•̀ꈊ•́Ꮚ⠀Ꮚ Ꮚ Style Sheep 22
Ꮚ^ꈊ^Ꮚ⠀Ꮚ Ꮚ Style Sheep 23
Ꮚ˟ꈊ˟Ꮚ⠀Ꮚ Ꮚ Style Sheep 24
Ꮚʻั֊̫ʻัᏊ⠀Ꮚ Ꮚ Style Sheep 25
Ꮚ˘̩̩̩ꍓ˘̩̩̩Ꮚ⠀Ꮚ Ꮚ Style Sheep 26
Ꮚ˃̶͈ ֊̫ ˂̶͈Ꮚ⠀Ꮚ Ꮚ Style Sheep 27
Ꮚ⁼ꈊ⁼Ꮚ⠀Ꮚ Ꮚ Style Sheep 28
ᏊˊꈊˋᏊ⠀Ꮚ Ꮚ Style Sheep 29
Ꮚ❛⃘ੌꈊ❛⃘ੌᏊ♡⠀Ꮚ Ꮚ Style Sheep 30
Ꮚ`ꈊ´Ꮚ⠀Ꮚ Ꮚ Style Sheep 31
ෆᏊᵔ֊̫ᵔᏊෆ⠀Ꮚ Ꮚ Style Sheep 32
Ꮚ˙ꈊ˙Ꮚ⠀Ꮚ Ꮚ Style Sheep 33
Ꮚˊ̥̥̥ꈊˋ̥̥ूᏊ⠀Ꮚ Ꮚ Style Sheep 34
Ꮚ°͈ꈊ°͈Ꮚ⠀Ꮚ Ꮚ Style Sheep 35
ᏊˊꈊˋᏊ⠀Ꮚ Ꮚ Style Sheep 36
Ꮚ<#8217<ꈊ<#8217<Ꮚ⠀Ꮚ Ꮚ Style Sheep 37
Ꮚ˃̶͈ꍓ˂̶͈Ꮚ⠀Ꮚ Ꮚ Style Sheep 38
Ꮚ｀ꈊ´Ꮚ⠀Ꮚ Ꮚ Style Sheep 39
Ꮚ⁰ꈊ⁰Ꮚ⠀Ꮚ Ꮚ Style Sheep 40
Ꮚ ்́ꈊ ்̀Ꮚ⠀Ꮚ Ꮚ Style Sheep 41
Ꮚ˃ꈊºัᏊ⠀Ꮚ Ꮚ Style Sheep 42
Ꮚᵕ̤ꈊᵕ̤Ꮚ⠀Ꮚ Ꮚ Style Sheep 43
ᏊᵕꈊᵕᏊ⠀Ꮚ Ꮚ Style Sheep 44
Ꮚ*ꈊ*Ꮚ⠀Ꮚ Ꮚ Style Sheep 45
Ꮚ⌀ꈊ⍉Ꮚ⠀Ꮚ Ꮚ Style Sheep 46
{ @θ ㅈ θ@ }⠀{@ @} Style Sheep 1
{ @ᵒ̴̶̷ꈊ˂̤@ }⠀{@ @} Style Sheep 2
{ @ºัꈊºั@ }⠀{@ @} Style Sheep 3
{ @˘̴͈́ꈊ˘̴͈̀@ }⋆✩⠀{@ @} Style Sheep 4
{ @ᵒ̴̶̷ꈊᵒ̴̶̷@ }⠀{@ @} Style Sheep 5
{ @¯ꈊ¯@ }⠀{@ @} Style Sheep 6
{ @ˊꍓˋ@ }⠀{@ @} Style Sheep 7
{ @꒵͒ꈊ꒵͒@ }⠀{@ @} Style Sheep 8
{ @˃̶͈ꈊ˂̶͈@ }⠀{@ @} Style Sheep 9
{ @˘ꈊ˘@ }⠀{@ @} Style Sheep 10
{ @˘̩̩̩ꈊ˘̩̩̩@ }⠀{@ @} Style Sheep 11
{ @ʻัꈊʻั@ }⠀{@ @} Style Sheep 12
{ @•ꈊ•@ }⠀{@ @} Style Sheep 13
{ @°ꈊ°<@ }⠀{@ @} Style Sheep 14
{ @☻̴̶̷̤ꈊ☻̴̶̷̤@ }⠀{@ @} Style Sheep 15
{ @˘ꍓ˘@ }⠀{@ @} Style Sheep 16
{ @ꈍꈊꈍ@ }⠀{@ @} Style Sheep 17
{ @ᵋꈊᵋ@ }⠀{@ @} Style Sheep 18
{ @❛ꈊ❛@ }⠀{@ @} Style Sheep 19
{ @⌀֊̫⍉@ }⠀{@ @} Style Sheep 20
{ @ᵔꈊ<#8217<@ }ෆ⠀{@ @} Style Sheep 21
{ @•̀ꈊ•́@ }⠀{@ @} Style Sheep 22
{ @^ꈊ^@ }⠀{@ @} Style Sheep 23
{ @˟ꈊ˟@ }⠀{@ @} Style Sheep 24
{ @ʻั֊̫ʻั@ }⠀{@ @} Style Sheep 25
{ @˘̩̩̩ꍓ˘̩̩̩@ }⠀{@ @} Style Sheep 26
{ @˃̶͈ ֊̫ ˂̶͈@ }⠀{@ @} Style Sheep 27
{ @⁼ꈊ⁼@ }⠀{@ @} Style Sheep 28
{ @ˊꈊˋ@ }⠀{@ @} Style Sheep 29
{ @❛⃘ੌꈊ❛⃘ੌ@ }♡⠀{@ @} Style Sheep 30
{ @`ꈊ´@ }⠀{@ @} Style Sheep 31
ෆ{ @ᵔ֊̫ᵔ@ }ෆ⠀{@ @} Style Sheep 32
{ @˙ꈊ˙@ }⠀{@ @} Style Sheep 33
{ @ˊ̥̥̥ꈊˋ̥̥ू@ }⠀{@ @} Style Sheep 34
{ @°͈ꈊ°͈@ }⠀{@ @} Style Sheep 35
{ @ˊꈊˋ@ }⠀{@ @} Style Sheep 36
{ @<#8217<ꈊ<#8217<@ }⠀{@ @} Style Sheep 37
{ @˃̶͈ꍓ˂̶͈@ }⠀{@ @} Style Sheep 38
{ @｀ꈊ´@ }⠀{@ @} Style Sheep 39
{ @⁰ꈊ⁰@ }⠀{@ @} Style Sheep 40
{ @ ்́ꈊ ்̀@ }⠀{@ @} Style Sheep 41
{ @˃ꈊºั@ }⠀{@ @} Style Sheep 42
{ @ᵕ̤ꈊᵕ̤@ }⠀{@ @} Style Sheep 43
{ @ᵕꈊᵕ@ }⠀{@ @} Style Sheep 44
{ @*ꈊ*@ }⠀{@ @} Style Sheep 45
{ @⌀ꈊ⍉@ }⠀{@ @} Style Sheep 46
(n˘v˘•)¬⠀Oh You! 1
(ง ◕ั⌑◕ั)ว ⁾⠀Oh You! 2
₍₍ (ง Ŏ౪Ŏ)ว ⁾⁾⠀Oh You! 3
(ง ´͈౪`͈)ว⠀Oh You! 4
ᕕ╏ ͡ ▾ ͡ ╏┐⠀Oh You! 5
(ﾍﾟ◇ﾟ)」⠀Oh You! 6
ᕕ[ ́ ل͜ ́ ]੭⠀Oh You! 7
₍₍ (ง ˙ω˙)ว ⁾⁾⠀Oh You! 8
(*´_ゝ｀)⠀Blushing Cheeks with an Asterisk 1
(*´∀`*)⠀Blushing Cheeks with an Asterisk 2
(*´ｪ｀*)⠀Blushing Cheeks with an Asterisk 3
｡(*^▽^*)ゞ⠀Blushing Cheeks with an Asterisk 4
(‘-’*)⠀Blushing Cheeks with an Asterisk 5
(*´∀`*)⠀Blushing Cheeks with an Asterisk 6
(*^^*)⠀Blushing Cheeks with an Asterisk 7
(*ﾟｰﾟ)ゞ⠀Blushing Cheeks with an Asterisk 8
(ノ*゜▽゜*)⠀Blushing Cheeks with an Asterisk 9
ฅ(*°ω°*ฅ)⠀Blushing Cheeks with an Asterisk 10
(*ﾟ∀ﾟ*)⠀Blushing Cheeks with an Asterisk 11
(*´ω｀*)⠀Blushing Cheeks with an Asterisk 12
(´ω｀*)⠀Blushing Cheeks with an Asterisk 13
(⁎❝᷀ົ ˙̫ ❝᷀ົ⁎)⠀Blushing Cheeks with an Asterisk 14
ε=ε=ε=ε=ε” “(/*’-‘*)/⠀Blushing Cheeks with an Asterisk 15
ヽ(＊<><<∇<<<<)ﾉ⠀Blushing Cheeks with an Asterisk 16
(*´-｀*)⠀Blushing Cheeks with an Asterisk 17
( *’ω’* )⠀Blushing Cheeks with an Asterisk 18
( *∵* )⠀Blushing Cheeks with an Asterisk 19
*:ﾟ*｡⋆ฺ(*´◡`)⠀Blushing Cheeks with an Asterisk 20
(#^.^#)⠀Blushing Cheeks with a # 1
(#｀ε´# )ゞ⠀Blushing Cheeks with a # 2
(＃⌒∇⌒＃)ゞ⠀Blushing Cheeks with a # 3
꒰⌗´͈ ᵕ ॣ`͈⌗꒱৩⠀Blushing Cheeks with a # 4
(#ﾟﾛﾟ#)⠀Blushing Cheeks with a # 5
꒰#’ω`#꒱੭⠀Blushing Cheeks with a # 6
(#^^#)ゞ⠀Blushing Cheeks with a # 7
(๑•́ ω •̀๑)⠀Blushing Cheeks with a ๑ 1
⁝(๑⑈௰⑈)◞⁝˚º꒰꒱⠀Blushing Cheeks with a ๑ 2
(๑•́ ₃ •̀๑)⠀Blushing Cheeks with a ๑ 3
(๑ˊ▵ॢˋ̥๑)⠀Blushing Cheeks with a ๑ 4
(๑´ㅂ`๑)⠀Blushing Cheeks with a ๑ 5
(๑ゝω╹๑)⠀Blushing Cheeks with a ๑ 6
(´๑•_•๑)⠀Blushing Cheeks with a ๑ 7
(๑•́ω•̀๑)⠀Blushing Cheeks with a ๑ 8
(๑⃙⃘·́ω·̀๑⃙⃘)੨⠀Blushing Cheeks with a ๑ 9
(◞ ๑⑈௰⑈)⠀Blushing Cheeks with a ๑ 10
(๑´ω`๑)⠀Blushing Cheeks with a ๑ 11
(๑癶ω癶๑)⠀Blushing Cheeks with a ๑ 12
(´•ω•`๑)⠀Blushing Cheeks with a ๑ 13
(๑´•ω • `๑)⠀Blushing Cheeks with a ๑ 14
(_๑˘ㅂ˘๑)⠀Blushing Cheeks with a ๑ 15
(๑´⍢`๑)⠀Blushing Cheeks with a ๑ 16
(๑′°︿°๑)⠀Blushing Cheeks with a ๑ 17
(๑́•∀•๑̀)ฅ⠀Blushing Cheeks with a ๑ 18
(๑ּగ⌄ּగ๑)⠀Blushing Cheeks with a ๑ 19
(⁶ੌ௰⁶ੌ๑)⠀Blushing Cheeks with a ๑ 20
(๑꒪̇⌄꒪̇๑)⠀Blushing Cheeks with a ๑ 21
(๑꒪⍘꒪๑)⠀Blushing Cheeks with a ๑ 22
(๑⁍᷄౪⁍᷅๑)⠀Blushing Cheeks with a ๑ 23
Σ(๑꒪⃙⃚᷄ꑣ꒪⃚⃙᷅๑۶)۶⠀Blushing Cheeks with a ๑ 24
(๑￫‿￩๑)⠀Blushing Cheeks with a ๑ 25
(๑•́‧̫•̀๑)⠀Blushing Cheeks with a ๑ 26
(๑･▱･๑)⠀Blushing Cheeks with a ๑ 27
(〃￣ω￣〃)ゞ⠀Flushed Cheeks with Vertical and Sometimes Slightly Diagonal Lines 1
(｡・//ε//・｡)⠀Flushed Cheeks with Vertical and Sometimes Slightly Diagonal Lines 2
（//･_･//)⠀Flushed Cheeks with Vertical and Sometimes Slightly Diagonal Lines 3
（〃・ω・〃）⠀Flushed Cheeks with Vertical and Sometimes Slightly Diagonal Lines 4
(〃▽〃)⠀Flushed Cheeks with Vertical and Sometimes Slightly Diagonal Lines 5
(///Σ///)⠀Flushed Cheeks with Vertical and Sometimes Slightly Diagonal Lines 6
(//∇//)⠀Flushed Cheeks with Vertical and Sometimes Slightly Diagonal Lines 7
(灬ºωº灬)⠀Flushed Cheeks with Vertical and Sometimes Slightly Diagonal Lines 8
(´,,•ω•,,)⠀Flushed Cheeks with Vertical and Sometimes Slightly Diagonal Lines 9
(⁄ ⁄•⁄ω⁄•⁄ ⁄)⁄⠀Flushed Cheeks with Vertical and Sometimes Slightly Diagonal Lines 10
(灬º 艸º灬)⠀Flushed Cheeks with Vertical and Sometimes Slightly Diagonal Lines 11
(✿ꈍ。 ꈍ✿)⠀Flushed Cheeks with Vertical and Sometimes Slightly Diagonal Lines 12
(⁄ ⁄^⁄ᗨ⁄^⁄ ⁄)⠀Flushed Cheeks with Vertical and Sometimes Slightly Diagonal Lines 13
(⸝⸝⸝ ≧ㅿ＼⸝⸝⸝)/⠀Flushed Cheeks with Vertical and Sometimes Slightly Diagonal Lines 14
⁽⁽ ◟(灬 ˊωˋ 灬)◞ ⁾⁾⠀Flushed Cheeks with Vertical and Sometimes Slightly Diagonal Lines 15
╰(⸝⸝⸝´꒳`⸝⸝⸝)╯⠀Flushed Cheeks with Vertical and Sometimes Slightly Diagonal Lines 16
(ؑ‷ᵕؑ̇‷)◞✧⠀Flushed Cheeks with Vertical and Sometimes Slightly Diagonal Lines 17
{•̴͈ ˔̇ •̴͈}⠀Flushed Cheeks with Vertical and Sometimes Slightly Diagonal Lines 18
ლ(///´◜⊜｀//////ლ)⠀Flushed Cheeks with Vertical and Sometimes Slightly Diagonal Lines 19
(⸝⸝⍢⸝⸝) ෆ⠀Flushed Cheeks with Vertical and Sometimes Slightly Diagonal Lines 20
⁄(⁄ ⁄ˊૢ⁄ ⌑ ⁄ˋૢ⁄ ⁄)⁄⠀Flushed Cheeks with Vertical and Sometimes Slightly Diagonal Lines 21
˚✧₊⁎˓˓⁽̨̡ ˚͈́꒳​˚͈̀*⁾̧̢˒˒⁎⁺˳✧༚⠀Flushed Cheeks with Vertical and Sometimes Slightly Diagonal Lines 22
(⺣◡⺣)♡*⠀Flushed Cheeks with Vertical and Sometimes Slightly Diagonal Lines 23
( ̧⸝⸝⍢⸝⸝)ི⠀Flushed Cheeks with Vertical and Sometimes Slightly Diagonal Lines 24
꒰ •͈́ ̫ •͈̀ ꒱ˉ̞̭⠀Flushed Cheeks with Vertical and Sometimes Slightly Diagonal Lines 25
(*ꈍ꒳ꈍ*)⠀Flushed Cheeks with Vertical and Sometimes Slightly Diagonal Lines 26
(*ꈍ꒙ꈍ*)⠀Flushed Cheeks with Vertical and Sometimes Slightly Diagonal Lines 27
ค{•̴͈ ˳̇ •̴͈}ค✧⠀Flushed Cheeks with Vertical and Sometimes Slightly Diagonal Lines 28
⁄(⁄ ⁄•⁄-⁄•⁄ ⁄)⁄⠀Flushed Cheeks with Vertical and Sometimes Slightly Diagonal Lines 29
(∗∕ ∕•̥̥̥̥∕ω∕•̥̥̥̥∕)⠀Flushed Cheeks with Vertical and Sometimes Slightly Diagonal Lines 30
(⸝⸝•́દ•̀⸝⸝)⠀Flushed Cheeks with Vertical and Sometimes Slightly Diagonal Lines 31
ꈍ .̮ ꈍ⠀Flushed Cheeks with Vertical and Sometimes Slightly Diagonal Lines 32
・:*(〃・ｪ・〃人)*:・⠀Flushed Cheeks with Vertical and Sometimes Slightly Diagonal Lines 33
⁄(⁄ ⁄•⁄ω⁄•⁄ ⁄)⁄⠀Flushed Cheeks with Vertical and Sometimes Slightly Diagonal Lines 34
(ृ°͈꒳​°͈ ृ)ु⠀Flushed Cheeks with Vertical and Sometimes Slightly Diagonal Lines 35
⁽͑ʺˊ˙̫ˋʺ⁾̉⠀Flushed Cheeks with Vertical and Sometimes Slightly Diagonal Lines 36
(˵¯͒⌄¯͒˵)⠀Flushed Cheeks with Vertical and Sometimes Slightly Diagonal Lines 37
⊂((〃’⊥’〃))⊃⠀Flushed Cheeks with Vertical and Sometimes Slightly Diagonal Lines 38
(灬╹ω╹灬)⠀Flushed Cheeks with Vertical and Sometimes Slightly Diagonal Lines 39
(〃ω〃)⠀Flushed Cheeks with Vertical and Sometimes Slightly Diagonal Lines 40
(〃´Å｀〃)⠀Flushed Cheeks with Vertical and Sometimes Slightly Diagonal Lines 41
ヾ( 〃ω〃)ｯ⠀Flushed Cheeks with Vertical and Sometimes Slightly Diagonal Lines 42
(･ω･`〃)⠀Flushed Cheeks with Vertical and Sometimes Slightly Diagonal Lines 43
ヾ(〃ω〃ヾ))⠀Flushed Cheeks with Vertical and Sometimes Slightly Diagonal Lines 44
((ﾉ〃ω〃)ﾉﾞ⠀Flushed Cheeks with Vertical and Sometimes Slightly Diagonal Lines 45
ヽ(〃v〃)ﾉ⠀Flushed Cheeks with Vertical and Sometimes Slightly Diagonal Lines 46
(〃´ﾉω`〃)⠀Flushed Cheeks with Vertical and Sometimes Slightly Diagonal Lines 47
<<<<(〃´∀｀〃)<><<⠀Flushed Cheeks with Vertical and Sometimes Slightly Diagonal Lines 48
・:*(〃∇〃人)*:・⠀Flushed Cheeks with Vertical and Sometimes Slightly Diagonal Lines 49
(〃・ω・〃)ノ~☆⠀Flushed Cheeks with Vertical and Sometimes Slightly Diagonal Lines 50
୧( ˵ ° ~ ° ˵ )୨⠀Flushed Cheeks with Vertical and Sometimes Slightly Diagonal Lines 51
（˶′◡‵˶）⠀Flushed Cheeks with Vertical and Sometimes Slightly Diagonal Lines 52
o(〃’▽’〃)o⠀Flushed Cheeks with Vertical and Sometimes Slightly Diagonal Lines 53
(〃´∀｀)⠀Flushed Cheeks with Vertical and Sometimes Slightly Diagonal Lines 54
(∥￣■￣∥)⠀Flushed Cheeks with Vertical and Sometimes Slightly Diagonal Lines 55
ヾ(〃ﾟーﾟ〃)ノ⠀Flushed Cheeks with Vertical and Sometimes Slightly Diagonal Lines 56
( 〃．．)⠀Flushed Cheeks with Vertical and Sometimes Slightly Diagonal Lines 57
(´,,•ω•,,｀)⠀Flushed Cheeks with Vertical and Sometimes Slightly Diagonal Lines 58
⁽˚̌ʷ˚̌ʺ⁾⠀Flushed Cheeks with Vertical and Sometimes Slightly Diagonal Lines 59
ｰ(°◇°〃)⠀Flushed Cheeks with Vertical and Sometimes Slightly Diagonal Lines 60
(●///▽///●)⠀Flushed Cheeks with Vertical and Sometimes Slightly Diagonal Lines 61
б(//x//)⠀Flushed Cheeks with Vertical and Sometimes Slightly Diagonal Lines 62
(灬ºωº灬)♡⠀Flushed Cheeks with Vertical and Sometimes Slightly Diagonal Lines 63
ο(‘・’〃)ο″⠀Flushed Cheeks with Vertical and Sometimes Slightly Diagonal Lines 64
（。-＿-。）⠀Circles for Cheeks 1
(｡･･｡)⠀Circles for Cheeks 2
(o・・o)/⠀Circles for Cheeks 3
(●ฅ́дฅ̀●)⠀Circles for Cheeks 4
( 。•_• 。)⠀Circles for Cheeks 5
(●˙꒳˙●)⠀Circles for Cheeks 6
(●°u°●)​ 」⠀Circles for Cheeks 7
(｡uωu｡)⠀Circles for Cheeks 8
ღ✉ღ•̥̑ .̮ •̥̑)⠀Circles for Cheeks 9
(o´∪｀o)⠀Circles for Cheeks 10
|´∀｀●)⠀Circles for Cheeks 11
（＠´＿｀＠）⠀Miscellaneous Cheeks 1
(。≖ˇ∀ˇ≖。)⠀Miscellaneous Cheeks 2
(∗ᵕ̴᷄◡ᵕ̴᷅∗)՞⠀Miscellaneous Cheeks 3
ల(*´= ◡ =｀*)⠀Miscellaneous Cheeks 4
▓⚗_⚗▓⠀Miscellaneous Cheeks 5
(w´ω｀w)⠀Miscellaneous Cheeks 6
((≡ຶ◡≡ຶ))⠀Miscellaneous Cheeks 7
(⊙﹏⊙✿)⠀Shy but not Blushing 1
⸜(ᶿ᷇ധᶿ᷆)⸝⠀Shy but not Blushing 2
( ͒•·̫|⠀Shy but not Blushing 3
( ´•௰•`)⠀Shy but not Blushing 4
(´°ω°`)⠀Shy but not Blushing 5
*⁂((✪⥎✪))⁂*⠀Shy but not Blushing 6
( ͒ ́ඉ .̫ ඉ ̀ ͒)⠀Shy but not Blushing 7
(◍´ಲ`◍)⠀Shy but not Blushing 8
(◍ ´꒳` ◍)b⠀Shy but not Blushing 9
(ˊˡ·̫ˡˋ)⠀Shy but not Blushing 10
(⌯꒪͒ ૢ౪ ૢ꒪͒)⠀Shy but not Blushing 11
(´ . .̫ . `)⠀Shy but not Blushing 12
˄̩̞(˒௰˓)⠀Shy but not Blushing 13
ԅ[ •́ ﹏ •̀ ]و⠀Shy but not Blushing 14
ԅ[ •́ ﹏├┬┴┬┴⠀Shy but not Blushing 15
(⌒_⌒<)⠀A Drop of Sweat 1
(<ﾞ°´ω°´)⠀A Drop of Sweat 2
(^_^<)⠀A Drop of Sweat 3
(^^<)⠀A Drop of Sweat 4
（；^ω^）⠀A Drop of Sweat 5
(^◇^；)⠀A Drop of Sweat 6
(ヾ<￣▽￣)ヾ⠀A Drop of Sweat 7
( /)u(\ )⠀Covering Your Face Because of Shyness 1
（*/∇＼*）⠀Covering Your Face Because of Shyness 2
(*/ω＼*)⠀Covering Your Face Because of Shyness 3
(*ﾉ▽ﾉ)⠀Covering Your Face Because of Shyness 4
(*ﾉωﾉ)⠀Covering Your Face Because of Shyness 5
（/｡＼)⠀Covering Your Face Because of Shyness 6
(／(ｴ)＼)⠀Covering Your Face Because of Shyness 7
(/□＼*)・゜⠀Covering Your Face Because of Shyness 8
(/ω＼)⠀Covering Your Face Because of Shyness 9
(#／。＼#)⠀Covering Your Face Because of Shyness 10
(╯_╰)⠀Covering Your Face Because of Shyness 11
(╯ಊ╰)⠀Covering Your Face Because of Shyness 12
(つω⊂* )⠀Covering Your Face Because of Shyness 13
(ﾉ)´∀｀(ヾ)⠀Covering Your Face Because of Shyness 14
(ʃᵕ̩̩ ᵕ̩̩⑅)⠀Covering Your Face Because of Shyness 15
(♡´艸`)⠀Covering Your Face Because of Shyness 16
(´つヮ⊂)⠀Covering Your Face Because of Shyness 17
(Ŏ艸Ŏ)⠀Covering Your Face Because of Shyness 18
(／▽￣)／⠀Covering Your Face Because of Shyness 19
(／≧ω＼)⠀Covering Your Face Because of Shyness 20
(*/∇＼*)⠀Covering Your Face Because of Shyness 21
ʕ*ﾉᴥﾉʔ⠀Covering Your Face Because of Shyness 22
( *´ﾉｪ`)⠀Covering Your Face Because of Shyness 23
(ﾉ∀｀●)⊃⠀Covering Your Face Because of Shyness 24
⊂((〃/⊥＼〃))⊃⠀Covering Your Face Because of Shyness 25
(/へ＼*)⠀Covering Your Face Because of Shyness 26
(ﾉ∇≦*)⠀Covering Your Face Because of Shyness 27
(〃ﾉωﾉ)⠀Covering Your Face Because of Shyness 28
(〃ﾉ∀｀〃)⠀Covering Your Face Because of Shyness 29
(ﾉ∀＼*)⠀Covering Your Face Because of Shyness 30
(*ﾉωヾ*)⠀Covering Your Face Because of Shyness 31
(*ﾉзﾉ*)⠀Covering Your Face Because of Shyness 32
♡(｡￫ˇ艸￩)⠀Covering Your Face Because of Shyness 33
（＊ノ∀｀＊）ノ⠀Covering Your Face Because of Shyness 34
(ノ∀￣〃)⠀Covering Your Face Because of Shyness 35
(*/▽＼*)⠀Covering Your Face Because of Shyness 36
(*´ﾉ∀｀)⠀Covering Your Face Because of Shyness 37
.ﾟ:<｡+。ε(ﾉ∀≦*)з｡+.｡ﾟ:⠀Covering Your Face Because of Shyness 38
(´•͈ुω•͈ू`)⠀Complex Shyness 1
( ੭⌯᷄௰⌯᷅ ू’<|)⠀Complex Shyness 2
|₋ॢọ̶̶̷̥᷅๑)‧˚⁺⠀Complex Shyness 3
(๑ᵉ̷͈◡ॢᵉ̷͈๑)Üfu♡⠀Complex Shyness 4
(⑉ ॢ• • ॢ⑉)⠀Complex Shyness 5
⁄(⁄⑅ॢ⁄˃̶͈̀⁄௰⁄˂̶͈́⁄⑅ॢ⁄)⁄⠀Complex Shyness 6
ू(ʚ̴̶̷́ .̠ ʚ̴̶̷̥̀ ू)⠀Complex Shyness 7
꒰ີᵒ̴̶̷͈́༝ॢᵒ̴̶̷͈̀ ૢ꒱ ິ⠀Complex Shyness 8
‾̠̠̠̠̠̠̠̄| ॣ•͈̀๑)⠀Complex Shyness 9
(*,,ºัωºั,,)⠀Complex Shyness 10
( ︠ु ௰︡ू)⠀Complex Shyness 11
(ˊσ̴̶̷̤ ₋̮̑ σ̴̶̷̤ˋ)₊ෆ⃛⁺˚⠀Complex Shyness 12
(⁎ ́ఊ ̫ఊ̀⁎)⠀Complex Shyness 13
·◌̊ˈ* (⁰̶̶̷ॢ ˙̶̮ ू⁰̴̷̷๑).°◌̊⠀Complex Shyness 14
(๑˘ु⑅ू˘๑)*✲ﾟ*｡⋆⠀Complex Shyness 15
亝˓˓( ª̷̛ॢ₎௰₍ª̷̛ॢ )˒˒亝⠀Complex Shyness 16
(ृ ु ´͈ ᵕ `͈ )ु⠀Complex Shyness 17
(ृ ´͈ ᵕ `͈ ृ )ु⠀Complex Shyness 18
•ू(ᵒ̴̶̷᷄ωᵒ̴̶̷᷅*•ू) )੭ु⁾⁾⠀Complex Shyness 19
ෆ⃛(ٛ⌯ॢ˃ ɪ ˂ٛ⌯ॢ)⠀Complex Shyness 20
(•́ ॣ·̫ ॣ•̀,)՞⠀Complex Shyness 21
‹(⁽˙́ʷ˙̀⁾ )∨( ⁽˙́ʷ˙̀⁾)›⠀Multiple People Being Shy 1
(v〃∇〃)ﾊ(〃∇〃v)⠀Multiple People Being Shy 2
(v〃ω〃)八(〃ω〃v)⠀Multiple People Being Shy 3
(v〃∇〃)ハ(〃∇〃v)⠀Multiple People Being Shy 4
( ￣з(〃´▽｀〃)ε￣ )⠀Multiple People Being Shy 5
◌⑅⃝*॰ॱᒄᵒᵏⁱ(꜆˘͈ෆ˘͈꜀)ᒄᵒᵏⁱ◌⑅⃝*॰ॱ⠀Shyness and Words 1
(⑅ᵒ̴̶̷᷄ωᵒ̴̶̷᷅⊞ོॢ)fෆr yෆu⋆*⋆✩⠀Shyness and Words 2
⁽͑ˀˉ˙̫ˉˁ⁾̉ ᵐᵘⁿⁱ⠀Shyness and Words 3
￡ονё Υου…..φ(〃∇〃 ))⠀Shyness and Words 4
(´〜｀*) zzz⠀Regular Sleeping or Sleepy Kaomojis 1
(-_-) zzz⠀Regular Sleeping or Sleepy Kaomojis 2
(-, – )…zzzZZZ⠀Regular Sleeping or Sleepy Kaomojis 3
(-ｪ-)｡o⠀Regular Sleeping or Sleepy Kaomojis 4
(。-ω-)zzz⠀Regular Sleeping or Sleepy Kaomojis 5
(*-ω-)⠀Regular Sleeping or Sleepy Kaomojis 6
(´～`)⠀Regular Sleeping or Sleepy Kaomojis 7
(∪｡∪)｡｡｡zzz⠀Regular Sleeping or Sleepy Kaomojis 8
(ᴗ˳ᴗ)⠀Regular Sleeping or Sleepy Kaomojis 9
(ᵕ≀ ̠ᵕ )⠀Regular Sleeping or Sleepy Kaomojis 10
［(－－)］zzz⠀Regular Sleeping or Sleepy Kaomojis 11
ε-(´・｀)⠀Regular Sleeping or Sleepy Kaomojis 12
Σ(￣。￣ノ)ノ⠀Regular Sleeping or Sleepy Kaomojis 13
✾꒡ .̮ ꒡✾⠀Regular Sleeping or Sleepy Kaomojis 14
(≚ᄌ≚)ƶƵ⠀Regular Sleeping or Sleepy Kaomojis 15
( ु⁎ᴗ_ᴗ⁎)ु.｡oO⠀Regular Sleeping or Sleepy Kaomojis 16
(-ι_- )))。。。⠀Regular Sleeping or Sleepy Kaomojis 17
(⌯͒ᵕɪᵕ⌯͒)zzZ⠀Regular Sleeping or Sleepy Kaomojis 18
꒰◍ᐡᐤᐡ◍꒱⠀Regular Sleeping or Sleepy Kaomojis 19
_(-ω-`_)⠀Regular Sleeping or Sleepy Kaomojis 20
( ⓥωⓥ)⠀Regular Sleeping or Sleepy Kaomojis 21
(｡･ˇ_ˇ･｡)⠀Regular Sleeping or Sleepy Kaomojis 22
(´-_ゝ-`)⠀Regular Sleeping or Sleepy Kaomojis 23
.꒰ϱ﹏-๑꒱‧*Zz｡⠀Regular Sleeping or Sleepy Kaomojis 24
(๑ᵕ⌓ᵕ̤)⠀Regular Sleeping or Sleepy Kaomojis 25
(- o – ) zzZ⠀Regular Sleeping or Sleepy Kaomojis 26
⁽⁽(ᵕ≀ ̠ᵕ ) ⋏º¬͜ Ɩ།⠀Regular Sleeping or Sleepy Kaomojis 27
꒰◍ᐡᐤᐡ◍꒱ᐝ.∗̥✩⁺˚⑅⠀Regular Sleeping or Sleepy Kaomojis 28
[(－－)]..zzZ⠀Regular Sleeping or Sleepy Kaomojis 29
(✿◡‿◡ฺ)zzz⠀Regular Sleeping or Sleepy Kaomojis 30
(｡v_v｡)⠀Regular Sleeping or Sleepy Kaomojis 31
川｡μ_μ)σ⠀Regular Sleeping or Sleepy Kaomojis 32
(︶｡︶✽)⠀Regular Sleeping or Sleepy Kaomojis 33
(ृ ु⁎ᴗᵨᴗ⁎)ु.zZ⠀Regular Sleeping or Sleepy Kaomojis 34
⎰≀.⺤_⺤≀⎰⠀Regular Sleeping or Sleepy Kaomojis 35
(｡´-д-)⠀Regular Sleeping or Sleepy Kaomojis 36
(﹡ꑓ ︿ ꑓ`﹡)⠀Regular Sleeping or Sleepy Kaomojis 37
|[(*´ｪ`)]|zZＺ⠀Regular Sleeping or Sleepy Kaomojis 38
(｡し_し｡)⠀Regular Sleeping or Sleepy Kaomojis 39
( ु⁎ᴗᵨᴗ⁎)ु.zZ⠀Regular Sleeping or Sleepy Kaomojis 40
_(⌒( ु`ω、) ु zzZz⠀Regular Sleeping or Sleepy Kaomojis 41
(　-益-)｡｡oＯ　ＺＺＺＺＺＺＺ⠀Regular Sleeping or Sleepy Kaomojis 42
＿ﾉ乙(､ﾝ､)_⠀Laying Down on Your Side 1
_(：3 」∠ )_⠀Laying Down on Your Side 2
_(┐「ε:)_⠀Laying Down on Your Side 3
【:εω⠀Laying Down on Your Side 4
(冫༵、)⠀Laying Down on Your Side 5
_:(‘Θ’ 」 ∠):_⠀Laying Down on Your Side 6
_:(´ཀ`」 ∠):_ …⠀Laying Down on Your Side 7
_( :⁍ 」 )_⠀Laying Down on Your Side 8
८(冫༙、)৲˒˒⠀Laying Down on Your Side 9
(ृ ᐛ ृ )ु⠀Laying Down on Your Side 10
_(」∠ ､ﾝ､)_⠀Laying Down on Your Side 11
_(┐「ε:)_♡⠀Laying Down on Your Side 12
_(°ω°｣ ∠)_⠀Laying Down on Your Side 13
_(ˇωˇ」∠)_⠀Laying Down on Your Side 14
_/￣|(冫、)-c⠀Laying Down on Your Side 15
– =͟͟͞͞ (¦3[▓▓])⠀Sleeping in an Actual Bed 1
▓▓ ु‹:) ु⠀Sleeping in an Actual Bed 2
(¦3ꇤ[▓▓]⠀Sleeping in an Actual Bed 3
˓(¦:ɝ[▓▓]⠀Sleeping in an Actual Bed 4
ꏂ[▓] ृ⑆)˚º꒰꒱⠀Sleeping in an Actual Bed 5
(˴́³[▒]꒱⌕˚º꒰…꒱⠀Sleeping in an Actual Bed 6
ᓬᗸᗳ[▓▓]ꍞ⠀Sleeping in an Actual Bed 7
(¦:ɜ[▓▓]⌕⁷̩ ̊⠀Sleeping in an Actual Bed 8
(»:ɜ[▒▒]˚º꒰꒱⠀Sleeping in an Actual Bed 9
(ː:̣̣̣̥з[▓▓]˚º꒰꒱⠀Sleeping in an Actual Bed 10
⁝(¦ꌲɜ[▓▓]⁝ ˚º꒰꒱⠀Sleeping in an Actual Bed 11
(:˒[￣]⠀Sleeping in an Actual Bed 12
[▒▒]ꇤꒊ¦`)ꍞ⠀Sleeping in an Actual Bed 13
⌈▒͟⌉ꅼ)ꍞ⠀Sleeping in an Actual Bed 14
(¦ꄰ[▓▓]⠀Sleeping in an Actual Bed 15
(¦ꃆ[▓▓]⠀Sleeping in an Actual Bed 16
˓˓(¦:ɝ[▓▓]⠀Sleeping in an Actual Bed 17
(¦ꎌ[▓▓]⠀Sleeping in an Actual Bed 18
(¦ꃎ[▓▓]⠀Sleeping in an Actual Bed 19
(¦ꃩ[▓▓]⠀Sleeping in an Actual Bed 20
(¦ꀝ[▓▓]⠀Sleeping in an Actual Bed 21
⌈▓͟⌉ꆟ)ꍞ⠀Sleeping in an Actual Bed 22
(¦ꀦ[▓▓]⠀Sleeping in an Actual Bed 23
(:ɜ[▒]꒱˚º꒰꒱⠀Sleeping in an Actual Bed 24
(¦ꒉ[▓▓]⠀Sleeping in an Actual Bed 25
(:3ꇤ[▓▓]ε¦)⠀Sleeping in an Actual Bed 26
(˴́³[▒]꒱⌕˚º꒰…꒱⠀Sleeping in an Actual Bed 27
(ृ·́௰·̀ू[▓▒▓]˒˒˚º꒰꒱⠀Sleeping in an Actual Bed 28
ﾘृ(·́௰·̀ू[▓▒▓]˒˒˚º꒰꒱⠀Sleeping in an Actual Bed 29
⋆｡˚ (¦3ꇤ[▓▓]⋆｡˚✩⠀Sleeping in an Actual Bed 30
– =͟͟͞͞ =͟͟͞͞(¦3[=͟͟͞͞__]=͟͟͞͞=͟͟͞͞ =͟͟͞͞)⠀Sleeping in an Actual Bed 31
⌒((:з)⌒((ε:)⌒((:3[___]=-3⠀Sleeping in an Actual Bed 32
[▓▒▓] ु‹:) ु˒˒✯*･☪:.｡⠀Sleeping in an Actual Bed 33
(:3[▓▓▓▓▓▓▓▓]⠀Sleeping in an Actual Bed 34
( -_-)<><<c[_]⠀Coffee 1
{zzz}°°°( -_-)<><<c[_]⠀Coffee 2
(。-ω-)<><<c[_]⠀Coffee 3
(*-ω-)<><<c[_]⠀Coffee 4
(ᴗ˳ᴗ)<><<c[_]⠀Coffee 5
(๑ᵕ⌓ᵕ̤)<><<c[_]⠀Coffee 6
(｡´-д-)<><<c[_]⠀Coffee 7
(﹡ꑓ ︿ ꑓ`﹡)<><<c[_]⠀Coffee 8
(｡v_v｡)<><<c[_]⠀Coffee 9
川｡μ_μ)σc[_]⠀Coffee 10
(ι´Д｀)ﾉ⠀Stretching 1
ᕙ(⇀‸↼‶)ᕗ⠀Stretching 2
₍₍ ᕕ( ･᷄ὢ･᷅ )ᕗ⁾⁾⠀Stretching 3
₍₍ ᕕ(´ ω` )ᕗ⁾⁾⠀Stretching 4
＼(o￣∇￣o)/⠀Stretching 5
ヾ(。￣□￣)ﾂ⠀Stretching 6
ヾ(￣□￣<)ﾉ⠀Stretching 7
ƪ(‾￣o￣”)ʃ⠀Stretching 8
*｡٩(ˊωˋ*)و✧*｡⠀Stretching 9
٩(ˊᗜˋ*)و⠀Stretching 10
٩(´Д` <)۶:.*⠀Stretching 11
٩( ‘ω’ )و⠀Stretching 12
٩(｡•ω•｡)و⠀Stretching 13
‘٩(๑´3｀๑)۶⠀Stretching 14
٩(๑˘ω˘๑)۶:.｡⠀Stretching 15
୧( ́⁰⃙⃘Ԑ⁰⃙ఁ̀ )୨⠀Stretching 16
₍₍ ᕕ(´◓ω◓)ᕗ⁾⁾⠀Stretching 17
ﾍ(´ω`)ゞ⠀Stretching 18
ヽ( ̐〥 ̐)ﾉ⠀Stretching 19
ᕕ(⁽゚⁾བ︡ ⁽ ْ ⁾ ╬)ᕗ⠀Stretching 20
٩( ⺤◊⺤)۶⠀Stretching 21
╰(⇀‸↼)╯⠀Stretching 22
╰(⇀⌂↼‶)╯⠀Stretching 23
＼(*-◇-)／｡ﾟоО⠀Stretching 24
（-＾〇＾-）⠀Yawning 1
(<´ρ`)⠀Yawning 2
（<≧皿≦）⠀Yawning 3
（)´д`(）⠀Yawning 4
(*´ο`*)⠀Yawning 5
（´□｀川）⠀Yawning 6
(▰˘o˘▰)⠀Yawning 7
(o´Д`)⠀Yawning 8
∑(￣□￣)⠀Yawning 9
˓˓˓ˇ̠̠̠⍥ˇ̠̠̠˒˒˒⠀Yawning 10
ヽ( ´O｀)ゞ⠀Yawning 11
ᕦ░ . ‾́ ◯ ‾́ . ░ᕤ⠀Yawning 12
ƪ(΄◞ิ۝◟ิ‵)ʃ⠀Yawning 13
ヾ(￣0￣； )ノ⠀Yawning 14
（◎´〇｀◎）⠀Yawning 15
《*´0｀》⠀Yawning 16
(*＇◎＇)⠀Yawning 17
（´○｀）～ゝ⠀Yawning 18
＼（´Ｏ｀）／⠀Yawning 19
( ੱ⋱口 ੱ⋱ )⠀Yawning 20
(_ _)ヾ(‘ロ‘)⠀Waking Someone Up 1
*ଘ( ॢᵕ꒶̮ᵕ(꒡ᵋ ꒡ღ)zZ‥⠀Waking Someone Up 2
ｰ(*ﾟﾛﾟ)-C＜*_ _)｡o○⠀Waking Someone Up 3
!!!!!(o≧o≦)○))ｏ(＿＿*)Ｚｚｚ⠀Waking Someone Up 4
!!!!!(o≧ω≦)○))ｏ(＿＿*)Ｚｚｚ⠀Waking Someone Up 5
!!!!!(o￣ω￣)○))ｏ(＿＿*)Ｚｚｚ⠀Waking Someone Up 6
ヾ(*￣O￣)ツ=====θ☆(o_ _)o)).o0○⠀Waking Someone Up 7
(+.+)(-.-)(_ _) ..zz⠀Falling Asleep or Waking Up 1
[▓▓]ᐖ) 三(۶ᐛ )۶⠀Falling Asleep or Waking Up 2
( ु́•̶̤ ‧̫ ⁃ ૂ̀ ).☽˚⁺⠀Falling Asleep or Waking Up 3
(๑ˊȫॢˋ)॰∘☼⠀Falling Asleep or Waking Up 4
ヾ(ｏ´Дゞｏ)｡o○⠀Falling Asleep or Waking Up 5
(´-εヾ )⠀Falling Asleep or Waking Up 6
（<´_ヘ<）⠀Falling Asleep or Waking Up 7
(P’_`)q+。⠀Falling Asleep or Waking Up 8
┤*￣Ｏ￣*├ ┤*－.－*├ ┤＿ ＿├⠀Falling Asleep or Waking Up 9
(:3 っ)3≡･◦∴*+◦º.+*.•。[][▓▓]⠀Dreaming, Astral Projection or some other Craziness 1
｡･*･:≡(:3 ) =͟͟͞͞ (¦3[▓▓]⠀Dreaming, Astral Projection or some other Craziness 2
⅀῍̩̖̬ ̎=͟͟͞͞=͟͟͞͞⁽◎͞˗̻̚=͟͟͞͞⁽◎͟˗̻̚ ͟͞=͟͟͞͞=͟͟͞͞=͟͟͞͞ (¦ꃩ[▓▓]⠀Dreaming, Astral Projection or some other Craziness 3
[▓▓]　☍(¦3ꇤ　꒱⠀Dreaming, Astral Projection or some other Craziness 4
꒰ ꒡⌓꒡꒱ᏩɵɵᎴ ɳɩɠɧ✟⠀Words 1
꒰´ ु-௰ू-॰`꒱⋆｡˚✩ɢ∞פ ɴⅈɢhт ༘*ೄ˚⠀Words 2
【☆swee< dream☆】(●ＵωU).zZZ⠀Words 3
(/-(ｴ)-＼)⠀Covering Your Eyes and or Face in Fear 1
( /)u(\ )⠀Covering Your Eyes and or Face in Fear 2
（*/∇＼*）⠀Covering Your Eyes and or Face in Fear 3
(*/ω＼*)⠀Covering Your Eyes and or Face in Fear 4
（／_＼）⠀Covering Your Eyes and or Face in Fear 5
（／．＼）⠀Covering Your Eyes and or Face in Fear 6
（/｡＼)⠀Covering Your Eyes and or Face in Fear 7
(／。＼)⠀Covering Your Eyes and or Face in Fear 8
(／(ｴ)＼)⠀Covering Your Eyes and or Face in Fear 9
(/ω＼)⠀Covering Your Eyes and or Face in Fear 10
(⊃‿⊂)⠀Covering Your Eyes and or Face in Fear 11
(ノдヽ)⠀Covering Your Eyes and or Face in Fear 12
(⊃д⊂)⠀Covering Your Eyes and or Face in Fear 13
(*/∇＼*)⠀Covering Your Eyes and or Face in Fear 14
(`･/д＼･)⠀Covering Your Eyes and or Face in Fear 15
◑.◑⠀Big Wide Open Eyes of Fear 1
( ⚆ _ ⚆ )⠀Big Wide Open Eyes of Fear 2
━(◯Δ◯∥)━ン⠀Big Wide Open Eyes of Fear 3
(　〇□〇）⠀Big Wide Open Eyes of Fear 4
(((φ(◎ロ◎<)φ)))⠀Big Wide Open Eyes of Fear 5
ゞ◎Д◎ヾ⠀Big Wide Open Eyes of Fear 6
（｀〇Д〇）⠀Big Wide Open Eyes of Fear 7
（ΟΔΟ；；）⠀Big Wide Open Eyes of Fear 8
(O∆O)⠀Big Wide Open Eyes of Fear 9
（　(≪●≫)　）Д（　(≪●≫)　）⠀Big Wide Open Eyes of Fear 10
ヽ(ﾟДﾟ)ﾉ⠀Scared Д Mouths 1
(((╹д╹<)))⠀Scared Д Mouths 2
(╬⁽⁽ ⁰ ⁾⁾ Д ⁽⁽ ⁰ ⁾⁾)⠀Scared Д Mouths 3
ヾ( •́д•̀ <)ﾉ⠀Scared Д Mouths 4
ヽ ( ꒪д꒪ )ﾉ⠀Scared Д Mouths 5
ヾ( ๑´д`๑)ﾂ⠀Scared Д Mouths 6
џ(ºДºџ)⠀Scared Д Mouths 7
( ⁰д⁰)⠀Scared Д Mouths 8
(ﾟДﾟ；)ゞ⠀Scared Д Mouths 9
－(゜Д゜<)-ン!⠀Scared Д Mouths 10
(ﾟДﾟ<)⠀Scared Д Mouths 11
(ﾟдﾟ；)⠀Scared Д Mouths 12
∠(ﾟДﾟ)/⠀Scared Д Mouths 13
‘`( ꒪Д꒪),､⠀Scared Д Mouths 14
(╬☉д⊙)⠀Scared Д Mouths 15
σ(ｏдｏ<<<)⠀Scared Д Mouths 16
(ﾟДﾟ?)⠀Scared Д Mouths 17
ヾ(´ﾟДﾟ｀<)ゝ⠀Scared Д Mouths 18
(#｀ﾟд´)ﾉ⠀Scared Д Mouths 19
゛(●ﾉ´・Д・｀)ﾉ⠀Scared Д Mouths 20
╰། ᵒ̌ д ᵒ̌ །╯⠀Scared Д Mouths 21
ヽ(○´Д｀)ﾉ⠀Scared Д Mouths 22
(゜Д゜*)⠀Scared Д Mouths 23
⊃゜Д゜）⊃⠀Scared Д Mouths 24
⊂（゜Д゜⊂⠀Scared Д Mouths 25
┗|*´ﾟДﾟ｀|┛⠀Scared Д Mouths 26
(ｼ<ﾟДﾟ)ｼ⠀Scared Д Mouths 27
ヾ(ﾟДﾟ<ヾ)⠀Scared Д Mouths 28
ヾ(<ﾟДﾟ<)ｼ⠀Scared Д Mouths 29
（ΩДΩ）⠀Scared Д Mouths 30
ヽ(#ﾟДﾟ)ﾉ⠀Scared Д Mouths 31
!!(ﾉ*ﾟДﾟ)ﾉ⠀Scared Д Mouths 32
,､’`( ꒪Д꒪),､’`’`,､⠀Scared Д Mouths 33
◝(๑⁺д⁺๑)◞՞⠀Scared Д Mouths 34
(⠀Scared Д Mouths 35
[emai<<#160<pro<ec<ed]⠀Scared Д Mouths 36
Д@)⠀Scared Д Mouths 37
(｢⊙Д⊙)｢⠀Scared Д Mouths 38
<<<<|๑⊙Д⊙|/⠀Scared Д Mouths 39
ლ|’Д’ლ|⠀Scared Д Mouths 40
（┛〃°　Д°）┛⠀Scared Д Mouths 41
ヽ〔ﾟДﾟ〕丿⠀Scared Д Mouths 42
)Д⊙`)⠀Scared Д Mouths 43
ฺ(☼Д☼)⠀Scared Д Mouths 44
工ｴｴｪｪ(<╹⌓╹)ｪｪｴｴ工⠀Surrounded by Fear 1
エｴｪｪｪ(●’Д’●)ｪｪｪｴエ⠀Surrounded by Fear 2
エエェェェェ（/×＼）ェェｴｴエエ⠀Surrounded by Fear 3
ε=ε=(っ*´□`)っ⠀Running Away in Fear 1
ε=ε=(怒ﾟДﾟ)ﾉ⠀Running Away in Fear 2
=͟͟͞͞ =͟͟͞͞ ﾍ( ´Д`)ﾉ⠀Running Away in Fear 3
ヽ(￣д￣<)ノ=3=3=3⠀Running Away in Fear 4
٩(´Д` <)۶:.*⠀Running Away in Fear 5
(´×д×`三꒪д꒪ <)⠀Running Away in Fear 6
– =͟͟͞͞ =͟͟͞͞ ﾍ( ´Д`)ﾉ⠀Running Away in Fear 7
ε＝ε＝ε＝(((((ﾉ｀･Д･)ﾉ⠀Running Away in Fear 8
(◞º❒º)◞₎₎(◟º❑º)◟⁾⁾➟➠➨⠀Running Away in Fear 9
ε=٩(●❛ö❛)۶⠀Running Away in Fear 10
Σ(ﾟДﾟ；≡；ﾟдﾟ)⠀Running Away in Fear 11
(c=(c=(c=(c=(ﾟﾛﾟ<c=⠀Running Away in Fear 12
⊂(ﾟДﾟ<⊂⌒`つ⠀Running Away in Fear 13
..･ヾ(。￣□￣)ﾂ⠀Running Away in Fear 14
≡≡≡=(ﾉTдT)ﾉ⠀Running Away in Fear 15
ε=ε=(⊃≧□≦)⊃⠀Running Away in Fear 16
!!Σ(ﾟДﾟ<≡≡≡≡≡ヾ(<ﾟдﾟ)/⠀Running Away in Fear 17
┃ ु ⠁⃘ ⠁⃘ू┃⁼³₌₃⠀Running Away in Fear 18
༻(〃ຶ⌂〃ຶ)⠀Running Away in Fear 19
ਭ३౽=͟͟͞͞(((ഽʻ⁸ʻ)ഽ⠀Running Away in Fear 20
ε=ε=ε=(ﾉ≧∀)ﾉ⠀Running Away in Fear 21
(❛ӧ❛三❛ӧ❛)⠀Running Away in Fear 22
Σ(°Д°；≡；°д°)⠀Running Away in Fear 23
ε=ε=ε=(ﾉTдT)ﾉ⠀Running Away in Fear 24
～ε～ε～┌(|||´Д｀)ノ⠀Running Away in Fear 25
゛(ﾉ~o~)ﾉ⠀Running Away in Fear 26
ε=ε=ε=┏(ﾟロﾟ<)┛⠀Running Away in Fear 27
ε==ε==(ﾉ゜д゜)ﾂ⠀Running Away in Fear 28
ヽ(д`ヽ)｡｡⠀Running Away in Fear 29
｡｡(ﾉ´д)ﾉ⠀Running Away in Fear 30
ヽ(´Д｀<≡<´Д｀)丿⠀Running Away in Fear 31
((ヽ(´Д`<ゞ=ヾ<´Д`)ﾉ))⠀Running Away in Fear 32
ヽ(ω；`ヽ))…((ﾉ´；ω)ﾉ⠀Running Away in Fear 33
ヽ(д｀ヽ彡ﾉ´д)ﾉ⠀Running Away in Fear 34
ε=ε=ε=(((怒ﾟДﾟ)ﾉﾉ⠀Running Away in Fear 35
ε=ε=ε=(*ﾉ´Д｀)ﾉﾟ⠀Running Away in Fear 36
ヾ(*゜、ω゜*)ﾉﾟ⠀Running Away in Fear 37
!!((((((っ<ﾟ∀ﾟ)っ⠀Running Away in Fear 38
へ( ʘ͡ ₒ ʘ͡ )╮/\╱\⠀Running Away in Fear 39
（（（（（（（（　゜□゜）ノ⠀Running Away in Fear 40
ヾ(･c_,･｡) ﾉ =з =з= з⠀Running Away in Fear 41
｡｡゛(ﾉ<><<<<<<)ﾉ⠀Running Away in Fear 42
ε≡Ξ≡Ξ≡ヽ( <￣〇￣)ﾉ⠀Running Away in Fear 43
ヽ(ﾟ□ﾟ＼*≡*／ﾟ□ﾟ)ﾉ⠀Running Away in Fear 44
ε＝（ﾉﾟдﾟ）ﾉ⠀Running Away in Fear 45
(＾ω＾ ≡ °д°)⠀Running Away in Fear 46
ヾ(((<ꈡ▱ꈡ<)))ﾉ⠀Running Away in Fear 47
✧.*(⌯ⅉॕੰૈ▱ⅉॕੰૈ)⠀Running Away in Fear 48
★⌒Ｙ⌒Ｙ⌒Ｙ⌒Ｙ⌒ ヾ(oﾟДﾟ)ﾉ⠀Running Away in Fear 49
へ(~Д~*へ))))… …((((ノ*~З~)ノ⠀Running Away in Fear 50
（´□｀；）=З=З=З=З=З=З⠀Running Away in Fear 51
(꒪ȏ꒪<)⠀Miscellaneous Fear 1
(˵¯͒ བ¯͒˵)⠀Miscellaneous Fear 2
ヽ(<ﾟ<∀<ﾟ< )ﾉ⠀Miscellaneous Fear 3
ヽ( <ﾟ<ж<ﾟ<)ﾉ⠀Miscellaneous Fear 4
y( ꒪◊꒪)y⠀Miscellaneous Fear 5
ヽ(≡ω≡<ヽ)⠀Miscellaneous Fear 6
(ﾉ<≡ω≡)ﾉ⠀Miscellaneous Fear 7
((ﾟ□ﾟ<))⠀Miscellaneous Fear 8
(●゜□゜)人(゜□゜○)⠀Miscellaneous Fear 9
§<ﾟﾛﾟ§⠀Miscellaneous Fear 10
(ノ´ロ`)ノ⠀Miscellaneous Fear 11
(ノ ゜口゜)ノ⠀Miscellaneous Fear 12
!!!!!!(ﾟﾛﾟ屮)屮⠀Miscellaneous Fear 13
ヾ(´囗｀｡)ﾉ⠀Miscellaneous Fear 14
(/<◇<)/⠀Miscellaneous Fear 15
ﾍ(<´o｀)ﾍ⠀Miscellaneous Fear 16
(°□°)⊅⠀Miscellaneous Fear 17
Σ(°□°)⊃⠀Miscellaneous Fear 18
…(ﾟⅩﾟ)…。⠀Miscellaneous Fear 19
(＠O＠<)⠀Miscellaneous Fear 20
〣( ºΔº )〣⠀Miscellaneous Fear 21
˓⁽͑ʺˀ́˙̻ˁ̀ʺ⁾̉ʾʾ ᵏᵞᵅ˞ᵎ⠀Words 1
=͟͟͞͞≠⌓̈⃝\ᵒᵐᵍ⠀Words 2
Ꮚˊ•⌔•ˋᏊ⠀Ꮚ Ꮚ Style Sheep 1
Ꮚᵒ̴̶̷ꈊ˂̤Ꮚ⠀Ꮚ Ꮚ Style Sheep 2
ᏊºัꈊºัᏊ⠀Ꮚ Ꮚ Style Sheep 3
Ꮚ˘̴͈́ꈊ˘̴͈̀Ꮚ⋆✩⠀Ꮚ Ꮚ Style Sheep 4
Ꮚᵒ̴̶̷ꈊᵒ̴̶̷Ꮚ⠀Ꮚ Ꮚ Style Sheep 5
Ꮚ¯ꈊ¯Ꮚ⠀Ꮚ Ꮚ Style Sheep 6
ᏊˊꍓˋᏊ⠀Ꮚ Ꮚ Style Sheep 7
Ꮚ꒵͒ꈊ꒵͒Ꮚ⠀Ꮚ Ꮚ Style Sheep 8
Ꮚ˃̶͈ꈊ˂̶͈Ꮚ⠀Ꮚ Ꮚ Style Sheep 9
Ꮚ˘ꈊ˘Ꮚ⠀Ꮚ Ꮚ Style Sheep 10
Ꮚ˘̩̩̩ꈊ˘̩̩̩Ꮚ⠀Ꮚ Ꮚ Style Sheep 11
ᏊʻัꈊʻัᏊ⠀Ꮚ Ꮚ Style Sheep 12
Ꮚ•ꈊ•Ꮚ⠀Ꮚ Ꮚ Style Sheep 13
Ꮚ°ꈊ°<Ꮚ⠀Ꮚ Ꮚ Style Sheep 14
Ꮚ☻̴̶̷̤ꈊ☻̴̶̷̤Ꮚ⠀Ꮚ Ꮚ Style Sheep 15
Ꮚ˘ꍓ˘Ꮚ⠀Ꮚ Ꮚ Style Sheep 16
ᏊꈍꈊꈍᏊ⠀Ꮚ Ꮚ Style Sheep 17
ᏊᵋꈊᵋᏊ⠀Ꮚ Ꮚ Style Sheep 18
Ꮚ❛ꈊ❛Ꮚ⠀Ꮚ Ꮚ Style Sheep 19
Ꮚ⌀֊̫⍉Ꮚ⠀Ꮚ Ꮚ Style Sheep 20
Ꮚᵔꈊ<#8217<Ꮚෆ⠀Ꮚ Ꮚ Style Sheep 21
Ꮚ•̀ꈊ•́Ꮚ⠀Ꮚ Ꮚ Style Sheep 22
Ꮚ^ꈊ^Ꮚ⠀Ꮚ Ꮚ Style Sheep 23
Ꮚ˟ꈊ˟Ꮚ⠀Ꮚ Ꮚ Style Sheep 24
Ꮚʻั֊̫ʻัᏊ⠀Ꮚ Ꮚ Style Sheep 25
Ꮚ˘̩̩̩ꍓ˘̩̩̩Ꮚ⠀Ꮚ Ꮚ Style Sheep 26
Ꮚ˃̶͈ ֊̫ ˂̶͈Ꮚ⠀Ꮚ Ꮚ Style Sheep 27
Ꮚ⁼ꈊ⁼Ꮚ⠀Ꮚ Ꮚ Style Sheep 28
ᏊˊꈊˋᏊ⠀Ꮚ Ꮚ Style Sheep 29
Ꮚ❛⃘ੌꈊ❛⃘ੌᏊ♡⠀Ꮚ Ꮚ Style Sheep 30
Ꮚ`ꈊ´Ꮚ⠀Ꮚ Ꮚ Style Sheep 31
ෆᏊᵔ֊̫ᵔᏊෆ⠀Ꮚ Ꮚ Style Sheep 32
Ꮚ˙ꈊ˙Ꮚ⠀Ꮚ Ꮚ Style Sheep 33
Ꮚˊ̥̥̥ꈊˋ̥̥ूᏊ⠀Ꮚ Ꮚ Style Sheep 34
Ꮚ°͈ꈊ°͈Ꮚ⠀Ꮚ Ꮚ Style Sheep 35
ᏊˊꈊˋᏊ⠀Ꮚ Ꮚ Style Sheep 36
Ꮚ<#8217<ꈊ<#8217<Ꮚ⠀Ꮚ Ꮚ Style Sheep 37
Ꮚ˃̶͈ꍓ˂̶͈Ꮚ⠀Ꮚ Ꮚ Style Sheep 38
Ꮚ｀ꈊ´Ꮚ⠀Ꮚ Ꮚ Style Sheep 39
Ꮚ⁰ꈊ⁰Ꮚ⠀Ꮚ Ꮚ Style Sheep 40
Ꮚ ்́ꈊ ்̀Ꮚ⠀Ꮚ Ꮚ Style Sheep 41
Ꮚ˃ꈊºัᏊ⠀Ꮚ Ꮚ Style Sheep 42
Ꮚᵕ̤ꈊᵕ̤Ꮚ⠀Ꮚ Ꮚ Style Sheep 43
ᏊᵕꈊᵕᏊ⠀Ꮚ Ꮚ Style Sheep 44
Ꮚ*ꈊ*Ꮚ⠀Ꮚ Ꮚ Style Sheep 45
Ꮚ⌀ꈊ⍉Ꮚ⠀Ꮚ Ꮚ Style Sheep 46
{ @θ ㅈ θ@ }⠀{@ @} Style Sheep 1
{ @ᵒ̴̶̷ꈊ˂̤@ }⠀{@ @} Style Sheep 2
{ @ºัꈊºั@ }⠀{@ @} Style Sheep 3
{ @˘̴͈́ꈊ˘̴͈̀@ }⋆✩⠀{@ @} Style Sheep 4
{ @ᵒ̴̶̷ꈊᵒ̴̶̷@ }⠀{@ @} Style Sheep 5
{ @¯ꈊ¯@ }⠀{@ @} Style Sheep 6
{ @ˊꍓˋ@ }⠀{@ @} Style Sheep 7
{ @꒵͒ꈊ꒵͒@ }⠀{@ @} Style Sheep 8
{ @˃̶͈ꈊ˂̶͈@ }⠀{@ @} Style Sheep 9
{ @˘ꈊ˘@ }⠀{@ @} Style Sheep 10
{ @˘̩̩̩ꈊ˘̩̩̩@ }⠀{@ @} Style Sheep 11
{ @ʻัꈊʻั@ }⠀{@ @} Style Sheep 12
{ @•ꈊ•@ }⠀{@ @} Style Sheep 13
{ @°ꈊ°<@ }⠀{@ @} Style Sheep 14
{ @☻̴̶̷̤ꈊ☻̴̶̷̤@ }⠀{@ @} Style Sheep 15
{ @˘ꍓ˘@ }⠀{@ @} Style Sheep 16
{ @ꈍꈊꈍ@ }⠀{@ @} Style Sheep 17
{ @ᵋꈊᵋ@ }⠀{@ @} Style Sheep 18
{ @❛ꈊ❛@ }⠀{@ @} Style Sheep 19
{ @⌀֊̫⍉@ }⠀{@ @} Style Sheep 20
{ @ᵔꈊ<#8217<@ }ෆ⠀{@ @} Style Sheep 21
{ @•̀ꈊ•́@ }⠀{@ @} Style Sheep 22
{ @^ꈊ^@ }⠀{@ @} Style Sheep 23
{ @˟ꈊ˟@ }⠀{@ @} Style Sheep 24
{ @ʻั֊̫ʻั@ }⠀{@ @} Style Sheep 25
{ @˘̩̩̩ꍓ˘̩̩̩@ }⠀{@ @} Style Sheep 26
{ @˃̶͈ ֊̫ ˂̶͈@ }⠀{@ @} Style Sheep 27
{ @⁼ꈊ⁼@ }⠀{@ @} Style Sheep 28
{ @ˊꈊˋ@ }⠀{@ @} Style Sheep 29
{ @❛⃘ੌꈊ❛⃘ੌ@ }♡⠀{@ @} Style Sheep 30
{ @`ꈊ´@ }⠀{@ @} Style Sheep 31
ෆ{ @ᵔ֊̫ᵔ@ }ෆ⠀{@ @} Style Sheep 32
{ @˙ꈊ˙@ }⠀{@ @} Style Sheep 33
{ @ˊ̥̥̥ꈊˋ̥̥ू@ }⠀{@ @} Style Sheep 34
{ @°͈ꈊ°͈@ }⠀{@ @} Style Sheep 35
{ @ˊꈊˋ@ }⠀{@ @} Style Sheep 36
{ @<#8217<ꈊ<#8217<@ }⠀{@ @} Style Sheep 37
{ @˃̶͈ꍓ˂̶͈@ }⠀{@ @} Style Sheep 38
{ @｀ꈊ´@ }⠀{@ @} Style Sheep 39
{ @⁰ꈊ⁰@ }⠀{@ @} Style Sheep 40
{ @ ்́ꈊ ்̀@ }⠀{@ @} Style Sheep 41
{ @˃ꈊºั@ }⠀{@ @} Style Sheep 42
{ @ᵕ̤ꈊᵕ̤@ }⠀{@ @} Style Sheep 43
{ @ᵕꈊᵕ@ }⠀{@ @} Style Sheep 44
{ @*ꈊ*@ }⠀{@ @} Style Sheep 45
{ @⌀ꈊ⍉@ }⠀{@ @} Style Sheep 46
(n˘v˘•)¬⠀Oh You! 1
(ง ◕ั⌑◕ั)ว ⁾⠀Oh You! 2
₍₍ (ง Ŏ౪Ŏ)ว ⁾⁾⠀Oh You! 3
(ง ´͈౪`͈)ว⠀Oh You! 4
ᕕ╏ ͡ ▾ ͡ ╏┐⠀Oh You! 5
(ﾍﾟ◇ﾟ)」⠀Oh You! 6
ᕕ[ ́ ل͜ ́ ]੭⠀Oh You! 7
₍₍ (ง ˙ω˙)ว ⁾⁾⠀Oh You! 8
(*´_ゝ｀)⠀Blushing Cheeks with an Asterisk 1
(*´∀`*)⠀Blushing Cheeks with an Asterisk 2
(*´ｪ｀*)⠀Blushing Cheeks with an Asterisk 3
｡(*^▽^*)ゞ⠀Blushing Cheeks with an Asterisk 4
(‘-’*)⠀Blushing Cheeks with an Asterisk 5
(*´∀`*)⠀Blushing Cheeks with an Asterisk 6
(*^^*)⠀Blushing Cheeks with an Asterisk 7
(*ﾟｰﾟ)ゞ⠀Blushing Cheeks with an Asterisk 8
(ノ*゜▽゜*)⠀Blushing Cheeks with an Asterisk 9
ฅ(*°ω°*ฅ)⠀Blushing Cheeks with an Asterisk 10
(*ﾟ∀ﾟ*)⠀Blushing Cheeks with an Asterisk 11
(*´ω｀*)⠀Blushing Cheeks with an Asterisk 12
(´ω｀*)⠀Blushing Cheeks with an Asterisk 13
(⁎❝᷀ົ ˙̫ ❝᷀ົ⁎)⠀Blushing Cheeks with an Asterisk 14
ε=ε=ε=ε=ε” “(/*’-‘*)/⠀Blushing Cheeks with an Asterisk 15
ヽ(＊<><<∇<<<<)ﾉ⠀Blushing Cheeks with an Asterisk 16
(*´-｀*)⠀Blushing Cheeks with an Asterisk 17
( *’ω’* )⠀Blushing Cheeks with an Asterisk 18
( *∵* )⠀Blushing Cheeks with an Asterisk 19
*:ﾟ*｡⋆ฺ(*´◡`)⠀Blushing Cheeks with an Asterisk 20
(#^.^#)⠀Blushing Cheeks with a # 1
(#｀ε´# )ゞ⠀Blushing Cheeks with a # 2
(＃⌒∇⌒＃)ゞ⠀Blushing Cheeks with a # 3
꒰⌗´͈ ᵕ ॣ`͈⌗꒱৩⠀Blushing Cheeks with a # 4
(#ﾟﾛﾟ#)⠀Blushing Cheeks with a # 5
꒰#’ω`#꒱੭⠀Blushing Cheeks with a # 6
(#^^#)ゞ⠀Blushing Cheeks with a # 7
(๑•́ ω •̀๑)⠀Blushing Cheeks with a ๑ 1
⁝(๑⑈௰⑈)◞⁝˚º꒰꒱⠀Blushing Cheeks with a ๑ 2
(๑•́ ₃ •̀๑)⠀Blushing Cheeks with a ๑ 3
(๑ˊ▵ॢˋ̥๑)⠀Blushing Cheeks with a ๑ 4
(๑´ㅂ`๑)⠀Blushing Cheeks with a ๑ 5
(๑ゝω╹๑)⠀Blushing Cheeks with a ๑ 6
(´๑•_•๑)⠀Blushing Cheeks with a ๑ 7
(๑•́ω•̀๑)⠀Blushing Cheeks with a ๑ 8
(๑⃙⃘·́ω·̀๑⃙⃘)੨⠀Blushing Cheeks with a ๑ 9
(◞ ๑⑈௰⑈)⠀Blushing Cheeks with a ๑ 10
(๑´ω`๑)⠀Blushing Cheeks with a ๑ 11
(๑癶ω癶๑)⠀Blushing Cheeks with a ๑ 12
(´•ω•`๑)⠀Blushing Cheeks with a ๑ 13
(๑´•ω • `๑)⠀Blushing Cheeks with a ๑ 14
(_๑˘ㅂ˘๑)⠀Blushing Cheeks with a ๑ 15
(๑´⍢`๑)⠀Blushing Cheeks with a ๑ 16
(๑′°︿°๑)⠀Blushing Cheeks with a ๑ 17
(๑́•∀•๑̀)ฅ⠀Blushing Cheeks with a ๑ 18
(๑ּగ⌄ּగ๑)⠀Blushing Cheeks with a ๑ 19
(⁶ੌ௰⁶ੌ๑)⠀Blushing Cheeks with a ๑ 20
(๑꒪̇⌄꒪̇๑)⠀Blushing Cheeks with a ๑ 21
(๑꒪⍘꒪๑)⠀Blushing Cheeks with a ๑ 22
(๑⁍᷄౪⁍᷅๑)⠀Blushing Cheeks with a ๑ 23
Σ(๑꒪⃙⃚᷄ꑣ꒪⃚⃙᷅๑۶)۶⠀Blushing Cheeks with a ๑ 24
(๑￫‿￩๑)⠀Blushing Cheeks with a ๑ 25
(๑•́‧̫•̀๑)⠀Blushing Cheeks with a ๑ 26
(๑･▱･๑)⠀Blushing Cheeks with a ๑ 27
(〃￣ω￣〃)ゞ⠀Flushed Cheeks with Vertical and Sometimes Slightly Diagonal Lines 1
(｡・//ε//・｡)⠀Flushed Cheeks with Vertical and Sometimes Slightly Diagonal Lines 2
（//･_･//)⠀Flushed Cheeks with Vertical and Sometimes Slightly Diagonal Lines 3
（〃・ω・〃）⠀Flushed Cheeks with Vertical and Sometimes Slightly Diagonal Lines 4
(〃▽〃)⠀Flushed Cheeks with Vertical and Sometimes Slightly Diagonal Lines 5
(///Σ///)⠀Flushed Cheeks with Vertical and Sometimes Slightly Diagonal Lines 6
(//∇//)⠀Flushed Cheeks with Vertical and Sometimes Slightly Diagonal Lines 7
(灬ºωº灬)⠀Flushed Cheeks with Vertical and Sometimes Slightly Diagonal Lines 8
(´,,•ω•,,)⠀Flushed Cheeks with Vertical and Sometimes Slightly Diagonal Lines 9
(⁄ ⁄•⁄ω⁄•⁄ ⁄)⁄⠀Flushed Cheeks with Vertical and Sometimes Slightly Diagonal Lines 10
(灬º 艸º灬)⠀Flushed Cheeks with Vertical and Sometimes Slightly Diagonal Lines 11
(✿ꈍ。 ꈍ✿)⠀Flushed Cheeks with Vertical and Sometimes Slightly Diagonal Lines 12
(⁄ ⁄^⁄ᗨ⁄^⁄ ⁄)⠀Flushed Cheeks with Vertical and Sometimes Slightly Diagonal Lines 13
(⸝⸝⸝ ≧ㅿ＼⸝⸝⸝)/⠀Flushed Cheeks with Vertical and Sometimes Slightly Diagonal Lines 14
⁽⁽ ◟(灬 ˊωˋ 灬)◞ ⁾⁾⠀Flushed Cheeks with Vertical and Sometimes Slightly Diagonal Lines 15
╰(⸝⸝⸝´꒳`⸝⸝⸝)╯⠀Flushed Cheeks with Vertical and Sometimes Slightly Diagonal Lines 16
(ؑ‷ᵕؑ̇‷)◞✧⠀Flushed Cheeks with Vertical and Sometimes Slightly Diagonal Lines 17
{•̴͈ ˔̇ •̴͈}⠀Flushed Cheeks with Vertical and Sometimes Slightly Diagonal Lines 18
ლ(///´◜⊜｀//////ლ)⠀Flushed Cheeks with Vertical and Sometimes Slightly Diagonal Lines 19
(⸝⸝⍢⸝⸝) ෆ⠀Flushed Cheeks with Vertical and Sometimes Slightly Diagonal Lines 20
⁄(⁄ ⁄ˊૢ⁄ ⌑ ⁄ˋૢ⁄ ⁄)⁄⠀Flushed Cheeks with Vertical and Sometimes Slightly Diagonal Lines 21
˚✧₊⁎˓˓⁽̨̡ ˚͈́꒳​˚͈̀*⁾̧̢˒˒⁎⁺˳✧༚⠀Flushed Cheeks with Vertical and Sometimes Slightly Diagonal Lines 22
(⺣◡⺣)♡*⠀Flushed Cheeks with Vertical and Sometimes Slightly Diagonal Lines 23
( ̧⸝⸝⍢⸝⸝)ི⠀Flushed Cheeks with Vertical and Sometimes Slightly Diagonal Lines 24
꒰ •͈́ ̫ •͈̀ ꒱ˉ̞̭⠀Flushed Cheeks with Vertical and Sometimes Slightly Diagonal Lines 25
(*ꈍ꒳ꈍ*)⠀Flushed Cheeks with Vertical and Sometimes Slightly Diagonal Lines 26
(*ꈍ꒙ꈍ*)⠀Flushed Cheeks with Vertical and Sometimes Slightly Diagonal Lines 27
ค{•̴͈ ˳̇ •̴͈}ค✧⠀Flushed Cheeks with Vertical and Sometimes Slightly Diagonal Lines 28
⁄(⁄ ⁄•⁄-⁄•⁄ ⁄)⁄⠀Flushed Cheeks with Vertical and Sometimes Slightly Diagonal Lines 29
(∗∕ ∕•̥̥̥̥∕ω∕•̥̥̥̥∕)⠀Flushed Cheeks with Vertical and Sometimes Slightly Diagonal Lines 30
(⸝⸝•́દ•̀⸝⸝)⠀Flushed Cheeks with Vertical and Sometimes Slightly Diagonal Lines 31
ꈍ .̮ ꈍ⠀Flushed Cheeks with Vertical and Sometimes Slightly Diagonal Lines 32
・:*(〃・ｪ・〃人)*:・⠀Flushed Cheeks with Vertical and Sometimes Slightly Diagonal Lines 33
⁄(⁄ ⁄•⁄ω⁄•⁄ ⁄)⁄⠀Flushed Cheeks with Vertical and Sometimes Slightly Diagonal Lines 34
(ृ°͈꒳​°͈ ृ)ु⠀Flushed Cheeks with Vertical and Sometimes Slightly Diagonal Lines 35
⁽͑ʺˊ˙̫ˋʺ⁾̉⠀Flushed Cheeks with Vertical and Sometimes Slightly Diagonal Lines 36
(˵¯͒⌄¯͒˵)⠀Flushed Cheeks with Vertical and Sometimes Slightly Diagonal Lines 37
⊂((〃’⊥’〃))⊃⠀Flushed Cheeks with Vertical and Sometimes Slightly Diagonal Lines 38
(灬╹ω╹灬)⠀Flushed Cheeks with Vertical and Sometimes Slightly Diagonal Lines 39
(〃ω〃)⠀Flushed Cheeks with Vertical and Sometimes Slightly Diagonal Lines 40
(〃´Å｀〃)⠀Flushed Cheeks with Vertical and Sometimes Slightly Diagonal Lines 41
ヾ( 〃ω〃)ｯ⠀Flushed Cheeks with Vertical and Sometimes Slightly Diagonal Lines 42
(･ω･`〃)⠀Flushed Cheeks with Vertical and Sometimes Slightly Diagonal Lines 43
ヾ(〃ω〃ヾ))⠀Flushed Cheeks with Vertical and Sometimes Slightly Diagonal Lines 44
((ﾉ〃ω〃)ﾉﾞ⠀Flushed Cheeks with Vertical and Sometimes Slightly Diagonal Lines 45
ヽ(〃v〃)ﾉ⠀Flushed Cheeks with Vertical and Sometimes Slightly Diagonal Lines 46
(〃´ﾉω`〃)⠀Flushed Cheeks with Vertical and Sometimes Slightly Diagonal Lines 47
<<<<(〃´∀｀〃)<><<⠀Flushed Cheeks with Vertical and Sometimes Slightly Diagonal Lines 48
・:*(〃∇〃人)*:・⠀Flushed Cheeks with Vertical and Sometimes Slightly Diagonal Lines 49
(〃・ω・〃)ノ~☆⠀Flushed Cheeks with Vertical and Sometimes Slightly Diagonal Lines 50
୧( ˵ ° ~ ° ˵ )୨⠀Flushed Cheeks with Vertical and Sometimes Slightly Diagonal Lines 51
（˶′◡‵˶）⠀Flushed Cheeks with Vertical and Sometimes Slightly Diagonal Lines 52
o(〃’▽’〃)o⠀Flushed Cheeks with Vertical and Sometimes Slightly Diagonal Lines 53
(〃´∀｀)⠀Flushed Cheeks with Vertical and Sometimes Slightly Diagonal Lines 54
(∥￣■￣∥)⠀Flushed Cheeks with Vertical and Sometimes Slightly Diagonal Lines 55
ヾ(〃ﾟーﾟ〃)ノ⠀Flushed Cheeks with Vertical and Sometimes Slightly Diagonal Lines 56
( 〃．．)⠀Flushed Cheeks with Vertical and Sometimes Slightly Diagonal Lines 57
(´,,•ω•,,｀)⠀Flushed Cheeks with Vertical and Sometimes Slightly Diagonal Lines 58
⁽˚̌ʷ˚̌ʺ⁾⠀Flushed Cheeks with Vertical and Sometimes Slightly Diagonal Lines 59
ｰ(°◇°〃)⠀Flushed Cheeks with Vertical and Sometimes Slightly Diagonal Lines 60
(●///▽///●)⠀Flushed Cheeks with Vertical and Sometimes Slightly Diagonal Lines 61
б(//x//)⠀Flushed Cheeks with Vertical and Sometimes Slightly Diagonal Lines 62
(灬ºωº灬)♡⠀Flushed Cheeks with Vertical and Sometimes Slightly Diagonal Lines 63
ο(‘・’〃)ο″⠀Flushed Cheeks with Vertical and Sometimes Slightly Diagonal Lines 64
（。-＿-。）⠀Circles for Cheeks 1
(｡･･｡)⠀Circles for Cheeks 2
(o・・o)/⠀Circles for Cheeks 3
(●ฅ́дฅ̀●)⠀Circles for Cheeks 4
( 。•_• 。)⠀Circles for Cheeks 5
(●˙꒳˙●)⠀Circles for Cheeks 6
(●°u°●)​ 」⠀Circles for Cheeks 7
(｡uωu｡)⠀Circles for Cheeks 8
ღ✉ღ•̥̑ .̮ •̥̑)⠀Circles for Cheeks 9
(o´∪｀o)⠀Circles for Cheeks 10
|´∀｀●)⠀Circles for Cheeks 11
（＠´＿｀＠）⠀Miscellaneous Cheeks 1
(。≖ˇ∀ˇ≖。)⠀Miscellaneous Cheeks 2
(∗ᵕ̴᷄◡ᵕ̴᷅∗)՞⠀Miscellaneous Cheeks 3
ల(*´= ◡ =｀*)⠀Miscellaneous Cheeks 4
▓⚗_⚗▓⠀Miscellaneous Cheeks 5
(w´ω｀w)⠀Miscellaneous Cheeks 6
((≡ຶ◡≡ຶ))⠀Miscellaneous Cheeks 7
(⊙﹏⊙✿)⠀Shy but not Blushing 1
⸜(ᶿ᷇ധᶿ᷆)⸝⠀Shy but not Blushing 2
( ͒•·̫|⠀Shy but not Blushing 3
( ´•௰•`)⠀Shy but not Blushing 4
(´°ω°`)⠀Shy but not Blushing 5
*⁂((✪⥎✪))⁂*⠀Shy but not Blushing 6
( ͒ ́ඉ .̫ ඉ ̀ ͒)⠀Shy but not Blushing 7
(◍´ಲ`◍)⠀Shy but not Blushing 8
(◍ ´꒳` ◍)b⠀Shy but not Blushing 9
(ˊˡ·̫ˡˋ)⠀Shy but not Blushing 10
(⌯꒪͒ ૢ౪ ૢ꒪͒)⠀Shy but not Blushing 11
(´ . .̫ . `)⠀Shy but not Blushing 12
˄̩̞(˒௰˓)⠀Shy but not Blushing 13
ԅ[ •́ ﹏ •̀ ]و⠀Shy but not Blushing 14
ԅ[ •́ ﹏├┬┴┬┴⠀Shy but not Blushing 15
(⌒_⌒<)⠀A Drop of Sweat 1
(<ﾞ°´ω°´)⠀A Drop of Sweat 2
(^_^<)⠀A Drop of Sweat 3
(^^<)⠀A Drop of Sweat 4
（；^ω^）⠀A Drop of Sweat 5
(^◇^；)⠀A Drop of Sweat 6
(ヾ<￣▽￣)ヾ⠀A Drop of Sweat 7
( /)u(\ )⠀Covering Your Face Because of Shyness 1
（*/∇＼*）⠀Covering Your Face Because of Shyness 2
(*/ω＼*)⠀Covering Your Face Because of Shyness 3
(*ﾉ▽ﾉ)⠀Covering Your Face Because of Shyness 4
(*ﾉωﾉ)⠀Covering Your Face Because of Shyness 5
（/｡＼)⠀Covering Your Face Because of Shyness 6
(／(ｴ)＼)⠀Covering Your Face Because of Shyness 7
(/□＼*)・゜⠀Covering Your Face Because of Shyness 8
(/ω＼)⠀Covering Your Face Because of Shyness 9
(#／。＼#)⠀Covering Your Face Because of Shyness 10
(╯_╰)⠀Covering Your Face Because of Shyness 11
(╯ಊ╰)⠀Covering Your Face Because of Shyness 12
(つω⊂* )⠀Covering Your Face Because of Shyness 13
(ﾉ)´∀｀(ヾ)⠀Covering Your Face Because of Shyness 14
(ʃᵕ̩̩ ᵕ̩̩⑅)⠀Covering Your Face Because of Shyness 15
(♡´艸`)⠀Covering Your Face Because of Shyness 16
(´つヮ⊂)⠀Covering Your Face Because of Shyness 17
(Ŏ艸Ŏ)⠀Covering Your Face Because of Shyness 18
(／▽￣)／⠀Covering Your Face Because of Shyness 19
(／≧ω＼)⠀Covering Your Face Because of Shyness 20
(*/∇＼*)⠀Covering Your Face Because of Shyness 21
ʕ*ﾉᴥﾉʔ⠀Covering Your Face Because of Shyness 22
( *´ﾉｪ`)⠀Covering Your Face Because of Shyness 23
(ﾉ∀｀●)⊃⠀Covering Your Face Because of Shyness 24
⊂((〃/⊥＼〃))⊃⠀Covering Your Face Because of Shyness 25
(/へ＼*)⠀Covering Your Face Because of Shyness 26
(ﾉ∇≦*)⠀Covering Your Face Because of Shyness 27
(〃ﾉωﾉ)⠀Covering Your Face Because of Shyness 28
(〃ﾉ∀｀〃)⠀Covering Your Face Because of Shyness 29
(ﾉ∀＼*)⠀Covering Your Face Because of Shyness 30
(*ﾉωヾ*)⠀Covering Your Face Because of Shyness 31
(*ﾉзﾉ*)⠀Covering Your Face Because of Shyness 32
♡(｡￫ˇ艸￩)⠀Covering Your Face Because of Shyness 33
（＊ノ∀｀＊）ノ⠀Covering Your Face Because of Shyness 34
(ノ∀￣〃)⠀Covering Your Face Because of Shyness 35
(*/▽＼*)⠀Covering Your Face Because of Shyness 36
(*´ﾉ∀｀)⠀Covering Your Face Because of Shyness 37
.ﾟ:<｡+。ε(ﾉ∀≦*)з｡+.｡ﾟ:⠀Covering Your Face Because of Shyness 38
(´•͈ुω•͈ू`)⠀Complex Shyness 1
( ੭⌯᷄௰⌯᷅ ू’<|)⠀Complex Shyness 2
|₋ॢọ̶̶̷̥᷅๑)‧˚⁺⠀Complex Shyness 3
(๑ᵉ̷͈◡ॢᵉ̷͈๑)Üfu♡⠀Complex Shyness 4
(⑉ ॢ• • ॢ⑉)⠀Complex Shyness 5
⁄(⁄⑅ॢ⁄˃̶͈̀⁄௰⁄˂̶͈́⁄⑅ॢ⁄)⁄⠀Complex Shyness 6
ू(ʚ̴̶̷́ .̠ ʚ̴̶̷̥̀ ू)⠀Complex Shyness 7
꒰ີᵒ̴̶̷͈́༝ॢᵒ̴̶̷͈̀ ૢ꒱ ິ⠀Complex Shyness 8
‾̠̠̠̠̠̠̠̄| ॣ•͈̀๑)⠀Complex Shyness 9
(*,,ºัωºั,,)⠀Complex Shyness 10
( ︠ु ௰︡ू)⠀Complex Shyness 11
(ˊσ̴̶̷̤ ₋̮̑ σ̴̶̷̤ˋ)₊ෆ⃛⁺˚⠀Complex Shyness 12
(⁎ ́ఊ ̫ఊ̀⁎)⠀Complex Shyness 13
·◌̊ˈ* (⁰̶̶̷ॢ ˙̶̮ ू⁰̴̷̷๑).°◌̊⠀Complex Shyness 14
(๑˘ु⑅ू˘๑)*✲ﾟ*｡⋆⠀Complex Shyness 15
亝˓˓( ª̷̛ॢ₎௰₍ª̷̛ॢ )˒˒亝⠀Complex Shyness 16
(ृ ु ´͈ ᵕ `͈ )ु⠀Complex Shyness 17
(ृ ´͈ ᵕ `͈ ृ )ु⠀Complex Shyness 18
•ू(ᵒ̴̶̷᷄ωᵒ̴̶̷᷅*•ू) )੭ु⁾⁾⠀Complex Shyness 19
ෆ⃛(ٛ⌯ॢ˃ ɪ ˂ٛ⌯ॢ)⠀Complex Shyness 20
(•́ ॣ·̫ ॣ•̀,)՞⠀Complex Shyness 21
‹(⁽˙́ʷ˙̀⁾ )∨( ⁽˙́ʷ˙̀⁾)›⠀Multiple People Being Shy 1
(v〃∇〃)ﾊ(〃∇〃v)⠀Multiple People Being Shy 2
(v〃ω〃)八(〃ω〃v)⠀Multiple People Being Shy 3
(v〃∇〃)ハ(〃∇〃v)⠀Multiple People Being Shy 4
( ￣з(〃´▽｀〃)ε￣ )⠀Multiple People Being Shy 5
◌⑅⃝*॰ॱᒄᵒᵏⁱ(꜆˘͈ෆ˘͈꜀)ᒄᵒᵏⁱ◌⑅⃝*॰ॱ⠀Shyness and Words 1
(⑅ᵒ̴̶̷᷄ωᵒ̴̶̷᷅⊞ོॢ)fෆr yෆu⋆*⋆✩⠀Shyness and Words 2
⁽͑ˀˉ˙̫ˉˁ⁾̉ ᵐᵘⁿⁱ⠀Shyness and Words 3
￡ονё Υου…..φ(〃∇〃 ))⠀Shyness and Words 4
(´〜｀*) zzz⠀Regular Sleeping or Sleepy Kaomojis 1
(-_-) zzz⠀Regular Sleeping or Sleepy Kaomojis 2
(-, – )…zzzZZZ⠀Regular Sleeping or Sleepy Kaomojis 3
(-ｪ-)｡o⠀Regular Sleeping or Sleepy Kaomojis 4
(。-ω-)zzz⠀Regular Sleeping or Sleepy Kaomojis 5
(*-ω-)⠀Regular Sleeping or Sleepy Kaomojis 6
(´～`)⠀Regular Sleeping or Sleepy Kaomojis 7
(∪｡∪)｡｡｡zzz⠀Regular Sleeping or Sleepy Kaomojis 8
(ᴗ˳ᴗ)⠀Regular Sleeping or Sleepy Kaomojis 9
(ᵕ≀ ̠ᵕ )⠀Regular Sleeping or Sleepy Kaomojis 10
［(－－)］zzz⠀Regular Sleeping or Sleepy Kaomojis 11
ε-(´・｀)⠀Regular Sleeping or Sleepy Kaomojis 12
Σ(￣。￣ノ)ノ⠀Regular Sleeping or Sleepy Kaomojis 13
✾꒡ .̮ ꒡✾⠀Regular Sleeping or Sleepy Kaomojis 14
(≚ᄌ≚)ƶƵ⠀Regular Sleeping or Sleepy Kaomojis 15
( ु⁎ᴗ_ᴗ⁎)ु.｡oO⠀Regular Sleeping or Sleepy Kaomojis 16
(-ι_- )))。。。⠀Regular Sleeping or Sleepy Kaomojis 17
(⌯͒ᵕɪᵕ⌯͒)zzZ⠀Regular Sleeping or Sleepy Kaomojis 18
꒰◍ᐡᐤᐡ◍꒱⠀Regular Sleeping or Sleepy Kaomojis 19
_(-ω-`_)⠀Regular Sleeping or Sleepy Kaomojis 20
( ⓥωⓥ)⠀Regular Sleeping or Sleepy Kaomojis 21
(｡･ˇ_ˇ･｡)⠀Regular Sleeping or Sleepy Kaomojis 22
(´-_ゝ-`)⠀Regular Sleeping or Sleepy Kaomojis 23
.꒰ϱ﹏-๑꒱‧*Zz｡⠀Regular Sleeping or Sleepy Kaomojis 24
(๑ᵕ⌓ᵕ̤)⠀Regular Sleeping or Sleepy Kaomojis 25
(- o – ) zzZ⠀Regular Sleeping or Sleepy Kaomojis 26
⁽⁽(ᵕ≀ ̠ᵕ ) ⋏º¬͜ Ɩ།⠀Regular Sleeping or Sleepy Kaomojis 27
꒰◍ᐡᐤᐡ◍꒱ᐝ.∗̥✩⁺˚⑅⠀Regular Sleeping or Sleepy Kaomojis 28
[(－－)]..zzZ⠀Regular Sleeping or Sleepy Kaomojis 29
(✿◡‿◡ฺ)zzz⠀Regular Sleeping or Sleepy Kaomojis 30
(｡v_v｡)⠀Regular Sleeping or Sleepy Kaomojis 31
川｡μ_μ)σ⠀Regular Sleeping or Sleepy Kaomojis 32
(︶｡︶✽)⠀Regular Sleeping or Sleepy Kaomojis 33
(ृ ु⁎ᴗᵨᴗ⁎)ु.zZ⠀Regular Sleeping or Sleepy Kaomojis 34
⎰≀.⺤_⺤≀⎰⠀Regular Sleeping or Sleepy Kaomojis 35
(｡´-д-)⠀Regular Sleeping or Sleepy Kaomojis 36
(﹡ꑓ ︿ ꑓ`﹡)⠀Regular Sleeping or Sleepy Kaomojis 37
|[(*´ｪ`)]|zZＺ⠀Regular Sleeping or Sleepy Kaomojis 38
(｡し_し｡)⠀Regular Sleeping or Sleepy Kaomojis 39
( ु⁎ᴗᵨᴗ⁎)ु.zZ⠀Regular Sleeping or Sleepy Kaomojis 40
_(⌒( ु`ω、) ु zzZz⠀Regular Sleeping or Sleepy Kaomojis 41
(　-益-)｡｡oＯ　ＺＺＺＺＺＺＺ⠀Regular Sleeping or Sleepy Kaomojis 42
＿ﾉ乙(､ﾝ､)_⠀Laying Down on Your Side 1
_(：3 」∠ )_⠀Laying Down on Your Side 2
_(┐「ε:)_⠀Laying Down on Your Side 3
【:εω⠀Laying Down on Your Side 4
(冫༵、)⠀Laying Down on Your Side 5
_:(‘Θ’ 」 ∠):_⠀Laying Down on Your Side 6
_:(´ཀ`」 ∠):_ …⠀Laying Down on Your Side 7
_( :⁍ 」 )_⠀Laying Down on Your Side 8
८(冫༙、)৲˒˒⠀Laying Down on Your Side 9
(ृ ᐛ ृ )ु⠀Laying Down on Your Side 10
_(」∠ ､ﾝ､)_⠀Laying Down on Your Side 11
_(┐「ε:)_♡⠀Laying Down on Your Side 12
_(°ω°｣ ∠)_⠀Laying Down on Your Side 13
_(ˇωˇ」∠)_⠀Laying Down on Your Side 14
_/￣|(冫、)-c⠀Laying Down on Your Side 15
– =͟͟͞͞ (¦3[▓▓])⠀Sleeping in an Actual Bed 1
▓▓ ु‹:) ु⠀Sleeping in an Actual Bed 2
(¦3ꇤ[▓▓]⠀Sleeping in an Actual Bed 3
˓(¦:ɝ[▓▓]⠀Sleeping in an Actual Bed 4
ꏂ[▓] ृ⑆)˚º꒰꒱⠀Sleeping in an Actual Bed 5
(˴́³[▒]꒱⌕˚º꒰…꒱⠀Sleeping in an Actual Bed 6
ᓬᗸᗳ[▓▓]ꍞ⠀Sleeping in an Actual Bed 7
(¦:ɜ[▓▓]⌕⁷̩ ̊⠀Sleeping in an Actual Bed 8
(»:ɜ[▒▒]˚º꒰꒱⠀Sleeping in an Actual Bed 9
(ː:̣̣̣̥з[▓▓]˚º꒰꒱⠀Sleeping in an Actual Bed 10
⁝(¦ꌲɜ[▓▓]⁝ ˚º꒰꒱⠀Sleeping in an Actual Bed 11
(:˒[￣]⠀Sleeping in an Actual Bed 12
[▒▒]ꇤꒊ¦`)ꍞ⠀Sleeping in an Actual Bed 13
⌈▒͟⌉ꅼ)ꍞ⠀Sleeping in an Actual Bed 14
(¦ꄰ[▓▓]⠀Sleeping in an Actual Bed 15
(¦ꃆ[▓▓]⠀Sleeping in an Actual Bed 16
˓˓(¦:ɝ[▓▓]⠀Sleeping in an Actual Bed 17
(¦ꎌ[▓▓]⠀Sleeping in an Actual Bed 18
(¦ꃎ[▓▓]⠀Sleeping in an Actual Bed 19
(¦ꃩ[▓▓]⠀Sleeping in an Actual Bed 20
(¦ꀝ[▓▓]⠀Sleeping in an Actual Bed 21
⌈▓͟⌉ꆟ)ꍞ⠀Sleeping in an Actual Bed 22
(¦ꀦ[▓▓]⠀Sleeping in an Actual Bed 23
(:ɜ[▒]꒱˚º꒰꒱⠀Sleeping in an Actual Bed 24
(¦ꒉ[▓▓]⠀Sleeping in an Actual Bed 25
(:3ꇤ[▓▓]ε¦)⠀Sleeping in an Actual Bed 26
(˴́³[▒]꒱⌕˚º꒰…꒱⠀Sleeping in an Actual Bed 27
(ृ·́௰·̀ू[▓▒▓]˒˒˚º꒰꒱⠀Sleeping in an Actual Bed 28
ﾘृ(·́௰·̀ू[▓▒▓]˒˒˚º꒰꒱⠀Sleeping in an Actual Bed 29
⋆｡˚ (¦3ꇤ[▓▓]⋆｡˚✩⠀Sleeping in an Actual Bed 30
– =͟͟͞͞ =͟͟͞͞(¦3[=͟͟͞͞__]=͟͟͞͞=͟͟͞͞ =͟͟͞͞)⠀Sleeping in an Actual Bed 31
⌒((:з)⌒((ε:)⌒((:3[___]=-3⠀Sleeping in an Actual Bed 32
[▓▒▓] ु‹:) ु˒˒✯*･☪:.｡⠀Sleeping in an Actual Bed 33
(:3[▓▓▓▓▓▓▓▓]⠀Sleeping in an Actual Bed 34
( -_-)<><<c[_]⠀Coffee 1
{zzz}°°°( -_-)<><<c[_]⠀Coffee 2
(。-ω-)<><<c[_]⠀Coffee 3
(*-ω-)<><<c[_]⠀Coffee 4
(ᴗ˳ᴗ)<><<c[_]⠀Coffee 5
(๑ᵕ⌓ᵕ̤)<><<c[_]⠀Coffee 6
(｡´-д-)<><<c[_]⠀Coffee 7
(﹡ꑓ ︿ ꑓ`﹡)<><<c[_]⠀Coffee 8
(｡v_v｡)<><<c[_]⠀Coffee 9
川｡μ_μ)σc[_]⠀Coffee 10
(ι´Д｀)ﾉ⠀Stretching 1
ᕙ(⇀‸↼‶)ᕗ⠀Stretching 2
₍₍ ᕕ( ･᷄ὢ･᷅ )ᕗ⁾⁾⠀Stretching 3
₍₍ ᕕ(´ ω` )ᕗ⁾⁾⠀Stretching 4
＼(o￣∇￣o)/⠀Stretching 5
ヾ(。￣□￣)ﾂ⠀Stretching 6
ヾ(￣□￣<)ﾉ⠀Stretching 7
ƪ(‾￣o￣”)ʃ⠀Stretching 8
*｡٩(ˊωˋ*)و✧*｡⠀Stretching 9
٩(ˊᗜˋ*)و⠀Stretching 10
٩(´Д` <)۶:.*⠀Stretching 11
٩( ‘ω’ )و⠀Stretching 12
٩(｡•ω•｡)و⠀Stretching 13
‘٩(๑´3｀๑)۶⠀Stretching 14
٩(๑˘ω˘๑)۶:.｡⠀Stretching 15
୧( ́⁰⃙⃘Ԑ⁰⃙ఁ̀ )୨⠀Stretching 16
₍₍ ᕕ(´◓ω◓)ᕗ⁾⁾⠀Stretching 17
ﾍ(´ω`)ゞ⠀Stretching 18
ヽ( ̐〥 ̐)ﾉ⠀Stretching 19
ᕕ(⁽゚⁾བ︡ ⁽ ْ ⁾ ╬)ᕗ⠀Stretching 20
٩( ⺤◊⺤)۶⠀Stretching 21
╰(⇀‸↼)╯⠀Stretching 22
╰(⇀⌂↼‶)╯⠀Stretching 23
＼(*-◇-)／｡ﾟоО⠀Stretching 24
（-＾〇＾-）⠀Yawning 1
(<´ρ`)⠀Yawning 2
（<≧皿≦）⠀Yawning 3
（)´д`(）⠀Yawning 4
(*´ο`*)⠀Yawning 5
（´□｀川）⠀Yawning 6
(▰˘o˘▰)⠀Yawning 7
(o´Д`)⠀Yawning 8
∑(￣□￣)⠀Yawning 9
˓˓˓ˇ̠̠̠⍥ˇ̠̠̠˒˒˒⠀Yawning 10
ヽ( ´O｀)ゞ⠀Yawning 11
ᕦ░ . ‾́ ◯ ‾́ . ░ᕤ⠀Yawning 12
ƪ(΄◞ิ۝◟ิ‵)ʃ⠀Yawning 13
ヾ(￣0￣； )ノ⠀Yawning 14
（◎´〇｀◎）⠀Yawning 15
《*´0｀》⠀Yawning 16
(*＇◎＇)⠀Yawning 17
（´○｀）～ゝ⠀Yawning 18
＼（´Ｏ｀）／⠀Yawning 19
( ੱ⋱口 ੱ⋱ )⠀Yawning 20
(_ _)ヾ(‘ロ‘)⠀Waking Someone Up 1
*ଘ( ॢᵕ꒶̮ᵕ(꒡ᵋ ꒡ღ)zZ‥⠀Waking Someone Up 2
ｰ(*ﾟﾛﾟ)-C＜*_ _)｡o○⠀Waking Someone Up 3
!!!!!(o≧o≦)○))ｏ(＿＿*)Ｚｚｚ⠀Waking Someone Up 4
!!!!!(o≧ω≦)○))ｏ(＿＿*)Ｚｚｚ⠀Waking Someone Up 5
!!!!!(o￣ω￣)○))ｏ(＿＿*)Ｚｚｚ⠀Waking Someone Up 6
ヾ(*￣O￣)ツ=====θ☆(o_ _)o)).o0○⠀Waking Someone Up 7
(+.+)(-.-)(_ _) ..zz⠀Falling Asleep or Waking Up 1
[▓▓]ᐖ) 三(۶ᐛ )۶⠀Falling Asleep or Waking Up 2
( ु́•̶̤ ‧̫ ⁃ ૂ̀ ).☽˚⁺⠀Falling Asleep or Waking Up 3
(๑ˊȫॢˋ)॰∘☼⠀Falling Asleep or Waking Up 4
ヾ(ｏ´Дゞｏ)｡o○⠀Falling Asleep or Waking Up 5
(´-εヾ )⠀Falling Asleep or Waking Up 6
（<´_ヘ<）⠀Falling Asleep or Waking Up 7
(P’_`)q+。⠀Falling Asleep or Waking Up 8
┤*￣Ｏ￣*├ ┤*－.－*├ ┤＿ ＿├⠀Falling Asleep or Waking Up 9
(:3 っ)3≡･◦∴*+◦º.+*.•。[][▓▓]⠀Dreaming, Astral Projection or some other Craziness 1
｡･*･:≡(:3 ) =͟͟͞͞ (¦3[▓▓]⠀Dreaming, Astral Projection or some other Craziness 2
⅀῍̩̖̬ ̎=͟͟͞͞=͟͟͞͞⁽◎͞˗̻̚=͟͟͞͞⁽◎͟˗̻̚ ͟͞=͟͟͞͞=͟͟͞͞=͟͟͞͞ (¦ꃩ[▓▓]⠀Dreaming, Astral Projection or some other Craziness 3
[▓▓]　☍(¦3ꇤ　꒱⠀Dreaming, Astral Projection or some other Craziness 4
꒰ ꒡⌓꒡꒱ᏩɵɵᎴ ɳɩɠɧ✟⠀Words 1
꒰´ ु-௰ू-॰`꒱⋆｡˚✩ɢ∞פ ɴⅈɢhт ༘*ೄ˚⠀Words 2
【☆swee< dream☆】(●ＵωU).zZZ⠀Words 3
( ；｀ヘ´)⠀ヘ Mouths 1
(((￣へ￣井)⠀ヘ Mouths 2
(`へ´*)ノ⠀ヘ Mouths 3
（￣へ￣）⠀ヘ Mouths 4
(｡-｀へ´-｡)⠀ヘ Mouths 5
ε-(‘ﾍ´○)┓⠀ヘ Mouths 6
(≧ヘ≦　)⠀ヘ Mouths 7
ρ(￣ﾍ￣ ﾒ)⠀ヘ Mouths 8
(*｀･へ･´*)⠀ヘ Mouths 9
(((0へ0)⠀ヘ Mouths 10
(*｀へ´*) 彡3⠀ヘ Mouths 11
(｀へ′)⠀ヘ Mouths 12
（’へ’）⠀ヘ Mouths 13
(*´ω｀)o⠀ω Mouths 1
(￣ω￣)⠀ω Mouths 2
(￣ω￣<)⠀ω Mouths 3
(✿´ ꒳ ` )⠀ω Mouths 4
✩⚫꒳⚫✩⠀ω Mouths 5
(´꒳`∗)⠀ω Mouths 6
(´꒳`)⠀ω Mouths 7
(∗´꒳`)⠀ω Mouths 8
(^～^)⠀~ Mouths 1
（￣～￣<）⠀~ Mouths 2
（￣～￣）⠀~ Mouths 3
ー(￣～￣)ξ⠀~ Mouths 4
೭੧(❛〜❛✿)੭೨⠀~ Mouths 5
(*´～｀*)⠀~ Mouths 6
੧| ‾́ 〜 ‾́ |੭⠀~ Mouths 7
(*・～・*)⠀~ Mouths 8
| ￣～￣|o⠀~ Mouths 9
（＾～＾；）⠀~ Mouths 10
(⁰ ◕〜◕ ⁰)⠀~ Mouths 11
（；￣ェ￣）⠀ェ Mouths 1
(￣ェ￣<)⠀ェ Mouths 2
(*´ェ｀)o⠀ェ Mouths 3
o(´ェ｀*)⠀ェ Mouths 4
(´ｪ｀*)⠀ェ Mouths 5
(*´ェ｀*)⠀ェ Mouths 6
੧| ‾́ェ ‾́ |੭⠀ェ Mouths 7
（￣ー￣）⠀Flat Mouths 1
(*´ー`)⠀Flat Mouths 2
（　｀ー´）⠀Flat Mouths 3
<<<<(￣ー￣)<><<⠀Flat Mouths 4
（；￣ー￣）⠀Flat Mouths 5
੧| ‾́ー ‾́ |੭⠀Flat Mouths 6
<<<<(￣︶￣)<><<⠀Happy Mouths 1
(｡◝‿◜｡)⠀Happy Mouths 2
§ԾᴗԾ§⠀Happy Mouths 3
੧| ‾́︶ ‾́ |੭⠀Happy Mouths 4
（；￣︶￣）⠀Happy Mouths 5
(￣︶￣<)⠀Happy Mouths 6
(*´︶｀*)⠀Happy Mouths 7
[●´︶｀●]⠀Happy Mouths 8
| ￣︶￣|o⠀Happy Mouths 9
[●´Å｀●]⠀Å Mouths 1
(´Å｀)⠀Å Mouths 2
(●´Å｀)⠀Å Mouths 3
（；￣Å￣）⠀Å Mouths 4
(*´Å｀)o⠀Å Mouths 5
(*´Å｀*)⠀Å Mouths 6
┏|￣Å￣* |┛⠀Å Mouths 7
o(´Å｀)o⠀Å Mouths 8
(￣Å￣)⠀Å Mouths 9
(#´Å｀)⠀Å Mouths 10
| ￣Å￣|o⠀Å Mouths 11
〳 ᓀÅᓂ)⠀Å Mouths 12
o(´^｀)o⠀Nose Up 1
（｀＾´）ノ⠀Nose Up 2
(￣^￣)⠀Nose Up 3
（￣＾￣）⠀Nose Up 4
(⌤⌗)⠀Nose Up 5
！(￣^^￣)⠀Nose Up 6
┏|￣＾￣* |┛⠀Nose Up 7
(￣^￣ﾒ)＼(_ _ <)⠀Nose Up 8
(#´＾｀)⠀Nose Up 9
(*｀Λ´*)｣⠀Nose Up 10
| ￣^￣|o⠀Nose Up 11
<<<<(￣＾￣)<><<⠀Nose Up 12
(((o(｀･∧･´)o)))⠀Nose Up 13
(｡•ˇ‸ˇ•｡)⠀Nose Up 14
(•̀⌄•́)⠀Miscellaneous Smugness 1
•̀.̫•́✧⠀Miscellaneous Smugness 2
(˵¯͒〰¯͒˵)⠀Miscellaneous Smugness 3
(๑ˇ ῁̫ ˇ)˒˒⠀Miscellaneous Smugness 4
(｀ڼ´)⠀Miscellaneous Smugness 5
(o＾皿＾)⠀Miscellaneous Smugness 6
| ￣∀￣ |⠀Miscellaneous Smugness 7
⚈ ̫ ⚈⠀Miscellaneous Smugness 8
╭⚈¬⚈╮⠀Miscellaneous Smugness 9
((o(●´皿｀●<)o))⠀Miscellaneous Smugness 10
〳 ᓀ ﹏ ᓂ 〵⠀Miscellaneous Smugness 11
(꒵꜅꒵)⠀Miscellaneous Smugness 12
<<<<( ￣ ≧￣)<><<⠀Miscellaneous Smugness 13
(￣´-`￣)⠀Miscellaneous Smugness 14
(＾⌒＾*)⠀Miscellaneous Smugness 15
(*´⌒`*)⠀Miscellaneous Smugness 16
₍₍ (　‾᷄꒫‾᷅　) ₎₎⠀Miscellaneous Smugness 17
(-、-)⠀Miscellaneous Smugness 18
(￣个￣)⠀Miscellaneous Smugness 19
┌( ‘o’)┐⠀Miscellaneous Smugness 20
╭〻◕`w´◕〻╮⠀Miscellaneous Smugness 21
┌(┌ 廿-廿)┐⠀Miscellaneous Smugness 22
(꒡ꜙ꒡)⠀Miscellaneous Smugness 23
( ྃ亽 ྃ)⠀Miscellaneous Smugness 24
（≧＊≦）⠀Miscellaneous Smugness 25
(ˊ˃ॣ~˂ˋॣ)«≈՞๑⠀Complex 1
( ๑‾̀◡‾́)σ»⠀Complex 2
⁎❝᷀ົཽ˴˷̮❝᷀ົཽ⁎⠀Complex 3
(♡´◠｀♡)✯*･☪:.｡⠀Complex 4
(๑⃙⃘⁼̴̀◡ु⁼̴́๑⃙⃘)⠀Complex 5
(❝ੌु˟❝ੌू⋆)⠀Complex 6
खิ৺खิ✧⠀Complex 7
(／_^)／ 　　　　　　●　＼(^_＼)⠀Catch 1
(ﾉ･ｪ･)ﾉ ● ＼(ﾟｰﾟ＼)⠀Catch 2
(ノ￣ー￣)ノ ● ＼(^ω^＼)⠀Catch 3
( ^o)ρ┳┻┳°σ(o^ )⠀Ping Pong or Table Tennis 1
ヽ(^o^)ρ┳┻┳°σ(^o^)/⠀Ping Pong or Table Tennis 2
(｡･ω･)ρ┳┷┳ﾟσ(･ω･*)⠀Ping Pong or Table Tennis 3
( ﾟ-ﾟ)_ρ┳┻┳ﾟσ彡(ﾟoﾟ )⠀Ping Pong or Table Tennis 4
(○´∇｀)0～━┳━゜0(´∇｀●)⠀Ping Pong or Table Tennis 5
＼（⌒∇⌒）ρ┳┻┳°σ（^o^）／⠀Ping Pong or Table Tennis 6
(^-^)ρ┳┷┳゜σ(^o^)⠀Ping Pong or Table Tennis 7
(」ﾟヘﾟ)」━┳┻┳━　…ニ(　ーo)_ρ　。⠀Ping Pong or Table Tennis 8
!(ﾉ｀◎´)ﾉミρ┳┷┳ﾟσ(￣○￣<<)⠀Ping Pong or Table Tennis 9
!(ﾉ｀◎´)ﾉ ρ┳┷┳ﾟσ(￣○￣￣<<)⠀Ping Pong or Table Tennis 10
(-^-^)p_____|_o____q(^-^ )⠀Regular Tennis 1
(<><<’.’)<><<=O____<_*__O=<<<<(‘.'<<<<)⠀Regular Tennis 2
ヽ(^o^)ρ_____|_____°σ(^o^)/⠀Regular Tennis 3
(｡･ω･)ρ_____|_____°σ(･ω･*)⠀Regular Tennis 4
(^-^)ρ _____|_____゜σ(^o^)⠀Regular Tennis 5
(⌗‵ꋪ′)⌕⠀Regular Tennis 6
＼（⌒∇⌒）ρ°_____|_____σ（^o^）／⠀Regular Tennis 7
（*＾＾）/~~~~~~~~~~◎⠀Yoyos 1
( ´ ▽ ` )ﾉ~~~~~~~~~~◎⠀Yoyos 2
(^▽^)/~~~~~~~~~~◎⠀Yoyos 3
(*⌒▽⌒)ﾉ~~~~~~~~~~◎⠀Yoyos 4
(・∀・)ノ~~~~~~~~~~◎⠀Yoyos 5
(／o^)/ °⊥ ＼(^o＼)⠀Volleyball 1
(／_^)／ 　　　⊥　　●　＼(^_＼)⠀Volleyball 2
(ﾉ･ｪ･)ﾉ ⊥ ● ＼(ﾟｰﾟ＼)⠀Volleyball 3
(ノ￣ー￣)ノ ● ⊥ ＼(^ω^＼)⠀Volleyball 4
＝( ^o^)ノ ．．．…___ｏ⠀Bowling 1
（*´∀｀）つ＝＝＝＝＝＝＝＝●ⅲⅲⅲ⠀Bowling 2
（*´∀｀）つ＝＝＝＝＝＝＝＝○ⅲⅲⅲ⠀Bowling 3
＝( o)ノ ．．．．．．．．．…___ｏ⠀Bowling 4
ヾ(*・-・)ﾂθ☆●⠀Soccer or Football 1
(((( ＿ ＿)☆ ≡〇　　┏┓⠀Soccer or Football 2
┏┓〝〇〟⊂(･∧･´⊂)))⠀Soccer or Football 3
C= C= C= C= C= C= ┌(<･_･)┘ ））●⠀Soccer or Football 4
!!! /( ＿0＿)￣θ☆≡≡≡≡≡○　┏┓⠀Soccer or Football 5
┏ヽ( ｀0´)ﾉ ┓　 ○⌒θ┐(｀ﾍ´；)⠀Soccer or Football 6
Ю　○三　＼(￣^￣＼）⠀Basketball 1
Ю ●　＼(^_＼)⠀Basketball 2
Ю ● ＼(ﾟｰﾟ＼)⠀Basketball 3
Ю ● ＼(^ω^＼)⠀Basketball 4
人人人人 ﾟ.+:｡ヽ(´∀｀)ﾉﾟ.+:｡ 人人人人⠀Swimming 1
人人人人　へ( ﾟｪﾟ)＿ 人人人人⠀Swimming 2
✽-(ˆ▽ˆ)/✽ ✽\(ˆ▽ˆ)-✽⠀Cheerleaders 1
p(*＾-＾*)q⠀Cheerleaders 2
✵(๑◊๑)✶⠀Cheerleaders 3
q(❂‿❂)p⠀Cheerleaders 4
✺(^▽^✺) ✺(^O^)✺ (✺^▽^)✺⠀Cheerleaders 5
P<ayin> wi<h a Ba<<⠀Miscellaneous Activities 1
ෆ⃛(ٛ ˃ ु⍘⃘ ٛ˂) ु˓˓ٍ❀⃝⠀Miscellaneous Activities 2
P<ayin> wi<h a Ba<<⠀Miscellaneous Activities 3
ෆ⃛(ٛ ❝͋॔ ु⍘⃘ ❝͋॓) ु˓˓ٍ❀⃝⠀Miscellaneous Activities 4
Snowba<< Fi>h<!⠀Miscellaneous Activities 5
˭̡̞(◞⁎˃ᆺ˂)◞₎₎=͟͟͞͞˳˚॰°ₒ৹๐⠀Miscellaneous Activities 6
Throwin> a Snowba<<⠀Miscellaneous Activities 7
(╬ᇂ..ᇂ)o彡°⠀Miscellaneous Activities 8
（・□・；）⠀Square Mouths 1
(」゜ロ゜)」⠀Square Mouths 2
(*ﾟﾛﾟ)⠀Square Mouths 3
Σ(゜ロ゜<)⠀Square Mouths 4
щ(゜ロ゜щ)⠀Square Mouths 5
∑(ﾟﾛﾟ〃)⠀Square Mouths 6
┌╏ º □ º ╏┐⠀Square Mouths 7
Σ(･口･)⠀Square Mouths 8
（○□○）⠀Square Mouths 9
（＊〇□〇）……！⠀Square Mouths 10
((((；゜Д゜)))⠀Д Style Mouths 1
( ꒪Д꒪)ノ⠀Д Style Mouths 2
(((( <°Д°))))⠀Д Style Mouths 3
((((；゜Д゜)))⠀Д Style Mouths 4
(屮゜Д゜)屮⠀Д Style Mouths 5
∑(<°Д°)⠀Д Style Mouths 6
━Σ(ﾟДﾟ|||)━⠀Д Style Mouths 7
(╬⁽⁽ ⁰ ⁾⁾ Д ⁽⁽ ⁰ ⁾⁾)⠀Д Style Mouths 8
Σ (　 Д )ﻌﻌﻌﻌ⊙ ⊙⠀Д Style Mouths 9
!!(⊃ Д)⊃≡ﾟ ﾟ⠀Д Style Mouths 10
w(@。@<)w⠀Small Round Mouths 1
˓˓ ⍥⃝⃝ ˒˒⠀Small Round Mouths 2
ପ(⑅ ॣ•͈૦•͈ ॣ)ଓ⠀Small Round Mouths 3
◟(◔ั₀◔ั )◞ ༘♡⠀Small Round Mouths 4
(ට˓˳̮ට๑)⠀Small Round Mouths 5
(✿☉｡☉)⠀Small Round Mouths 6
(മ̈ ̥̆ മ̈)⠀Small Round Mouths 7
(ల◕ั˘๐◕ั˘ల)⠀Small Round Mouths 8
(⋆⁰ ̥̮⁽⁰)(⁰⁾ ̥̮⁰⋆)⠀Small Round Mouths 9
[ □ ₒ □ ]⠀Small Round Mouths 10
(๑°o°๑)⠀Small Round Mouths 11
(*´･o･)⠀Small Round Mouths 12
(。･o･｡)⠀Small Round Mouths 13
（◔ฺo◔ฺ）⠀Small Round Mouths 14
(；゜○゜)⠀Small Round Mouths 15
(・о・)⠀Small Round Mouths 16
(∗❛ั௦❛ั∗)⠀Small Round Mouths 17
L(・o・)」⠀Medium Sized Round Mouths 1
( ॣ•͈૦•͈ ॣ)⠀Medium Sized Round Mouths 2
（°o°；）⠀Medium Sized Round Mouths 3
(○o○)⠀Medium Sized Round Mouths 4
(◐ o ◑ )⠀Medium Sized Round Mouths 5
＼(<><<o<<<<)ノ⠀Medium Sized Round Mouths 6
w(°ｏ°)w⠀Medium Sized Round Mouths 7
(<꒪ö꒪)⠀Medium Sized Round Mouths 8
(´ ˙○˙ `)⠀Medium Sized Round Mouths 9
༼⁰o⁰；༽⠀Medium Sized Round Mouths 10
(´⊙o⊙`；)⠀Medium Sized Round Mouths 11
（〇o〇；） ！！⠀Medium Sized Round Mouths 12
｜ｏ゜）⠀Medium Sized Round Mouths 13
(°o°:)⠀Medium Sized Round Mouths 14
(° o°)!⠀Medium Sized Round Mouths 15
oh!((ﾟoﾟ#⠀Medium Sized Round Mouths 16
(ﾟoﾟ)⠀Medium Sized Round Mouths 17
٩(●ö●)۶⠀Medium Sized Round Mouths 18
(ू′o‵ ू)*✲ﾟ⠀Medium Sized Round Mouths 19
( ｣｡╹o╹｡)｣⠀Medium Sized Round Mouths 20
(⑉⊙ȏ⊙)⠀Medium Sized Round Mouths 21
Σ(꒪ȏ꒪)⠀Medium Sized Round Mouths 22
( ﾟoﾟ)⠀Medium Sized Round Mouths 23
⑉ႣỏႣ⑉⠀Medium Sized Round Mouths 24
(இ௦இ)⠀Medium Sized Round Mouths 25
(•̪ o •̪)⠀Medium Sized Round Mouths 26
（三・o・）⠀Medium Sized Round Mouths 27
॥ँऀ ଠି ॥ँऀ⠀Medium Sized Round Mouths 28
༼ つ ◕o◕ ༽つ⠀Medium Sized Round Mouths 29
Σ(･o･<)⠀Medium Sized Round Mouths 30
(〇o〇；)⠀Medium Sized Round Mouths 31
(●’o’●)⠀Medium Sized Round Mouths 32
╚═། . ◯ o ◯ . །═╝⠀Medium Sized Round Mouths 33
@(。・0・)@⠀Medium Sized Round Mouths 34
(ﾉﾟοﾟ)ﾉ⠀Medium Sized Round Mouths 35
(ﾉ*0*)ﾉ⠀Medium Sized Round Mouths 36
(((<ꏿöꏿ<)))⠀Medium Sized Round Mouths 37
੧[ ⁰ o ⁰ ]ʋ⠀Medium Sized Round Mouths 38
༼ . ° o ° . ༽⠀Medium Sized Round Mouths 39
⋋░ ✿ ⁰ o ⁰ ✿ ░⋌⠀Medium Sized Round Mouths 40
（＞0＜；；；）⠀Medium Sized Round Mouths 41
∑(‘0‘＠)⠀Medium Sized Round Mouths 42
（ФоФ)⠀Medium Sized Round Mouths 43
(ﾟoﾟ〃)⠀Medium Sized Round Mouths 44
(๑•́o•̀๑)⠀Medium Sized Round Mouths 45
ლ(^o^ლ)⠀Medium Sized Round Mouths 46
∩(。・o・。)∩⠀Medium Sized Round Mouths 47
(ﾟοﾟ人))⠀Medium Sized Round Mouths 48
(⸝⸝⸝ª̷̛იॢª̷̛⸝⸝⸝)ᵒʰ┈⠀Medium Sized Round Mouths 49
（◎0◎）⠀Medium Sized Round Mouths 50
(ﾉﾟ0ﾟ)ﾉ~⠀Medium Sized Round Mouths 51
(*0*)/⠀Medium Sized Round Mouths 52
(・0・。(・-・。(・0・。(・-・。)⠀Medium Sized Round Mouths 53
(＃´Ｏ｀)⠀Large Round Mouths 1
(!!´◯`)∑⠀Large Round Mouths 2
⊙０⊙⠀Large Round Mouths 3
(⁎❛ ꒩ુ ❛⁎)⠀Large Round Mouths 4
(*ﾟOﾟ*)⠀Large Round Mouths 5
☉̥̆ Ô☉̥̆⠀Large Round Mouths 6
（´〇｀）⠀Large Round Mouths 7
‧˚₊*̥(* ⁰̷̴͈꒨⁰̷̴͈)‧˚₊*̥⠀Large Round Mouths 8
‧˚₊*̥(∗*⁰͈꒨⁰͈)‧˚₊*̥⠀Large Round Mouths 9
(｡☬０☬｡)⠀Large Round Mouths 10
꒪ꄱ꒪⠀Large Round Mouths 11
‧˚₊*̥꒰❃•̤ॢ꒩•̤ॢ꒱‧˚₊*̥⠀Large Round Mouths 12
˛( ❝᷀ົཽႭू ❝᷀ົཽ⁎)⠀Large Round Mouths 13
❝᷀ัႭृ❝᷀ั⠀Large Round Mouths 14
b(’０’)d⠀Large Round Mouths 15
(*ﾟ◯ﾟ*)⠀Large Round Mouths 16
ヾ(*’Ｏ’*)ｲ⠀Large Round Mouths 17
ԅ║ . º ◯ º . ║ノ⠀Large Round Mouths 18
(○`･｣０･´)｣⠀Large Round Mouths 19
☉̥̆ Ô☉̥̆⠀Large Round Mouths 20
╰║ ❛ ◯ ❛ ║╯⠀Large Round Mouths 21
░ ⊚ ◯ ⊚ ░⠀Large Round Mouths 22
║ ” ◕ ◯ ◕ ” ║⠀Large Round Mouths 23
░ ි ◯ ි ░⠀Large Round Mouths 24
(＠･０･)ﾉ⠀Large Round Mouths 25
╰། ◉ ◯ ◉ །╯⠀Large Round Mouths 26
ے( Ö )ص⠀Large Round Mouths 27
(´⊙ω⊙`)！⠀Miscellaneous Mouths 1
（゜◇゜）⠀Miscellaneous Mouths 2
⊙▂⊙⠀Miscellaneous Mouths 3
Σ(゜゜)⠀Miscellaneous Mouths 4
Σ(ಠิωಠิ|||)⠀Miscellaneous Mouths 5
〣( ºΔº )〣⠀Miscellaneous Mouths 6
Σ░(꒪◊꒪ ))))⠀Miscellaneous Mouths 7
(∗॔꒪⺫ॢ꒪)⠀Miscellaneous Mouths 8
ლ(☮╹◊╹☮)ლ⠀Miscellaneous Mouths 9
‷̗ↂ凸ↂ‴̖ i⠀Miscellaneous Mouths 10
◎ܫ◎⠀Miscellaneous Mouths 11
(ʘᗩʘ’)⠀Miscellaneous Mouths 12
（○Ａ○）⠀Miscellaneous Mouths 13
=͟͟͞͞(　 ω )=͟͟͞͞　³ ³⠀Miscellaneous Mouths 14
w(ﾟ△ﾟ)w⠀Miscellaneous Mouths 15
(‘◇’｀)⠀Miscellaneous Mouths 16
o(ﾟ◇ﾟo）⠀Miscellaneous Mouths 17
(゜◇゜ ))⠀Miscellaneous Mouths 18
(( ゜◇゜)⠀Miscellaneous Mouths 19
(ؔᓒ⍥⃘ؔᓒ)⠀Miscellaneous Mouths 20
٩(⌯꒦ິ̆ᵔ꒦ິ)۶ᵒᵐᵍᵎᵎᵎ⠀OMG! 1
(๑o̴̶̷̥᷅﹏o̴̶̷̥᷅๑)ᵒᵐᵍᵎᵎᵎ⠀OMG! 2
(´⊙ω⊙`)ᵒᵐᵍᵎᵎᵎ⠀OMG! 3
║ ” ◕ ◯ ◕ ” ║ᵒᵐᵍᵎᵎᵎ⠀OMG! 4
ԅ║ . º ◯ º . ║ノᵒᵐᵍᵎᵎᵎ⠀OMG! 5
（◎0◎）ᵒᵐᵍᵎᵎᵎ⠀OMG! 6
༼⁰o⁰；༽ᵒᵐᵍᵎᵎᵎ⠀OMG! 7
┌╏ º □ º ╏┐ᵒᵐᵍᵎᵎᵎ⠀OMG! 8
w(°ｏ°)w ᵒᵐᵍᵎᵎᵎ⠀OMG! 9
(；゜○゜)ᵒᵐᵍᵎᵎᵎ⠀OMG! 10
∑(<°Д°)ᵒᵐᵍᵎᵎᵎ⠀OMG! 11
(ᵒ̤̑ ₀̑ ᵒ̤̑)wow!*✰⠀WOW! 1
!(ᵒ̤̑ ◁ ᵒ̤̑)wow!৹ᢄᵍᵎᵎ⠀WOW! 2
(⑅ ॣ•͈૦•͈ ॣ)꒳ᵒ꒳ᵎᵎᵎ⠀WOW! 3
˶⍤⃝˶꒳ᵒ꒳ᵎᵎᵎ⠀WOW! 4
꒰⑅ ॣ•͈૦•͈ ॣ꒱໊꒳ᵒ꒳ᵎᵎᵎ⠀WOW! 5
ʸᵉᵃʰᵎᵎ े ̡̡⍤⃝  ̢̢ेे ꒳ᵒ꒳ᵎᵎ⠀WOW! 6
╰║ ❛ ◯ ❛ ║╯꒳ᵒ꒳ᵎᵎᵎ⠀WOW! 7
（◎0◎）꒳ᵒ꒳ᵎᵎᵎ⠀WOW! 8
(இ௦இ)꒳ᵒ꒳ᵎᵎᵎ⠀WOW! 9
(๑o̴̶̷̥᷅﹏o̴̶̷̥᷅๑)꒳ᵒ꒳ᵎᵎᵎ⠀WOW! 10
༼⁰o⁰；༽꒳ᵒ꒳ᵎᵎᵎ⠀WOW! 11
(´･艸･｀)⠀Hands of Shock 1
(ﾟ艸ﾟ<)⠀Hands of Shock 2
∴(O艸O★)⠀Hands of Shock 3
|✿´・ლ・`|⠀Hands of Shock 4
║ . º 艸 º . ║⠀Hands of Shock 5
(＃´艸｀)⠀Hands of Shock 6
(๑°艸°๑)⠀Hands of Shock 7
▨-▨¬ლ(•_•) (▨_▨¬)⠀Square Shaped Sunglasses 1
(⌐▨_▨)⠀Square Shaped Sunglasses 2
(⌐■_■)⠀Square Shaped Sunglasses 3
( •_•) ( •_•)<><<⌐■-■ (⌐■_■)⠀Square Shaped Sunglasses 4
( ∙_∙) ( ∙_∙)<><<⌐■-■ (⌐■_■)⠀Square Shaped Sunglasses 5
( •_•) ( •_•)<><<⌐■ (⌐■_•)⠀Square Shaped Sunglasses 6
ヽ(⌐■_■)ノ♪♬⠀Square Shaped Sunglasses 7
( ͡° ͜ʖ ͡°)<><<⌐■-■⠀Square Shaped Sunglasses 8
ლ(▀̿̿Ĺ̯̿̿▀̿ლ)⠀Square Shaped Sunglasses 9
┌(▀Ĺ̯ ▀-͠ )┐⠀Square Shaped Sunglasses 10
༼⌐■ل͜■༽⠀Square Shaped Sunglasses 11
(ﾒ■_■)y-～⠀Square Shaped Sunglasses 12
( •_•)<><<⌐■-■⠀Square Shaped Sunglasses 13
(̿▀̿ ̿Ĺ̯̿̿▀̿ ̿)̄⠀Square Shaped Sunglasses 14
┌(▀Ĺ̯▀)┐⠀Square Shaped Sunglasses 15
༼⌐■ل͟■༽⠀Square Shaped Sunglasses 16
(ง⌐□ل͜□)ง⠀Square Shaped Sunglasses 17
(७⌐■ل͟■)७⠀Square Shaped Sunglasses 18
ᕕ༼⌐■-■༽ᕗ⠀Square Shaped Sunglasses 19
(ง⌐□ل͜□)⠀Square Shaped Sunglasses 20
( ▀ 益 ▀ )⠀Square Shaped Sunglasses 21
（■Д■*）⠀Square Shaped Sunglasses 22
(つ▀¯▀)つ⠀Square Shaped Sunglasses 23
⊂(▀¯▀⊂)⠀Square Shaped Sunglasses 24
˓˓( ु∎௰∎ू )՞⠀Square Shaped Sunglasses 25
┌༼▀̿ Ĺ̯▀̿༽┐⠀Square Shaped Sunglasses 26
༼ ຈل͜ຈ༽ノ⌐■-■⠀Square Shaped Sunglasses 27
┬┴┬┴┤ᕦ( ▀̿ Ĺ̯ ▀̿├┬┴┬⠀Square Shaped Sunglasses 28
━╤デ╦︻(▀̿̿Ĺ̯̿̿▀̿ ̿)⠀Square Shaped Sunglasses 29
(*▼▽▼*)⠀Triangle Shaped Sunglasses 1
(▼皿▼ﾒ)ﾉ⠀Triangle Shaped Sunglasses 2
(*▼o▼*)ノ⠀Triangle Shaped Sunglasses 3
//(*▼▽▼)∩//⠀Triangle Shaped Sunglasses 4
◎(▼●▼)◎ｙ－゜゜゜⠀Triangle Shaped Sunglasses 5
σ(*▼▽▼*)⠀Triangle Shaped Sunglasses 6
Σ(▼□▼ﾒ)⠀Triangle Shaped Sunglasses 7
σ(＊▼‐▼＊)⠀Triangle Shaped Sunglasses 8
┌(▼▼メ)┘⠀Triangle Shaped Sunglasses 9
└( ▼▼ )┐⠀Triangle Shaped Sunglasses 10
┌(メ▼▼)┘⠀Triangle Shaped Sunglasses 11
ヽ( ▼∀▼)ﾉ⠀Triangle Shaped Sunglasses 12
v(▼ω▼ﾒ)ゞ⠀Triangle Shaped Sunglasses 13
(▼∀▼)⠀Triangle Shaped Sunglasses 14
(▼-▼*)⠀Triangle Shaped Sunglasses 15
▼ω▼⠀Triangle Shaped Sunglasses 16
(ﾒ▼_▼)⠀Triangle Shaped Sunglasses 17
( ▼Д▼)y─┛~~⠀Triangle Shaped Sunglasses 18
ヽ(▼ｰ▼ｷ)⠀Triangle Shaped Sunglasses 19
(▼へ▼ﾒ)σ⠀Triangle Shaped Sunglasses 20
(ﾒ▼皿▼)ノ　⌒　○┼＜⠀Triangle Shaped Sunglasses 21
(▼O▼ﾒ)⠀Triangle Shaped Sunglasses 22
(ｷ▼O▼)/⠀Triangle Shaped Sunglasses 23
|*▼皿▼)⠀Triangle Shaped Sunglasses 24
（▼(00）▼ﾒ）⠀Triangle Shaped Sunglasses 25
(｡▼皿▼)σ⠀Triangle Shaped Sunglasses 26
~~・-v(▼、▼ﾒ)⠀Triangle Shaped Sunglasses 27
ヽ(▼皿▼ヽ)⠀Triangle Shaped Sunglasses 28
(ﾉ▼皿▼)ﾉ⠀Triangle Shaped Sunglasses 29
(▼ω▼o)y-~~~⠀Triangle Shaped Sunglasses 30
(▼皿▼)y-.｡o○⠀Triangle Shaped Sunglasses 31
(▼皿▼#)⠀Triangle Shaped Sunglasses 32
ヾ(▼ﾍ▼；)⠀Triangle Shaped Sunglasses 33
(▼▽▼)人(▼▽▼)⠀Triangle Shaped Sunglasses 34
щ(▼ﾛ▼щ)⠀Triangle Shaped Sunglasses 35
(ｷ▼⊿▼)ﾉ⠀Triangle Shaped Sunglasses 36
（▼∀▼）⠀Triangle Shaped Sunglasses 37
ヾ(*▼・▼)ﾉ⌒☆⠀Triangle Shaped Sunglasses 38
(メ▼ー▼)/●~*⠀Triangle Shaped Sunglasses 39
*~●＼(▼ー▼メ)⠀Triangle Shaped Sunglasses 40
（♯▼皿▼）⠀Triangle Shaped Sunglasses 41
(‡▼益▼)⠀Triangle Shaped Sunglasses 42
( ╬◣ 益◢）y━･~⠀Triangle Shaped Sunglasses 43
(ｷ▼д▼)y─┛~~ﾟﾟﾟ⠀Triangle Shaped Sunglasses 44
“o(▼皿▼メ<)o”⠀Triangle Shaped Sunglasses 45
(メノ▼□▼)ノ⠀Triangle Shaped Sunglasses 46
凸（◆◆メ⠀Other Shaped Sunglasses 1
ヾ(*●Д●)ﾉ゛⠀Other Shaped Sunglasses 2
-●-●-ヽ(｀∀´)ゝ⠀Other Shaped Sunglasses 3
♪(*・д・)ﾉ●-●⠀Other Shaped Sunglasses 4
ヾ(●ε●)ノ⠀Other Shaped Sunglasses 5
(*´∀｀）ヽ＜◆－◆＞→（*◆T◆）⠀Other Shaped Sunglasses 6
ಠ_ರೃ⠀Monocles 1
ヽ༼ຈل͜ರೃ༽ﾉ⠀Monocles 2
ヽ( ͡°╭͜ʖ╮͡ರೃ )ﾉ⠀Monocles 3
[ ಠ Ĺ̯ ಠೃ ]⠀Monocles 4
[ . ಠ o ಠೃ . ]⠀Monocles 5
(╭ರ_•́)⠀Monocles 6
(╭ರᴥ•́)⠀Monocles 7
( ರ Ĺ̯ ರೃ )⠀Monocles 8
ᕙ〳 ರ ︿ ರೃ 〵ᕗ⠀Monocles 9
(╭ರ_⊙)⠀Monocles 10
༼ ಠ ▃ ಠೃ ༽⠀Monocles 11
( ಠ_ರೃ)⠀Monocles 12
(╯°□°）╯︵ ┻━┻⠀Flipping a Large Table 1
(ノಠ益ಠ)ノ彡┻━┻⠀Flipping a Large Table 2
ʕノ•ᴥ•ʔノ ︵ ┻━┻⠀Flipping a Large Table 3
(/¯◡ ‿ ◡)/¯ ~ ┻━┻⠀Flipping a Large Table 4
(ノ-_-)ノ ~┻━┻⠀Flipping a Large Table 5
(ﾉ；；)ﾉ~┻━┻⠀Flipping a Large Table 6
(ﾉ-_-)ﾉ ~┻━┻ ☆`⠀Flipping a Large Table 7
(ノ-_-)ノ・・・~~┻━┻⠀Flipping a Large Table 8
(ノ-_-)ノ~┻━┻⠀Flipping a Large Table 9
ノ￣□￣)ノ ~┻━┻⠀Flipping a Large Table 10
(ﾉꐦ ⊙曲ఠ)ﾉ彡┻━┻⠀Flipping a Large Table 11
(ﾉ｀□´)ﾉ⌒┻━┻⠀Flipping a Large Table 12
(ﾉꐦ ๑´Д`๑)ﾉ彡┻━┻⠀Flipping a Large Table 13
┻━┻ミ＼（≧ロ≦＼）⠀Flipping a Large Table 14
(ﾉ￣□￣)ﾉ ~┻━┻⠀Flipping a Large Table 15
（ノ♯｀△´）ノ~’┻━┻⠀Flipping a Large Table 16
（ノT＿T)ノ ＾┻━┻⠀Flipping a Large Table 17
(┛ಠДಠ)┛彡┻━┻⠀Flipping a Large Table 18
(ノ°▽°)ノ︵┻━┻⠀Flipping a Large Table 19
(ﾉ*’ω’*)ﾉ彡┻━┻⠀Flipping a Large Table 20
‎(ﾉಥ益ಥ）ﾉ ┻━┻⠀Flipping a Large Table 21
(╯’□’)╯︵ ┻━┻⠀Flipping a Large Table 22
(ﾉಥДಥ)ﾉ︵┻━┻･/⠀Flipping a Large Table 23
(._.) ~ ︵ ┻━┻⠀Flipping a Large Table 24
┗[© ♒ ©]┛ ︵ ┻━┻⠀Flipping a Large Table 25
┻━┻ ︵ ლ(⌒-⌒ლ)⠀Flipping a Large Table 26
(ﾉ＾◡＾)ﾉ︵ ┻━┻⠀Flipping a Large Table 27
༼ ᕤ ºل͟º ༽ᕤ ︵┻━┻⠀Flipping a Large Table 28
ヽ༼ ツ ༽ﾉ ︵┻━┻⠀Flipping a Large Table 29
༼ ͠ຈ ͟ل͜ ͠ຈ༽ง︵┻━┻⠀Flipping a Large Table 30
ヽ༼ຈل͜ຈ༽ﾉ︵┻━┻⠀Flipping a Large Table 31
(╯ຈل͜ຈ) ╯︵ ┻━┻⠀Flipping a Large Table 32
༼ノಠل͟ಠ༽ノ ︵ ┻━┻⠀Flipping a Large Table 33
༼ﾉຈل͜ຈ༽ﾉ︵┻━┻⠀Flipping a Large Table 34
(╯ ͝° ͜ʖ͡°)╯︵ ┻━┻⠀Flipping a Large Table 35
(つ☢益☢)つ︵┻━┻⠀Flipping a Large Table 36
ヽ༼ຈل͜ຈ༽ﾉ︵ ┻━┻⠀Flipping a Large Table 37
(┛◉Д◉)┛彡┻━┻⠀Flipping a Large Table 38
(ﾉ≧∇≦)ﾉ ﾐ ┸━┸⠀Flipping a Large Table 39
┻━┻ミ＼(≧ﾛ≦＼)⠀Flipping a Large Table 40
(ノ｀´)ノ ~┻━┻ ～⠀Flipping a Large Table 41
ʕ ⊃･ ◡ ･ ʔ⊃︵┻━┻⠀Flipping a Large Table 42
(ﾉ▼д▼)ﾉ ~┻━┻ ☆`⠀Flipping a Large Table 43
(┛❍ᴥ❍)┛彡┻━┻⠀Flipping a Large Table 44
(ʘ∇ʘ)ク 彡 ┻━┻⠀Flipping a Large Table 45
┻━┻ ︵ ლ(ಠ益ಠლ)⠀Flipping a Large Table 46
(╯ಠ_ರೃ)╯︵ ┻━┻⠀Flipping a Large Table 47
/(ò.ó)┛彡┻━┻⠀Flipping a Large Table 48
(╯=▃=)╯︵┻━┻⠀Flipping a Large Table 49
(ノ｀ー´)ノ・・・~~┻━┻⠀Flipping a Large Table 50
(ﾉ｀◇´)ﾉ~┻━┻⠀Flipping a Large Table 51
┻━┻ ヘ╰( •̀ε•́ ╰)⠀Flipping a Large Table 52
(ノ｀Д´)ノ~┻━┻⠀Flipping a Large Table 53
(ﾉ｀△´)ﾉ~┻━┻⠀Flipping a Large Table 54
(⑅ノ-_-)ノ~┻━┻⠀Flipping a Large Table 55
(╯ ･ ᗜ ･ )╯︵ ┻━┻⠀Flipping a Large Table 56
(ノ ﾟДﾟ)ノ　＝＝＝＝　┻━━┻⠀Flipping a Large Table 57
!!!!|┛*｀Д´|┛・・~~┻━┻　┳━┳⠀Flipping a Large Table 58
(/#-_-)/~┻┻〃⠀Flipping a Medium Sized Table 1
(/ToT)/ ~┻┻⠀Flipping a Medium Sized Table 2
（ノ－＿－）ノ･･･~┻┻⠀Flipping a Medium Sized Table 3
(ﾉ*’‐’)ﾉ ﾐ ┸┸⠀Flipping a Medium Sized Table 4
(ノ#-_-)ノ ミ　┴┴⠀Flipping a Medium Sized Table 5
（ノ｀_´）ﾉ~~┴┴⠀Flipping a Medium Sized Table 6
(ノ｀´）ノミ┻┻⠀Flipping a Medium Sized Table 7
ノToT)ノ ~┻┻⠀Flipping a Medium Sized Table 8
(ﾉ｀Д)ﾉ:・’∵:.┻┻⠀Flipping a Medium Sized Table 9
(ﾉToT)ﾉ ﾐ ┸┸⠀Flipping a Medium Sized Table 10
(メ–)ノノ。。。┻┻⠀Flipping a Medium Sized Table 11
(ﾉ≧∇≦)ﾉ ﾐ ┸┸⠀Flipping a Medium Sized Table 12
(ノToT)ノ ~┻┻⠀Flipping a Medium Sized Table 13
┳┳ヾ(T(エ)Tヽ)⠀Flipping a Medium Sized Table 14
(ﾉTwT)ﾉ ┫:･’.::･┻┻:･’.::･⠀Flipping a Medium Sized Table 15
(ノ͡° ͜ʖ ͡°)ノ︵┻┻⠀Flipping a Medium Sized Table 16
（ノ－＿－）ノ・・・~~~┻┻⠀Flipping a Medium Sized Table 17
(ノ；o；)ノ ┫:･’.::･┻┻:･’.::･⠀Flipping a Medium Sized Table 18
(ノ；ω；)ノ ┫:･’.::･┻┻:･’.::･⠀Flipping a Medium Sized Table 19
(ノToT)ノ ┫:・’.::・┻┻:・’.::・⠀Flipping a Medium Sized Table 20
(ノTДT)ノ ┫:･’.::･┻┻:･’.::･⠀Flipping a Medium Sized Table 21
(ノToT)ノ　┫：･’.::･┻┻:･’.::･⠀Flipping a Medium Sized Table 22
（ﾉ｀Д´）ﾉ－－－－－┻┻　-３-３⠀Flipping a Medium Sized Table 23
（ノ￣＾￣）ノ　┳┳　┣　┻┻　┫　┳┳⠀Flipping a Medium Sized Table 24
(ﾉ´□｀)ﾉ ┫:･’∵:.┻┻:･’.:┣∵･:. ┳┳⠀Flipping a Medium Sized Table 25
(ノ｀０)ノ ⌒┫：・’.：：・┻┻：・’.：：・⠀Flipping a Medium Sized Table 26
(ﾉ｀⌒´)ﾉ ┫：・’.：：・┻┻：・’.：：・⠀Flipping a Medium Sized Table 27
(ノ｀⌒´)ノ ┫：・’.：：・┻┻：・’.：：・⠀Flipping a Medium Sized Table 28
( ｀o)ﾉﾉ ┫⠀Flipping a Small Table 1
( ﾉo|o)ﾉ ┫｡ﾟ:.:⠀Flipping a Small Table 2
（；－－）ノノ ┫：・゜’⠀Flipping a Small Table 3
(/-o-)/ ⌒ ┤⠀Flipping a Small Table 4
(/｀ο´)/ ⌒ ┫:’ﾟ:｡･,. 。゜⠀Flipping a Small Table 5
(/ToT)/_┫・..⠀Flipping a Small Table 6
(ノ－＿－）ノ　┫〝〟∵⠀Flipping a Small Table 7
(ノ-0-)ノ　┫∵：．⠀Flipping a Small Table 8
(ﾉ-ｏ-)ﾉ ~┫：・’.：：・⠀Flipping a Small Table 9
(ノ-o-)ノ⌒┳ ┫┻┣⠀Flipping a Small Table 10
(ノ￣＿￣）ノ　┫〝〟∵⠀Flipping a Small Table 11
(丿<><<ロ<<<<)丿 ┤∵:.⠀Flipping a Small Table 12
（ノ￣ー￣）ノ　┫：・’.::⠀Flipping a Small Table 13
(ノ￣ー￣）ノ　┫〝〟∵⠀Flipping a Small Table 14
(ﾉ＝ﾟﾛﾟ)ﾉ ⌒┫:･’.::⠀Flipping a Small Table 15
(ノ＞o＜)ノ ┫:･’.::⠀Flipping a Small Table 16
（ノ≧∇≦）ノ　┫　゜・∵。⠀Flipping a Small Table 17
（ノ≧ο≦）ノ　┫　゜・∵。⠀Flipping a Small Table 18
（ノ○Д○）ノ＝＝＝┠⠀Flipping a Small Table 19
（ノー”ー）ノ　┫　゜・∵。⠀Flipping a Small Table 20
(ノToT)ノ ┫:・’.::・⠀Flipping a Small Table 21
((((ﾉ｀皿´)ﾉ ⌒┫:･┫┻┠’.⠀Flipping a Small Table 22
(ﾉ*｀▽´*)ﾉ ⌒┫ ┻ ┣ ┳⠀Flipping a Small Table 23
(ノ￣皿￣）ノ ⌒=== ┫⠀Flipping a Small Table 24
･.:ﾟ｡┣＼(’ﾛ´＼)⠀Flipping a Small Table 25
(ﾉ#▼o▼)ﾉ ┫:･’.::･⠀Flipping a Small Table 26
┣¨┣¨┣¨ヾ(゜Д゜ )ノ┣¨┣¨┣⠀Flipping a Small Table 27
┣¨ ୧(๑ ⁼̴̀ᐜ⁼̴́๑)૭⠀Flipping a Small Table 28
((|||||┝＼(｀д´)／┥|||||))⠀Flipping a Small Table 29
┝＼( ‘∇^*)^☆／┥⠀Flipping a Small Table 30
(ﾉﾟ∀ﾟ)ﾉ ┫:｡･:*:･ﾟ’★,｡･:*:♪･ﾟ’☆━━━!!!!⠀Flipping a Small Table 31
┻━┻ ︵ ¯\ (ツ)/¯ ︵ ┻━┻⠀Flipping Two Tables at Once 1
┻━┻ ︵ヽ(`Д´)ﾉ︵ ┻━┻⠀Flipping Two Tables at Once 2
┻━┻ ︵ヽ(`Д´)ﾉ︵ ┻━┻⠀Flipping Two Tables at Once 3
┻━┻ ︵ ¯\(ツ)/¯ ︵ ┻━┻⠀Flipping Two Tables at Once 4
┫┻┠⌒ヾ(-_-ヾ 三 ﾉ-_-)ﾉ⌒┫:･┫┻⠀Flipping Two Tables at Once 5
（/＞□＜）/亠亠⠀Flipping Other Tables 1
(ノ￣＿￣)ノ＼。:・゛。⠀Flipping Other Tables 2
(ノÒ益Ó)ノ彡▔▔▏⠀Flipping Other Tables 3
_|___|_ ╰(º o º╰)⠀Flipping Other Tables 4
(ノ￣￣∇￣￣)ノ~~~~~⌒━━┻━━┻━━⠀Flipping Other Tables 5
⊂(ﾉ￣￣￣(工)￣￣￣)⊃ﾉ~~~~~━━━┻━━┻━━━⠀Flipping Other Tables 6
(ノ-o-)ノ┸┸)`3゜)・<’.⠀Hitting People With Tables 1
(ノ-。-）ノ┻━┻☆(　　^)⠀Hitting People With Tables 2
(ノ-_-)ノ ~┻━┻ (/o＼)⠀Hitting People With Tables 3
(ノ#-◇-)ノ ~~~~┻━┻☆(x _ x)ノ⠀Hitting People With Tables 4
(ノ｀０)ノ ⌒┫ ┻ ┣ ┳☆(x x)⠀Hitting People With Tables 5
(ノ｀m´)ノ ~┻━┻ (/o＼)⠀Hitting People With Tables 6
(ﾉ`Д´)ﾉ.:･┻┻)｀з゜)･:ﾞ<⠀Hitting People With Tables 7
(ノ￣▽￣)ノ┻━┻☆)*￣□)ノ))⠀Hitting People With Tables 8
(ノ￣◇￣)ノ~┻━┻/(×。×)⠀Hitting People With Tables 9
(ﾉToT)ﾉ ┫:･’.::･＼┻┻(･_＼)⠀Hitting People With Tables 10
(╯°□°)╯︵ ┻━┻ ︵ ╯(°□° ╯)⠀Hitting People With Tables 11
(ノ^_^)ノ┻━┻ ┬─┬ ノ( ^_^ノ)⠀Hitting People With Tables 12
ﾐ┻┻(ﾉ<><<｡<<<<)ﾉ⠀Hitting People With Tables 13
.::･┻┻☆()ﾟOﾟ)⠀Hitting People With Tables 14
(ﾉ｀A”)ﾉ ⌒┫ ┻ ┣ ┳☆(x x)⠀Hitting People With Tables 15
(ノ｀m´)ノ ~┻━┻ (/o＼)⠀Hitting People With Tables 16
⌒┫ ┻ ┣ ⌒┻☆)ﾟ⊿ﾟ)ﾉ⠀Hitting People With Tables 17
(ﾉ≧∇≦)ﾉ ﾐ ┸┸)`νﾟ)･<’.⠀Hitting People With Tables 18
(ﾉToT)ﾉ ┫:･’.::･＼┻┻(･_＼)⠀Hitting People With Tables 19
（ノ－ｏ－）ノ　”″┻━┻☆（<><<○<<<<）⠀Hitting People With Tables 20
ミ(ノ￣^￣)ノ!≡≡≡≡≡━┳━☆()￣□￣)/⠀Hitting People With Tables 21
（メ｀д´）┫～┻┻ ～┣～┳┳　　（。@ﾍ@。川⠀Hitting People With Tables 22
ミ(ノ￣^￣)ノ≡≡≡≡≡━┳━☆()￣□￣)/⠀Hitting People With Tables 23
┬──┬◡ﾉ(° -°ﾉ)⠀Putting the Table Back 1
┬─┬ノ(ಠ_ಠノ)⠀Putting the Table Back 2
┬━┬ ノ( ゜¸゜ノ)⠀Putting the Table Back 3
┬━┬ ノ( ゜-゜ノ)⠀Putting the Table Back 4
┳━┳ ヽ༼ಠل͜ಠ༽ﾉ⠀Putting the Table Back 5
┬──┬ ¯\_(ツ)⠀Putting the Table Back 6
┬──┬ ノ( ゜-゜ノ)⠀Putting the Table Back 7
(ヘ･_･)ヘ┳━┳⠀Putting the Table Back 8
┻o(Ｔ＿Ｔ )ミ( ；＿；)o┯⠀Putting the Table Back 9
┣ﾍ(≧∇≦ﾍ)… (≧∇≦)/┳━┳⠀Putting the Table Back 10
┣ﾍ(^▽^ﾍ)Ξ(ﾟ▽ﾟ*)ﾉ┳━┳⠀Putting the Table Back 11
(╯°Д°）╯︵/(.□ . )⠀Flipping People 1
(ノಠ ∩ಠ)ノ彡( o°o)⠀Flipping People 2
/( .□.) ︵╰(゜益゜)╯︵ /(.□. /)⠀Flipping People 3
≡/( .-.)\ ︵╰(«○»益«○»)╯︵ /(.□. /)̨⠀Flipping People 4
(/ .□.)\ ︵╰(゜Д゜)╯︵ /(.□. \)⠀Flipping People 5
（╯°□°）╯︵( .o.)⠀Flipping People 6
(╯°□°）╯︵ (\ . 0 .)\⠀Flipping People 7
(/￣(ｴ)￣)/ ⌒ ○┼<<<<⠀Flipping People 8
(╯°□°）╯︵ /( ‿⌓‿ )\⠀Flipping People 9
ノ┬─┬ノ ︵ ( o°o)⠀Table Flips You! 1
┬─┬ ︵ /(.□. \）⠀Table Flips You! 2
┬──┬╯︵ /(.□. \）⠀Table Flips You! 3
┬──┬ ︵(╯。□。）╯⠀Table Flips You! 4
ヘ(´° □°)ヘ┳━┳⠀Table Flips You! 5
(╯°□°)╯︵ ʞooqǝɔɐℲ⠀Flipping Words 1
(╯°□°)╯︵ ɹǝʇʇıʍ⊥⠀Flipping Words 2
(∿°○°)∿ ︵ ǝʌo<⠀Flipping Words 3
(╯°□°)╯︵ ∀ԀIԀ ∀ԀOS⠀Flipping Words 4
(╯°□°)╯︵ ɯsıɥdɹoɯouǝʞs⠀Flipping Words 5
(╯°□°)╯︵ sɯɐxǝ⠀Flipping Words 6
(╯°□°)╯︵ ƃuıʎpnʇs⠀Flipping Words 7
(╯°□°)╯︵ ʞɹoʍ⠀Flipping Words 8
∀ԀOS ∀ԀIԀ ︵╰(°□°)╯︵ ∀ԀIԀ ∀ԀOS⠀Flipping Words 9
(੭ ◕㉨◕)੭ =͟͟͞͞=͟͟͞͞三❆)’дº)<,’:=͟͟͞͞⠀Flipping Other Things 1
(ﾉꐦ ◎曲◎)ﾉ=͟͟͞͞ ⌨⠀Flipping Other Things 2
(っ ºДº)っ ︵ ⌨⠀Flipping Other Things 3
(╯^□^)╯︵ ❄☃❄⠀Flipping Other Things 4
(╯ `Д ́)╯︵ (฿)⠀Flipping Other Things 5
♡╰(*ﾟxﾟ​*)╯♡⠀Flipping Other Things 6
˭̡̞(◞⁎˃ᆺ˂)◞₎₎=͟͟͞͞✉⠀Flipping Other Things 7
(۶ૈ ۜ ᵒ̌▱๋ᵒ̌ )۶ૈ=͟͟͞͞ ⌨`ワ°)・<’.⠀Flipping Other Things 8
╰( ^o^)╮-=ﾆ=一＝三⠀Flipping Other Things 9
（ノ<><<_<<<<）ノ　≡●⠀Flipping Other Things 10
●~*⌒ ヽ(´ｰ｀ )⠀Flipping Other Things 11
!!(⊃ Д)⊃≡ﾟ ﾟ⠀Flipping Other Things 12
(╬☉д⊙)＝◯)๏д๏))･<’.⠀Flipping Other Things 13
(ര̀⍨ര́)و ̑̑༉ լਕ ̏੭ჯ ૅੁ~ɭ ɿ❢❢⠀Flipping Other Things 14
˭̡̞(◞⁎˃ᆺ˂)◞₎₎=͟͟͞͞˳˚॰°ₒ৹๐⠀Flipping Other Things 15
૮(ꂧ᷆⺫ꂧ᷇)ა=͟͟͞͞ꊞ⠀Flipping Other Things 16
ヽ［・∀・］ﾉ(((((((((●～*⠀Flipping Other Things 17
ﾍ|･∀･|ﾉ*~●⠀Flipping Other Things 18
(*ﾉﾟ▽ﾟ)ﾉ ⌒((((●⠀Flipping Other Things 19
(╯°□°）╯︵ ส็็็็็็็ส⠀Flipping Other Things 20
⌨ █▬▬◟(`ﮧ´ ◟ )⠀Flipping Other Things 21
○三　＼(￣^￣＼）⠀Flipping Other Things 22
,,,,,,,,((*￣(ｴ)￣)ﾉ ⌒☆ o*＿(x)_)⠀Flipping Other Things 23
(۶ૈ‡▼益▼)۶ૈ=͟͟͞͞ ⌨⠀Flipping Other Things 24
(ノω・)ノ⌒゛◆⠀Flipping Other Things 25
(۶ૈ ۜ ᵒ̌▱๋ᵒ̌ )۶ૈ=͟͟͞͞ ⌨⠀Flipping Other Things 26
(۶ૈ ᵒ̌ Дᵒ̌)۶ૈ=͟͟͞͞ ⌨⠀Flipping Other Things 27
☆(ﾉ^o^)ﾉ‥‥‥…━━━━〇(^~^)⠀Flipping Other Things 28
( つ•̀ω•́)つ・・*:・:・゜:==≡≡Σ=͟͟͞͞(✡)`Д´）⠀Flipping Other Things 29
(<¬_¬)⠀Seriously? 1
（；¬＿¬)⠀Seriously? 2
(¬_¬)⠀Seriously? 3
(¬ω¬)⠀Seriously? 4
( ¬_¬)⠀Seriously? 5
눈_눈⠀Seriously? 6
(҂⌣̀_⌣́)⠀Seriously? 7
( ･᷄ㅂ･᷅ )⠀Seriously? 8
(.﹒︣︿﹒︣.)⠀Seriously? 9
(∩⌣̀_⌣́)⠀Seriously? 10
( •́ ⍨ •̀)⠀Seriously? 11
m(￢0￢)m⠀Seriously? 12
<<<<(¬＿¬<<<<)⠀Seriously? 13
( ´⍪⌂⍪`)⠀Seriously? 14
(¯―¯٥)⠀Seriously? 15
(눈_눈)⠀Seriously? 16
(<￢＿￢)⠀Seriously? 17
(〠_〠)⠀Seriously? 18
(ಢ⊱ಢ ｡)⠀Seriously? 19
(⌍་д་⌌)⠀Seriously? 20
(,Ծ_Ծ,)⠀Seriously? 21
ᗜੂ௰ᗜੂ⠀Seriously? 22
┌༼ σ ‸ σ ༽┐⠀Seriously? 23
(￢ε￢　)⠀Seriously? 24
(〃´o｀)=3⠀Seriously? 25
( ꂧ᷆ ◞ ˑ̼̬ ◟ ꂧ᷇ )⠀Seriously? 26
⁽་º་⁾⠀Seriously? 27
(*´Д｀)=з⠀Seriously? 28
(￢з￢)⠀Seriously? 29
(ு८ு_ .:)⠀Seriously? 30
┌[ O ʖ̯ O ]┐⠀Seriously? 31
―(´￢O￢)(￢O￢｀)―⠀Seriously? 32
║ * ರ Ĺ̯ ರ * ║⠀Seriously? 33
⁞ ˵ •̀ ل͟ •́ ˵ ⁞⠀Seriously? 34
(；￢＿￢)⠀Seriously? 35
(￢ω￢<A)⠀Seriously? 36
（￢з￢）⠀Seriously? 37
（─。─）⠀Seriously? 38
( ੭눈 _ 눈 )੭⠀Seriously? 39
(ಠ.ಠ)⠀Seriously? 40
( ͡°Ĺ̯̿̿ ͡°)⠀Seriously? 41
(눈_눈<)⠀Seriously? 42
( ¬ _ ¬ <)⠀Seriously? 43
(¬‿¬)⠀I See What You Did There 1
( ͡° ͜ʖ ͡°)⠀I See What You Did There 2
( ་ ⍸ ་ )⠀I See What You Did There 3
( ج_ج )⠀I See What You Did There 4
(¬ -̮ ¬)⠀I See What You Did There 5
◤¬ ˒̫̮ ¬◥⠀I See What You Did There 6
〳 ͡° Ĺ̯ ͡° 〵⠀I See What You Did There 7
(ఠ ̥̆ ఠ)⠀I See What You Did There 8
(ര௰ര)⠀I See What You Did There 9
(ؔꇵ ˻̠ ؔꇵ)⠀I See What You Did There 10
（ ಠωಠ）⠀I See What You Did There 11
(•᷉ुε ू•᷈,)⠀Colour Me Intrigued 1
(๑•̆૩•̆)⠀Colour Me Intrigued 2
(ԾεԾ|||)⠀Colour Me Intrigued 3
(๏็ટૄ ๏็ (๏็ટૄ◟๏็ )⠀Colour Me Intrigued 4
ಠ , ಥ⠀Colour Me Intrigued 5
ʕ ͠° ʖ̫ °͠ ʔ⠀Colour Me Intrigued 6
໒( ” ͠° ʖ̫ °͠ ” )७⠀Colour Me Intrigued 7
(/ヘ￣､)⠀Facepalms 1
(ノ◇≦。)⠀Facepalms 2
(◞‸ლ)⠀Facepalms 3
(－‸ლ)⠀Facepalms 4
(<¬_ლ)⠀Facepalms 5
( ･᷄ㅂლ )⠀Facepalms 6
(눈_ლ)⠀Facepalms 7
( ¬_ლ)⠀Facepalms 8
(￢ε ლ)⠀Facepalms 9
(,Ծ_ლ)⠀Facepalms 10
(〠_ლ)⠀Facepalms 11
<#8220<(<><<ლ)<#8221<⠀Facepalms 12
(ʃ⌣́,⌣́ƪ)⠀Thinking Real Hard 1
Σ(-᷅_-᷄๑)⠀Thinking Real Hard 2
(˃̴̀ᄇॢ˂̴́ ∗)⠀Thinking Real Hard 3
( ｰ̀εｰ́ )⠀Thinking Real Hard 4
(-｡-<⠀Thinking Real Hard 5
( מּ,_מּ)⠀Thinking Real Hard 6
♒((⇀‸↼))♒⠀Thinking Real Hard 7
ƪ(•̃͡•̃͡ ƪ⠀Thinking Real Hard 8
(ー_ーゞ⠀Thinking Real Hard 9
(,,-`_●-)⠀Thinking Real Hard 10
(´～ヾ)⠀Thinking Real Hard 11
( *´罒`* )⠀Thinking Real Hard 12
(´⊂_｀人)⠀Thinking Real Hard 13
(⍞∻⍞ॢ)₎₎⠀Thinking Real Hard 14
˓˓₍ʔˊԶ͡ˋʕ₎˒˒⠀Thinking Real Hard 15
(p〒д〒q)⠀Thinking Real Hard 16
(；◔ิд◔ิ)⠀Thinking Real Hard 17
Σ (°ζ‿°　)⠀Thinking Real Hard 18
། ﹒︣ ‸ ﹒︣ །⠀Thinking Real Hard 19
ɖී؀ීϸ⠀Thinking Real Hard 20
(ὸ⍸ό)✧⠀Thinking Real Hard 21
ॱ॰⋆(˶ॢ‾᷄﹃‾᷅˵ॢ)ӵᵘᵐᵐᵞ♡♡♡⠀Thinking Real Hard 22
⁝(๑⑈௰⑈)◞⁝˚º꒰꒱⠀Thought Bubbles 1
(‾͈̑ ◟  ॢ‾͈̑๑)ഽ̵ᵘഽ̵ᵘ४꒰…꒱⠀Thought Bubbles 2
| ू*꒦ິ꒳꒦ີ)｡oO⠀Thought Bubbles 3
( ᵕ́ૢ‧̮ᵕ̀ૢ)‧̊·*⠀Thought Bubbles 4
( ु⁎ᴗ_ᴗ⁎)ु.｡oO⠀Thought Bubbles 5
(*´ ˘ `*).｡oO ( ♡ )⠀Thought Bubbles 6
(*˘︶˘*).｡.:*♡⠀Thought Bubbles 7
（´-`）.｡oO（）⠀Thought Bubbles 8
| ू･᷄ω･᷅)｡oOஇo｡⠀Thought Bubbles 9
(´._.`).｡oஇ()⠀Thought Bubbles 10
❤︎⁄⁄꒰* ॢꈍ◡ꈍ ॢ꒱.*˚‧⠀Thought Bubbles 11
(❛ॕ௰❛ॕૢ๑)˚º꒰꒱⠀Thought Bubbles 12
=͟͟͞͞ ऀืົཽ≀ ͔ ͕̮ ऀืົཽ✧॰৹꒰❢❢꒱⠀Thought Bubbles 13
ღ˘◡˘ற♡.｡oO⠀Thought Bubbles 14
=͟͟͞͞ ऀืົཽ≀ ͔ ͕̮ ऀืົཽ✧॰৹꒰꒱⠀Thought Bubbles 15
|´ε ｀ゞ)*.。oO( )⠀Thought Bubbles 16
(‾͈̑ ◟  ॢ‾͈̑๑)ഽ̵ᵘഽ̵ᵘ४꒰ ꒱⠀Thought Bubbles 17
*¨*•.¸꒰๑ ᷄ω ᷅꒱⠀Thought Bubbles 18
(⁽͈˙̑⁾˔̉⁽˙̑⁾͈)˚º꒰꒱⠀Thought Bubbles 19
(ღ✪ｖ✪)｡o○⠀Thought Bubbles 20
⸂⸂( ृ[▒͠]꒱⸒⸒⌕˚º꒰❣꒱⠀Thought Bubbles 21
|˄·͈༝·͈˄₎.｡oO⠀Thought Bubbles 22
(ृᓎੁ⁎ ृ　)ुᐝ꒰꒱⠀Thought Bubbles 23
ꏂ　: ृ⑆)˚º꒰꒱⠀Thought Bubbles 24
○o。／((-＿-メ))＼｡o○⠀Thought Bubbles 25
(*ゝ(ェ)･)ﾉ.｡o○⠀Thought Bubbles 26
(*´∀｀).。o○⠀Thought Bubbles 27
(ꆤ⍸ꆤ)⠀Lost in Thought 1
(º﹃º )⠀Lost in Thought 2
(*´﹃｀*)⠀Lost in Thought 3
( ｡_｡)⠀Lost in Thought 4
(´-ι_-｀)⠀Lost in Thought 5
v(´-ι_-｀)v⠀Lost in Thought 6
(。ⓥдⓥ)ノ⠀Lost in Thought 7
(´-_ゝ-`)⠀Lost in Thought 8
( ﾟｰﾟ)⠀Lost in Thought 9
(.•̵̑⌓•̵̑)⠀Lost in Thought 10
【•】_【•】⠀Lost in Thought 11
(◦ˇ _̆ ˇ◦)⠀Lost in Thought 12
(　`_ゝ´)⠀Lost in Thought 13
(ര⸏ुര)⠀Lost in Thought 14
(●･̆⍛･̆●)⠀Lost in Thought 15
( ⁝ื ‸ ⁝ื )⠀Lost in Thought 16
(ꉺ⍸ꉺ)⠀Lost in Thought 17
(´ι_｀ )⠀Lost in Thought 18
(ᇂ_ᇂ|||)⠀Lost in Thought 19
ε(´･●_･｀)з⠀Lost in Thought 20
(•Ṵ•)⠀Lost in Thought 21
(ᇂ_Jᇂ)⠀Lost in Thought 22
(⁎छ˼̲̮छ)⠀Lost in Thought 23
(`L_` )⠀Lost in Thought 24
( ´_<><<`)⠀Lost in Thought 25
┏། ﹒ _ ﹒ །┓⠀Lost in Thought 26
(｡･~･｡)⠀Lost in Thought 27
(´･＿･‘)⠀Lost in Thought 28
（´―оヽ）⠀Lost in Thought 29
( ˇ÷ˇ　 )⠀Lost in Thought 30
୧╏ ՞ _ ՞ ╏୨⠀Lost in Thought 31
( 　ﾟ,_ゝﾟ)⠀Lost in Thought 32
(｡･ˇ⊆ˇ･｡)⠀Lost in Thought 33
(•‾॒̑ ູ॒‾̑•)⠀Lost in Thought 34
(ↂↄ̫ↂ)⠀Lost in Thought 35
❛ͬ˓˷❛ͬ⠀Lost in Thought 36
(´･Ω･｀)⠀Lost in Thought 37
( ´∵｀)⠀Lost in Thought 38
╭( ๐_๐)╮⠀Lost in Thought 39
( ｡･-･｡｀)⠀Lost in Thought 40
( ･ิ,_ゝ･ิ)⠀Lost in Thought 41
(ඟ⍘ඟ)⠀Lost in Thought 42
(⍬⍸⍬)⠀Lost in Thought 43
⁽͑ʺˊ꜅ˋʺ⁾̉⠀Lost in Thought 44
▭⃘ ப̲ ▭⃘⠀Lost in Thought 45
‹(•¿•)›⠀Lost in Thought 46
(๑≖ˇдˇ≖๑)⠀Lost in Thought 47
(٭ꇵ᷅ ؛ ꇵ᷅٭)⠀Lost in Thought 48
(⚙Լ⚙)⠀Lost in Thought 49
꜏˔꜊⠀Lost in Thought 50
໒( ⊡ _ ⊡ )७⠀Lost in Thought 51
°L°⠀Lost in Thought 52
בּ_בּ⠀Some Kind of Style 1
טּ_טּ⠀Some Kind of Style 2
לּ_לּ⠀Some Kind of Style 3
מּ_מּ⠀Some Kind of Style 4
סּ_סּ⠀Some Kind of Style 5
תּ_תּ⠀Some Kind of Style 6
(⑅ ‘﹃’ )⠀Miscellaneous Thinking Emoticons 1
๐छ ੂछ๐⠀Miscellaneous Thinking Emoticons 2
(ಡωಡ)⠀Miscellaneous Thinking Emoticons 3
◔̯◔⠀Miscellaneous Thinking Emoticons 4
(◔ૂ◔)⠀Miscellaneous Thinking Emoticons 5
(⊹◕ʖ̯◕)⠀Miscellaneous Thinking Emoticons 6
⇎_⇎⠀Miscellaneous Thinking Emoticons 7
(•ṋ•)⠀Miscellaneous Thinking Emoticons 8
(✿╹m╹)⠀Miscellaneous Thinking Emoticons 9
(❛ัॢᵕ❛ั ॢ)✩*ೃ.⋆⠀Miscellaneous Thinking Emoticons 10
（*థ౪థ）⠀Miscellaneous Thinking Emoticons 11
(o˘д˘)o⠀Miscellaneous Thinking Emoticons 12
[⸍હ⸌]⠀Miscellaneous Thinking Emoticons 13
(᷅᷆⁎ ົ̅࿉ ົ̅⁎)᷄᷇⠀Miscellaneous Thinking Emoticons 14
(⚭᷄ˬ̛⚭᷅)⠀Miscellaneous Thinking Emoticons 15
(ಢധಢ)⠀Miscellaneous Thinking Emoticons 16
q(╯ᆺ╰๑)⠀Miscellaneous Thinking Emoticons 17
(ತ◞౪◟ತ‵)⠀Miscellaneous Thinking Emoticons 18
ರ⍜ರ⠀Miscellaneous Thinking Emoticons 19
ﾐ☆( *uωu人)+ﾟ⠀Miscellaneous Thinking Emoticons 20
(人´口`)⠀Miscellaneous Thinking Emoticons 21
(*•̀ᴗ•́*)و ̑̑⠀On Hand up Success Fist 1
╭( ･ㅂ･)و ̑̑⠀On Hand up Success Fist 2
(๑•̀ㅂ•́)و⠀On Hand up Success Fist 3
(๑˃̵ᴗ˂̵)و⠀On Hand up Success Fist 4
╭( ･ㅂ･)و⠀On Hand up Success Fist 5
( •̀ᄇ• ́)ﻭ✧⠀On Hand up Success Fist 6
(ര̀ᴗര́)و ̑̑⠀On Hand up Success Fist 7
╭(♡･ㅂ･)و ̑̑⠀On Hand up Success Fist 8
◝( ′ㅂ`)و ̑̑⠀On Hand up Success Fist 9
╭( ･ㅂ･)و ̑̑ ＂⠀On Hand up Success Fist 10
╭( ･ㅂ･)و )))⠀On Hand up Success Fist 11
╭(๑ ॔ㅂ ਂ ॓)و ̑̑⠀On Hand up Success Fist 12
( ⁼̴̤̆ ළ̉ ⁼̴̤̆)و ̑̑⠀On Hand up Success Fist 13
(๑˃̵ᴗ˂̵)و⠀On Hand up Success Fist 14
(๑•̀ㅂ•́)و✧⠀On Hand up Success Fist 15
꒰๑͒•̀ुꇵ͒•꒱و ̑̑⠀On Hand up Success Fist 16
ଘ꒰ ๑ ˃̶ ᴗ ᵒ̴̶̷๑꒱و ̑̑⠀On Hand up Success Fist 17
(ฅ⁍̴̀◊⁍̴́)و ̑̑⠀On Hand up Success Fist 18
╭( ･ㅂ･)و ̑̑ ˂ᵒ͜͡ᵏᵎ⁾✩⠀On Hand up Success Fist 19
(•́⌄•́๑)૭✧⠀On Hand up Success Fist 20
(•̀ᴗ•́)൬༉⠀On Hand up Success Fist 21
!(•̀ᴗ•́)و ̑̑⠀On Hand up Success Fist 22
(•̀o•́)ง⠀On Hand up Success Fist 23
٩(•̤̀ᵕ•̤́๑)ᵒᵏᵎᵎᵎᵎ⠀One Hand Up Success Fist, Other Direction! 1
ೕ(`･୰･´)⠀One Hand Up Success Fist, Other Direction! 2
ೕ(･ㅂ･ )⠀One Hand Up Success Fist, Other Direction! 3
ೕ(•̀ᴗ•́)⠀One Hand Up Success Fist, Other Direction! 4
٩(ര̀ᴗര́)⠀One Hand Up Success Fist, Other Direction! 5
ೕ(˃̵ᴗ˂̵ ๑)⠀One Hand Up Success Fist, Other Direction! 6
ೕ(•̀ㅂ•́ )⠀One Hand Up Success Fist, Other Direction! 7
✧٩(•́⌄•́๑)⠀One Hand Up Success Fist, Other Direction! 8
ೕ(⁍̴̀◊⁍̴́ฅ)⠀One Hand Up Success Fist, Other Direction! 9
٩(｡•ω•｡)و⠀Two Hands Up, Double Success Fist! 1
٩(⸝⸝⸝◕ั ௰ ◕ั⸝⸝⸝ )و⠀Two Hands Up, Double Success Fist! 2
٩(✪ꀾ⍟༶)و⠀Two Hands Up, Double Success Fist! 3
୧( ⁼̴̶̤̀ω⁼̴̶̤́ )૭⠀Two Hands Up, Double Success Fist! 4
٩(˃̶͈̀௰˂̶͈́)و⠀Two Hands Up, Double Success Fist! 5
٩( <#8216<ω<#8217< )و⠀Two Hands Up, Double Success Fist! 6
٩(｡•ㅅ•｡)و⠀Two Hands Up, Double Success Fist! 7
٩( ´･ш･)و⠀Two Hands Up, Double Success Fist! 8
٩(•̤̀ᵕ•̤́๑)૭✧⠀Two Hands Up, Double Success Fist! 9
ː̗̀٩꒰ꋃ꒱وː̖́⠀Two Hands Up, Double Success Fist! 10
٩(๑❛ワ❛๑)و⠀Two Hands Up, Double Success Fist! 11
(۶•̀ᴗ•́)۶⠀Two Hands Up, Double Success Fist! 12
٩( ᐛ )و⠀Two Hands Up, Double Success Fist! 13
✧٩(•́⌄•́๑)و ✧⠀Two Hands Up, Double Success Fist! 14
ೕ(`･୰･´)و ̑̑⠀Two Hands Up, Double Success Fist! 15
٩(๑•̀ㅂ•́)و⠀Two Hands Up, Double Success Fist! 16
٩(๑˃̵ᴗ˂̵)و⠀Two Hands Up, Double Success Fist! 17
(((ೕ( ･ㅂ･)و )))⠀Two Hands Up, Double Success Fist! 18
٩( ′ㅂ`)و ̑̑⠀Two Hands Up, Double Success Fist! 19
٩(ˊᗜˋ*)و⠀Two Hands Up, Double Success Fist! 20
(و ˃̵ᴗ˂̵)و⠀Two Hands Up, Double Success Fist! 21
(ง ͡ʘ ͜ʖ ͡ʘ)ง⠀Two Hands Up, Double Success Fist! 22
(ง ͠ ͠° ل͜ °)ง⠀Two Hands Up, Double Success Fist! 23
٩(╬ŏ3ŏ)و⠀Two Hands Up, Double Success Fist! 24
✧٩(ˊωˋ*)و✧⠀Two Hands Up, Double Success Fist! 25
٩̋(ˊ•͈ ꇴ •͈ˋ)و⠀Two Hands Up, Double Success Fist! 26
٩( ᐛ )و⠀Two Hands Up, Double Success Fist! 27
＼\ ٩( ᐛ )و /／⠀Super Success 1
＼＼\ ٩(๑❛ワ❛๑)و //／／⠀Super Success 2
＼＼\(۶•̀ᴗ•́)۶//／／⠀Super Success 3
\ \ \٩( ′ㅂ`)و ̑̑/ / /⠀Super Success 4
＼＼\└(‘ω’)┘//／／⠀Super Success 5
\ \ \\٩(｡•ω•｡)و // / /⠀Super Success 6
\\\٩(✪ꀾ⍟༶)و///⠀Super Success 7
＼＼\\୧( ⁼̴̶̤̀ω⁼̴̶̤́ )૭ //／／⠀Super Success 8
＼＼\\٩(˃̶͈̀௰˂̶͈́)و //／／⠀Super Success 9
\\\٩( <#8216<ω<#8217< )و///⠀Super Success 10
\ \ \٩(｡•ㅅ•｡)و/ / /⠀Super Success 11
\ \ \\٩( ´･ш･)و// / /⠀Super Success 12
\\\٩(•́⌄•́๑)و////⠀Super Success 13
\\\\\ೕ(`･୰･´)و/////⠀Super Success 14
＼＼\٩(๑•̀ㅂ•́)و//／／⠀Super Success 15
\ \ \٩(๑˃̵ᴗ˂̵)و/ / /⠀Super Success 16
\ \ \ೕ( ･ㅂ･)و / / /⠀Super Success 17
✧*｡٩(ˊᗜˋ*)و✧*｡⠀Super Success 18
¡¡¡( •̀ ᴗ •́ )و!!!⠀Super Success 19
＼＼\\ ⱶ˝୧(๑ ⁼̴̀ᐜ⁼̴́๑)૭兯 //／／⠀Super Success 20
“(`(エ)´)ノ⠀Waving to the Right 1
( ･ω･)ﾉ⠀Waving to the Right 2
(⁎ ✪͡ ◡͐✪͡ ⁎)ﾉ”⠀Waving to the Right 3
( ´ ▽ ` )ﾉ⠀Waving to the Right 4
( ^_^)／⠀Waving to the Right 5
(^ _ ^)/⠀Waving to the Right 6
(,, ･∀･)ﾉ゛⠀Waving to the Right 7
（ ゜ρ゜)ノ⠀Waving to the Right 8
(^ Q ^)/⠀Waving to the Right 9
(<-_-)/⠀Waving to the Right 10
( ﾟ▽ﾟ)/⠀Waving to the Right 11
(^o^)/⠀Waving to the Right 12
(｡･ω･)ﾉﾞ⠀Waving to the Right 13
(。-ω-)ﾉ⠀Waving to the Right 14
(￣(oo)￣)ﾉ⠀Waving to the Right 15
(。･д･)ﾉﾞ⠀Waving to the Right 16
(。^_・)ノ⠀Waving to the Right 17
(￣(ｴ)￣)ﾉ⠀Waving to the Right 18
(｡´∀｀)ﾉ⠀Waving to the Right 19
(*^･ｪ･)ﾉ⠀Waving to the Right 20
(￣▽￣)ノ⠀Waving to the Right 21
(´・ω・)ﾉ⠀Waving to the Right 22
(*＾▽＾)／⠀Waving to the Right 23
(=ﾟωﾟ)ﾉ⠀Waving to the Right 24
(=ﾟωﾟ)ノ⠀Waving to the Right 25
(*￣Ｏ￣)ノ⠀Waving to the Right 26
(≧∇≦)/⠀Waving to the Right 27
( ・_・)ノ⠀Waving to the Right 28
(*●⁰ꈊ⁰●)ﾉ⠀Waving to the Right 29
(○´3｀)ﾉ⠀Waving to the Right 30
(o・・o)/⠀Waving to the Right 31
(o´ω`o)ﾉ⠀Waving to the Right 32
@(o・ェ・)@ノ⠀Waving to the Right 33
~(＾◇^)/⠀Waving to the Right 34
☆ﾐ(o*･ω･)ﾉ⠀Waving to the Right 35
ー( ´ ▽ ` )ﾉ⠀Waving to the Right 36
(*ﾟ⚙͠ ∀ ⚙͠)ﾉ⠀Waving to the Right 37
(。･∀･)ﾉ⠀Waving to the Right 38
(^▽^)/ ʸᵉᔆᵎ⠀Waving to the Right 39
(｀･ω･´)ﾉ⠀Waving to the Right 40
(◍˃̶ᗜ˂̶◍)ﾉ”⠀Waving to the Right 41
(●´∀｀)ノ~⠀Waving to the Right 42
o｜◕ˇ▽ˇ◕｜ツ⠀Waving to the Right 43
(ஐ০౪০)ﾉ⠀Waving to the Right 44
(￣ｰ￣)ﾉ⠀Waving to the Right 45
(ж^□^ж)ﾉ⠀Waving to the Right 46
ｰ(☆∀☆)/”⠀Waving to the Right 47
(*´∇｀)ノ⠀Waving to the Right 48
(*σωσ）シ⠀Waving to the Right 49
（｀∀´）ノ⠀Waving to the Right 50
（｡≧◇≦）ﾉ⠀Waving to the Right 51
( ´_ゝ｀)ﾉ⠀Waving to the Right 52
(✿´꒳`)ﾉ°⠀Waving to the Right 53
( ✪ワ✪)ノʸᵉᵃʰᵎ⠀Waving to the Right 54
꒰๑˃͈꒳˂͈๑꒱ﾉ*ﾞ̥⠀Waving to the Right 55
(♦亝д 亝)ﾉ⠀Waving to the Right 56
(✧∇✧)╯⠀Waving to the Right 57
(●°u°●)​ 」⠀Waving to the Right 58
(*´∇｀)ﾉ⠀Waving to the Right 59
∪*ゝω･)ﾉ”⠀Waving to the Right 60
(◜௰◝)╯⠀Waving to the Right 61
(๑ ؔؖؕ◉͠ ◡͐ ◉ؕؔؕؖ͠)ノ⠀Waving to the Right 62
(ஐ╹◡╹)ノ⠀Waving to the Right 63
o(*’▽’*)/☆ﾟ’⠀Waving to the Right 64
(｡Ő▽Ő｡)ﾉﾞ⠀Waving to the Right 65
(*´･д･)ﾉ⠀Waving to the Right 66
(⋆ʾ ꆚ ʿ⋆)۶⁾⁾⿻⠀Waving to the Right 67
(。･∀･)ﾉ゛⠀Waving to the Right 68
(●<><<ω<<<<)ﾉﾞ⠀Waving to the Right 69
(ゝω･)ﾉ⠀Waving to the Right 70
♪( ･ｪ･)ﾂ彡⠀Waving to the Right 71
(*ゝω・)ﾉ⠀Waving to the Right 72
o｜๑⊙Д⊙๑｜ツ⠀Waving to the Right 73
(●ゝ∀･)ﾉ⠀Waving to the Right 74
( *՞ਊ՞*)ﾉ⠀Waving to the Right 75
(o゜◇゜)ノ⠀Waving to the Right 76
φ(*⌒▽⌒)ﾉ⠀Waving to the Right 77
(◕ฺー≦)ノ⠀Waving to the Right 78
(*ﾟ_っﾟ)ﾉﾞ⠀Waving to the Right 79
(ό‿ὸ)ﾉ⠀Waving to the Right 80
|。･ω･|ﾉ⠀Waving to the Right 81
(* ﾟ∀ﾟ)ﾉｼ⠀Waving to the Right 82
(*・ｪ･*)ﾉ⠀Waving to the Right 83
(*・∀・)ノ゛⠀Waving to the Right 84
o(*ﾟ∇ﾟ)ﾉ⠀Waving to the Right 85
(●＞д＜)ノ⠀Waving to the Right 86
(＾◇＾）ノ⠀Waving to the Right 87
（*・Ｕ・）ノ☆⠀Waving to the Right 88
[○´・ω・]ﾉ⠀Waving to the Right 89
☆⌒c(´∀｀)ノ⠀Waving to the Right 90
(｡･o･｡)ﾉ⠀Waving to the Right 91
(*´∀｀*)ﾉ｡+ﾟ *｡⠀Waving to the Right 92
((*´ω｀*)ﾉ⠀Waving to the Right 93
￥( ´ω`)/⠀Waving to the Right 94
o｜#╹ー╹｜ツ⠀Waving to the Right 95
(ه’́⌣’̀ه )／⠀Waving to the Right 96
( * ́꒳`*)੭⠀Waving to the Right 97
(･仄･)ﾉ⠀Waving to the Right 98
(〃･ω･)ﾉ~☆･ﾟ+｡*ﾟ･.+⠀Waving to the Right 99
(∩｡･ｏ･｡)っ.ﾟ☆｡’`⠀Waving to the Right 100
✲ﾟ｡.(✿╹◡╹)ﾉ☆.｡₀:*ﾟ✲ﾟ*:₀｡⠀Waving to the Right 101
(✿◕ ‿◕ฺ)ノ))。₀: *゜⠀Waving to the Right 102
ﾟ.+:｡(≧∇≦)ﾉﾟ.+:｡⠀Waving to the Right 103
＼(°o°；）⠀Waving to the Left 1
＼(＾▽＾*)⠀Waving to the Left 2
＼(￣O￣)⠀Waving to the Left 3
~ヾ ＾∇＾⠀Waving to the Left 4
~ヾ(＾∇＾)⠀Waving to the Left 5
ヾ( ‘ – ‘*)⠀Waving to the Left 6
ヾ(･ω･`｡)⠀Waving to the Left 7
ヾ(・ω・ｏ)⠀Waving to the Left 8
ヾ(｡･ω･｡)⠀Waving to the Left 9
ヾ(｡´･_●･`｡)☆⠀Waving to the Left 10
ヾ(´･ω･｀)⠀Waving to the Left 11
ヾ(＾∇＾)⠀Waving to the Left 12
ヾ(☆▽☆)⠀Waving to the Left 13
ヾ ^_^⠀Waving to the Left 14
ヾ(^ิ∀^ิ)⠀Waving to the Left 15
╰(✧∇✧)⠀Waving to the Left 16
ヾ(°∇°*)⠀Waving to the Left 17
ヾ(･ω･*∪⠀Waving to the Left 18
❣ヾ( ؔ✪̥ ⌔ ؔ✪̥`﹡)⠀Waving to the Left 19
ヾ[･ω･`●]⠀Waving to the Left 20
✧*｡٩(ˊ⺫ ˋ ृ )⠀Waving to the Left 21
ヾ(=´･∀･｀=)⠀Waving to the Left 22
ヾ(*Ő౪Ő*)⠀Waving to the Left 23
ヾ(▼ﾍ▼；)⠀Waving to the Left 24
ヾ(*●´∀｀●*）⠀Waving to the Left 25
ヾ(o｀Å´o)⠀Waving to the Left 26
ヾ(・∀・*)⠀Waving to the Left 27
ヾ(<><<ω<<<<○)⠀Waving to the Left 28
ヾ(･ω･ )⠀Waving to the Left 29
ヾ(*´Д｀*)⠀Waving to the Left 30
ヽ(*´ω｀*))⠀Waving to the Left 31
☆ヾ(･ェ･｡｀Ｕ⠀Waving to the Left 32
(ヾ(´・ω・｀)⠀Waving to the Left 33
╰(❛∀❛ )⠀Waving to the Left 34
╰|･ิД･ิ |⠀Waving to the Left 35
“Σ⊂(☉ω☉∩ )⠀Waving to the Left 36
.:*･✿ ✿.｡.:*･ヾ(Ő‿Ő✿)⠀Waving to the Left 37
：*：°・☆ヾ(δ_δ。)⠀Waving to the Left 38
ヾ(・◇・)ﾉ⠀Waving both Hands 1
ヽ(ﾟ◇ﾟ )ﾉ⠀Waving both Hands 2
ヾ(๑╹ꇴ◠๑)ﾉ”⠀Waving both Hands 3
ヽ(･∀･)ﾉ⠀Waving both Hands 4
ヾ(◍’౪`◍)ﾉﾞ♡⠀Waving both Hands 5
ヾ(๑ㆁᗜㆁ๑)ﾉ”⠀Waving both Hands 6
ヾ(＠⌒ー⌒＠)ノ⠀Waving both Hands 7
ヾ(oﾟｘﾟo)ﾉ⠀Waving both Hands 8
ヾ(*❦ω❦)ノ⠀Waving both Hands 9
ヽ(๏∀๏ )ﾉ⠀Waving both Hands 10
ヾ(´｡••｡`)ﾉ⠀Waving both Hands 11
ヾ(Ő∀Ő๑)ﾉ⠀Waving both Hands 12
ヾ(´(ｴ)｀ﾉﾞ⠀Waving both Hands 13
ヾ( ´｡ •x• ｡` )ﾉ”⠀Waving both Hands 14
ヾ(˹ᆺ˺✿)ﾉﾞ⠀Waving both Hands 15
ヾ(´￢｀)ﾉ⠀Waving both Hands 16
ヾ(*´∀｀*)ﾉ⠀Waving both Hands 17
ヾ(´∀｀○)ﾉ⠀Waving both Hands 18
ヾ(＾-＾)ノ⠀Waving both Hands 19
ヾ(๑╹ヮ╹๑)ﾉ”⠀Waving both Hands 20
ヾ(・ᆺ・✿)ﾉﾞ⠀Waving both Hands 21
ヽ(´▽`)ﾉ⠀Waving both Hands 22
ヽ(｡･c_，･｡)ﾉﾞ⠀Waving both Hands 23
ヾ(῀ ⚙⌄⚙ ῀)ﾉ”⠀Waving both Hands 24
ヾ( o･∀)ﾉﾞ⠀Waving both Hands 25
ヾ(o･∀･o)ﾉﾞ⠀Waving both Hands 26
ヾ(∀･o )ﾉﾞ⠀Waving both Hands 27
ヾ(ﾟдﾟ)ﾉ゛⠀Waving both Hands 28
ヾ(*･∀･*）/☆ﾟ。･＋⠀Waving both Hands 29
ヾ(・m・*)ノ゛⠀Waving both Hands 30
ヾ(*･ω･*)o⠀Waving Forward 1
◦°˚(´•̛ᴗ•̛`)/˚°◦⠀Waving Forward 2
ヽ(´･ω･`)､⠀Waving Forward 3
◞(⚭⃚⃙͐·̫⚭⃚⃙͐)˩✧⠀Waving Forward 4
└╏ ･ ᗜ ･ ╏┐⠀Waving Forward 5
ヽ། ﹒ ~ ﹒ །╮⠀Waving Forward 6
ｰ<<<<(´∀｀)/⠀Waving Forward 7
(ﾉ´∀｀*)ﾉ⠀Waving Forward 8
ヾ(◜▿‾ 三 ‾▿◝)ﾉ⠀Waving Back and Forth 1
(ृ°͈꒳​°͈＝°͈꒳​°͈)੭ु⁾⁾*⠀Waving Back and Forth 2
ヾ(´ω｀＝´ω｀)ノ⠀Waving Back and Forth 3
‘`ﾛｰヽ(⊡ㅂ⊡｡ Ξ ｡⊡ㅂ⊡)ﾉ ‘`ﾛｰ⠀Waving Back and Forth 4
＼（＾∀＾）メ（＾∀＾）ノ⠀Multiple People Waving 1
ヽ(＾▽＾)人(＾▽＾)人(＾▽＾)ﾉ⠀Multiple People Waving 2
ヾ(⌒(_๑˘ㅂ˘๑)_⠀Multiple People Waving 3
ヾ(◜▿‾ ( ´▿｀ ) ‾▿◝)ﾉ⠀Multiple People Waving 4
(●´Д)ﾉ”　ヾ(∀｀●)⠀Multiple People Waving 5
ヾ｜*￣ー￣｜*￣∇￣｜/”⠀Multiple People Waving 6
ヾ｜*￣ー￣｜*￣ー￣｜/”　　ヾ｜*￣∇￣*｜⠀Multiple People Waving 7
ヘ(‘◇’、)/⠀Oh You 1
ヘ(゜Д、゜)ノ⠀Oh You 2
ヘ(°￢°)ノ⠀Oh You 3
ヘ(°◇、°)ノ⠀Oh You 4
ﾍ(ﾟ∀ﾟ*)ﾉ⠀Oh You 5
⌒(o＾▽＾o)ノﾟ⠀Oh You 6
ヾ(*<><<v<<<<)⠀Oh You 7
(<><<v<<<<*)ｼ⠀Oh You 8
ﾍ(￣ー￣)ﾉ⠀Oh You 9
(ง °Θ°)ว⠀Oh You 10
(¬_¬)ﾉ⠀Forget it! 1
(￣∠ ￣ )ﾉ⠀Forget it! 2
(<-_-)ノ⠀Forget it! 3
(^-^*)/⠀Forget it! 4
＼(-_- )⠀Forget it! 5
＼( ･_･)⠀Forget it! 6
＼(-o- )⠀Forget it! 7
ヾ(-_-<)⠀Forget it! 8
Σ(<´□｀)ﾉ⠀Forget it! 9
(/・0・)⠀Side Arms 1
(ノ^∇^)⠀Side Arms 2
(ヾﾉ･ω･`)⠀Side Arms 3
(ﾉﾟ∇ﾟ)⠀Side Arms 4
ヾﾉ≧∀≦)o⠀Side Arms 5
川o･-･)ﾉ⠀Hiding 1
┻┳|･ω･)ﾉ⠀Hiding 2
]ｮ◡◕ั⁎)ﾉ✰⁎*⠀Hiding 3
|ʘ‿ʘ)╯⠀Hiding 4
|･ω･`*)ッ⠀Hiding 5
|/// |(ω･ )ﾉ| ///|⠀Hiding 6
|/// |ω･｀*)ﾉ| ///|⠀Hiding 7
|｡･益･)ﾉ⠀Hiding 8
(ﾉ)’ω`(ヾ)⠀Miscellaneous 1
*+( ๑´•ω•)۶”⠀Miscellaneous 2
(๑ò◊ó ﾉ)ﾉ⠀Miscellaneous 3
‘`,､(((ꏿwꏿ<)))⠀Miscellaneous 4
(´っω･o)⠀Miscellaneous 5
⁽(ી₍₍⁽⁽(ી(◟̊◞̊)ʃ)₎₎⁾⁾ʃ)₎₎⠀Miscellaneous 6
且_(ﾟ◇ﾟ；)ノﾞ⠀Miscellaneous 7
(ʻ͈ჲ̫ʻ͈)◞⠀Miscellaneous 8
o(*･ｰ･)〇⠀Miscellaneous 9
໒(◕ヮ◕)〜⊹⠀Miscellaneous 10
╰( ^o^)╮⠀Miscellaneous 11
╭(°ﾛ°”)╯⠀Miscellaneous 12
(；ﾞﾟ’ωﾟ’):⁾⠀Miscellaneous 13
(੭ ᐕ)੭*⁾⁾⠀Miscellaneous 14
˛(ˊʙˋ)੭˒˒⠀Miscellaneous 15
(･ｪ-)⠀Dash Winks 1
(－ｏ⌒)⠀Dash Winks 2
（＾＿－）⠀Dash Winks 3
(^_-)⠀Dash Winks 4
（＾_-）⠀Dash Winks 5
（＾＿－）≡★⠀Dash Winks 6
（＾＿−）⠀Dash Winks 7
(^_−)☆⠀Dash Winks 8
(⌒.−)＝★⠀Dash Winks 9
d(-_^)⠀Dash Winks 10
(｡•̀ᴗ-)✧⠀Dash Winks 11
Y（・ω‐）Y⠀Dash Winks 12
(^_-)—☆⠀Dash Winks 13
(*・∀-)☆⠀Dash Winks 14
(´ ◕◞౪◟-)-☆⠀Dash Winks 15
(ﾉ･_-)☆⠀Dash Winks 16
★<><<d(,,･ε´-,,)⌒☆⠀Dash Winks 17
ヾ(о-ω･)ﾉ⌒★⠀Dash Winks 18
（　＾▽-）∠※☆⠀Dash Winks 19
♪├(*Θ∇ー)┤‐☆⠀Dash Winks 20
☆｡ﾟ+.(人-ω◕ฺ)ﾟ+.ﾟ⠀Dash Winks 21
(。・艸-。)-☆　ｗiйκ⠀Dash Winks 22
(。^_・)ノ⠀^ Style Winks 1
（＾＿・）⠀^ Style Winks 2
（○゜ε＾○）⠀^ Style Winks 3
＼（^０＾）／⠀^ Style Winks 4
~(＾◇^)/⠀^ Style Winks 5
♪(ﾟ▽^*)ﾉ⌒☆⠀^ Style Winks 6
v(*’-^*)ｂ⠀^ Style Winks 7
v(°∇^*)⌒☆⠀^ Style Winks 8
σ(ﾟｰ^*)⠀^ Style Winks 9
(ﾟ∇^*)⠀^ Style Winks 10
☆⌒(*＾-°)v⠀^ Style Winks 11
v(*’-^*)-☆⠀^ Style Winks 12
(*^-°)v⠀^ Style Winks 13
(v^ー°)⠀^ Style Winks 14
く(^ｰﾟ)ﾉ⠀^ Style Winks 15
(*＾∀ﾟ)ъ⠀^ Style Winks 16
☆⌒（＊＾∇゜）v⠀^ Style Winks 17
☆～（ゝ。∂）⠀ゝStyle Winks 1
ヾ(*ゝω・*)ﾉ⠀ゝStyle Winks 2
ｄ(ゝc_,・●)⠀ゝStyle Winks 3
d(*ゝωб*)⠀ゝStyle Winks 4
(๑ゝᴗම๑) ৷ਕკ~ෆ⠀ゝStyle Winks 5
ヽ(。ゝω･)ﾉ☆<:*⠀ゝStyle Winks 6
(ゝω･)ﾉ⠀ゝStyle Winks 7
（ゝ。∂）⠀ゝStyle Winks 8
(´ゝз・`)ﾉ⌒☆⠀ゝStyle Winks 9
(´ゝз・)─☆⠀ゝStyle Winks 10
(๑ゝڡ◕๑)⠀ゝStyle Winks 11
ヽ(。ゝω・)ノ☆⠀ゝStyle Winks 12
d(｡ゝд･)⠀ゝStyle Winks 13
☆（*ゝω・*）ﾉ⠀ゝStyle Winks 14
ヾ(*ゝω・*)ノ⠀ゝStyle Winks 15
o（｀ゝ曲°〃）b⌒☆⠀ゝStyle Winks 16
☆*．･(*ゝ∀・*)ﾉ⠀ゝStyle Winks 17
☆⌒（●ゝω・）⠀ゝStyle Winks 18
(ゝ∀･)⠀ゝStyle Winks 19
★⌒(●ゝω・)ｂ⠀ゝStyle Winks 20
(*ゝω・)ﾉ⠀ゝStyle Winks 21
d(ゝ∀･)⠀ゝStyle Winks 22
(●ゝ∀･)ﾉ⠀ゝStyle Winks 23
(ゝω´･)b⌒☆⠀ゝStyle Winks 24
☆=(ゝω･)⠀ゝStyle Winks 25
(○ゝω・○)ﾉﾟ+.☆⠀ゝStyle Winks 26
ヽ(｡ゝ∀･)☆･ﾟ:*☆⠀ゝStyle Winks 27
★~(◠︿◕✿)⠀Winking Flower Kaomojis With Stars 1
★~(◠﹏◕✿)⠀Winking Flower Kaomojis With Stars 2
★~(◡﹏◕✿)⠀Winking Flower Kaomojis With Stars 3
★~(◠ω◕✿)⠀Winking Flower Kaomojis With Stars 4
★~(◡‿⊙✿)⠀Winking Flower Kaomojis With Stars 5
★~(◡△⊙✿)⠀Winking Flower Kaomojis With Stars 6
★~(◠﹏⊙✿)⠀Winking Flower Kaomojis With Stars 7
★~(◡﹏⊙✿)⠀Winking Flower Kaomojis With Stars 8
★~(◠‿◕✿)⠀Winking Flower Kaomojis With Stars 9
★~(◡ω◕✿)⠀Winking Flower Kaomojis With Stars 10
★~(◠△◕✿)⠀Winking Flower Kaomojis With Stars 11
★~(◠△⊙✿)⠀Winking Flower Kaomojis With Stars 12
★~(◠ω⊙✿)⠀Winking Flower Kaomojis With Stars 13
★~(◡﹏◡✿)⠀Winking Flower Kaomojis With Stars 14
★~(◡︿⊙✿)⠀Winking Flower Kaomojis With Stars 15
★~(◠︿⊙✿)⠀Winking Flower Kaomojis With Stars 16
★~(◡ω◡✿)⠀Winking Flower Kaomojis With Stars 17
★~(◡ω⊙✿)⠀Winking Flower Kaomojis With Stars 18
(*⸰‿-) (☉_☉) (-‿◦☀)⠀Two People Winking at Someone and Making them Uncomfortable 1
๏[-ิ_•ิ]๏⠀Complex Winking 1
✩⃛˞(๑ꆨ৺ꉺ๑)⠀Complex Winking 2
(๑ꄱͦॢ◡ु ˂̶͈́๑)⠀Complex Winking 3
｡ﾟ+.ღ(ゝ◡ ⚈᷀᷁ღ)⠀Complex Winking 4
˄̻ ̊σ(˃̴͈◡ुමੈॆ⋆)˄̻ ̊~♡⃛⠀Complex Winking 5
ෆ⃛(ᶿ̴͈᷇◟̵◞̵˂͈᷆ ფ⠀Complex Winking 6
⌓⌓⌕(˃̴◡ुؔ՞ઁ)♡⃛⠀Complex Winking 7
(˃̶᷄︿๏）⠀Complex Winking 8
(∗ᵒ̶̶̷̀ω˂̶́∗)੭₎₎̊₊♡⠀Complex Winking 9
۴(๑ꆨ◡ꉺ๑)⠀Complex Winking 10
( ᐤ◞◡ु̑◟˂ )⁺ₒ✩⠀Complex Winking 11
（◍●◡ु‹◍)☆⠀Complex Winking 12
ʸ(➜◡ु⚈᷉)♡⃛⠀Complex Winking 13
⁽͑ʺ˚˙̫ʿʺ⁾̉ˀ*⠀Complex Winking 14
(o‿∩)⠀Miscellaneous Winks 1
৲( ᵒ ૩ᵕ )৴♡*৹⠀Miscellaneous Winks 2
(๑◕ㅂ▰)⠀Miscellaneous Winks 3
ಠ‿↼⠀Miscellaneous Winks 4
( ͡~ ͜ʖ ͡°)⠀Miscellaneous Winks 5
(◕ฺー≦)ノ⠀Miscellaneous Winks 6
☆(<><<ω・)⠀Miscellaneous Winks 7
(･ω<<<<)☆⠀Miscellaneous Winks 8
(・ω<<<<)⠀Miscellaneous Winks 9
ｖ(･Д<<<<*)☆⠀Miscellaneous Winks 10
(＞ω)＝☆⠀Miscellaneous Winks 11
(*ﾟｰ~)^☆⠀Miscellaneous Winks 12
^.~⠀Miscellaneous Winks 13
ヾ(･ω･｀*)【｡ﾟ+.нё<<о｡ﾟ+.】(*´･ω･)ﾉﾞ⠀Hello 1
ﾟ+｡нё<<о☆(*-`ω´- )人(ц｀ω´ц*)нё<<о☆｡+ﾟ⠀Hello 2
(○≧з)○oо｡<#8230<【нё<<о】<#8230<｡oо○(ω≦★)⠀Hello 3
【o´∀｀】ﾉ┣┫Ё┗└О☆⠀Hello 4
(◎´▽｀)ゞнё<<о(´▽｀◎)нё<<о⠀Hello 5
♡հҽӀӀօ♡* ૂི•̮͡• ૂ ྀෆ⃛﹡೫٭ॢ*⋆♡⁎೨ ♡⃛ෆ͙⃛ ॢ٭ॢ*⋆♡⁎೨⠀Hello 6
(☆´益`)c<<<<【。+ﾟъойjоця。+ﾟ】⠀Hello 7
|*｡´Д｀|┛<<<<<<<< +｡:.ﾟβyёβyё♪⠀Goodbye 1
(*ﾟ∀ﾟ)っ［.+:｡★βyё βyё★.+:｡］⠀Goodbye 2
(●´・∀・｀)ﾉ”βｙё-βｙё☆⠀Goodbye 3
ﾟ+.βуёﾟ+.(つ●_｀*)ﾉ”ﾟ+.βуёﾟ+.⠀Goodbye 4
|。･ω･|づ　βyё βyё☆彡⠀Goodbye 5
(✿◕ ‿◕ฺ)ノ))｡₀: *ﾟ✲ฺβyё βyё✲ฺﾟ*:₀⠀Goodbye 6
★ВУёヽ(‘∀`○)ﾉВУё☆⠀Goodbye 7
ε(*´･∀･｀)зﾞβуёβуё”ε(´･∀･｀*)з⠀Goodbye 8
ヾ(◆’｀◇)ｼ.+ﾟ*ВчёВчё｡:ﾟ+ヾ(◇´’◆)ｼ⠀Goodbye 9
ヾ(ﾟεÅ) βyё βyё☆彡⠀Goodbye 10
꒰⁎ ✪̼ ◡ ✪̼` ⁎꒱﹡Տҽҽ վօմ⁎☪*✩⠀Goodbye 11
│*-ω-)ノβyё*･゜☆βyё.｡.:*･⠀Goodbye 12
☆｡:*ﾟβуёβуё☆｡:*ﾟゞ(･ω･*ヽ)⠀Goodbye 13
(●´卅｀)☆βｙё☆(´卅｀●)⠀Goodbye 14
ε(*´・∀・)з゛βуё βуё<#8221<ε(・∀・｀*)з⠀Goodbye 15
^(*･｡･)ﾉ~~~βｙё　βｙё♪⠀Goodbye 16
┏|*´Д｀|´Д｀*|┛βЧёβЧё♪⠀Goodbye 17
(人-ω-)｡o.ﾟ｡*･★βyё βyё★･*｡ﾟo｡(-ω-人)⠀Goodbye 18
【o´Д｀o】†｡o○o｡SёёYou｡o○o｡†【o´Д｀o】⠀Goodbye 19
ヾ(｡<><<д<<<<)ﾉ *+:｡.｡:+*ВчёВчё*+:｡.｡:+* (ﾉД｀｡)ﾉｼ⠀Goodbye 20
★☆。.:*:･”ﾟ★βyёヾ(*ﾟ∇ﾟ*)ﾉβyё★｡.:*:･”☆★⠀Goodbye 21
★☆。.:*:･”ﾟ★βyёヾ(⌒∇⌒)ﾉβyё★｡.:*:･”☆★⠀Goodbye 22
★☆。.:*:･”ﾟ★βyёヾ(o･(ェ)･o)ﾉβyё★｡.:*:･”☆★⠀Goodbye 23
ε(●’-‘)з†.。*・☆вуe вуe☆･*｡.†ε(‘-’●)з⠀Goodbye 24
ヾ(‘ｖ｀○((ﾟ+｡:.ﾟВЧЁ♪ВЧЁﾟ.:｡+ﾟ))○’ｖ｀)ｼ⠀Goodbye 25
★☆。.:*:･<#8221<ﾟ★βyёヾ(⌒∇⌒)ﾉβyё★｡.:*:･<#8221<☆★⠀Goodbye 26
★☆。.:*:･<#8221<ﾟ★βyёヾ(*ﾟ∇ﾟ*)ﾉβyё★｡.:*:･<#8221<☆★⠀Goodbye 27
┃*´・ω・┠┛ﾟ･:,｡★ΒΥЁΒΥЁﾟ･:,｡★⠀Goodbye 28
Ⴚ࿁࿁ძ ൬໐ɼႶ૧ฑႺ⠀Good Morning 1
☆❋──❁ɢ∞פ ʍօ®ɴɪɴɢ❃──❋⠀Good Morning 2
Gооd Мояйiи>＿〆(●-Дゞ●)⠀Good Morning 3
Gооd Мояйiи>…..φ|o-Дゞo|⠀Good Morning 4
୨୧˖⋆.♡Ꮹℴℴ ⅆ ണℴ ɾஸⅈஸϧ♡.⋆˖୨୧⠀Good Morning 5
♡ͫ ͦ ͬⁿⁱⁿᵍ꒰ •ᴗ•｡꒱۶⠀Good Morning 6
Ꮹꄲꄲძ ℳꄲᖇᘉɪ̊ᘉ꒸.͙✼̥୭⁺⠀Good Morning 7
꒸ᵒ০ⅆ ᵐꄲᖇ∩ⁱ∩ᵍ ♡ ⡷⠶⢾⠀Good Morning 8
㇏( ෆั ⌣ ෆั )ﾉցօօժ ʍօɾղíղց❣⠀Good Morning 9
☻⋆˚✩Ꮹ∞ძ ოǫɾлілϧ ༘*ೄ˚☻⠀Good Morning 10
ﾟ+o｡o｡o+ﾟＧｏｏｄМｏяйｉйｇ(★´∀｀☆)ﾉﾟ+o｡o｡o+ﾟ⠀Good Morning 11
ﾟo｡oﾟGооd Мояйiи>ﾟo｡oﾟヾ(★-дゞ★)⠀Good Morning 12
┗|o･⊥･|ﾟo｡oﾟＧooｄ мｏγйｉйｇﾟo｡oﾟ|･⊥･o|┓⠀Good Morning 13
●*○ｇｏｏｄヾ(ﾟ∀ﾟ　)三(　ﾟ∀ﾟ)ﾉﾞмｏяйｉйｇ○*●⠀Good Morning 14
★.:ﾟ+｡☆ (◎＾□＾)bＧＯＯＤМＯЯЙＩＧd(＾□＾◎)☆.:ﾟ+｡★⠀Good Morning 15
(｡-3-)Ｇｏｏｄ мｏγйｉйｇ(uεu｡)⠀Good Morning 16
Gооd Мояйiи>┗┐(｀∀´○)oﾎﾞｺｯ　(ﾟдﾟ<<<)ｪ･･･⠀Good Morning 17
((*´_●｀☆ﾟ+.Gооd Могйiй>.+ﾟ☆´●_｀*))⠀Good Morning 18
=。(◆’v｀b)b。+G○○D　ЁⅤЁЙΙЙG⠀Good Evening 1
G◎◎D　ЁⅤЁЙΙЙG|´・ω・)ﾉ~⠀Good Evening 2
(●b’ｖﾟd)ﾟ+o｡G○◎D　ЁⅤЁЙΙЙG｡o+ﾟ(ｂﾟｖ’d●)⠀Good Evening 3
꒰ ꒡⌓꒡꒱ᏩɵɵᎴ ɳɩɠɧ✟⠀Good Night 1
(*´з｀)ＧＯＯＤ ＤЯЁΑΜ(´ε｀*)⠀Good Night 2
(*-_●p【ﾟ+｡Ｇooｄ йｉｇнт｡+ﾟ 】q⠀Good Night 3
(人*′ω`)★Ｇ００Ｄ ЙΙＧΗТ☆(′ω`*人)⠀Good Night 4
(人uc_u●)[>ооd йi>нт]+.☆ﾟ+.☆⠀Good Night 5
【☆swee< dream☆】(●ＵωU).zZZ⠀Good Night 6
Gооd Йi>h<(´ε｀*)ιον∈ Υου⠀Good Night 7
ヾ(ﾟÅﾟ*)ﾉGооd Йi>h<☆.｡.:*･ﾟ⠀Good Night 8
(＊<#8217<͜<#8217< )⋆ᎶᎾᎾⅅ ℕᏐᎶℍᎢ ☾⠀Good Night 9
⋆｡˚ᎶᎾᎾⅅ ℕᏐᎶℍᎢ⋆｡˚✩⠀Good Night 10
.｡.:*･ﾟ☆ｓωεετ*･ﾟｄｒεαｍ☆.｡.:*･ﾟ”￡(｡･”･)-†⠀Good Night 11
(●´v｀人)*:.｡o○>ood йｉｇнт○o｡.:*(人´v｀○)⠀Good Night 12
[｡ﾟo｡ＧＯＯＤ ЙＩＧＨT｡oﾟ｡](*ゝД･)ﾉ))⠀Good Night 13
∑Σ(☆′Д’b)bﾞ *:..｡o○GOOD ЙΙGНΤ○o。..:*⠀Good Night 14
☆<:*:<★<:*ｇｏｏｄ(*^∇^*)ﾉйｉｇнт*:<★<:*☆⠀Good Night 15
o(u＿u◎{{ｇｏｏｄ йｉｇнт}}◎u＿u)o⠀Good Night 16
p[☆ﾟ+.ＧООＤ ЙΙＧΗТ.+ﾟ☆]q´・∪・)ﾉ゛⠀Good Night 17
βёd]ぅω｀)ﾉｼ～3 ﾟ+｡:.ﾟGood Йi>h<ﾟ.:｡+ﾟ⠀Good Night 18
ヾ(●_ﾟ【ﾟo｡Ｇooｄ йｉｇнт｡oﾟ】ﾟ_○)ﾉ⠀Good Night 19
ヾ(ﾟωﾟ｀=*:<<<:*Ｇood Йι>нт*:<<<:*=´ﾟωﾟ)ﾉｼ⠀Good Night 20
(●´ω｀)｡ﾟ.o｡коηβαηΗα｡o.ﾟ｡(´ω｀●)⠀Good Night 21
(♡u‿u)⊹⊱【.:*ﾟ..:｡:.::.*OУаsυмi:..:*ﾟ..:｡:.::.*】⊰⊹⠀Good Night 22
(*´-ω-)ﾉ ﾟ+｡:.ﾟＧｏｏｄ йｉｇнтﾟ.:｡+ﾟ⠀Good Night 23
*॰ْ✧ً⋆｡˚ᎶᎾᎾⅅ (ව̐ ˒̫̮ ව̐) ℕᏐᎶℍᎢ⋆｡˚*ْ✧ं॰*⠀Good Night 24
⋆ᗰદ૨૨ʏ⋆ᐠ₍⁽˚⑅̆˚⁾₎ᐟ⋆ᘓમ૨ıડτന੨ડ⋆⠀Holidays 1
～ΜᎧrRγ сняᎥᎦτмᏜs*～⠀Holidays 2
༶･･ᗰદ૨૨ʏ ᘓમ૨ıડτന੨ડ･･༶⠀Holidays 3
ପ(๑•̀ᴗ-♡ॢ)fෆr yෆu*೨⋆*✩⠀Holidays 4
(꒪ิཫ꒪ )ノิิิ ḟ৹ʳᵧ৹ᵤ⠀Holidays 5
(⑅ᵒ̴̶̷᷄ωᵒ̴̶̷᷅⊞ོॢ)fෆr yෆu⋆*⋆✩⠀Holidays 6
v(*´・ｖ・｀)φ…..|Мёγγё Х’мд∫☆|⠀Holidays 7
[｀+･ｖ･+]мёяяч　х’　мдs[+･ｖ･+´]⠀Holidays 8
(◎･ω･)っ〔ﾟ+｡ργё∫ёйт｡+ﾟ〕⠀Holidays 9
(yωy*) мёггу снгisтмдsﾟ･*:.｡. ☆⠀Holidays 10
ﾟ･:*:･｡(〃･ω･)ﾉ由☆*:<<<:*Ｍｅｒｒｙ　Ｘ’ｍａｓ*:<<<:*☆由ヽ(･ω･〃)｡･:*:･ﾟ⠀Holidays 11
ﾟ･:*:･｡♪☆彡^･∋／[☆<:* Merry X<#8217<mas*:<☆ ]＼∈･^ミ☆♪｡･:*:･ﾟ⠀Holidays 12
･:★.．☆.<*≡ゝ(ﾟｖﾟ=)Merry( ﾟｖﾟ )X’mas(=ﾟ▽ﾟ)ﾉ`･:.☆．.<★*⠀Holidays 13
。o○★ヾ(´ﾟ∀ﾟ`*)Ｍｅｒｒｙ☆ Ｘｍａｓ(*´ﾟ∀ﾟ`)★。o○⠀Holidays 14
(〃´ω)ﾉ『☆｡o○☆мёЯЯЧ χ<#8217<мдs☆○o｡☆』ヽ(ω`〃 )⠀Holidays 15
(☆`･Θ･)v[゜ﾟ*☆мёγγч Хмд∫☆*ﾟﾟ]v(･Θ･´★)⠀Holidays 16
ヾ(☆ゝ∀・)ﾉ※ﾟﾟＳ｡*※Йﾟﾟ｡*※Оﾟﾟ｡※Ｗ*ヾ(ゝω・｀*)ﾉ⠀Holidays 17
ヾ(*´Д｀*)ノ*+:.★МёЯЯУ　X’маs☆.:+*ヾ(*´Д｀*)ノ⠀Holidays 18
Σ(★´・ェ・)=C<<<<☆・゜:*мёяяу Ⅹмαδ*:゜・☆⠀Holidays 19
ﾟ･:，｡★＼(*’v`*)♪merryXmas♪(*’v`*)/★，｡･:･ﾟ⠀Holidays 20
*※*(。uωu)(uωu。)*※*　Мёγγч Х’мд∫⠀Holidays 21
.｡+ﾟ*[o･ω･]ﾉ*мёЯЯЧ CнЯIsтмДs*.｡+ﾟ*⠀Holidays 22
($’v｀d)･.｡*MёяячＸ’мдｓ*。.･(ｂ´ｖ’$)⠀Holidays 23
(☆ﾟｖ｀)э【*:<:*мёяячｘ’мдｓ*:<:*】ε(´ｖ’☆)⠀Holidays 24
o<<<<( ´∀｀)っ┌iii┐　Ｍｅｒｒｙ　Ｘ’ｍａｓ⠀Holidays 25
ヾ(uωu*[++мёггу снгisтмдs++]*uωu)ﾉ⠀Holidays 26
♫Happy☻໌*✰☻ັBir<hday☆+｡⠀Holidays 27
✯ℋᵅᵖᵖᵞ ℬⁱʳᵗᑋᵈᵃᵞ✯⠀Holidays 28
୨୧ᕼᗩᑭᑭY ᗷIᖇTᕼᗞᗩY୨୧⠀Holidays 29
*ℋᵅᵖᵖᵞℬⁱʳᵗᑋᵈᵃᵞ*⠀Holidays 30
～ΒΙяΤΗDΑΥ LOVE❤(◍•ᴗ•◍)/⠀Holidays 31
◌⑅⃝ℋ⍲ᵖᴘᵞ ℬⁱᖇᐪમᵈ੨ყ♡ෆ ͙⁎♡⑅⃝◌⠀Holidays 32
∮(´･ω･)＜ндρρч ьдγтнｄдч∮⠀Holidays 33
ヾ(・∀・)ﾉ <<<<<<<< Happy Bir<hday♪⠀Holidays 34
(*´p∀q｀*)ﾉ《*ﾟ:+.｡☆ＨДРРЧ ВＩЯтＨＤДЧ☆｡.+:ﾟ*》ヾ(*´p∀q｀*)⠀Holidays 35
(●ﾟ∀ﾟ)ﾉ♭ﾟ’･:*♪:.ндρρч ьｉγтнｄдч.:♪*:･’ﾟ♭ヾ(ﾟ∀ﾟ○)⠀Holidays 36
(☆-Ⅴ･)p||*:<<<:*ＨДРРЧ ВＩЯтＨ ＤДЧ*:<<<:*||q･Ⅴ-★)⠀Holidays 37
(☆<><<∪<<<< b)b｡*†*｡★Ｈдρρч Вｉγтн Ｄдч☆｡*†*｡d(d<><<∪<<<<★)⠀Holidays 38
*+:<нарру<<:+*(●´∀`人´∀`●)*+:<вiятнＤау<<:+*⠀Holidays 39
♪вiятнＤауヽ(´Д｀*)ﾉ ♪ヽ(*´Д｀)ﾉDайсё♪⠀Holidays 40
o(★´∀｀★)o☆*:<<:*★ＨДРРЧ ВＩЯтＨＤДЧ★*:<<:*☆o(☆´∀｀☆)o⠀Holidays 41
РЯЁＳЁЙТ　ＦОЯ　УОЦ・・・(*´∀｀*)σ[畄][畄][畄]⠀Holidays 42
.*･ﾟ☆Happyヾ(*∇*)ﾉBir<hday☆ﾟ･*.⠀Holidays 43
.*･ﾟ☆ндрру(*⌒▽⌒*)b вiятнDду☆ﾟ･*⠀Holidays 44
.*･ﾟ☆ндрруヾ(*^▽^*)ﾉвiятнDду☆ﾟ･*.⠀Holidays 45
ヽ（≧ω≦）｛☆HAPPY★BIRTHDAY☆｝（≧ω≦）/⠀Holidays 46
.*･ﾟ☆ндрруヾ(*＾-＾*)ﾉвiятнDду☆ﾟ･*.⠀Holidays 47
⋈‧̍̊·̊‧̥°̩̥˚̩̩̥͙°̩̥‧̥·̊‧̍̊наppעෆ⃛вiянтᏂᎴע‧̍̊·̊‧̥°̩̥˚̩̩̥͙°̩̥‧̥·̊‧̍̊⋈⠀Holidays 48
(*´uωu)Ｈдρρч☆Вiятнｄдч*+:｡.｡:+*⠀Holidays 49
.*･ﾟ☆Happyヾ(*ε*)ﾉBir<hday☆ﾟ･*.⠀Holidays 50
(●´Д｀)＜Д Ндррч Йёш Чёдя♪＞(´Д｀●)⠀Holidays 51
(U´･ｪ･)ﾉ♪ﾟ+.Д нДρРч ЙёЩ чЁдЯ.+ﾟ♪ヾ(･ｪ･｀U)⠀Holidays 52
(σ^▽^)σﾟ･｡･ﾟ+｡+ﾟ*:<<:*ＨДРРЧ★ЙЁЩ★ЧЁДЯ*:<<:*ﾟ+｡+ﾟ･｡･⊂(^∀^⊂)⠀Holidays 53
ﾟ*｡☆ヾ(´∀｀)Д Ндррч Йёш Чёдя！(´∀｀)ノ☆｡*ﾟ⠀Holidays 54
★～*~*～☆ндρρч(+≧3≦)йёщ(≧ε≦+)чёдγ☆～*~*～★⠀Holidays 55
♪ﾟ+.ｏ(<#8216<v`★)Α ｈαρρψ ηεｗ ψεαγ (★<#8217<v`)♪ﾟ+.ｏ⠀Holidays 56
(●´∀｀)ノ*:<<<:*Д нДρРч ЙёЩ чЁдЯ*:<<<:*ヽ(´∀｀●)⠀Holidays 57
(●´艸｀)。゜.o。Д ＨДРРЧ ЙЁЩ ЧЁДЯ。o.゜。(´艸｀●)⠀Holidays 58
(●≧ノд≦)<<<<Д нДρРч ЙёЩ чЁдЯ゜゜*☆⠀Holidays 59
(U´・ェ・)ノ♪゜+.Д нДρРч ЙёЩ чЁдЯ.+゜♪ヾ(・ェ・｀U)⠀Holidays 60
(ノ´∀｀)ノ*.ﾟ･｡:*:．ﾟ・☆A HAPPY NEW YEAR☆・ﾟ．:*:｡･ﾟ.*ヽ(´∀｀ヽ)⠀Holidays 61
*:<<<:*Д ＨДРРЧ ЙЁЩ ЧЁДЯ*:<<<:*Σ(゜艸゜*)⠀Holidays 62
゜゜.:。+ ゜+。:.д ндρρч йёщ чγдγ.:。+゜ ゜+。:.゜⠀Holidays 63
.:。+゜ Д ＨДРРЧヽ(*´Д｀*)ノЙЁЩ ЧЁДЯ ゜+。:.゜⠀Holidays 64
゜+.*:<<<<<:* Α ｈαρρψ ηεｗ ψεαγ *:<<<<<:*ﾟ+.⠀Holidays 65
゜・。・゜+。+゜*:<<:*ＨДРРЧ★ЙЁЩ★ЧЁДЯ*:<<:*゜+。+゜・⠀Holidays 66
☆*ﾟ ゜ﾟ*☆Д нαρρy ЙёЩ ЧёαЯ!!☆*ﾟ ゜ﾟ*☆⠀Holidays 67
:*:.｡.:*(´∀｀*)Д Ндррч Йёш Чёдя*:.｡.:*:⠀Holidays 68
(●≧ﾉдﾉ≦)<<<<Д нДρРч ЙёЩ чЁдЯ゜ﾟ*☆⠀Holidays 69
Д ＨДРРЧЙЁЩ ЧЁДЯ_φ(´ｪ｀*U⠀Holidays 70
(●´Д｀)＜Д Ндррч Йёш Чёдя♪＞(´Д｀●)⠀Holidays 71
*:<<<:*Д ＨДРРЧ ЙЁЩ ЧЁДЯ*:<<<:*Σ(ﾟ艸ﾟ*)⠀Holidays 72
(m▼w▼)m[ ☆･ﾟ:*нαΙΙощёёй*:ﾟ･☆]m(▼w▼m)⠀Holidays 73
【ﾟ+｡τγιсκ★σγ★τγεατﾟ+｡】Ψ(oﾟ∀ﾟo)Ψ⠀Holidays 74
～(☆´∀｀っ)っ【。:+:†+Тяiск оя Тяёат+†:+:゜】q(ゝε・★)～⠀Holidays 75
～(m`･Å･´)m *†*Тяiск оя тяёат*†* Ψ(ゝc_･´☆)⠀Holidays 76
人*´∀｀)＜Тяiск оя тяёат♪＞(´∀｀*人⠀Holidays 77
ʕ•̫͡•ॽु✚⃞ྉ*✲ﾟ*｡⋆ ℳෆ<h ℯr’s ⅅ ੨Ꮍ⠀Holidays 78
*.+(◇´v’σ【 ДρяiΙFооΙ 】ョ’v｀◆)+.*ﾟ⠀Holidays 79
Мотнёя’δ Dαу:*:♪・゜’☆…((φ(‘ー’*)⠀Holidays 80
【☆･ﾟ:*сносоΙαтё*:ﾟ･☆ 】ｮω｀｡)⠀Holidays 81
ヾ(*´・∀)ﾉ*:..｡o○∫μммёγ υдcдтioй○o｡..:*ヾ(∀・｀*)ﾉ⠀Holidays 82
::.*゜:.。:.ⅤдＬ ёйтiйёＤду::.*゜:.。:.〆(uωu●)⠀Holidays 83
☆ﾟ+｡(｀･ｪ´･+｡)b【Vд<ёйтiйё dду】d(｡+･｀ｪ･´)｡+ﾟ☆⠀Holidays 84
☆ﾟ+o｡o｡o+ﾟ ⅤΑгЁЙтΙЙЁ ＤΑY ﾟ+o｡o｡o+ﾟ☆⠀Holidays 85
★´・ω・ｐ≪*+｡ﾟ･ⅤД￡ЁЙТΙЙЁＤДЧ･ﾟ｡+*≫ｑ・ω・｀★⠀Holidays 86
٩(๑•◡-๑)۶ⒽⓤⒼ❤⠀Love Themed 1
(๑′ᴗ‵๑)Ｉ Lᵒᵛᵉᵧₒᵤ♥⠀Love Themed 2
꒒ ০ ⌵ ୧ ♡⠀Love Themed 3
࿒ℓ࿆࿆࿆ෆ࿆౮࿆୧࿆♡࿆༝࿆༚࿆༝࿆༚࿆ ࿒⠀Love Themed 4
꒰๑˃͈꒵˂͈๑꒱୭̥*ﾞ̥♡⃛ Ɛn꒻öႸ⠀Love Themed 5
♡+* Ɗɑɫë*+♡⠀Love Themed 6
(ㅅꈍ﹃ꈍ)*>ᵒᵒᒄ ᵑⁱ>ᑋᵗ*(ꈍ﹃ꈍㅅ)♡⠀Love Themed 7
˪৹⌵ೕ꒰๑•‧̮ૣ•ૣ๑꒱⠀Love Themed 8
♡+:｡.｡❣LﾛVЁ❣｡.｡:+♡⠀Love Themed 9
◌⑅⃝●♡⋆♡⃝ ˻˳˯ₑ♡⃝⋆●♡⑅⃝◌⠀Love Themed 10
*♡೫̥͙*:・ℋɑppყ Ϣәԁԁıɲɠﾟ･:* ೫̥͙♡*⠀Love Themed 11
(ෆˊ͈ ु꒳ ूˋ͈ෆ) ˡºᵛᵉ❤⃛⠀Love Themed 12
✧˖°(˶‾᷄ ॢ⁻̫ ‾᷅˵ॢ)◌⑅⃝*॰ॱᗪ੨ⅈઽᵘᵏⁱ✧˖°⠀Love Themed 13
◌⑅⃝*॰ॱᒄᵒᵏⁱ(꜆˘͈ෆ˘͈꜀)ᒄᵒᵏⁱ◌⑅⃝*॰ॱ⠀Love Themed 14
ιоνё(●´Å`)ε`○)снц♪⠀Love Themed 15
*.･｡ヾ(◍ᄏᴗ))ﾉﾟ+.β੨ყ♡ β੨ყ+.°⠀Love Themed 16
Ꮭσνєஐ(๑´ლ`๑)♡⠀Love Themed 17
•*ꑄೞᵉᵉ৳～❥˪৹⌵ೕ⋆.∗̥✩⁺˚⠀Love Themed 18
˻ᵒ♡ͮᵉ⸝⸝⑅⠀Love Themed 19
✨Lᵒᵛᵉᵧₒᵤ⠀Love Themed 20
˪৹⌵ೕෆ⃛(˃͈ દ ˂͈ )⠀Love Themed 21
ⓛⓞⓥⓔ♡⠀Love Themed 22
Ⓜɨ ʂ ʂ Ⓨσư❤ (◡ε◡ฺ❤)⠀Love Themed 23
Ⓜɨ ʂ ʂ Ⓨσư (̥ ̥এ́ ̼ এ̥̀)̥̥⠀Love Themed 24
ℓօⓥɪɴ<#8217< ϋ*॰¨̮ ♡➳♡ₓₒₓₒ⠀Love Themed 25
ʚ♡⃛ɞLᵒᵛᵉᵧₒᵤʚ♡⃛ɞ(ू•ᴗ•ू❁)⠀Love Themed 26
(ღˇ◡ˇ)♥ℒᵒᵛᵉᵧₒᵤ♥⠀Love Themed 27
ᎥᏝᵒᵛᵉϋෆ*⠀Love Themed 28
( ´͈ ॢꇴ  `͈)੭ु⁾⁾·°˖ᔆᵘᵗᵉᵏⁱ✧˖°⠀Love Themed 29
ℓ ❤ ϚϦοςӧԼձϮϵ❣⃛⠀Love Themed 30
(๑′ᴗ‵๑)Ｉ Lᵒᵛᵉᵧₒᵤ♡⠀Love Themed 31
Ｉ ￡ονё Υου…..φ┃*･ω･*┃⠀Love Themed 32
￡ονё Υου<#8230<..φ(〃∇〃 ))⠀Love Themed 33
ℒℴѵℯℒᎥѵℯ⠀Love Themed 34
✿*ﾟ¨ﾟ✎･ ✿.｡.:* *.:｡✿*ﾟ¨ﾟ✎･✿.｡.:* ♡LOVE♡LOVE♡ ✿*ﾟ¨ﾟ✎･ ✿.｡.:*⠀Love Themed 35
( ﾟ∀ﾟ)ﾉ【LOVE】⠀Love Themed 36
( ﾟ∀ﾟ)ﾉ　　　　　～【LOVE】⠀Love Themed 37
Σ(<ﾟ∀ﾟ)ﾉ　　　　　　　　　　　　三【LOVE:<*.’:|⠀Love Themed 38
ﾟ･*:.｡. ☆κｉss мё(人uзu*)ρｌёдsё☆.｡.:*･ﾟ⠀Love Themed 39
((*´３｀)｡o○ﾟ･*:.｡. ☆κｉss мё☆ﾟ･*:.｡.⠀Love Themed 40
ღԵհɑղƘՏღ( ؔ✪̤ ◡ ؔ✪̤` ๑)⠀Thank You 1
*⁎ᎢℋᎪɳᏦ ᎩӫᏌ⁎*⋆⠀Thank You 2
ପ(๑•̀ुᴗ•̀ु)* ॣ৳৸ᵃᵑᵏ Ꮍ৹੫ᵎ *ॣ⠀Thank You 3
꒰♥︎꒱४ᵃʳⁱᵍᵅᵗᵒ꒰´͈ॢદॢˋ͈♡꒱⠀Thank You 4
˓ٛ˃̵̢̡̢ˊ͈ˣੰॢˋ͈ॢٛٛ˂̵̡̢̡༿˒˒৳ɦ੨৸кઽ❣༚˚·° ஐ｡✼⠀Thank You 5
ෆ⃛ෆ⃛ෆ⃛ ♡♡[τ̲̅н̲̅a̲̅и̲̅κ̲̅ ч̲̅o̲̅u̲̅]ᴗ͈ₒᴗ͈♡⠀Thank You 6
Ƭʜᵃℕҡ ყօϋ୨୧ᐝ⠀Thank You 7
ෆ⃛ [τ̲̅н̲̅a̲̅и̲̅κ̲̅ ч̲̅o̲̅u̲̅]ｮᴗ ◕ั๑)ෆ⃛⠀Thank You 8
(ﾟ⊿ﾟ)৳৸ᵃᵑᵏ Ꮍ৹੫ᵎ♫ ªʳⁱ૭ªᵗ°♫⠀Thank You 9
(人❛ᴗ❛)♪тнайк　чоц♪(❛ᴗ❛*人)⠀Thank You 10
(人*´∪`)♪тнайк　чоц♪(´∪`*人)⠀Thank You 11
(*･艸･)｡+:*○тнайк　чоц｡+:*○⠀Thank You 12
｜*´I｀*｜тнДЙКЧоц⠀Thank You 13
(●*’v｀*人).o0[*ТНДЙК уОЦ*]⠀Thank You 14
●○ТНДЙК(oﾟ∀ﾟo)УﾛЦ♪○●⠀Thank You 15
░♡░┳┣I░A░Ⓝ░К▒❀▒УOЦ░♡░⠀Thank You 16
(๑ˊ͈ ॢꇴ ˋ͈)ᵃʳⁱᵍᵃᵗᵒ〜♡॰ॱ⠀Thank You 17
♡*.·ा৸੨꒖ઝ ഴ०꒵ ･:*♡⠀Thank You 18
⑅✩♡ᵗʱᵃᵑᵏઽ*♡♬＊°⠀Thank You 19
ᵗᑋᵃᐢᵏ ᵞᵒᵘ♡⃝⃜⠀Thank You 20
ℒℴѵℯ*¨*• ♡⠀Thank You 21
тндйк[○´・ω・]人[・ω・｀●] уoц⠀Thank You 22
(●・ω・)ﾉтнДЙκ∫　LIЙκ ヽ(･ω･○)⠀Thank You 23
Ƭ ɧ ձ ƞ Ƙ ʂ❤ (◦˘ З(◦<#8217<ںˉ◦) Ȼ ɧ ư ♡⠀Thank You 24
【★тндйκ чoμ.ﾟ+｡☆ 】ｮ´∀｀)⠀Thank You 25
ﾟ･*:.｡. .｡.:тндйк уoц　(○・∀・)b 　тндйк уoцﾟ･*:.｡..｡:*⠀Thank You 26
(｡ﾉuωu)ﾉ≡【｡*†*｡☆тндйκчｏμ☆｡*†*｡】⠀Thank You 27
(*´д｀)｡+ﾟ☆ﾟ+｡+:*┬ΗАикｓ｡+:*｡+ﾟ☆ﾟ+｡⠀Thank You 28
Ⓣⓗⓐⓝⓚ｡:.ﾟヽ(｡☉౪ ⊙♥)ﾉﾟ.:｡+ﾟ Ⓨⓞⓤ☆⠀Thank You 29
♥(✿ฺ´∀`✿ฺ)ﾉ ✿ฺ･:*:ТНДЙК УОЦ･･:*:･✿ฺ~⠀Thank You 30
:*･ﾟ☆.｡.:*･ﾟ￡(｡･<#8221<･)o[†<#8230<Thanks<#8230<†]o(･<#8221<･｡)β｡.:*･ﾟ☆.｡.:*⠀Thank You 31
ﾟ･*:.｡. .｡.:тндйк уoц　(○・∀・)b тндйк уoцﾟ･*:.｡. .｡.:⠀Thank You 32
(*ﾉ∀｀*)｡｡ooO((【･:*:･∫ρёCIДL　тнДЙκ∫ ･:*:･】))⠀Thank You 33
(●´艸｀）。ｏ*тнайк чоц*ｏ。(´艸｀○)⠀Thank You 34
･ﾟ･(〃´∩｀p◇SΟЯЯΥ◆q´∩｀〃)･ﾟ･⠀Sorry 1
･ﾟ･δояяу･ﾟ･(○ﾉдﾉ)⠀Sorry 2
Ｓ○ЯЯΥ＿φ┃´･ι_ｑ｀ ┃ﾟｏ｡⠀Sorry 3
ʎɹɹoS ʎɹɹos’ɥO ¨●౹౽‥ㆀ⠀Sorry 4
๑•́ㅿ•̀๑) ᔆᵒʳʳᵞ⠀Sorry 5
ＳΟЯЯΥ＿φ（･益ｑ｡｀)･ﾟ･ｏ｡⠀Sorry 6
ヾ((●＞□＜)ﾉ*:..｡o○ＳＯЯЯЧ○o。..:*ヽ(＞□＜●))ﾉｼ⠀Sorry 7
(●TΩT)-o*◇*―ЙＩＣЁ тＯ МЁЁт ЧＯЦ―*◆*o-(TΩT○)⠀Nice to Meet You 1
(★-ω-)σ*☆*―【Йｉｃё тｏ Мёёт Чｏμ】―*★*a(-ω-☆)⠀Nice to Meet You 2
(★’ω’)ﾉ*+:｡.｡:+*Йｉｃё тｏ Мёёт Чｏμ*+:｡.｡:+*ヽ(‘ω’☆)⠀Nice to Meet You 3
(☆･U)-o☆･*:.｡ЙＩＣЁ тＯ МЁЁт ЧＯЦ..｡.:*･★o-(U･★)⠀Nice to Meet You 4
★ﾟ+.p(☆’w｀((ЙｉｃЁ тＯ Мёёт ЧｏЦ))’w｀★)q.+ﾟ☆⠀Nice to Meet You 5
(◎ゝ∀･)ノ【*｡｡｡*Йiсё то мёёт чоц*｡｡｡*】⠀Nice to Meet You 6
(●´･Å･)⊃☆◆Йiсё то мёёт чоц◇★⊂(･Å･`○)⠀Nice to Meet You 7
(●´皿｀p【ﾟ+.ЙｉｃЁ тＯ Мёёт ЧｏЦﾟ+.】q⠀Nice to Meet You 8
ﾟ+.∮(*′д’b)ЙｉｃЁ тＯ Мёёт ЧｏЦ∮ﾟ+.⠀Nice to Meet You 9
［∮Йiсё то мёёт чоц∮］ｮ´Å｀*)⠀Nice to Meet You 10
(●´ω｀b(((ﾟ+:.ﾟЙiсё то мёёт чоцﾟ.:+ﾟ)))d⠀Nice to Meet You 11
(**ﾉ≧Ｏ≦)ﾉ<<<<<<<<<<<<Йiсё то мёёт уоц☆*ﾟ ゜ﾟ*☆⠀Nice to Meet You 12
.+ﾟ*｡:ﾟ+{{ЧЁＳ}}.+ﾟ*｡:ﾟ+ヾ(*ﾟ∀ﾟ*)⠀Yes 1
ﾍ(　´∀｀)ﾉ┌┛三|｡+.ЧЁS｡+.|⠀Yes 2
( ›◡ु‹ )˂ᵒ͜͡ᵏᵎ⁾⠀Yes 3
(^▽^)/ ʸᵉᔆᵎ⠀Yes 4
( ✪ワ✪)ノʸᵉᵃʰᵎ⠀Yes 5
(۶ꈨຶꎁꈨຶ )۶ʸᵉᵃʰᵎ⠀Yes 6
(ˀ̢⋅⃘‧̮⋅⃘ˁ̡ી˂ᵒ͜͡ᵏᵎ⁾⠀Yes 7
٩(•̤̀ᵕ•̤́๑)ᵒᵏᵎᵎᵎᵎ⠀Yes 8
ヾ(<><<u<<<<●【*:..｡o○ЧЁＳ○o。..:*】●<><<u<<<<)ﾉ⠀Yes 9
꒰ ꒪⌑꒪꒱˖ꂚ*ᵎ⠀No 1
(⁎⁍̴̆ ▿乂)⁎ꂚ*ᵎᵎᵎ⠀No 2
१(ǒರಿ̮ǒ)՞ꂚ…⠀No 3
o͡͡͡͡͡͡╮(｡<><<口<<<<｡)╭o͡͡͡͡͡͡ ᵑ৹!⠀No 4
(ᵒ̤̑ ₀̑ ᵒ̤̑)wow!*✰⠀Miscellaneous 1
٩(⌯꒦ິ̆ᵔ꒦ິ)۶ᵒᵐᵍᵎᵎᵎ⠀Miscellaneous 2
p(⁎✪͠ _̆ ✪͠ ⁎)q✧ƒíցհԵ✧⠀Miscellaneous 3
*⋆ᐪᐜᑊᵗᵗᵉʳ⃝✎⁎°.·⠀Miscellaneous 4
ɢ∞פ⋆ᖙᵒᵝ ٩꒰<#8221<̮*ू꒱⠀Miscellaneous 5
˓⁽͑ʺˀ́˙̻ˁ̀ʺ⁾̉ʾʾ ᵏᵞᵅ˞ᵎ⠀Miscellaneous 6
♬°⋆ɱUꑄյ͛ʗ⋆°♬⠀Miscellaneous 7
=͟͟͞͞≠⌓̈⃝\ᵒᵐᵍ⠀Miscellaneous 8
(ㆀ˘･з･˘)ωҺaｔ？⠀Miscellaneous 9
!(ᵒ̤̑ ◁ ᵒ̤̑)wow!৹ᢄᵍᵎᵎ⠀Miscellaneous 10
☆º°˚*☆ Have a ηice ϑay ☆º°˚*☆⠀Miscellaneous 11
☻…☻…ⓗⓔⓛⓛⓞ…☻…☻⠀Miscellaneous 12
ɿ(｡･ɜ･)ɾⓌⓗⓨ？⠀Miscellaneous 13
Ⓗⓐⓟⓟⓨ❤ヾ(◍<#8217<౪`◍)ﾉﾞ⠀Miscellaneous 14
(⁎⚈ैꇴ⚈ै⁎⚑)⚐╒ⅰᵍһ৳ǁ͚⠀Miscellaneous 15
ɿ(｡･ɜ･)ɾⓌⓗⓐⓣ？⠀Miscellaneous 16
ᙚᵐⁱᒻᵉ¨̮♡⠀Miscellaneous 17
(๑o̴̶̷̥᷅﹏o̴̶̷̥᷅๑)ᵒᵐᵍᵎᵎᵎ⠀Miscellaneous 18
કⁱᵍʰᵗᵎકⁱᵍʰᵗᵎ⚑⠀Miscellaneous 19
(｢๑•₃•)｢ ʷʱʸ?⠀Miscellaneous 20
Ⓗⓐⓟⓟⓨ⠀Miscellaneous 21
Ɛn꒻⍢⃝Ⴘ♫⠀Miscellaneous 22
೦തᵉᵈᵉ৳૦♥︎⠀Miscellaneous 23
✧*.◟(ˊᗨˋ)◞.*✧ᗯ੨~ɪ̊♪ْ˖⋆⠀Miscellaneous 24
ʱᵃᵐⁱᵖᵃᵑ♡⃛⠀Miscellaneous 25
✧⁛◟₍⋰⃘⁾ ᷇␟␎˗ ᷅⁽⋱⃘₎◞⁘✧⠀Miscellaneous 26
ᑦᑋᵃᵑ*୨୧*˚·⠀Miscellaneous 27
Ƒ ư ɕ ƙ (╬ﾟ◥益◤ﾟ) ╬ﾟ⠀Miscellaneous 28
(。・艸-。)-☆　ｗiйκ⠀Miscellaneous 29
ヾ(。◣∀◢。)ノⒼⓞ ⓐⓗⓔⓐⓓ!!⠀Miscellaneous 30
｟❛◡❛ॣॣ｠*.･｡╟╢ᎯƤƤᎽ*.･｡⠀Miscellaneous 31
⋈*⋆┠┨⍺ѵє ⍺ ɢㆀԀ Ԁ੨ƴ ⋆*⋈⠀Miscellaneous 32
(ʾ̌ˆʿ̌)pͪoͣnͬpͣoͥnͭpͣa͡inͥ⠀Miscellaneous 33
ຄ✡⃛HappyஐHappy❤⃛ଓ*⠀Miscellaneous 34
ℱᵒᒻᒻᵒ꒳◡̈⃝⠀Miscellaneous 35
MIN ■■■■■■■■■■ MAX o(｀Θ´)○☆⠀Miscellaneous 36
*ꀿªᵖᵖᵞ⋆⑅◌◟̊◞̊◌*⠀Miscellaneous 37
꒳ᵃ꒳ᵃ꒳ᵃ~(๑°ᗨૢ°๑)♡ӵᵉ੨ᑋ✧⠀Miscellaneous 38
(•ᵕᴗᵕ•)⁾⁾ᵖᵉᵏᵒ⠀Miscellaneous 39
(•ᵕᴒ̫ᵕ•)⁾⁾ᵖᵉᵏᵒ⠀Miscellaneous 40
βακα<#8230<_φ(ﾟ∀ﾟ )⠀Miscellaneous 41
ꊞ̩⁌•͡˻•⁍ᵒᵈᵃⁿᵍᵒ ⁿᵉ⠀Miscellaneous 42
*ғᐤᐦᐤᐜ⃝⋆⠀Miscellaneous 43
Σ(<#8216<Д<#8217<⁕)ահɑԵ<#8217<Տ up !?⠀Miscellaneous 44
ʸᵉᵃʰᵎᵎ े ̡̡⍤⃝  ̢̢ेे ꒳ᵒ꒳ᵎᵎ⠀Miscellaneous 45
⁽͑ˀˉ˙̫ˉˁ⁾̉ ᵐᵘⁿⁱ⠀Miscellaneous 46
◌⑅⃝♡*ℋᵅᵖᵖᵞ*♡⑅⃝◌⠀Miscellaneous 47
✩*ℋᵃᵛᵉ ᵃ ⁿⁱᑦᵉ ᵈᵃᵞ✩‧*˚⠀Miscellaneous 48
βακα<#8230<_〆(ﾟ▽ﾟ*)⠀Miscellaneous 49
βακα…_〆(・ｪ・*)⠀Miscellaneous 50
βακα…_〆(´･ｪ･｀*)⠀Miscellaneous 51
βακα…_φ(´ι _` 　)⠀Miscellaneous 52
βακα?…_φ(￣ ￣|||)⠀Miscellaneous 53
βακαУαЯο…_〆(ﾟ▽ﾟ*)⠀Miscellaneous 54
ВАКА❣ฺ✍ฺ（◕ฺｖ◕ฺ）✌ฺ⠀Miscellaneous 55
||☆FIGHT☆||´Д`*)9⠀Miscellaneous 56
βακα<#8230<_〆(゜▽゜*)⠀Miscellaneous 57
(●ﾟ∀ﾟ)ﾉ【L】*【I】*【N】*【K】⠀Miscellaneous 58
(ﾉ*･_●･)ﾉ~☆彡мёЙЦ☆彡~ヽ(･○_･*ヽ)⠀Miscellaneous 59
..φ(｀･ω´･+)ﾉ【FЯIёЙD∫ LIЙκ 】⠀Miscellaneous 60
【ДβOЦт　мё】＼_(´Д｀●)⠀Miscellaneous 61
【ъака】＼_(・ω・`)⠀Miscellaneous 62
(*´<><<ω<<<<｀p[。+ﾟ:.Яiφμёδт.:ﾟ+。]q<#8221<⠀Miscellaneous 63
(●´-ω-)ノ【ЯIQЦё∫т 】ヽ(-ω-｀○)⠀Miscellaneous 64
ЯIQЦё∫т_φ(・●_・。｀)⠀Miscellaneous 65
ЯIQЦё∫т|ω・｀)ノ⠀Miscellaneous 66
p[ＤЁАЯ○○]q･ω･o)⠀Miscellaneous 67
βακα?<#8230<_φ(￣ ￣|||)⠀Miscellaneous 68
［*:<<<:*ＣЦтЁ*:<<<:*］’v`*)ゞ⠀Miscellaneous 69
ʱᵃᵑᵃᵍᵉ ᵈᵉᵗᵉʳᵘᵞᵒ♡⃛⠀Miscellaneous 70
ηακετα<#8230<_〆(；ωq｀)⠀Miscellaneous 71
βακα<#8230<_〆(・ｪ・*)⠀Miscellaneous 72
βακα<#8230<_〆(´･ｪ･｀*)⠀Miscellaneous 73
βακα<#8230<_φ(´ι _` 　)⠀Miscellaneous 74
d【☆＾∀＾】Ｃｏйｇядтμｌдтｉｏй【＾∀＾★】b⠀Miscellaneous 75
+ﾟ*｡:ﾟ+Hi>h(￫㉨￩)ﾊ(￫㉨￩)Five!+ﾟ*｡:ﾟ+⠀Miscellaneous 76
■■■■■■■■■■■□□□ NOWLOADING⠀Miscellaneous 77
ﾟ･:,｡*:..｡o○☆(✿ฺ◕ฺ‿ฺ◕ฺฺ)ⓦⓔⓛⓒⓞⓜⓔ⠀Miscellaneous 78
(｡･(ｴ)･｡)p|｡+ﾟЙёνёг*Giνё*Цp!!+ﾟ｡|⠀Miscellaneous 79
(σ｀･ω･)σ『*.<~:.Йёνёг*Giνё*Цp!!.:~<.*』⠀Miscellaneous 80
。〇ﾟ｡*，*｡οЩнДт’∫ヽ(*･ω･*)ﾉЙёЩ？ ο｡*，*｡ﾟ〇｡⠀Miscellaneous 81
(。-｀ω´-)つ　三【☆:*:・ЯIQЦё∫т・:*ﾟ☆ 】⠀Miscellaneous 82
☆+。゜Яiφμёδт o((・c_,・。))o Яiφμёδт゜。+☆⠀Miscellaneous 83
ε(*’-<#8216<)з†.*・゜☆ЯIQЦё∫т☆゜・*.†ε(‘-’*)з⠀Miscellaneous 84
ε(*´・ω・)з☆:*:・　<#8221<Яiφμёδт<#8221<・:*゜☆ ε(・ω・｀*)з⠀Miscellaneous 85
ε=ε=ε=【゜.+:。ЯIQЦё∫т ♪゜.+:。】<><<c=(●・ω・)ゝ⠀Miscellaneous 86
ヾ(*∪ДＵ｀*)ｏｃ<<<<【。゜・+：.・ЯIQЦё∫т ・.：+・゜。】ヽ(*ＵωＵ｀*)ノ⠀Miscellaneous 87
Ⓖⓞ ⓐⓗⓔⓐⓓ!! ( `)3<#8242<)▃▃▃▅▆▇▉⠀Miscellaneous 88
(◎p∵*)尸<#8221<［。ﾟ+.ﾟＦＩＧＨＴﾟ+.ﾟ。］⠀Miscellaneous 89
(*´∀｀*)ﾉ[☆ﾟ･*F i > h <*･ﾟ☆]ヽ(*´∀｀*)⠀Miscellaneous 90
ヽ(●´ｖ｀○)ﾉ★FЯIЙD∫ LIЙκ☆(●´ｗ｀○)ﾉ⠀Miscellaneous 91
РЯЁТТЧﾟ+.(´・Д・｀人´･ω･｀)ﾟ+.РЯЁТТЧ⠀Miscellaneous 92
( ´△｀)⠀Triangle Shaped Worried Mouths 1
ฅ(๑’Δ’๑)⠀Triangle Shaped Worried Mouths 2
(❁°͈▵°͈)⠀Triangle Shaped Worried Mouths 3
(๑⃙⃘°̧̧̧ㅿ°̧̧̧๑⃙⃘)⠀Triangle Shaped Worried Mouths 4
ฅ=͟͟͞͞((꒪∆꒪<)ฅ⠀Triangle Shaped Worried Mouths 5
(๑ʘ∆ʘ๑)⠀Triangle Shaped Worried Mouths 6
(๑ˊ▵ॢˋ̥๑)⠀Triangle Shaped Worried Mouths 7
(๑ ˊ͈ ᐞ ˋ͈ )ƅ̋⠀Triangle Shaped Worried Mouths 8
ల(｀°Δ°)⠀Triangle Shaped Worried Mouths 9
(,,꒪꒫꒪,,)⠀Triangle Shaped Worried Mouths 10
((((爾△爾))))⠀Triangle Shaped Worried Mouths 11
（●´･△･｀）⠀Triangle Shaped Worried Mouths 12
Σ(,,oΔo,,*)⠀Triangle Shaped Worried Mouths 13
(⊙△⊙✿)⠀Triangle Shaped Worried Mouths 14
⊙△⊙⠀Triangle Shaped Worried Mouths 15
〝〇〟⊂(｀･Δ･´)⊃〝〇〟⠀Triangle Shaped Worried Mouths 16
(　ﾟдﾟ)⠀Д Style Mouths 1
(๏д๏)⠀Д Style Mouths 2
( ；´Д｀)⠀Д Style Mouths 3
(<´Д`)⠀Д Style Mouths 4
(((( <°Д°))))⠀Д Style Mouths 5
((*゜Д゜)ゞ”⠀Д Style Mouths 6
(＠￣Д￣＠；)⠀Д Style Mouths 7
(´；Д；｀)⠀Д Style Mouths 8
(´Д` )⠀Д Style Mouths 9
(ι´Д｀)ﾉ⠀Д Style Mouths 10
《ﾟДﾟ》⠀Д Style Mouths 11
∑(<°Д°)⠀Д Style Mouths 12
(；๏д๏)⠀Д Style Mouths 13
Σ（ﾟдﾟ<<<）⠀Д Style Mouths 14
(((╹д╹<)))⠀Д Style Mouths 15
(๑⁺᷄д⁺᷅๑)◞՞⠀Д Style Mouths 16
(╬⁽⁽ ⁰ ⁾⁾ Д ⁽⁽ ⁰ ⁾⁾)⠀Д Style Mouths 17
( ᵒ̴̶̷᷄ д ᵒ̴̶̷᷅ )⠀Д Style Mouths 18
(●ฅ́дฅ̀●)⠀Д Style Mouths 19
(๑ŐдŐ)b⠀Д Style Mouths 20
(･:ﾟдﾟ:･)⠀Д Style Mouths 21
(๑´•д • `๑)⠀Д Style Mouths 22
(´◑д◐｀)⠀Д Style Mouths 23
(◐д◑´,,)⠀Д Style Mouths 24
d(ŐдŐ๑)⠀Д Style Mouths 25
(ꐦ°᷄д°᷅)⠀Д Style Mouths 26
(╬ ꒪Д꒪)ノ⠀Д Style Mouths 27
(*´ﾟд)(дﾟ｀*)⠀Д Style Mouths 28
(*´･Д･)⠀Д Style Mouths 29
(υ´Д｀)⠀Д Style Mouths 30
(´Д｀υ)⠀Д Style Mouths 31
(･д･｀o)⠀Д Style Mouths 32
(:.<ﾟ<Д<ﾟ<.:)⠀Д Style Mouths 33
( <ﾟдﾟ)⠀Д Style Mouths 34
Σ(ﾟдﾟ；)⠀Д Style Mouths 35
(ﾉﾟдﾟ(<￣Д￣)⠀Д Style Mouths 36
Σ【*ﾟдﾟ*】⠀Д Style Mouths 37
๑ΘдΘ๑⠀Д Style Mouths 38
(⌇ຶД⌇ຶ)⠀Д Style Mouths 39
(๑Ő д Ő๑)⠀Д Style Mouths 40
(･д･)⠀Д Style Mouths 41
⊂(⊙д⊙)つ⠀Д Style Mouths 42
(||ﾟДﾟ)⠀Д Style Mouths 43
(ﾟДﾟ||)⠀Д Style Mouths 44
⊂((ﾒ´Д｀))⊃⠀Д Style Mouths 45
( ﾟдﾟ)⠀Д Style Mouths 46
(σ･Д･)σ⠀Д Style Mouths 47
(*σ´Д｀*)⠀Д Style Mouths 48
Σ(っﾟДﾟ；)っ⠀Д Style Mouths 49
ヽ(<ﾟ<Д<ﾟ<< )⠀Д Style Mouths 50
(´д｀ι)⠀Д Style Mouths 51
o┤*´Д｀*├o⠀Д Style Mouths 52
(；´ﾟДﾟ)ゞ⠀Д Style Mouths 53
(<ﾟ<Д<ﾟ；<)⠀Д Style Mouths 54
w(´ﾟДﾟ｀)w⠀Д Style Mouths 55
(# ﾟДﾟ)⠀Д Style Mouths 56
ヾ(ﾟдﾟ)ﾉﾞ⠀Д Style Mouths 57
m(*´Д｀)m⠀Д Style Mouths 58
(；´･Д･)⠀Д Style Mouths 59
|*´・Д・)r))ﾟ⠀Д Style Mouths 60
Σ(ﾟДﾟ<≡｀ﾟдﾟ)⠀Д Style Mouths 61
(σ ´゜д゜)σ⠀Д Style Mouths 62
( ﾟдﾟ )⠀Д Style Mouths 63
((*｀ﾟдﾟ)ゞ⠀Д Style Mouths 64
σ(°Д°*)⠀Д Style Mouths 65
┌┤´д`├┐⠀Д Style Mouths 66
ミ（゜д゜○）⠀Д Style Mouths 67
(ﾟдﾟ)⠀Д Style Mouths 68
(｡´･д･)o⠀Д Style Mouths 69
o(ﾟДﾟ)っ⠀Д Style Mouths 70
Σ꒰๑•ॢд •ॢ๑꒱⠀Д Style Mouths 71
(。´д｀。)⠀Д Style Mouths 72
Σ(`･Д･ﾉ)ﾉ⠀Д Style Mouths 73
(οдО<)⠀Д Style Mouths 74
◍´Д‵◍⠀Д Style Mouths 75
o｜๑⊙Д⊙๑｜ツ⠀Д Style Mouths 76
(✽ ﾟдﾟ ✽)⠀Д Style Mouths 77
(´д｀、)⠀Д Style Mouths 78
(,,ﾟДﾟ)⠀Д Style Mouths 79
o(*´д`*)o⠀Д Style Mouths 80
(´･Д･<<<)ゞ⠀Д Style Mouths 81
o(･´д･｀o)))三(((o´･д｀･)o⠀Д Style Mouths 82
☂o(ﾟДﾟ = ﾟДﾟ)o ☂⠀Д Style Mouths 83
☂o(⑅ﾟДﾟ = ﾟДﾟ)o ☂⠀Д Style Mouths 84
(´･(´･(´･(´･(´･(´･д･`) ･`)･`)･`)･`)･`)⠀Д Style Mouths 85
(╯•﹏•╰)⠀Squiggly Mouths 1
(☍﹏⁰)⠀Squiggly Mouths 2
(◍•﹏•)⠀Squiggly Mouths 3
(๑•﹏•)⠀Squiggly Mouths 4
(‘﹏*๑)⠀Squiggly Mouths 5
(ó﹏ò｡)⠀Squiggly Mouths 6
(੭ ･᷄﹏･᷅)੭ु⁾⠀Squiggly Mouths 7
(｡ŏ﹏ŏ)⠀Squiggly Mouths 8
ᗜੂͦ﹏ᗜੂͦ⠀Squiggly Mouths 9
( ･ั﹏･ั)⠀Squiggly Mouths 10
(﹗︠﹏︠﹗︡)⠀Squiggly Mouths 11
(´-﹏-`；)⠀Squiggly Mouths 12
ꐑ(*ꐌ﹋ꐌꐐ*)⠀Squiggly Mouths 13
•(◐﹏◐)•⠀Squiggly Mouths 14
(.`･﹏･´.)⠀Squiggly Mouths 15
c໒( ◐ ﹏ ◐ )७੭⠀Squiggly Mouths 16
ԅ[ •́ ﹏├┬┴┬┴⠀Squiggly Mouths 17
☁ 。७﹏७ 。☁⠀Squiggly Mouths 18
(¤﹏¤)⠀Squiggly Mouths 19
●﹏●⠀Squiggly Mouths 20
へ[ : ⊚ ﹏ ⊚ : ]ง⠀Squiggly Mouths 21
╏ ˵ ✪ ﹏ ✪ ˵ ╏⠀Squiggly Mouths 22
▐ ” ⊗ ﹏ ⊗ ”▐⠀Squiggly Mouths 23
⊙﹏⊙⠀Squiggly Mouths 24
ミ●﹏☉ミ⠀Squiggly Mouths 25
ヾ(｡﹏｡)ﾉﾞ⠀Squiggly Mouths 26
〳 •́ ﹏ •̀ 〵⠀Squiggly Mouths 27
╰[ ⁰﹏⁰ ]╯⠀Squiggly Mouths 28
=⠀Squiggly Mouths 29
。:.ﾟ٩⠀Squiggly Mouths 30
(⠀Squiggly Mouths 31
⑅๑꒪﹏꒪๑⠀Squiggly Mouths 32
)⠀Squiggly Mouths 33
۶:.｡⠀Squiggly Mouths 34
+⠀Squiggly Mouths 35
ﾟ⠀Squiggly Mouths 36
(๑ó⌓ò๑)⠀Crescent Mouths 1
(●´⌓`●)⠀Crescent Mouths 2
(꒪⌓꒪)⠀Crescent Mouths 3
ଽ꒰⌓̈ ॢ꒱ ̉ ̉⠀Crescent Mouths 4
( •᷄⌓•᷅ )⠀Crescent Mouths 5
(´๑・⌓・｀)⠀Crescent Mouths 6
( ꒪ͧ⌓꒪ͧ ⊂⠀Crescent Mouths 7
( ³⌓³)⠀Crescent Mouths 8
(๑°⌓°๑)⠀Crescent Mouths 9
(<ↀ⌓ↀ)⠀Crescent Mouths 10
(◕⌓◕<)⠀Crescent Mouths 11
Σ(‘◉⌓◉’)⠀Crescent Mouths 12
(ὀ⌓ὀ⑅)⠀Crescent Mouths 13
˛˛૧(˵¯͒▱¯͒˵)⠀Rhombus Mouths 1
˛૧(˵¯͒▱¯͒˵)⠀Rhombus Mouths 2
૮( ‘▱๋’ )ა⠀Rhombus Mouths 3
૮( ´⁰▱๋⁰` )ა⠀Rhombus Mouths 4
ଽ ૮( ⁰▱๋⁰ )ა⠀Rhombus Mouths 5
˚▱˚⠀Rhombus Mouths 6
(ⅈ▱ⅈ)⠀Rhombus Mouths 7
／(￣ロ￣<)＼⠀Square Mouths 1
(￣□￣)⠀Square Mouths 2
Σ੧(❛□❛✿)⠀Square Mouths 3
[ ∗ ◕ □ ◕ ∗ ]⠀Square Mouths 4
(oﾟ□ﾟ)o⠀Square Mouths 5
(oﾐﾟﾛﾟﾐ)o⠀Square Mouths 6
(๑º ﾛ º๑)⠀Square Mouths 7
(๑⊙ﾛ⊙๑)⠀Square Mouths 8
∩(￣□￣#)∩⠀Square Mouths 9
(˚☐˚! )/⠀Square Mouths 10
o(*･ﾛ･*)o⠀Square Mouths 11
⁞ ✪ ⌂ ✪ ⁞⠀House Shaped Mouths 1
(✱°⌂°✱)⠀House Shaped Mouths 2
╏ ⁰ ⌂ ⁰ ╏⠀House Shaped Mouths 3
ヽ[ ಡ ⌂ ಡ ]⊃⠀House Shaped Mouths 4
₍₍ (̨̡ ‾᷄⌂‾᷅)̧̢ ₎₎⠀House Shaped Mouths 5
⚆ᗝ⚆⠀House Shaped Mouths 6
＼(°o°；）⠀Drops of Sweat 1
~~旦_(･o･<)⠀Drops of Sweat 2
(<´・`)<><<⠀Drops of Sweat 3
（；￣ェ￣）⠀Drops of Sweat 4
(<° ロ°)⠀Drops of Sweat 5
(；☉_☉)⠀Drops of Sweat 6
（￣□￣；）⠀Drops of Sweat 7
(￣□￣<)!!⠀Drops of Sweat 8
(￣◇￣<)⠀Drops of Sweat 9
(°◇°<)⠀Drops of Sweat 10
（°o°；）⠀Drops of Sweat 11
(~_~<)⠀Drops of Sweat 12
（−＿−；）⠀Drops of Sweat 13
(ーー<)⠀Drops of Sweat 14
（ｏ。ｏ；）⠀Drops of Sweat 15
(-｡-<⠀Drops of Sweat 16
༼⁰o⁰；༽⠀Drops of Sweat 17
(´⊙o⊙`；)⠀Drops of Sweat 18
･(•́⍛•̀< ≡ •́⍛•̀<)⠀Drops of Sweat 19
(◞‸◟；)⠀Drops of Sweat 20
( ´<ﾟ<ё<ﾟ<)⠀Drops of Sweat 21
:<(∩´﹏`∩)<:⠀Drops of Sweat 22
(ﾟAﾟ<)⠀Drops of Sweat 23
( ﾟÅﾟ；)⠀Drops of Sweat 24
٩̋(•᷄◟̵◞̵•᷅‧̣̥̇)’`~✧⠀Drops of Sweat 25
(φ╻φ；)⠀Drops of Sweat 26
(≖╻≖；)⠀Drops of Sweat 27
(；ꏿ︿ꏿ)⠀Drops of Sweat 28
༼ : ౦ ‸ ౦ : ༽⠀Drops of Sweat 29
(´エ｀；)⠀Drops of Sweat 30
(-∀-`< )⠀Drops of Sweat 31
(･∀･；)⠀Drops of Sweat 32
(*<´□`)ゞ⠀Drops of Sweat 33
[ : • 益 • : ]⠀Drops of Sweat 34
ʕ･_･ <ʔ≡ʕ< ･_･ʔ⠀Drops of Sweat 35
（￣ー￣；）⠀Drops of Sweat 36
((´∀`<))⠀Drops of Sweat 37
(( ´∀`<))⠀Drops of Sweat 38
。(<><<_<<<<<=<<><<_<<<<)。⠀Drops of Sweat 39
（；○□○）⠀Drops of Sweat 40
(*ﾟÅﾟ；*)⠀Drops of Sweat 41
((((｡(´°Α°｀)｡))))⠀Drops of Sweat 42
f(^_^<⠀Drops of Sweat 43
(°m°<)⠀Drops of Sweat 44
(-∧-；)⠀Drops of Sweat 45
｡:ﾟ*+<(●´･д･`●)<+*ﾟ:｡⠀Drops of Sweat 46
(:.<ﾟ<益<ﾟ<益<ﾟ<益<ﾟ<益<ﾟ<益<ﾟ<益<ﾟ<.)⠀Drops of Sweat 47
(」゜ロ゜)」⠀Raised Arms 1
＼(●o○<)ノ⠀Raised Arms 2
┗┐ヽ(′Д、`*)ﾉ┌┛⠀Raised Arms 3
ヽ（・＿・；)ノ⠀Raised Arms 4
ヾ(´･ ･｀｡)ノ”⠀Raised Arms 5
ヽ(￣д￣<)ノ⠀Raised Arms 6
ヽ（゜ロ゜；）ノ⠀Raised Arms 7
ヾ(=ﾟ･ﾟ=)ﾉ⠀Raised Arms 8
Σ(ﾟﾛﾟ｣)｣⠀Raised Arms 9
ლ(´﹏`ლ)⠀Raised Arms 10
╭(°A°`)╮⠀Raised Arms 11
┌┤´ﾟДﾟ`├┐⠀Raised Arms 12
ヾ( •́д•̀ <)ﾉ⠀Raised Arms 13
ヽ(*´Д｀*)ﾉ⠀Raised Arms 14
ヽ(ﾟДﾟ)ﾉ⠀Raised Arms 15
ヾ(◎o◎,,；)ﾉ⠀Raised Arms 16
ヾ( ๑´д`๑)ﾂ⠀Raised Arms 17
ヾ(*ㅿ*๑)ﾂ⠀Raised Arms 18
ヾ(๑ ³ㅿ³)ﾉ⠀Raised Arms 19
ヾ(((<ꈡ▱ꈡ<)))ﾉ⠀Raised Arms 20
ʿʿ⁽⁽((⁰ⅈ⁰))⁾⁾ʾʾ⠀Raised Arms 21
ヾ(ﾟдﾟ<)⠀Raised Arms 22
ヽ(<´Д｀)ﾉ⠀Raised Arms 23
ヾ(o´０ω０o)ﾉ⠀Raised Arms 24
ヾ(o´０Д０o)ﾉ⠀Raised Arms 25
<<<<(´・д・｀)ノ⠀Raised Arms 26
ɭ ɿ (•᷄દ•᷅)⠀Raised Arms 27
(ι´ Д｀)ﾉ⠀Raised Arms 28
ヽ༼☯﹏☯༽ﾉ⠀Raised Arms 29
੧║ ” ◔ Ĺ̯ ◔ ” ║و⠀Raised Arms 30
ゞ( ͡°⍛ ͡°)ゞ⠀Raised Arms 31
ヽ༼⊙_⊙༽ﾉ⠀Raised Arms 32
ヾ(*’□’*)ｰ⠀Raised Arms 33
ヾ(･ω･`；))ﾉ⠀Raised Arms 34
<<<<(<<ﾟ◇ﾟ<<)<><<⠀Raised Arms 35
ヾ((；´･ω･)ﾉ⠀Raised Arms 36
ヾ(･ω･`；)ﾉ⠀Raised Arms 37
ヽ(*´□`)ﾉﾞ⠀Raised Arms 38
ヾ(<ﾟ<Д<ﾟ<)ﾉﾞ⠀Raised Arms 39
(*ﾉ´□`)ﾉ~⠀Raised Arms 40
╰໒(⸝⸝⸝⚆Ĺ̯⚆⸝⸝⸝)७ノ⠀Raised Arms 41
ヽ(‘ºل͟º)ノ⠀Raised Arms 42
へ( ̿̿ o ̿̿ )╮⠀Raised Arms 43
ԅ། , ◔ ﹏ ◔ , །ᓄ⠀Raised Arms 44
ヽ(◕﹏◕)ﾉ⠀Raised Arms 45
(○´･д･)ﾉ⠀Raised Arms 46
(*′口`)ﾉ⠀Raised Arms 47
ヽ(´･д･`)ﾉ⠀Raised Arms 48
ヽ(･д･｀｡)ﾉ⠀Raised Arms 49
ヽ(｡´･д･)ﾉ⠀Raised Arms 50
ヾ(゜д゜)ノ⠀Raised Arms 51
ヽ(*´□｀*)ッ⠀Raised Arms 52
（┓゜Ａ゜）┓⠀Raised Arms 53
ლ(ﾟдﾟლ)⠀Raised Arms 54
ヽ(*゜∀゜*)ノ⠀Raised Arms 55
ヾ(◕д◕❀)ﾂ⠀Raised Arms 56
ヾ(❀◕д◕)ﾉ⠀Raised Arms 57
（゜」∀」゜）⠀Raised Arms 58
o|✿´・ェ・`|o⠀Raised Arms 59
ヽ(▣﹏▣＼*≡*／▣﹏▣)ﾉ⠀Raised Arms 60
/~＼o=(<ﾟﾛﾟ)=o/~＼⠀Raised Arms 61
.+:｡ヽUﾟДﾟUﾉﾟ.+:｡⠀Raised Arms 62
ﾍ(ﾟ∀ﾟﾍ)ﾍ(ﾟ∀ﾟﾍ)ﾍ(ﾟ∀ﾟﾍ)⠀Raised Arms 63
ଵ˛̼ଵ⠀Fancy Faces 1
⁎ۜ′̛˷˒′̛⌕⠀Fancy Faces 2
⋆ᶿ̵᷄ ˒̼ ᶿ̵᷅⋆⠀Fancy Faces 3
๑•́ㅿ•̀๑) ᔆᵒʳʳᵞ⠀Words 1
(๑o̴̶̷̥᷅﹏o̴̶̷̥᷅๑)ᵒᵐᵍᵎᵎᵎ⠀Words 2
(･_-｡ )⠀Miscellaneous Forms of Worry 1
（’-’*)⠀Miscellaneous Forms of Worry 2
(´ ˙○˙ `)⠀Miscellaneous Forms of Worry 3
Σ(´ﾟωﾟ｀ )⠀Miscellaneous Forms of Worry 4
((유∀유|||))⠀Miscellaneous Forms of Worry 5
(｡´╹A╹｀｡)⠀Miscellaneous Forms of Worry 6
(╯•ω•╰)⠀Miscellaneous Forms of Worry 7
(๑ŏ _ ŏ๑)⠀Miscellaneous Forms of Worry 8
~( ´•︵•` )~⠀Miscellaneous Forms of Worry 9
(･᷄ὢ･᷅)⠀Miscellaneous Forms of Worry 10
(ૢ•᷄⊱•᷅ ╬)⠀Miscellaneous Forms of Worry 11
(๑´•ω • `๑)⠀Miscellaneous Forms of Worry 12
(ʘᗩʘ’)⠀Miscellaneous Forms of Worry 13
[･Å･` ○]⠀Miscellaneous Forms of Worry 14
‷̗ↂ凸ↂ‴̖⠀Miscellaneous Forms of Worry 15
ꀯ(⑈ꑒ᷅⺫ꑒ᷄)⠀Miscellaneous Forms of Worry 16
(⌯꒪͒ .̼ ꒪͒)⠀Miscellaneous Forms of Worry 17
=͟͟͞͞(꒪ᗜ꒪ ‧̣̥̇)⠀Miscellaneous Forms of Worry 18
(⋆ꁏہꁏ⋆)⠀Miscellaneous Forms of Worry 19
(*´･Å･｀)⠀Miscellaneous Forms of Worry 20
(☪̤̆_̆ ☪̤̆)⠀Miscellaneous Forms of Worry 21
(๑•́ω•̀)⠀Miscellaneous Forms of Worry 22
(ૢ•᷄ۿ•᷅╬)⠀Miscellaneous Forms of Worry 23
[･A･` ○]⠀Miscellaneous Forms of Worry 24
ჴ˘ര‸രჴ⠀Miscellaneous Forms of Worry 25
(੭ु⍨)੭ु⁾⁾⠀Miscellaneous Forms of Worry 26
(*ꑒꆯꑒ*)冫⠀Miscellaneous Forms of Worry 27
꒰๑´ඹ.̫ ඹ `๑꒱⠀Miscellaneous Forms of Worry 28
/･_･ヾ＼⠀Miscellaneous Forms of Worry 29
(⁎·́ˍູˑ·̀)⠀Miscellaneous Forms of Worry 30
┌╏ •́ – •̀ ╏┐⠀Miscellaneous Forms of Worry 31
（ ´ﾟ,_」ﾟ）⠀Miscellaneous Forms of Worry 32
o(°ω°メ)Ｏ))⠀Miscellaneous Forms of Worry 33
(*´○∧○`*）⠀Miscellaneous Forms of Worry 34
░ ര Ĺ̯ ര ░⠀Miscellaneous Forms of Worry 35
~( ~´･_･`)~⠀Miscellaneous Forms of Worry 36
（ 　ﾟ々ﾟ）⠀Miscellaneous Forms of Worry 37
[*っ´･Å･]⠀Miscellaneous Forms of Worry 38
ε=(ﾟ∀゜´)⠀Miscellaneous Forms of Worry 39
(´σωσ*)⠀Miscellaneous Forms of Worry 40
(´･⊥･｀)⠀Miscellaneous Forms of Worry 41
(⊙…⊙ )⠀Miscellaneous Forms of Worry 42
(-’๏_๏’-)⠀Miscellaneous Forms of Worry 43
(⊙︿⊙✿)⠀Miscellaneous Forms of Worry 44
◑.◑⠀Miscellaneous Forms of Worry 45
꒰(⋅⃝ ௰͡ ⋅⃝)꒱⠀Miscellaneous Forms of Worry 46
( ˵ ◐ ︿ ◐ ˵ )⠀Miscellaneous Forms of Worry 47
( ° ^ ° )⠀Miscellaneous Forms of Worry 48
❛ॕ̀ੇ≀ ̼❛ॕ̀ੇ˵⠀Miscellaneous Forms of Worry 49
໒(•න꒶̼න•)७⠀Miscellaneous Forms of Worry 50
╏ ” ⊚ ͟ʖ ⊚ ” ╏⠀Miscellaneous Forms of Worry 51
(✿˵•́ ‸ •̀˵)⠀Miscellaneous Forms of Worry 52
“(´≖ ‸ ≖｀)”⠀Miscellaneous Forms of Worry 53
.,.,.,∵゜⊂-o(´･ω･｀o)三(o´･ω･｀)o-⊃゜∵.,.,.,⠀Miscellaneous Forms of Worry 54
(⚰⃘ ̠⚰⃘) ͞ ̿͟͟͞͞(⚰⃘ ̠⚰⃘) ͞ ̿͟͟͞͞(⚰⃘ ̠⚰⃘) ͞ ̿͟͟͞͞(⚰⃘ ̠⚰⃘) ͞⠀Miscellaneous Forms of Worry 55
Y⌒Y⌒Y⌒Y⌒Y⌒Y⌒(｡Ａ｡)!!!⠀Miscellaneous Forms of Worry 56
Σ(◦⃝⃚⃙⃘⃙⃚⃙⃚⃙⃘⃑△◦⃝⃚⃙⃘⃙⃐ﾉ)ﾉ⠀Miscellaneous Forms of Worry 57
（ ͒๑㉾ܫ㉾๑ ͒）⠀Complex 1
(٭ॢꏿ᷄ ູ̠ꏿ᷅) ॢ⠀Complex 2
(•᷊᷄ṏ̮•᷊᷅)⠀Complex 3
⁝ʺ̢͈̗̋ •᷊᷄ṏ̮•᷊᷅ ˵̡̖̎̏⁝⠀Complex 4
(⌓⍢⌓〣)⠀Complex 5
(‖ⁱ꒪♖꒪)⠀Complex 6
૮( ᵒ̌ัૢ▱ᵒ̌ัૢ )ა⠀Complex 7
o͡͡͡╮〳 ~ ☉ ₒ ☉ ~ 〵╭o͡͡͡⠀Complex 8
₊·(ϱ॔﹏ᵕ๑॓)‧*⠀Complex 9
Σू(((ↂ⃙⃙⃚⌑ↂ⃙⃙⃚<)))ू⠀Complex 10
( ◦⃝⃚⃙⃘⃙⃚⃙⃚⃙⃘⃑д◦⃝⃚⃙⃘⃙⃐ )∕⌚⠀Complex 11
₍ॢ﹒︠⍛ू﹒︡ ॢ₎⠀Complex 12
“(#ﾟ,_ゝﾟ)”⠀Complex 13
“(ﾟc_,ﾟ｀｡)ﾌﾟ⠀Complex 14
(❛ॕ⌓ ̣̣̥❛ॕ•ॢ)⠀Complex 15
＿φ( °-°)/⠀Writing with a φ 1
φ（．．）⠀Writing with a φ 2
φ(￣￢￣ヾ)⠀Writing with a φ 3
＿φ(°-°=)⠀Writing with a φ 4
φ(￣ー￣ )ノ⠀Writing with a φ 5
φ(●ﾟ益ﾟ)っ⠀Writing with a φ 6
φ(．．<)⠀Writing with a φ 7
φ(°ρ°*)メ⠀Writing with a φ 8
φ(´ω｀●)⠀Writing with a φ 9
φ(^∇^ )⠀Writing with a φ 10
φ(^ω^*)ﾉ⠀Writing with a φ 11
φ(ﾟ ωﾟ//）♡⠀Writing with a φ 12
φ(◎◎ヘ)⠀Writing with a φ 13
…φ(o´ωﾟo)φ…⠀Writing with a φ 14
_φ(●ﾟ益ﾟ)っ⠀Writing with a φ 15
＿φ(￣ー￣ )⠀Writing with a φ 16
σ(ൈ)φ⠀Writing with a φ 17
φ(´д｀ｏ)⠀Writing with a φ 18
＿φ(□□ヘ)⠀Writing with a φ 19
(๑╹o╹)φ⠀Writing with a φ 20
≡≡≡≡φ(＾∇＾*)⠀Writing with a φ 21
(‘•̀ ▽ •́ )φ⠀Writing with a φ 22
φ|o-Дゞo|⠀Writing with a φ 23
φ(･c_,･｡)⠀Writing with a φ 24
φ(・ω・｀ )⠀Writing with a φ 25
((φ(．．｡)⠀Writing with a φ 26
φ(ﾟｪﾟ♡)⠀Writing with a φ 27
φ(._.)⠀Writing with a φ 28
“φʕ•ᴥ•oʔ⠀Writing with a φ 29
…..φ(・∀・＊)⠀Writing with a φ 30
_φ［・ω・｀*］⠀Writing with a φ 31
φ(-｀Д´-*)⠀Writing with a φ 32
…..φ(〃∇〃 ）⠀Writing with a φ 33
…..φ(-ω-｡`)⠀Writing with a φ 34
…..φ(〃∇〃 )))⠀Writing with a φ 35
φ(´ω｀= )⠀Writing with a φ 36
φ( =´∀｀)ﾉ⠀Writing with a φ 37
..φ(ｰ￣*)⠀Writing with a φ 38
_φ(*￣0￣)ﾉ⠀Writing with a φ 39
…φ(ω￣*)⠀Writing with a φ 40
_φ(*￣ω￣)ﾉ⠀Writing with a φ 41
[＼／]…..φ(・д・。)⠀Writing with a φ 42
ψ(。。)⠀Writing with a ψ 1
___ψ(‥ )⠀Writing with a ψ 2
＿ψ(°-°=)⠀Writing with a ψ 3
ψ(°ρ°*)メ⠀Writing with a ψ 4
“ψʕ•ᴥ•oʔ⠀Writing with a ψ 5
ψ(´ω｀●)⠀Writing with a ψ 6
ψ(-｀Д´-*)⠀Writing with a ψ 7
..ψ(ｰ￣*)⠀Writing with a ψ 8
ψ(・∀・＠)⠀Writing with a ψ 9
ψ(・⺫・‶)⠀Writing with a ψ 10
….ψ(･ω･。)⠀Writing with a ψ 11
_ψ(-c_,-。)⠀Writing with a ψ 12
＿〆(。。)⠀Writing with a 〆 1
〆(・∀・＠)⠀Writing with a 〆 2
〆(´Ｕ_｀*)⠀Writing with a 〆 3
[≡] 〆(・⺫・‶)⠀Writing with a 〆 4
_〆(´Д⊂⠀Writing with a 〆 5
＿〆(●-Дゞ●)⠀Writing with a 〆 6
〆(´ω`●)ゞ⠀Writing with a 〆 7
＿〆ヾ(￣(エ)￣)⠀Writing with a 〆 8
_〆(･_･｡)⠀Writing with a 〆 9
_〆((ﾐ￣ｴ￣ﾐ))⠀Writing with a 〆 10
_〆(ﾟ▽ﾟ*)⠀Writing with a 〆 11
_〆(･･　)♪⠀Writing with a 〆 12
＿〆((=´ｴ `= ) )⠀Writing with a 〆 13
…_〆(ﾟ▽ﾟ*)⠀Writing with a 〆 14
…_〆(・∀・＠)⠀Writing with a 〆 15
…〆（´Ｕ｀*）⠀Writing with a 〆 16
….〆(･ω･。)⠀Writing with a 〆 17
_〆┤’-‘*├⠀Writing with a 〆 18
＿〆(´∀｀●)⠀Writing with a 〆 19
＿〆(=´ｴ ｀= )⠀Writing with a 〆 20
_〆(-c_,-。)⠀Writing with a 〆 21
＿〆(-ε･｀)ﾉ^☆⠀Writing with a 〆 22
…〆(・Å・｀ｏ)ノ⠀Writing with a 〆 23
_〆(ﾟ□ﾟ*)⠀Writing with a 〆 24
〆(･ω･*)⠀Writing with a 〆 25
_〆(´Ｕ_｀*)⠀Writing with a 〆 26
〆(°°*)⠀Writing with a 〆 27
_￠(T-T*)⠀Writing with a ￠ 1
_￠(･ω･`)⠀Writing with a ￠ 2
￠(-∀・○)⠀Writing with a ￠ 3
￠(･ω･`)⠀Writing with a ￠ 4
￠(-∀-○)⠀Writing with a ￠ 5
_￠(･ω･｀)⠀Writing with a ￠ 6
￠(￣ー￣ )ノ⠀Writing with a ￠ 7
￠(・∀・＠)⠀Writing with a ￠ 8
໒(⊙ᴗ⊙)७✎▤⠀Writing with an Actual Pencil 1
╰(⊡-⊡)و✎⮹⠀Writing with an Actual Pencil 2
(๑╹o╹)✎⠀Writing with an Actual Pencil 3
(‘•̀ ▽ •́ )✎⠀Writing with an Actual Pencil 4
ʕo•ᴥ•ʔ✎⠀Writing with an Actual Pencil 5
(-｀Д´-*)✎⠀Writing with an Actual Pencil 6
( ^∇^)✎⠀Writing with an Actual Pencil 7
(*･ω･)✎⠀Writing with an Actual Pencil 8
( =´∀｀)✎⠀Writing with an Actual Pencil 9
(*￣0￣)✎⠀Writing with an Actual Pencil 10
(○-∀-)✎⠀Writing with an Actual Pencil 11
(=°-°)✎⠀Writing with an Actual Pencil 12
(@・∀・)✎⠀Writing with an Actual Pencil 13
✍(΄◞ิ౪◟ิ‵)⠀Writing with an Actual Hand Holding a Pencil 1
௸˓˓✍(ீଞீ๑)⠀Writing with an Actual Hand Holding a Pencil 2
✉✍(ග⍛ග੭⠀Writing with an Actual Hand Holding a Pencil 3
✍(・∀・＠)⠀Writing with an Actual Hand Holding a Pencil 4
“✍ʕ•ᴥ•oʔ⠀Writing with an Actual Hand Holding a Pencil 5
✍(´ω｀●)⠀Writing with an Actual Hand Holding a Pencil 6
＿✍(￣ー￣ )⠀Writing with an Actual Hand Holding a Pencil 7
✍(´ω｀●)⠀Writing with an Actual Hand Holding a Pencil 8
….✍(･ω･。)⠀Writing with an Actual Hand Holding a Pencil 9
_✍(･_･｡)⠀Writing with an Actual Hand Holding a Pencil 10
✍(・∀・＠)⠀Writing with an Actual Hand Holding a Pencil 11
…✍(・Å・｀ｏ)ノ⠀Writing with an Actual Hand Holding a Pencil 12
＿✍(´∀｀●)⠀Writing with an Actual Hand Holding a Pencil 13
_✍(･_･｡)⠀Writing with an Actual Hand Holding a Pencil 14
[≡] ✍(・⺫・‶)⠀Writing with an Actual Hand Holding a Pencil 15
_✍(-c_,-。)⠀Writing with an Actual Hand Holding a Pencil 16
✍(-∀・○)⠀Writing with an Actual Hand Holding a Pencil 17
✍(´ι _` 　)⠀Writing with an Actual Hand Holding a Pencil 18
❣ฺ✍ฺ（◕ฺｖ◕ฺ）✌ฺ⠀Writing with an Actual Hand Holding a Pencil 19
＼＿ﾍ(ω｀*)⠀Writing on a Laptop 1
＼_(･ω･｀)⠀Writing on a Laptop 2
＼＿ﾍ(ﾟeﾟ#)⠀Writing on a Laptop 3
＼_(ω・｀*)ゞ⠀Writing on a Laptop 4
＼＿ﾍ(´ω｀)⠀Writing on a Laptop 5
＼＿ﾍ(◕‿◕✰)⠀Writing on a Laptop 6
＼_(´ι _` 　)⠀Writing on a Laptop 7
βακα…_〆(´･ω･｀*)⠀Baka 1
βακα…_φ(ﾟωﾟ )⠀Baka 2
βακα…_〆(ﾟ▽ﾟ*)⠀Baka 3
βακα…_〆(・ｪ・*)⠀Baka 4
βακα…_〆(´･ｪ･｀*)⠀Baka 5
βακα…_φ(´ι _` 　)⠀Baka 6
βακα?…_φ(￣ ￣|||)⠀Baka 7
βακαУαЯο…_〆(ﾟ▽ﾟ*)⠀Baka 8
вакатΙη…￠(-∀・○)⠀Baka 9
【ъака】＼_(・ω・`)⠀Baka 10
βακα…_〆(゜▽゜*)⠀Baka 11
βακα…_φ(ﾟ∀ﾟ )⠀Baka 12
ВАКА❣ฺ✍ฺ（◕ฺｖ◕ฺ）✌ฺ⠀Baka 13
ＳΟЯЯΥ＿φ（･益ｑ｡｀)･ﾟ･ｏ｡⠀Other Words 1
Ｉ ￡ονё Υου…..φ┃*･ω･*┃⠀Other Words 2
ηακετα…_〆(；ωq｀)⠀Other Words 3
￡ονё Υου…..φ(〃∇〃 ))⠀Other Words 4
†=”Ⴛ̸ ♡(˃͈ દ ˂͈ ༶ )⠀Miscellaneous 1
ණ⃛(ᵒ͈̑ᴗ̂ᵒ͈̑ )”⠀Miscellaneous 2
＿ø(●ʘ╻ʘ●)⠀Miscellaneous 3
(๑ ऀืົཽ₍₍ළ₎₎ ऀืົཽ)✧⠀Freaky or Bizarre Looking 1
(≼⓪≽◟⋌⋚⋛⋋◞≼⓪≽)⠀Freaky or Bizarre Looking 2
(◞≼۩۞۩≽◟◞౪◟◞≼۩۞۩≽◟)⠀Freaky or Bizarre Looking 3
(◞≼◎≽◟◞౪◟◞≼◎≽◟)⠀Freaky or Bizarre Looking 4
(◞≼●≽◟◞౪◟◞≼●≽◟)⠀Freaky or Bizarre Looking 5
(◞≼☉≽◟◞౪◟◞≼☉≽◟)⠀Freaky or Bizarre Looking 6
(◞≼థ≽◟◞౪◟◞≼థ≽◟)⠀Freaky or Bizarre Looking 7
(☝΄◞ิ۝◟ิ‵)☝⠀Freaky or Bizarre Looking 8
ཀ༼ༀ༽ཫ་῍̩̖̬ ̎ ̎✧⠀Freaky or Bizarre Looking 9
(₍ˀ˟͈͈͈᷄ළ˟͈͈͈᷅ˁ₎)⠀Freaky or Bizarre Looking 10
(ּơ̑ළּơ̑)⠀Freaky or Bizarre Looking 11
⁽₍੭ ՞̑◞ළ̫̉◟՞̑₎⁾੭⠀Freaky or Bizarre Looking 12
↻( ꑡ᷉ˋ͈۝ˊ͈)ꑡ᷉༄⠀Freaky or Bizarre Looking 13
་ཀ༼ༀ༽ཫ་῍̩̖̬ ̎ ̎✧⠀Freaky or Bizarre Looking 14
━꒰ ⁎꒦ິཽ ۝꒦ິཽॢ꒱━⠀Freaky or Bizarre Looking 15
Ⴤ༼༎ত:౧:ত༎༽Ⴤ⠀Freaky or Bizarre Looking 16
⑉౦ළ౦⑉⠀Freaky or Bizarre Looking 17
(•චළච•)⠀Freaky or Bizarre Looking 18
_̴ı̴̴̡̡̡ ̡͌<̡̡̡ ̡͌<̡*̡̡ ̴̡ı̴̴̡ ̡̡͡|̲̲̲͡͡͡ ̲▫̲͡ ̲̲̲͡͡π̲̲͡͡ ̲̲͡▫̲̲͡͡ ̲|̡̡̡ ̡ ̴̡ı̴̡̡ ̡͌<̡̡̡⠀Freaky or Bizarre Looking 19
ʅ͡͡͡͡͡͡͡͡͡͡͡(Ɵ۝Ө)ʃ͡͡͡͡͡͡͡͡͡͡⠀Freaky or Bizarre Looking 20
.̸̸̸̸̸̸̸̸̸̸̸̸̸̸̸̸̸̸̸̸̸̸̸̸̨̨̨̨̨̨̨̨̨̨̨̨.̸̸̨̨ↂ⃝⃓⃙⃚⃘۝ↂ⃝⃓⃙⃚⃘.̸̸̸̸̸̸̸̸̸̸̸̸̸̸̸̸̸̸̸̸̸̸̸̸̨̨̨̨̨̨̨̨̨̨̨̨.̸̸̨̨⠀Freaky or Bizarre Looking 21
*:･✧⃛(ཽ๑ඕัළඕั๑)✧⃛*:･⠀Freaky or Bizarre Looking 22
ꐑ(ཀ ඊູ ఠీੂ)༼ू༈೧ູ࿃ूੂ༽(ଳծູɵੂ≢)ꐑ⠀Freaky or Bizarre Looking 23
( ⌒⃘ཽ⃜ ◞ළ̆◟ ⌒⃘ཽ⃜ )⠀Freaky or Bizarre Looking 24
ſ░▓░▃░▓░ƪ. ◖ƪ❍⊁◞..◟⊀❍|◗⠀Freaky or Bizarre Looking 25
༎ຶ‿༎ຶ⠀Freaky Eyes 1
<´༎ຶਊ ༎ຶ`<⠀Freaky Eyes 2
( ༎ຶŎ༎ຶ )⠀Freaky Eyes 3
( ཀ͝ ∧ ཀ͝ )⠀Freaky Eyes 4
(<´༎ຶД༎ຶ`)⠀Freaky Eyes 5
(<´༎ຶٹ༎ຶ`)⠀Freaky Eyes 6
(<´༎ຶ益༎ຶ`)♡⠀Freaky Eyes 7
(( ༎ຶ‿༎ຶ ))⠀Freaky Eyes 8
⁽⁽(ཀ д ཀ)⁾⁾⠀Freaky Eyes 9
(༎ຶꈊ༎ຶ╬)⠀Freaky Eyes 10
(´༎ຶ༎ຶ)⠀Freaky Eyes 11
༼<´༎ຶ ۝ ༎ຶ༽⠀Freaky Eyes 12
☜(:༎ຶ<益<༎ຶ<)☞⠀Freaky Eyes 13
ヾ(<<<<<<<<<<<<´༎ຶ ۝ ༎ຶ)ﾉ⠀Freaky Eyes 14
v(<´༎ຶД༎ຶ`)v⠀Freaky Eyes 15
(༎ຶ⌑༎ຶ)⠀Freaky Eyes 16
(<´༎ຶ益༎ຶ`)♡⠀Freaky Eyes 17
(•ؔ༎ຶළॆؔ༎ຶ)⠀Freaky Eyes 18
(༎ຶ ෴ ༎ຶ)⠀Freaky Eyes 19
( ´༎ຶㅂ༎ຶ`)⠀Freaky Eyes 20
(<´༎ຶ༎ຶ`)⠀Freaky Eyes 21
(༎ຶ ༎ຶ 三 ༎ຶ ༎ຶ)⠀Freaky Eyes 22
(´༎ຶ۝༎ຶ)⠀Freaky Eyes 23
༼<´༎ຶ ༎ຶ༽⠀Freaky Eyes 24
(๑ؔ༎̐৫῎ؔ༎̐)⁝⠀Freaky Eyes 25
(ཫ͝⁔ੂཀ͝)⠀Freaky Eyes 26
(ཫ͝﹏ੂཀ͝)⠀Freaky Eyes 27
㠭(:༑༎ຶ䍏༎ຶ༑:)㠭⠀Freaky Eyes 28
(༎ຶ ۝ ༎ຶ 三 ༎ຶ ۝ ༎ຶ)⠀Freaky Eyes 29
૮(༎໊ඏ༎໊)ა⠀Freaky Eyes 30
•ू(༎ຶ۝༎ຶ`•ू) )੭ु⁾⁾⠀Freaky Eyes 31
o͡͡͡͡͡͡͡͡͡͡͡͡͡͡╮༼<´༎ຶ.̸̸̸̸̸̸̸̸̸̸̸̸̸̸̸̸̸̸̸̸̸̸̸̸̨̨̨̨̨̨̨̨̨̨̨̨.̸̸̨̨۝ ༎ຶ༽╭o͡͡͡͡͡͡͡͡͡͡͡͡͡͡⠀Freaky Eyes 32
o͡͡͡͡͡͡͡͡͡͡͡͡͡͡╮(<´༎ຶД༎ຶ`)╭o͡͡͡͡͡͡͡͡͡͡͡͡͡͡⠀Freaky Eyes 33
(‿ˠ‿)⠀Buttmoji 1
(‿ꜟ‿)⠀Buttmoji 2
˓˓(‿◟̩ ͜ )˒˒⠀Buttmoji 3
( ＾◡＾)っ (‿|‿)⠀Buttmoji 4
༼ つ ✿◕‿◕✿༽つ (‿ˠ‿)⠀Buttmoji 5
( , )⠀Buttmoji 6
(_______I_______)⠀Buttmoji 7
(‿!‿)⠀Buttmoji 8
(‿!‿) ԅ(´ڡ`ԅ)⠀Buttmoji 9
(‿!‿) ԅ(≖‿≖ԅ)⠀Buttmoji 10
╰U╯☜(◉ɷ◉ )⠀Probably NSFW 1
( ◜◡＾)っ✂╰⋃╯⠀Probably NSFW 2
ღ╰⋃╯ღ•̥̑ .̮ •̥̑)⠀Probably NSFW 3
╰⋃╯ლ(´ڡ`ლ)⠀Probably NSFW 4
(´◔౪◔)✂╰⋃╯⠀Probably NSFW 5
╰⋃╯(ԾДԾ)७⠀Probably NSFW 6
⊍⊍ ლ(◉◡◉ლ)⠀Probably NSFW 7
(◉۝◉)╰U╯⠀Probably NSFW 8
( ◜◡＾)っ╰⋃╯⠀Probably NSFW 9
╭∩╮(︶ε︶*)chu⠀Probably NSFW 10
( ๑´•ω•)۶”╰⋃╯ (ㆆᴗㆆ)⠀Probably NSFW 11
༼ つ ✿◕‿◕✿༽つ╰⋃╯⠀Probably NSFW 12
(~° ͜ʖ͡°)~ ( . ( . )⠀Probably NSFW 13
(✿ ◕‿◕) ᓄ✂╰⋃╯⠀Probably NSFW 14
ヽ༼✿ʘ̚ل͜ʘ̚༽ﾉ╰⋃╯⠀Probably NSFW 15
╰⋃╯ლ(´ڡ`ლ)？⠀Probably NSFW 16
(◔‸◔ )っ✄╰⋃╯⠀Probably NSFW 17
( ° ͜ʖ͡°)╭∩╮⠀Probably NSFW 18
✂╭∩╮(°□° )⠀Probably NSFW 19
( ͝° ͜ʖ͡°)つ✂╰⋃╯⠀Probably NSFW 20
(▀̿̿Ĺ̯̿̿▀̿ ̿) ✂╰⋃╯⠀Probably NSFW 21
(つ°ヮ°)つ └⋃┘⠀Probably NSFW 22
(✿ ◕‿◕) ᓄ✂╰U╯⠀Probably NSFW 23
(Ɔ˘⌣˘)(˘⌣˘)˘⌣˘ C) ᑦ∪ᔿ ᵒᐢ ᔿᵉᵎᵎ⠀Probably NSFW 24
( ◜◡＾)っ✂ღ╰⋃╯ღ•̥̑ .̮ •̥̑)⠀Probably NSFW 25
"""

rofi = Popen(
    args=[
        'rofi',
        '-dmenu',
        '-i',
        '-p',
        ' Kaomoji : ',
        '-width',
        '50',
        '-location',
        '2',
        '-yoffset',
        '600',
        '-bw',
        '1',
        '-lines',
        '13',
        '-font',
        'hack 14',
        '-fake-transparency',
        '-kb-custom-1',
        'Alt+c'
    ],
    stdin=PIPE,
    stdout=PIPE
)
(stdout, stderr) = rofi.communicate(input=emojis.encode('utf-8'))

if rofi.returncode == 1:
    exit()
else:
    split = stdout.find('⠀')
    emoji = stdout[:split]
    if rofi.returncode == 0:
        Popen(
            args=[
                'xdotool',
                'type',
                '--delay',
                '32',
                '--clearmodifiers',
                #emoji.decode('utf-8')
                emoji
                ]
        )
    elif rofi.returncode == 10:
        xsel = Popen(
            args=[
                'xsel',
                '-i',
                '-b'
            ],
            stdin=PIPE
        )
        xsel.communicate(input=emoji)
