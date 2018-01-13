# Kaomoji Picker
### A Fork of [Rofimoji](https://github.com/fdw/rofimoji)

An utility to insert kaomoji from Rofi.

## Usage

1. Run `rofimoji.py`
2. Search for the kaomoji you want
3. - Hit enter to insert the emoji directly
   - Hit `Alt+c` to copy it to the clipboard
4. (* ^ ω ^)

## Installation

Download `rofimoji.py` and move it somewhere on your path, for example `/usr/local/bin`.

What else do you need:
- Python 2
- xdotool for typing the text
- xsel to copy the text to the clipboard

For Ubuntu zesty: `sudo aptitude install python3 fonts-emojione xsel xdotool`

## Installing

1. Clone the repository, eg `git clone https://github.com/Longhinus/rofimoji`
2. Go to the repository `cd rofimoji`
3. Install Python and `pip install -r requirements-dev.txt`

* (Optional) Create a bind (~/.config/i3/config) `bindsym $mod+Tab ./usr/local/bin/rofimoji.py`
* (Fellow French) Use 'setxkbmap fr' to have it working correctly

## Change Notes

* I added a delay (30ms) in the xdotool options
