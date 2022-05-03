from time import time

def initialiser():
    """initialises the config that saves the last medium chosen, and the list of media."""
    # check for config file
    # creating config file

    return "WIP"

def checkConfigExistence():
    return False

## media CRUD operations

def mediumAdder(input):
    """
    takes in the input from the command line and adds the item(s) into the media config file.
    e.g., books, TV => separated at the comma => inserted into the media config file.
    """
    # should be okay with one input
    # comma separating logic
    # file writing logic

    creater = open(input + ".txt", "w" )
    
    creater.close();

    return False

def mediaAdder(medium, other):
    """Loops of input asking."""
    pass

def mediaParser():
    """returns the media from within the config file, as well as the last used medium."""
    # checking if config exists.
    # parsing the last used medium.
    # parsing the media list from the config file.

    return ["podcasts", "books", "add media", "add items"]


def mediaUpdater(medium, newMedium):
    """ takes in the medium and changes its text name."""
    # checking if the config exists.
    # finding by old, updating with the new.
     
    return "WIP"


def mediaDeleter(medium):
    """ Deletes media from the config file"""
    # checking if config exists.
    # finding by old, deleting.

    return "WIP"


## item CRUD operations

def itemAdder(medium, isTest = False):
    """
    takes in the input from the command line and adds the item(s) into the text file of the medium at hand.
    e.g., Myths and Legends, The History of China => separated at the comma => inserted into the medium list.
    """
    # check for one or many input
    
    print("Add to: {}.".format(medium));
    print("E.g.: A, B, C");

    if not isTest:
        string = inputAsker();
    else:
        string = "Misha, Tal Kitty, Bing, Dino Saurus, Mad men, Jalapeno, Giraffe, Turkey"

    anList = stringPreprocessor(string, isTest);

    # file writing logic
    # TODO: unsolved case: existing medium, new items, not overwriting the before.

    filehandler = open(medium + ".txt", "w");

    for item in anList:
        filehandler.writelines(item);
        
    filehandler.close();

    return itemParser(medium);


def itemParser(medium): 
    """
    parses the items from the files from the folder.
    args:

    returns a cleansed list.
    """
    textObject = [];
    # TODO: we need to put them into the catalogues folder.

    fileHandler = open(medium + ".txt", "r");
    
    for line in fileHandler:
        textObject.append(
            line[0:-1] # this cuts the \n item.
            );

    fileHandler.close();
    
    #print('Output from readlines() method. \n', textObject);
    if not (textObject):
        textObject 
    
    return textObject

def inputAsker(options = "Change this later."):

    while(True):
        string = input(">> ");

        # option checking against logic.
        # if string in [options]:
            # break;
        if string:
            break;

        print("\nSorry, I did not get that (REPLACE THE PRESENCE CHECK WITH THE OPTIONS CHECK).");
    
    return string

def itemUpdater(medium, item, newItem, isTest = False):
    """
    Updates an item's name in the format:
    old_name=newName, ...
    """
    # check for one or many input
    print("\nUpdate: {}.".format(medium));
    print("E.g.: A1 = A2, ...");
    
    if not isTest:
        string = inputAsker();
    else:
        string = "Misha, Tal Kitty, Bing, Dino Saurus"
    # comma separating logic
    #.split("=")
    # find line by the old, overwrite it with the new one.
    # updating logic
    fileHandler = open(medium + ".txt", "w");
   
    fileHandler.close();
    
    return False


def itemDeleter(medium, isTest = False):
    """ Deletes items from the medium list."""
    # check for one or many input
    # comma separating logic
       
    print("\nDelete from: {}.".format(medium));
    print("E.g.: A, B, C");

    if not isTest:
        string = inputAsker();
    else:
        string = "Misha, Tal Kitty, Bing, Dino Saurus"

    anList = stringPreprocessor(string, isTest)

    # find line by anList
    #  
    # deleting logic
    fileHandler = open(medium + ".txt", "r+");

    lines = fileHandler.readlines(); # returns the lines
    
    if isTest:
        print("\n DELETION START")
        print("lines:", lines)
        print("anList:", anList)
    
    for i in range(0, len(lines)):
        print(i, lines[i]);
        print(lines[1]);
    
    for line in lines:
        print("before line:", line, line == "Tal Kitty");
        
        # TODO: figure out why this does not take in Tal Kitty
        for item in anList:
            #print("{}. {} == {} is {}".format(i, item, line, item == line))
            if item == line:
                #print("after item:", item);
                #print("removed line", line);
                lines.remove(item)

    # TODO: remove the undscore.
    print("lines:", lines);

    fileHandler.truncate(0);
    fileHandler.seek(0);
    fileHandler.writelines(lines);
    fileHandler.close();
    
    print("DELETION OVER")
        
    return "WIP"

## refactored functions
def stringPreprocessor(string, isTest):
    # comma separating & general pre-processing logic
    anList = string.split(","); # split returns a list.

    if (isTest):
        print("\nPRE-PROCESS Start !");
        startTime = time();
        print("Before: ", anList);
        
    for i in range(0, len(anList)):
        # adds a newline to the end, removes spaces from the beginning, and replaces space with underscore.
        anList[i] = ( 
            anList[i] + "\n"
            ).lstrip();
    
    if (isTest):
        print("After: ", anList);
        print("PRE-PROCESS OVER !");
        endTime = time();
        print("It took {} seconds.".format( str(endTime - startTime) ));

    return anList

## main and test suite.
if __name__ == "__main__":
    print("parsing is run as main. \n");

    test_medium = "TEST"
    itemAdder(test_medium, True);
    # itemParser
    # itemUpdater();
    itemDeleter(test_medium, True);

#else:
    #print(__name__);
