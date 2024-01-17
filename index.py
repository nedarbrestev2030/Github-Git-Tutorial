import shapes

def main():
    # TODO: Use the shapes module to calculate some shape stuff
    r1_area = shapes.area_rectangle(2,3)
    print(f"The area of rectangle with sides 2 and 3 is : {r1_area}")
    
    r2_area = shapes.area_rectangle(4,9)
    print(f"The area of rectangle with sides 4 and 9 is : {r2_area}")
    
if __name__ == '__main__':
    main()