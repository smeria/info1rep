# Please do not modify this part of the code!
def tokenize(text):
    return text.split()


# ======== You can define the search_text function here. Do not write any code other than your solution here! ================

def search_text(filename, query):
    occurrences = 0
    file = open(filename, 'r')
    text = file.read().lower()
    file.close()

    query = query.lower()
    for token in tokenize(text):
        if token == query:
            occurrences = occurrences + 1
        else:
            pass
    return occurrences




# ====================================================================================================================================


"""if __name__ == '__main__':
	# Here you can write code to test your function. Code you write here is solely for testing and will not be evaluated.
    """
query = 'lorem'
occurrences = search_text('lorem-ipsum.txt', query)

print(f'Found {occurrences} occurrences of {query} in text.')

