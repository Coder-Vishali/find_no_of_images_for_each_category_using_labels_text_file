'''
This code is used to check the class imbalance in the dataset
'''

import os

# Encoded label details: (Consider total 4 categories)
# cat = 0
# dog = 1
# cow = 2
# bird = 3

def main():
    # Initialize the counters
    count_cat = 0
    count_dog = 0
    count_cow = 0
    count_bird = 0
    
    # To iterate all the files inside a labels folder
    folder = os.path.join(os.getcwd(), r'data/labels')
    for count, filename in enumerate(os.listdir(folder)):
        # Read each label text file
        file1 = open(os.path.join(folder, filename), 'r')
        print(f"\nReading {filename}")
        Lines = file1.readlines()
        for line in Lines:
            # Get the encoded value from the text file
            encoded_value = line.strip().split(' ', 1)[0]
            print("Encoded value: ", encoded_value)
            encoded_value = int(encoded_value)
            
            # Increment the counter crossponding to each category according to the encoded value
            if encoded_value == 0:
                print("Incrementing counter for cat")
                count_cat += 1
            elif encoded_value == 1:
                print("Incrementing counter for dog")
                count_dog += 1
            elif encoded_value == 2:
                print("Incrementing counter for cow")
                count_cow += 1
            else:
                print("Incrementing counter for bird")
                count_bird += 1
                
    print("\nResults: ")
    print("Total cat: ", count_cat)
    print("Total dog: ", count_dog)
    print("Total cow: ", count_cow)
    print("Total bird: ", count_bird)
    
# Driver Code
if __name__ == '__main__':
    # Calling main() function
    main()
