# Write a Python function that takes a list and returns a new list with
# distinct elements from the first list.

# Following is given sample input (Sample List) and output (Unique List).
# The if the function is called with SampleList as argument then
# it should return the UniqueList as output

# Input was  [1,1,1,2,3,3,3,3,4,5,5]
# List with only unique values is  : [1, 2, 3, 4, 5]

def UniqueList(inputlist):
    serverlist = []
    for element in inputlist:
        if element not in serverlist:
            serverlist.append(element)
    return serverlist


samplelist = [1, 1, 1, 2, 3, 3, 3, 3, 4, 5, 5]
print(UniqueList(samplelist))
