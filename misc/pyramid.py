
def pyramid(height):
    
    space_no=height
    for star_no in range(1,2*height,2):
        print(' ' *space_no + "*" *star_no)
        space_no=space_no-1

height=int(input("enter the height of the pyramid \n"))
pyramid(height)