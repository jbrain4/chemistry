import json


class Chemistry():
    class PeriodicTable():
        def __init__(self):
            global table
            global colors
            global categories
            table = json.load(open('Elements.json'))['elements']
            colors = json.load(open('color-schemes.json'))

            # Store a list of attributes avalible for the elements
            attributes = []
            for key in table[0]:
                attributes.append(key)

            # Store the different categories
            categories = []
            for category in colors['default']:
                categories.append(category)

        # Identify unknown traits of an element by other known traits
        def getElementAttribute(self, attribute=None, queryAttribute=None,
                                value=None):

            def checkForElement(queryTable):
                return str(queryTable[queryAttribute]) == str(value)

            try:
                matchingElement = list(filter(checkForElement, table))
                return matchingElement[0][attribute]
            except IndexError:
                return 'No element was found with the {} attribute paired \
with the value {}'.format(queryAttribute, value)
            except KeyError:
                return 'The element attribute "%s" does not \
exist' % queryAttribute

        # Print out the periodic table of elements to the terminal
        def printTable(self, theme='default'):
            global table
            global colors
            try:
                colorScheme = colors[theme]
                row = self.getElementAttribute('ypos', 'name', 'Hydrogen')
                dist = 1
                print(' ')
                for element in table:
                    y = element['ypos']
                    x = element['xpos']
                    sym = element['symbol']
                    cat = element['category']
                    if len(sym) == 1:
                        spacing = 1
                    else:
                        spacing = 0
                    if y > row:
                        print('\n')
                        row = y
                    print('   ' * (x - (dist + 1)), end='')
                    for category in categories:
                        if category in cat:
                            print('\x1b[' + colorScheme[category] + sym + ' '
                                  * spacing + '\x1b[' + colorScheme['reset'],
                                  end=' ')
                            break
                    dist = x
                print('\n')
            except KeyError:
                print('The theme %s does not exist.' % theme)

        # Displays the queried element's location on the periodic table
        def elementLocation(self, queryAttribute=None, value=None,
                            theme='default'):
            global table
            global colors
            queriedElement = self.getElementAttribute('name', queryAttribute,
                                                      value)

            try:
                colorScheme = colors[theme]
                row = self.getElementAttribute('ypos', 'name', 'Hydrogen')
                dist = 1
                isElementFound = False
                print(' ')
                for element in table:
                    y = element['ypos']
                    x = element['xpos']
                    sym = element['symbol']
                    cat = element['category']
                    if queriedElement == element['name']:
                        isElementFound = True
                    else:
                        isElementFound = False
                    if len(sym) == 1:
                        spacing = 1
                    else:
                        spacing = 0
                    if y > row:
                        print('\n')
                        row = y
                    print('   ' * (x - (dist + 1)), end='')
                    for category in categories:
                        if category in cat and not isElementFound:
                            print('\x1b[' + colorScheme['unknown'] + sym + ' '
                                  * spacing + '\x1b[' + colorScheme['reset'],
                                  end=' ')
                            break
                        elif category in cat and isElementFound:
                            print('\x1b[' + colorScheme[category] + sym + ' '
                                  * spacing + '\x1b[' + colorScheme['reset'],
                                  end=' ')
                            break
                    dist = x
                print('\n')
            except KeyError:
                print('The theme %s does not exist.' % theme)
