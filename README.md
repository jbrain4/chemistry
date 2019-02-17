# Periodic Table
## Methods:
- `getElementAttribute` can be used to get an unknown attribute of an element based on a known attribute
  - `attribute` argument defines the attribute you would like to get (string)
  - `queryAttribute` is the name of the attribute that is known (string)
  - `value` is the value tied to the attribute that is known (string or int)
- `printTable` Prints the entire periodic table to the console
  - `theme` argument is used to define a color scheme to use (`color-schemes.json`) (string)
- `elementLocation` Highlights the location of an element
  - `queryAttribute` see `getElementAttribute` (string)
  - `value` see `getElementAttribute` (string or int)
