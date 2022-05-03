from parsing import itemAdder, itemParser, mediaAdder, mediaParser;
import random;
import os;

media_mediums = mediaParser();
wheel_mediums = {0: "take it", 1: "re-spin", 2: "exit", 3: "change medium", 4: "replenish"};
# TODO: we need an medium called 'other' in media_mediums and wheel_mediums.
# media mediums should also come from parsing.py.

def ask_media():
    """ should ask about the medium"""
    print("Please select the medium by either typing its rank or name.")
    
    # the medium medium creation
    for m in range(0, len(media_mediums)):        
        print("{}. {}.".format(m, media_mediums[m]));

    ask_medium = input(">> ").lower();
    
    # value error - when str.

    return (media_mediums[int(ask_medium)])

def randomiser(indices): 
    """ randomises the index chosen. """
    return random.randint(0, indices)

def replenish_wheel():
    print("\nYou can't spin on an empty wheel...")
    replenish = False;
    
    # the replenish medium creation
    for r in range(2, len(wheel_mediums)):        
        print("{}. {}.".format(r, wheel_mediums[r]));

    ask_replenish = input(">> ").lower();

    # breaking it
    if ( (ask_replenish == "replenish") or (int(ask_replenish) == 4) ):
        replenish = True;

    return replenish

def main():

    itemsList = [];
    cached_itemsList = []
    itemIndex = 0;
    emptyList = False
    replenishList = False
    medium = ask_media();

    if not (os.path.exists(medium + ".txt")):
        print("Creating", medium)
        mediaAdder(medium);

    #print("parsing...");
    itemsList = itemParser(medium); # Should return a list.
    
    # asks to add for an empty list.
    if not itemsList:
        print("\nThe medium seems to have nothing in it, care to add some items ?")
        itemsList = itemAdder(medium);

    #print("parsed.\n");
    cached_itemsList = itemsList.copy();

    # needs logic to ask to say 'no items, no spins !'
    while (itemsList):
        #print("randomising...");
        itemIndex = randomiser(len(itemsList) - 1); # Should return an int.
        #print("randomised.\n");

        #print("sending...");
        print("\nYour item is the... '{}' !".format(itemsList[itemIndex]));
        print("A one in {} chance !".format( len(itemsList) - 1 ));

        # the spin medium creation
        for s in range(0, 3):        
            print("{}. {}.".format(s, wheel_mediums[s]));
        
        ask_spin = (input(">> ")).lower();
        # ValueError: invalid literal for int() with base 10: ''
        # TODO: ensure this is also in a for loop that denies any option that is not displayed

        # breaking it
        if ((ask_spin in ["take it", "exit"]) or (int(ask_spin) in [0, 2])):
            break

        # changing the media
        if (ask_spin == "change medium" or int(ask_spin) == 3):
            ask_media();
        
        # removing for re-spin.
        print("Re-spinning without {}.".format(itemsList.pop(itemIndex)));

        # checking if empty, then asking for replenishing, and if so, doing so.
        if (len(itemsList) == 0):
            emptyList = True;

        if (emptyList): 
            replenishList = replenish_wheel();

        if (replenishList):    
            itemsList = cached_itemsList.copy();
            print("Replenished wheel.")
    
    print("\nBye bye !")

if __name__ == "__main__":
    #print("picking is run on main.");
    main();
#else:
    #print(__name__);