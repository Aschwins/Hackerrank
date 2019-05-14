# Regex
https://docs.python.org/3/library/re.html

## Matching Characters

### Meta Characters:

```
. ^ $ * ? { } [ ] \ | ( )
```

### `[ ]` Brackets

Used to specify a set of characters. With `-` also a range of characters can be
defined. `[a-zA-z]` is all the lower and upper characters, `[abc]` is just `a`, `b` 
and `c`.

All meta-characters are stripped of there special usage inside brackets. 

#### `^` Hat
The complement of a set. `[^a-z]` equals all characters except the lower characters.

### `\` Backlash
Backslash is used to use a special metacharacter without its specialness.
So `\\` or `\$`.

Backslashes can also indicate a special predefined set of characters:

-   `\w`: all alphanumeric characters.
-   `\D`: any non-digit character.
-   `\s`: any whitespace character <=> `[\t\n\r\f\v]`
-   `\S`: any non whitespace character

etc. for more: https://docs.python.org/3/library/re.html#re-syntax

### `.` Dot

The dot is the wildcard. It matches anything except a newline (`\n`). If you also want to include newline use: `re.DOTALL`.

## Repeating things

Now that we know how to find, and ask for characters we don't want to type out something repeatedly if we want the same thing again and again.

### `*` Star
The `*` character is used after another character to specify that the previous character can be matched zero or more times.

### `+` Plus
The `+` character is used after another character to specify that the previous character can be matched one or more times.

### `?` Question mark
The `?` character is used after another charadter to specify that the previous character can be matched one or zero times. Think of it as marking something being optional.

### `{m, n}` Minimum `m` and maximum `n` repititions.
This character is used after another character to specify that the previous character can be matched a minimum of `m` and a maximum of `n` times.

## Compiling regular expressions

One can put a regular expression in a variable to later match more easily.

```
import re
p = re.compile('[a-z]+')

print(p.match(""))
>>> None

print(p.match("hello"))
>>> <_sre.SRE_Match object; span=(0, 5), match='hello'>
```

Use of raw string notation is highly recommended:

```
'\n' = newline
r'\n' = '\\n'
r'\\section' = '\\\\section'
```

## Performing Matches

`match()` See if it matches the beginning of a string. Returns a `match object` which can be quered with methods: `group()` (returns the string match by the RE), `start()` (returns the starting position), `end()` (returns the ending position), `span()` (returns a tuple with the span.)

`search()` Finds the first occurence of the RE in the string. 

`findall()` Finds all the occurences of the RE in the string.

`finditer()`

## Misc

`(?<=)` Look behind. Matches anything that comes next, but doesnt match anythin in this group.
`(?<=-).+` Matches anything that comes after a `-`.