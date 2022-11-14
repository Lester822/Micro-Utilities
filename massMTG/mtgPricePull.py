import scrypy

INPUT_NAME = 'cards.txt'
OUTPUT_NAME = 'prices.csv'

def extractData(filename):
    '''Get list of line by line from file'''
    input_file = open(filename, 'r')
    clean_lines = []
    for line in input_file:
        clean_lines.append(line.strip())
    input_file.close()
    return clean_lines

def outCSV(priceDict):
    '''Export best prices to output file'''
    output_file = open(OUTPUT_NAME, 'w')
    output_file.write('name,set,price,foil_price\n')
    for card, info in priceDict.items():
        output_file.write(f'{card},{info[1]},{info[0]},{info[2]}\n')
    output_file.close()

def main():
    cardList = extractData(INPUT_NAME)  # Gets list of cards
    prices = {}
    for item in cardList:  # Goes through each line of input file
        versions = scrypy.card_versions(item)  # Gets a scryfall query of each version of given card name
        better_price = [10000000, 'aaa']  # Sets arbitrary best price value
        for card in versions.cards():  # Goes through each card in scryfall querey
            if card.price() is not None:  # Checks if it has price
                if card.price() < better_price[0]:  # Sees if price is better than current best price
                    better_price = [card.price(), card.set(), card.price_foil()]  # If it is, override better_price with list that goes [price, set]
        prices[card.name()] = better_price  # Adds to dictonary
    outCSV(prices)  # Sends for output

main()