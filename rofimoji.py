#!/usr/bin/python3
# -*- coding: utf-8 -*-

from subprocess import Popen, PIPE
import sys
reload(sys)
sys.setdefaultencoding('UTF8')


emojis=u"""
⠀(Joy)
⠀(Love)
⠀(Embarrassment)
⠀(Sympathy)
⠀(Dissatisfaction)
⠀(Anger)
⠀(Sadness)
⠀(Pain)
⠀(Fear)
⠀(Indifference)
⠀(Confusion)
⠀(Doubt)
⠀(Surprise)
⠀(Greeting)
⠀(Hugging)
⠀(Winking)
⠀(Apologizing)
⠀(Nosebleeding)
⠀(Writing)
⠀(Running)
⠀(Sleeping)
⠀(Cat)
⠀(Bear)
⠀(Dog)
⠀(Rabbit)
⠀(Pig)
⠀(Bird)
⠀(Fish)
⠀(Spider)
⠀(Friends)
⠀(Ennemies)
⠀(Weapons)
⠀(Magic)
⠀(Food)
⠀(Music)
⠀(Games)
⠀(Faces)
⠀(Spacial)

(ﾉ◕ヮ◕)ﾉ*:･ﾟ✧⠀Joy, 1
(* ^ ω ^)⠀Joy, 2
(´ ∀ ` *)⠀Joy, 3
٩(◕‿◕｡)۶⠀Joy, 4
☆*:.｡.o(≧▽≦)o.｡.:*☆⠀Joy, 5
(o^▽^o)⠀Joy, 6
(⌒▽⌒)☆⠀Joy, 7
<(￣︶￣)>⠀Joy, 8
。.:☆*:･'(*⌒―⌒*)))⠀Joy, 9
ヽ(・∀・)ﾉ⠀Joy, 10
(´｡• ω •｡`)⠀Joy, 11
(￣ω￣)⠀Joy, 12
｀;:゛;｀;･(°ε° )⠀Joy, 13
(o･ω･o)⠀Joy, 14
(＠＾◡＾)⠀Joy, 15
ヽ(*・ω・)ﾉ⠀Joy, 16
(o_ _)ﾉ彡☆⠀Joy, 17
(^人^)⠀Joy, 18
(o´▽`o)⠀Joy, 19
(*´▽`*)⠀Joy, 20
｡ﾟ( ﾟ^∀^ﾟ)ﾟ｡⠀Joy, 21
( ´ ω ` )⠀Joy, 22
(((o(*°▽°*)o)))⠀Joy, 23
(≧◡≦)⠀Joy, 24
(o´∀`o)⠀Joy, 25
(´• ω •`)⠀Joy, 26
(＾▽＾)⠀Joy, 27
(⌒ω⌒)⠀Joy, 28
∑d(°∀°d)⠀Joy, 29
╰(▔∀▔)╯⠀Joy, 30
(─‿‿─)⠀Joy, 31
(*^‿^*)⠀Joy, 32
ヽ(o^ ^o)ﾉ⠀Joy, 33
(✯◡✯)⠀Joy, 34
(◕‿◕)⠀Joy, 35
(*≧ω≦*)⠀Joy, 36
(☆▽☆)⠀Joy, 37
(⌒‿⌒)⠀Joy, 38
＼(≧▽≦)／⠀Joy, 39
ヽ(o＾▽＾o)ノ⠀Joy, 40
☆ ～('▽^人)⠀Joy, 41
(*°▽°*)⠀Joy, 42
٩(｡•́‿•̀｡)۶⠀Joy, 43
(✧ω✧)⠀Joy, 44
ヽ(*⌒▽⌒*)ﾉ⠀Joy, 45
(´｡• ᵕ •｡`)⠀Joy, 46
( ´ ▽ ` )⠀Joy, 47
(￣▽￣)⠀Joy, 48
╰(*´︶`*)╯⠀Joy, 49
ヽ(>∀<☆)ノ⠀Joy, 50
o(≧▽≦)o⠀Joy, 51
(☆ω☆)⠀Joy, 52
(っ˘ω˘ς )⠀Joy, 53
＼(￣▽￣)／⠀Joy, 54
(*¯︶¯*)⠀Joy, 55
＼(＾▽＾)／⠀Joy, 56
٩(◕‿◕)۶⠀Joy, 57
(o˘◡˘o)⠀Joy, 58
\(★ω★)/⠀Joy, 59
\(^ヮ^)/⠀Joy, 60
(〃＾▽＾〃)⠀Joy, 61
(╯✧▽✧)╯⠀Joy, 62
o(>ω<)o⠀Joy, 63
o( ❛ᴗ❛ )o⠀Joy, 64
｡ﾟ(TヮT)ﾟ｡⠀Joy, 65
( ‾́ ◡ ‾́ )⠀Joy, 66
(ﾉ´ヮ`)ﾉ*: ･ﾟ⠀Joy, 67
(b ᵔ▽ᵔ)b⠀Joy, 68
(๑˃ᴗ˂)ﻭ⠀Joy, 69
(๑˘︶˘๑)⠀Joy, 70
( ˙꒳​˙ )⠀Joy, 71
(*꒦ິ꒳꒦ີ)⠀Joy, 72
°˖✧◝(⁰▿⁰)◜✧˖°⠀Joy, 73
(´･ᴗ･ ` )⠀Joy, 74

(ﾉ´ з `)ノ⠀Love, 1
(♡μ_μ)⠀Love, 2
(*^^*)♡⠀Love, 3
☆⌒ヽ(*'､^*)chu⠀Love, 4
(♡-_-♡)⠀Love, 5
(￣ε￣＠)⠀Love, 6
ヽ(♡‿♡)ノ⠀Love, 7
( ´ ∀ `)ノ～ ♡⠀Love, 8
(─‿‿─)♡⠀Love, 9
(´｡• ᵕ •｡`) ♡⠀Love, 10
(*♡∀♡)⠀Love, 11
(｡・//ε//・｡)⠀Love, 12
(´ ω `♡)⠀Love, 13
♡( ◡‿◡ )⠀Love, 14
(◕‿◕)♡⠀Love, 15
(/▽＼*)｡o○♡⠀Love, 16
(ღ˘⌣˘ღ)⠀Love, 17
(♡°▽°♡)⠀Love, 18
♡(｡- ω -)⠀Love, 19
♡ ～('▽^人)⠀Love, 20
(´• ω •`) ♡⠀Love, 21
(´ ε ` )♡⠀Love, 22
(´｡• ω •｡`) ♡⠀Love, 23
( ´ ▽ ` ).｡ｏ♡⠀Love, 24
╰(*´︶`*)╯♡⠀Love, 25
(*˘︶˘*).｡.:*♡⠀Love, 26
(♡˙︶˙♡)⠀Love, 27
♡＼(￣▽￣)／♡⠀Love, 28
(≧◡≦) ♡⠀Love, 29
(⌒▽⌒)♡⠀Love, 30
(*¯ ³¯*)♡⠀Love, 31
(っ˘з(˘⌣˘ ) ♡⠀Love, 32
♡ (˘▽˘>ԅ( ˘⌣˘)⠀Love, 33
( ˘⌣˘)♡(˘⌣˘ )⠀Love, 34
(/^-^(^ ^*)/ ♡⠀Love, 35
٩(♡ε♡)۶⠀Love, 36
σ(≧ε≦σ) ♡⠀Love, 37
♡ (⇀ 3 ↼)⠀Love, 38
♡ (￣З￣)⠀Love, 39
(❤ω❤)⠀Love, 40
(˘∀˘)/(μ‿μ) ❤⠀Love, 41
❤ (ɔˆз(ˆ⌣ˆc)⠀Love, 42
(´♡‿♡`)⠀Love, 43
(°◡°♡)⠀Love, 44
Σ>―(〃°ω°〃)♡→⠀Love, 45

(⌒_⌒;)⠀Embarrassment, 1
(o^ ^o)⠀Embarrassment, 2
(*/ω＼)⠀Embarrassment, 3
(*/。＼)⠀Embarrassment, 4
(*/_＼)⠀Embarrassment, 5
(*ﾉωﾉ)⠀Embarrassment, 6
(o-_-o)⠀Embarrassment, 7
(*μ_μ)⠀Embarrassment, 8
( ◡‿◡ *)⠀Embarrassment, 9
(ᵔ.ᵔ)⠀Embarrassment, 10
(*ﾉ∀`*)⠀Embarrassment, 11
(//▽//)⠀Embarrassment, 12
(//ω//)⠀Embarrassment, 13
(ノ*°▽°*)⠀Embarrassment, 14
(*^.^*)⠀Embarrassment, 15
(*ﾉ▽ﾉ)⠀Embarrassment, 16
(￣▽￣*)ゞ⠀Embarrassment, 17
(⁄ ⁄•⁄ω⁄•⁄ ⁄)⠀Embarrassment, 18
(*/▽＼*)⠀Embarrassment, 19
(⁄⁄>⁄ ▽ ⁄<⁄⁄)⠀Embarrassment, 20
(„ಡωಡ„)⠀Embarrassment, 21
(ง ื▿ ื)ว⠀Embarrassment, 22

(ノ_<。)ヾ(´ ▽ ` )⠀Sympathy, 1
｡･ﾟ･(ﾉД`)ヽ(￣ω￣ )⠀Sympathy, 2
ρ(- ω -、)ヾ(￣ω￣; )⠀Sympathy, 3
ヽ(￣ω￣(。。 )ゝ⠀Sympathy, 4
(*´ I `)ﾉﾟ(ﾉД｀ﾟ)ﾟ｡⠀Sympathy, 5
ヽ(~_~(・_・ )ゝ⠀Sympathy, 6
(ﾉ_；)ヾ(´ ∀ ` )⠀Sympathy, 7
(; ω ; )ヾ(´∀`* )⠀Sympathy, 8
(*´ー)ﾉ(ノд`)⠀Sympathy, 9
(´-ω-`( _ _ )⠀Sympathy, 10
(っ´ω`)ﾉ(╥ω╥)⠀Sympathy, 11
(ｏ・_・)ノ”(ノ_<、)⠀Sympathy, 12

(＃＞＜)⠀Dissatisfaction, 1
(；⌣̀_⌣́)⠀Dissatisfaction, 2
☆ｏ(＞＜；)○⠀Dissatisfaction, 3
(￣ ￣|||)⠀Dissatisfaction, 4
(；￣Д￣)⠀Dissatisfaction, 5
(￣□￣」)⠀Dissatisfaction, 6
(＃￣0￣)⠀Dissatisfaction, 7
(＃￣ω￣)⠀Dissatisfaction, 8
(￢_￢;)⠀Dissatisfaction, 9
(＞ｍ＜)⠀Dissatisfaction, 10
(」°ロ°)」⠀Dissatisfaction, 11
(〃＞＿＜;〃)⠀Dissatisfaction, 12
(＾＾＃)⠀Dissatisfaction, 13
(︶︹︺)⠀Dissatisfaction, 14
(￣ヘ￣)⠀Dissatisfaction, 15
<(￣ ﹌ ￣)>⠀Dissatisfaction, 16
(￣︿￣)⠀Dissatisfaction, 17
(＞﹏＜)⠀Dissatisfaction, 18
(--_--)⠀Dissatisfaction, 19
凸(￣ヘ￣)⠀Dissatisfaction, 20
ヾ( ￣O￣)ツ⠀Dissatisfaction, 21
(⇀‸↼‶)⠀Dissatisfaction, 22
o(>< )o⠀Dissatisfaction, 23
(」＞＜)」⠀Dissatisfaction, 24
(ᗒᗣᗕ)՞⠀Dissatisfaction, 25
(눈_눈)⠀Dissatisfaction, 26

(＃`Д´)⠀Anger, 1
(`皿´＃)⠀Anger, 2
( ` ω ´ )⠀Anger, 3
ヽ( `д´*)ノ⠀Anger, 4
(・`ω´・)⠀Anger, 5
(`ー´)⠀Anger, 6
ヽ(`⌒´メ)ノ⠀Anger, 7
凸(`△´＃)⠀Anger, 8
( `ε´ )⠀Anger, 9
ψ( ` ∇ ´ )ψ⠀Anger, 10
ヾ(`ヘ´)ﾉﾞ⠀Anger, 11
ヽ(‵﹏´)ノ⠀Anger, 12
(ﾒ` ﾛ ´)⠀Anger, 13
(╬`益´)⠀Anger, 14
┌∩┐(◣_◢)┌∩┐⠀Anger, 15
凸( ` ﾛ ´ )凸⠀Anger, 16
Σ(▼□▼メ)⠀Anger, 17
(°ㅂ°╬)⠀Anger, 18
ψ(▼へ▼メ)～→⠀Anger, 19
(ノ°益°)ノ⠀Anger, 20
(҂ `з´ )⠀Anger, 21
(‡▼益▼)⠀Anger, 22
(҂` ﾛ ´)凸⠀Anger, 23
((╬◣﹏◢))⠀Anger, 24
٩(╬ʘ益ʘ╬)۶⠀Anger, 25
(╬ Ò﹏Ó)⠀Anger, 26
＼＼٩(๑`^´๑)۶／／⠀Anger, 27
(凸ಠ益ಠ)凸⠀Anger, 28
↑_(ΦwΦ)Ψ⠀Anger, 29
←~(Ψ▼ｰ▼)∈⠀Anger, 30
୧((31Φ益Φ31))୨⠀Anger, 31
٩(ఠ益ఠ)۶⠀Anger, 32
(ﾉಥ益ಥ)ﾉ⠀Anger, 33

(ノ_<。)⠀Sadness, 1
(-_-)⠀Sadness, 2
(´-ω-`)⠀Sadness, 3
.･ﾟﾟ･(／ω＼)･ﾟﾟ･.⠀Sadness, 4
(μ_μ)⠀Sadness, 5
(ﾉД`)⠀Sadness, 6
(-ω-、)⠀Sadness, 7
。゜゜(´Ｏ`) ゜゜。⠀Sadness, 8
o(TヘTo)⠀Sadness, 9
( ; ω ; )⠀Sadness, 10
(｡╯︵╰｡)⠀Sadness, 11
｡･ﾟﾟ*(>д<)*ﾟﾟ･｡⠀Sadness, 12
( ﾟ，_ゝ｀)⠀Sadness, 13
(个_个)⠀Sadness, 14
(╯︵╰,)⠀Sadness, 15
｡･ﾟ(ﾟ><ﾟ)ﾟ･｡⠀Sadness, 16
( ╥ω╥ )⠀Sadness, 17
(╯_╰)⠀Sadness, 18
(╥_╥)⠀Sadness, 19
.｡･ﾟﾟ･(＞_＜)･ﾟﾟ･｡.⠀Sadness, 20
(／ˍ・、)⠀Sadness, 21
(ノ_<、)⠀Sadness, 22
(╥﹏╥)⠀Sadness, 23
｡ﾟ(｡ﾉωヽ｡)ﾟ｡⠀Sadness, 24
(つω`｡)⠀Sadness, 25
(｡T ω T｡)⠀Sadness, 26
(ﾉω･､)⠀Sadness, 27
･ﾟ･(｡>ω<｡)･ﾟ･⠀Sadness, 28
(T_T)⠀Sadness, 29
(>_<)⠀Sadness, 30
(っ˘̩╭╮˘̩)っ⠀Sadness, 31
｡ﾟ･ (>﹏<) ･ﾟ｡⠀Sadness, 32
o(〒﹏〒)o⠀Sadness, 33
(｡•́︿•̀｡)⠀Sadness, 34
(ಥ﹏ಥ)⠀Sadness, 35

~(>_<~)⠀Pain, 1
☆⌒(> _ <)⠀Pain, 2
☆⌒(>。<)⠀Pain, 3
(☆_@)⠀Pain, 4
(×_×)⠀Pain, 5
(x_x)⠀Pain, 6
(×_×)⌒☆⠀Pain, 7
(x_x)⌒☆⠀Pain, 8
(×﹏×)⠀Pain, 9
☆(＃××)⠀Pain, 10
(＋_＋)⠀Pain, 11
[ ± _ ± ]⠀Pain, 12

(ノωヽ), 1
(／。＼)⠀Fear, 2
(ﾉ_ヽ)⠀Fear, 3
..・ヾ(。＞＜)シ⠀Fear, 4
(″ロ゛)⠀Fear, 5
(;;;*_*)⠀Fear, 6
(・人・)⠀Fear, 7
＼(〇_ｏ)／⠀Fear, 8
(/ω＼)⠀Fear, 9
(/_＼)⠀Fear, 10
〜(＞＜)〜⠀Fear, 11
Σ(°△°|||)︴⠀Fear, 12
(((＞＜)))⠀Fear, 13
{{ (>_<) }}⠀Fear, 14
＼(º □ º l|l)/⠀Fear, 15
〣( ºΔº )〣⠀Fear, 16

ヽ(ー_ー )ノ⠀Indifference, 1
ヽ(´ー` )┌⠀Indifference, 2
┐(‘～` )┌⠀Indifference, 3
ヽ(　￣д￣)ノ⠀Indifference, 4
┐(￣ヘ￣)┌⠀Indifference, 5
ヽ(￣～￣　)ノ⠀Indifference, 6
╮(￣_￣)╭⠀Indifference, 7
ヽ(ˇヘˇ)ノ⠀Indifference, 8
┐(￣～￣)┌⠀Indifference, 9
┐(︶▽︶)┌⠀Indifference, 10
╮(￣～￣)╭⠀Indifference, 11
¯\_(ツ)_/¯⠀Indifference, 12
┐( ´ д ` )┌⠀Indifference, 13
╮(︶︿︶)╭⠀Indifference, 14
┐(￣∀￣)┌⠀Indifference, 15
┐( ˘ ､ ˘ )┌⠀Indifference, 16
╮(︶▽︶)╭⠀Indifference, 17
╮( ˘ ､ ˘ )╭⠀Indifference, 18
┐( ˘_˘ )┌⠀Indifference, 19
╮( ˘_˘ )╭⠀Indifference, 20
ᕕ( ᐛ )ᕗ⠀Indifference, 21

(￣ω￣;)⠀Confusion, 1
σ(￣、￣〃)⠀Confusion, 2
(￣～￣;)⠀Confusion, 3
(-_-;)・・・⠀Confusion, 4
┐('～`;)┌⠀Confusion, 5
(・_・ヾ⠀Confusion, 6
(〃￣ω￣〃ゞ⠀Confusion, 7
┐(￣ヘ￣;)┌⠀Confusion, 8
(・_・;)⠀Confusion, 9
(￣_￣)・・・⠀Confusion, 10
╮(￣ω￣;)╭⠀Confusion, 11
(￣.￣;)⠀Confusion, 12
(＠_＠)⠀Confusion, 13
(・・;)ゞ⠀Confusion, 14
Σ(￣。￣ﾉ)⠀Confusion, 15
(・・ ) ?⠀Confusion, 16
(•ิ_•ิ)?⠀Confusion, 17
(◎ ◎)ゞ⠀Confusion, 18
(ーー;)⠀Confusion, 19
ლ(ಠ_ಠ ლ)⠀Confusion, 20
ლ(¯ロ¯"ლ)⠀Confusion, 21

(￢_￢)⠀Doubt, 1
(→_→)⠀Doubt, 2
(￢ ￢)⠀Doubt, 3
(￢‿￢ )⠀Doubt, 4
(¬_¬ )⠀Doubt, 5
(←_←)⠀Doubt, 6
(¬ ¬ )⠀Doubt, 7
(¬‿¬ )⠀Doubt, 8
(↼_↼)⠀Doubt, 9
(⇀_⇀)⠀Doubt, 10

w(°ｏ°)w⠀Surprise, 1
ヽ(°〇°)ﾉ⠀Surprise, 2
Σ(O_O)⠀Surprise, 3
Σ(°ロ°)⠀Surprise, 4
(⊙_⊙)⠀Surprise, 5
(o_O)⠀Surprise, 6
(O_O;)⠀Surprise, 7
(O.O)⠀Surprise, 8
(°ロ°) !⠀Surprise, 9
(o_O) !⠀Surprise, 10
(□_□)⠀Surprise, 11
Σ(□_□)⠀Surprise, 12
∑(O_O;)⠀Surprise, 13
( : ౦ ‸ ౦ : )⠀Surprise, 14

(*・ω・)ﾉ⠀Greeting, 1
(￣▽￣)ノ⠀Greeting, 2
(°▽°)/⠀Greeting, 3
( ´ ∀ ` )ﾉ⠀Greeting, 4
(^-^*)/⠀Greeting, 5
(＠´ー`)ﾉﾞ⠀Greeting, 6
(´• ω •`)ﾉ⠀Greeting, 7
( ° ∀ ° )ﾉﾞ⠀Greeting, 8
ヾ(*'▽'*)⠀Greeting, 9
＼(⌒▽⌒)⠀Greeting, 10
ヾ(☆▽☆)⠀Greeting, 11
( ´ ▽ ` )ﾉ⠀Greeting, 12
(^０^)ノ⠀Greeting, 13
~ヾ(・ω・)⠀Greeting, 14
(・∀・)ノ⠀Greeting, 15
ヾ(^ω^*)⠀Greeting, 16
(*°ｰ°)ﾉ⠀Greeting, 17
(・_・)ノ⠀Greeting, 18
(o´ω`o)ﾉ⠀Greeting, 19
ヾ(☆'∀'☆)⠀Greeting, 20
(￣ω￣)/⠀Greeting, 21
( ´ ω ` )ノﾞ⠀Greeting, 22
(⌒ω⌒)ﾉ⠀Greeting, 23
(o^ ^o)/⠀Greeting, 24
(≧▽≦)/⠀Greeting, 25
(✧∀✧)/⠀Greeting, 26
(o´▽`o)ﾉ⠀Greeting, 27
(￣▽￣)/⠀Greeting, 28

(づ￣ ³￣)づ⠀Hugginh, 1
(つ≧▽≦)つ⠀Hugginh, 2
(つ✧ω✧)つ⠀Hugginh, 3
(づ ◕‿◕ )づ⠀Hugginh, 4
(⊃｡•́‿•̀｡)⊃⠀Hugginh, 5
(つ . •́ _ʖ •̀ .)つ⠀Hugginh, 6
(っಠ‿ಠ)っ⠀Hugginh, 7
(づ◡﹏◡)づ⠀Hugginh, 8
⊂(´• ω •`⊂)⠀Hugginh, 9
⊂(･ω･*⊂)⠀Hugginh, 10
⊂(￣▽￣)⊃⠀Hugginh, 11
⊂( ´ ▽ ` )⊃⠀Hugginh, 12

(^_~)⠀Winking, 1
( ﾟｏ⌒)⠀Winking, 2
(^_-)≡☆⠀Winking, 3
(^ω~)⠀Winking, 4
(>ω^)⠀Winking, 5
(~人^)⠀Winking, 6
(^_-)⠀Winking, 7
( -_・)⠀Winking, 8
(^_<)〜☆⠀Winking, 9
(^人<)〜☆⠀Winking, 10
☆⌒(≧▽​° )⠀Winking, 11
☆⌒(ゝ。∂)⠀Winking, 12
(^_<)⠀Winking, 13
(^_−)☆⠀Winking, 14
(･ω<)☆⠀Winking, 15

m(_ _)m⠀Apologizing, 1
(シ_ _)シ⠀Apologizing, 2
m(. .)m⠀Apologizing, 3
<(_ _)>⠀Apologizing, 4
人(_ _*)⠀Apologizing, 5
(*_ _)人⠀Apologizing, 6
m(_ _;m)⠀Apologizing, 7
(m;_ _)m⠀Apologizing, 8
(シ. .)シ⠀Apologizing, 9

(*￣ii￣)⠀Nosebleeding, 1
(￣ﾊ￣*)⠀Nosebleeding, 2
\(￣ﾊ￣)⠀Nosebleeding, 3
(＾་།＾)⠀Nosebleeding, 4
(＾〃＾)⠀Nosebleeding, 5
(￣ ¨ヽ￣)⠀Nosebleeding, 6
(￣ ;￣)⠀Nosebleeding, 7
(￣ ;;￣)⠀Nosebleeding, 8

__φ(．．)⠀Writing, 1
( ￣ー￣)φ__⠀Writing, 2
__φ(。。)⠀Writing, 3
__φ(．．;)⠀Writing, 4
ヾ( `ー´)シφ__⠀Writing, 5
__〆(￣ー￣ )⠀Writing, 6
....φ(・∀・*)⠀Writing, 7
___〆(・∀・)⠀Writing, 8
( ^▽^)ψ__⠀Writing, 9
....φ(︶▽︶)φ....⠀Writing, 10
( . .)φ__⠀Writing, 11
__φ(◎◎ヘ)⠀Writing, 12

☆ﾐ(o*･ω･)ﾉ⠀Running, 1
C= C= C= C= C=┌(;・ω・)┘⠀Running, 2
─=≡Σ((( つ＞＜)つ⠀Running, 3
ε=ε=ε=ε=┌(;￣▽￣)┘⠀Running, 4
ε=ε=┌( >_<)┘⠀Running, 5
C= C= C= C=┌( `ー´)┘⠀Running, 6
ε===(っ≧ω≦)っ⠀Running, 7
ヽ(￣д￣;)ノ=3=3=3⠀Running, 8
。。。ミヽ(。＞＜)ノ⠀Running, 9

[(－－)]..zzZ⠀Sleeping, 1
(－_－) zzZ⠀Sleeping, 2
(∪｡∪)｡｡｡zzZ⠀Sleeping, 3
(－ω－) zzZ⠀Sleeping, 4
(￣o￣) zzZZzzZZ⠀Sleeping, 5
(( _ _ ))..zzzZZ⠀Sleeping, 6
(￣ρ￣)..zzZZ⠀Sleeping, 7
(－.－)...zzz⠀Sleeping, 8
(＿ ＿*) Z z z⠀Sleeping, 9
(x . x) ~~zzZ⠀Sleeping, 10

(=^･ω･^=)⠀Cat, 1
(=^･ｪ･^=)⠀Cat, 2
(=①ω①=)⠀Cat, 3
( =ω=)..nyaa⠀Cat, 4
(= ; ｪ ; =)⠀Cat, 5
(=`ω´=)⠀Cat, 6
(=^‥^=)⠀Cat, 7
( =ノωヽ=)⠀Cat, 8
(=⌒‿‿⌒=)⠀Cat, 9
(=^ ◡ ^=)⠀Cat, 10
(=^-ω-^=)⠀Cat, 11
ヾ(=`ω´=)ノ”⠀Cat, 12
(＾• ω •＾)⠀Cat, 13
(/ =ω=)/⠀Cat, 14
ฅ(•ㅅ•❀)ฅ⠀Cat, 15
ฅ(• ɪ •)ฅ⠀Cat, 16
ଲ(ⓛ ω ⓛ)ଲ⠀Cat, 17
(^=◕ᴥ◕=^)⠀Cat, 18
( =ω= )⠀Cat, 19
ଲ(ⓛ ω ⓛ)ଲ⠀Cat, 20
(^=◕ᴥ◕=^)⠀Cat, 21
( =ω= )⠀Cat, 22
(^˵◕ω◕˵^)⠀Cat, 23
(^◔ᴥ◔^)⠀Cat, 24
(^◕ᴥ◕^)⠀Cat, 25

( ´(ｴ)ˋ )⠀Bear, 1
(*￣(ｴ)￣*)⠀Bear, 2
ヽ(￣(ｴ)￣)ﾉ⠀Bear, 3
(／￣(ｴ)￣)／⠀Bear, 4
(￣(ｴ)￣)⠀Bear, 5
ヽ( ˋ(ｴ)´ )ﾉ⠀Bear, 6
⊂(￣(ｴ)￣)⊃⠀Bear, 7
(／(ｴ)＼)⠀Bear, 8
⊂(´(ェ)ˋ)⊃⠀Bear, 9
(/-(ｴ)-＼)⠀Bear, 10
(/°(ｴ)°)/⠀Bear, 11
ʕ ᵔᴥᵔ ʔ⠀Bear, 12
ʕ •ᴥ• ʔ⠀Bear, 13
ʕ •̀ ω •́ ʔ⠀Bear, 14
ʕ •̀ o •́ ʔ⠀Bear, 15

∪＾ェ＾∪⠀Dog, 1
∪･ω･∪⠀Dog, 2
∪￣-￣∪⠀Dog, 3
∪･ｪ･∪⠀Dog, 4
Ｕ^皿^Ｕ⠀Dog, 5
ＵＴｪＴＵ⠀Dog, 6
U^ｪ^U⠀Dog, 7
V●ᴥ●V⠀Dog, 8

／(≧ x ≦)＼⠀Rabbit, 1
／(･ × ･)＼⠀Rabbit, 2
／(=´x`=)＼⠀Rabbit, 3
／(^ x ^)＼⠀Rabbit, 4
／(=･ x ･=)＼⠀Rabbit, 5
／(^ × ^)＼⠀Rabbit, 6
／(＞×＜)＼⠀Rabbit, 7
／(˃ᆺ˂)＼⠀Rabbit, 8

( ´(00)ˋ )⠀Pig, 1
(￣(ω)￣)⠀Pig, 2
ヽ( ˋ(00)´ )ノ⠀Pig, 3
( ´(oo)ˋ )⠀Pig, 4
＼(￣(oo)￣)／⠀Pig, 5
｡ﾟ(ﾟ´(00)`ﾟ)ﾟ｡⠀Pig, 6
(￣(00)￣)⠀Pig, 7
(ˆ(oo)ˆ)⠀Pig, 8

(￣Θ￣)⠀Bird, 1
(`･Θ･´)⠀Bird, 2
( ˋ Θ ´ )⠀Bird, 3
(◉Θ◉)⠀Bird, 4
＼( ˋ Θ ´ )／⠀Bird, 5
(･θ･)⠀Bird, 6
(・Θ・)⠀Bird, 7
ヾ(￣◇￣)ノ〃⠀Bird, 8

(°)1))<<⠀Fish, 1
<・ )))><<⠀Fish, 2
ζ°)))彡⠀Fish, 3
>°))))彡⠀Fish, 4
(°))<<⠀Fish, 5
>^)))<～～⠀Fish, 6
≧( ° ° )≦⠀Fish, 7

/╲/\╭(ఠఠ益ఠఠ)╮/\╱\⠀Spider, 1
/╲/\╭(ರರ⌓ರರ)╮/\╱\⠀Spider, 2
/╲/\╭༼ ººل͟ºº ༽╮/\╱\⠀Spider, 3
/╲/\╭( ͡°͡° ͜ʖ ͡°͡°)╮/\╱\⠀Spider, 4
/╲/\╭[ ᴼᴼ ౪ ᴼᴼ]╮/\╱\⠀Spider, 5
/╲/\( •̀ ω •́ )/\╱\⠀Spider, 6
/╲/\╭[☉﹏☉]╮/\╱\⠀Spider, 7

ヾ(・ω・)メ(・ω・)ノ⠀Friends, 1
ヽ(∀° )人( °∀)ノ⠀Friends, 2
ヽ( ⌒o⌒)人(⌒-⌒ )ﾉ⠀Friends, 3
(*^ω^)八(⌒▽⌒)八(-‿‿- )ヽ⠀Friends, 4
＼(＾∀＾)メ(＾∀＾)ノ⠀Friends, 5
ヾ(￣ー￣(≧ω≦*)ゝ⠀Friends, 6
ヽ( ⌒ω⌒)人(=^‥^= )ﾉ⠀Friends, 7
ヽ(≧◡≦)八(o^ ^o)ノ⠀Friends, 8
(*・∀・)爻(・∀・*)⠀Friends, 9
｡*:☆(・ω・人・ω・)｡:゜☆｡⠀Friends, 10
o(^^o)(o^^o)(o^^o)(o^^)o⠀Friends, 11
(((￣(￣(￣▽￣)￣)￣)))⠀Friends, 12
(°(°ω(°ω°(☆ω☆)°ω°)ω°)°)⠀Friends, 13
ヾ(・ω・`)ノヾ(´・ω・)ノ゛⠀Friends, 14
Ψ( `∀)(∀´ )Ψ⠀Friends, 15
(っ˘▽˘)(˘▽˘)˘▽˘ς)⠀Friends, 16
(((*°▽°*)八(*°▽°*)))⠀Friends, 17
☆ヾ(*´・∀・)ﾉヾ(・∀・`*)ﾉ☆⠀Friends, 18
(*＾ω＾)人(＾ω＾*)⠀Friends, 19
٩(๑･ิᴗ･ิ)۶٩(･ิᴗ･ิ๑)۶⠀Friends, 20
(☞°ヮ°)☞ ☜(°ヮ°☜)⠀Friends, 21
＼(▽￣ \ (￣▽￣) / ￣▽)／⠀Friends, 22

ヽ( ･∀･)ﾉ_θ彡☆Σ(ノ `Д´)ノ⠀Ennemies, 1
(*´∇`)┌θ☆(ﾉ>_<)ﾉ⠀Ennemies, 2
( ￣ω￣)ノﾞ⌒☆ﾐ(o _ _)o⠀Ennemies, 3
(*`0´)θ☆(メ°皿°)ﾉ⠀Ennemies, 4
(o¬‿¬o )...☆ﾐ(*x_x)⠀Ennemies, 5
(╬￣皿￣)=○＃(￣6)３￣)⠀Ennemies, 6
(; -_-)――――――C<―_-)⠀Ennemies, 7
＜( ￣︿￣)︵θ︵θ︵☆(＞口＜－)⠀Ennemies, 8
(￣ε(9￣)☆╰╮o(￣▽￣///)⠀Ennemies, 9
ヽ(>_<ヽ) ―⊂|=0ヘ(^‿^ )⠀Ennemies, 10
ヘ(>_<ヘ) ￢o(￣‿￣ﾒ)⠀Ennemies, 11
,,((( ￣□)_／ ＼_(○￣ ))),,⠀Ennemies, 12
(҂` ﾛ ´)︻デ═一 ＼(º □ º l|l)/⠀Ennemies, 13
(╯°Д°)╯︵ /(.□ . ＼)⠀Ennemies, 14
(¬_¬'')ԅ(￣ε￣ԅ)⠀Ennemies, 15
/( .□.)＼ ︵╰(°益°)╯︵ /(.□. /)⠀Ennemies, 16
(ﾉ-.-)ﾉ….((((((((((((●~* ( >_<)⠀Ennemies, 17
!!(ﾒ￣ ￣)_θ☆°0°)/⠀Ennemies, 18
(`⌒*)O-(`⌒´Q)⠀Ennemies, 19
(((ง’ω’)و三 ง’ω’)ڡ≡　☆⌒ﾐ((x_x)⠀Ennemies, 20
(งಠ_ಠ)ง　σ( •̀ ω •́ σ)⠀Ennemies, 21
(っ•﹏•)っ ✴==≡눈٩(`皿´҂)ง⠀Ennemies, 22

(/-_・)/D・・・・・------ →⠀Weapons, 1
(^ω^)ノﾞ(((((((((●～*⠀Weapons, 2
( -ω-)／占~~~~~⠀Weapons, 3
(/・・)ノ　　 (( く ((へ⠀Weapons, 4
―⊂|=0ヘ(^^ )⠀Weapons, 5
○∞∞∞∞ヽ(^ー^ )⠀Weapons, 6
(; ・_・)――――C⠀Weapons, 7
(ಠ o ಠ)¤=[]:::::>⠀Weapons, 8
(*＾＾)/~~~~~~~~~~◎⠀Weapons, 9
￢o(￣-￣ﾒ)⠀Weapons, 10
―(T_T)→⠀Weapons, 11
((( ￣□)_／⠀Weapons, 12
(ﾒ` ﾛ ´)︻デ═一⠀Weapons, 13
( ´-ω･)︻┻┳══━一⠀Weapons, 14
(ﾒ￣▽￣)︻┳═一⠀Weapons, 15
✴==≡눈٩(`皿´҂)ง⠀Weapons, 16
Q(`⌒´Q)⠀Weapons, 17

(ノ ˘_˘)ノ　ζ|||ζ　ζ|||ζ　ζ|||ζ⠀Magic, 1
(ﾉ≧∀≦)ﾉ ‥…━━━★⠀Magic, 2
(ﾉ>ω<)ﾉ :｡･:*:･ﾟ’★,｡･:*:･ﾟ’☆⠀Magic, 3
(ノ°∀°)ノ⌒･*:.｡. .｡.:*･゜ﾟ･*☆⠀Magic, 4
╰( ͡° ͜ʖ ͡° )つ──☆*:・ﾟ⠀Magic, 5
(＃￣□￣)o━∈・・━━━━☆⠀Magic, 6
(⊃｡•́‿•̀｡)⊃━✿✿✿✿✿✿⠀Magic, 7
(∩ᄑ_ᄑ)⊃━☆ﾟ*･｡*･:≡( ε:)⠀Magic, 8
(/￣ー￣)/~~☆’.･.･:★’.･.･:☆⠀Magic, 9
(∩` ﾛ ´)⊃━炎炎炎炎炎⠀Magic, 10

(っ˘ڡ˘ς)⠀Food, 1
( o˘◡˘o) ┌iii┐⠀Food, 2
(　’ω’)旦~~⠀Food, 3
( ˘▽˘)っ♨⠀Food, 4
♨o(>_<)o♨⠀Food, 5
( ・ω・)o-{{[〃]}}⠀Food, 6
(　・ω・)⊃-[二二]⠀Food, 7
( ・・)つ―{}@{}@{}-⠀Food, 8
( ・・)つ-●●●⠀Food, 9
(*´ー`)旦 旦(￣ω￣*)⠀Food, 10
(*´з`)口ﾟ｡ﾟ口(・∀・ )⠀Food, 11
( o^ ^o)且 且(´ω`*)⠀Food, 12
( ￣▽￣)[] [](≧▽≦ )⠀Food, 13
( *^^)o∀*∀o(^^* )⠀Food, 14
( ^^)_旦~~　 ~~U_(^^ )⠀Food, 15
(*￣▽￣)旦 且(´∀`*)⠀Food, 16
-●●●-ｃ(・・ )⠀Food, 17
( ・・)つ―●○◎-⠀Food, 18

ヾ(´〇`)ﾉ♪♪♪⠀Music, 1
ヘ(￣ω￣ヘ)⠀Music, 2
(〜￣▽￣)〜⠀Music, 3
〜(￣▽￣〜)⠀Music, 4
ヽ(o´∀`)ﾉ♪♬⠀Music, 5
(ﾉ≧∀≦)ﾉ⠀Music, 6
♪ヽ(^^ヽ)♪⠀Music, 7
♪(/_ _ )/♪⠀Music, 8
♪♬((d⌒ω⌒b))♬♪⠀Music, 9
└(￣-￣└))⠀Music, 10
((┘￣ω￣)┘⠀Music, 11
√(￣‥￣√)⠀Music, 12
└(＾＾)┐⠀Music, 13
┌(＾＾)┘⠀Music, 14
＼(￣▽￣)＼⠀Music, 15
／(￣▽￣)／⠀Music, 16
(￣▽￣)/♫•*¨*•.¸¸♪⠀Music, 17
(^_^♪)⠀Music, 18
(~˘▽˘)~⠀Music, 19
~(˘▽˘~)⠀Music, 20
ヾ(⌐■_■)ノ♪⠀Music, 21
(〜￣△￣)〜⠀Music, 22
(~‾▽‾)~⠀Music, 23
~(˘▽˘)~⠀Music, 24
乁( • ω •乁)⠀Music, 25
(｢• ω •)｢⠀Music, 26
⁽⁽◝( • ω • )◜⁾⁾⠀Music, 27
✺◟( • ω • )◞✺⠀Music, 28
♬♫♪◖(● o ●)◗♪♫♬⠀Music, 29
( ˘ ɜ˘) ♬♪♫⠀Music, 30
♪♪♪ ヽ(ˇ∀ˇ )ゞ⠀Music, 31

( ^^)p_____|_o____q(^^ )⠀Games, 1
(／o^)/ °⊥ ＼(^o＼)⠀Games, 2
!(;ﾟoﾟ)o/￣￣￣￣￣￣￣~ >ﾟ))))彡⠀Games, 3
ヽ(^o^)ρ┳┻┳°σ(^o^)ノ⠀Games, 4
(／_^)／　　●　＼(^_＼)⠀Games, 5
"( (≡|≡))_／ ＼_((≡|≡) )"⠀Games, 6
( ノ-_-)ノﾞ_□ VS □_ヾ(^-^ヽ)⠀Games, 7
ヽ(；^ ^)ノﾞ ．．．...___〇⠀Games, 8
(=O*_*)=O Q(*_*Q)⠀Games, 9
Ю　○三　＼(￣^￣＼)⠀Games, 10

( ͡° ͜ʖ ͡°)⠀Faces, 1
( ͡° ʖ̯ ͡°)⠀Faces, 2
( ͠° ͟ʖ ͡°)⠀Faces, 3
( ͡ᵔ ͜ʖ ͡ᵔ)⠀Faces, 4
( . •́ _ʖ •̀ .)⠀Faces, 5
( ఠ ͟ʖ ఠ)⠀Faces, 6
( ͡ಠ ʖ̯ ͡ಠ)⠀Faces, 7
( ಠ ʖ̯ ಠ)⠀Faces, 8
( ಠ ͜ʖ ಠ)⠀Faces, 9
( ಥ ʖ̯ ಥ)⠀Faces, 10
( ͡• ͜ʖ ͡• )⠀Faces, 11
( ･ิ ͜ʖ ･ิ)⠀Faces, 12
( ͡  ͜ʖ ͡  )⠀Faces, 13
(≖ ͜ʖ≖)⠀Faces, 14
(ʘ ʖ̯ ʘ)⠀Faces, 15
(ʘ ͟ʖ ʘ)⠀Faces, 16
(ʘ ͜ʖ ʘ)⠀Faces, 17

٩(ˊ〇ˋ*)و⠀Special, 1
(￣^￣)ゞ⠀Special, 2
(－‸ლ)⠀Special, 3
(╯°益°)╯彡┻━┻⠀Special, 4
(╮°-°)╮┳━━┳ ( ╯°□°)╯ ┻━━┻⠀Special, 5
┬─┬ノ( º _ ºノ)⠀Special, 6
(oT-T)尸⠀Special, 7
( ͡° ͜ʖ ͡°)⠀Special, 8
[̲̅$̲̅(̲̅ ͡° ͜ʖ ͡°̲̅)̲̅$̲̅]⠀Special, 9
(ಠ_ಠ)⠀Special, 10
౦０o ｡ (‾́。‾́ )y~~⠀Special, 11
(￣﹃￣)⠀Special, 12
(x(x_(x_x(O_o)x_x)_x)x)⠀Special, 13
(　･ω･)☞⠀Special, 14
(⌐■_■)⠀Special, 15
(◕‿◕✿)⠀Special, 16
(　￣.)o-　　【　TV　】⠀Special, 17
｀、ヽ｀ヽ｀、ヽ(ノ＞＜)ノ ｀、ヽ｀☂ヽ｀、ヽ⠀Special, 18
‿︵‿︵‿︵‿ヽ(°□° )ノ︵‿︵‿︵‿︵⠀Special, 19
( • )( • )ԅ(≖‿≖ԅ)⠀Special, 20
( ＾▽＾)っ✂╰⋃╯⠀Special, 21
〜〜(／￣▽)／　〜ф⠀Special, 22
ଘ(੭ˊᵕˋ)੭* ੈ✩‧₊˚⠀Special, 23
ଘ(੭ˊ꒳​ˋ)੭✧⠀Special, 24
_(:3 」∠)_⠀Special, 25
∠( ᐛ 」∠)＿⠀Special, 26
"""

rofi = Popen(
    args=[
        'rofi',
        '-dmenu',
        '-i',
        '-p',
        ' Kaomoji : ',
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
