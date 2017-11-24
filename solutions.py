def python1():
    letters = 'abcdefg'
    {letters[i]: letters[(i + 1)::] for i in range(len(letters) - 1)} 



def python3():
    class fooClass: pass
    def fooFunc(): pass

    print 'Function attributes no in class attributes', endl, set(dir(fooFunc())) - set(dir(fooClass()))

    class fooClass(object): pass
    print endl, 'When deriving from object things are not quite the same:' 
    print set(dir(fooClass())) - set(dir(fooFunc()))



def pythonCapstone():
    import random as ran

    # Create a random text
    # 1. Define your alphabet first
    characters = [chr(_) for _ in range(40, 124)]

    # 2. Create a list of words at most 8 characters long
    words = [''.join([ran.choice(characters) for l in range(ran.randint(1, 8))]) for _ in range(100)]

    # 3. Break the word list into lines of 10 words each
    lines = [words[i: i + 10] for i in range(0, len(words), 10)]

    for line in lines: print line
    


def numpy1():
    arr = np.random.randn(10, 5)
    xSlice = np.random.choice(10, 4)
    ySlice = np.random.choice(5, 3)

    print arr[xSlice, :][:, ySlice]



def pandas1():
    # Saturday sales by store
    storeSales[storeSales['DAY'].dt.dayofweek == 5].groupby('STORE').mean()

    # What if I just want the total sales on Ssturdays?
    storeSales.loc[storeSales['DAY'].dt.dayofweek == 6, 'SALES'].mean() 

