# May Pena
# This program processes a csv file that has been downloaded
# from the department of eduction of the U.S. government.
# Then it outputs the 10 cities that contain the largest number
# of colleges and universities.

place = {} # where cities and states will be stored as keys to their
           # respective number of colleges

def getWebData( URL ):
    '''gets the list of lines from the Web page at URL and split it into lines'''
    # import the library for accessing Web URLs
    from urllib.request import urlopen
    from urllib.error import URLError

    # attempt to get the Web page
    try:
        f = urlopen( URL )
        text = f.read().decode('utf-8')
    except URLError as e:
        # if error, print error message and
        # return empty list
        print( "ERROR!\n", e.reason )
        return [ ]
    
    # return the list of lines
    lines = text.split( "\n" )
    return lines

def breakdown( info ):
    '''gets the list of lines and adds college to the state key
       and outputs it in format'''
    #prepare 2 empty lists
    List  = [ ]
    List2 = [ ]
    
    # adds college to the state key
    for line in info:
        try:
            linex   = line.split(",")       
            if len( linex[5].strip() ) == 2: #if the line has a correct state
                colcity = linex[4], linex[5] 
                if colcity not in place:     #add college+city if not in library
                    place[colcity] = 1
                else:
                    place[colcity] += 1      #add 1 to college+city if in library             
        except IndexError:
            # avoid any empty / lines that can't be processed
            continue
    
    # makes a list of tuples with ( number of colleges, city and state )
    for item in place:
        tuplex = ( place[item], item )
        List.append( tuplex )

    # sort that list from highest to lowest in number of colleges
    List.sort()
    List.reverse()

    # append the first 10 to a second list
    for i in List[0:10]:
        List2.append( i )
        
    #print in format
    for tuplex in List2:
        print( "{0} {1}, {2}".format( tuplex[0], tuplex[1][0], tuplex[1][1]) )
        
def main():
    info = getWebData("http://cs.smith.edu/~dthiebaut/111/collegeScorecard.csv")
    print( "Number of Colleges, City")
    breakdown(info)

main()
