# ======== You can define the handshakes function here. Do not write any code other than your solution here! ================

n = int(input("Number of people at the party:"))
def handshakes(n):
    if (n < 2):
        return 0
    else:
        return (n-1) + handshakes(n-1)

print(handshakes(n), "handshakes are needed.")


# ====================================================================================================================================


"""if __name__ == '__main__':
	# Here you can write code to test your function. Code you write here is solely for testing and will not be evaluated.
    """



