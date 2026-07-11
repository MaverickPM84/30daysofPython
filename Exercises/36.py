'''
Exercise 36 - Word Counter

Question: Please download the words1.txt file from the attachment and then create a Python function that takes a text file as input and returns the number of words contained in the text file.

Example -- how to read a file as a string using read() method
In this example, the file at the specified path ('example.txt') is opened, and its entire content is read into a string using the read() method. The with statement ensures proper handling of the file, automatically closing it after reading.


file_path = 'example.txt'

with open(file_path, 'r') as file:
    file_content = file.read()

print(file_content)
Output:

Hii,
I am a GeeksforGeeks student.
I am a web developer and DSA enthusiast
'''

def word_counter(file_path):
    '''
    function that takes a file path as input, 
    reads the file, splits the content, 
    and counts the items of the split output.
    
    '''

    with open(file_path, "r") as file:
        # read file as a string using read() method
        file_content = file.read()
        print(file_content)
        file_list = file_content.split()
        return(len(file_list))


file_path = "words1.txt"

num_of_words = word_counter(file_path)

print(num_of_words)

'''
The function here takes as input a file path. If the file path is in the same directory as your Python script, you can pass in the file name as in the above script. If your text file is somewhere else, then you need to pass the full path when calling the function. Example:

print(count_words("C:/Home/words1.txt"))

'''