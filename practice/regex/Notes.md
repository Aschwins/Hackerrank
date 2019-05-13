# Regex
https://docs.python.org/3/library/re.html

## Meta Characters:

```
. ^ $ * ? { } [ ] \ | ( )
```

### `[ ]`

Used to specify a set of characters. With `-` also a range of characters can be
defined. `[a-zA-z]` is all the lower and upper characters, `[abc]` is just `a`, `b` 
and `c`.

All meta-characters are stripped of there special usage inside brackets. 

#### `^`
The complement of a set. `[^a-z]` equals all characters except the lower characters.

### `\`
Backslash is used to use a special metacharacter without its specialness.
So `\\` or `\$`.

Backslashes can also indicate a special predefined set of characters:

-   `\w` all alphanumeric characters.

