import glob

def add_image() -> None:
    dir = '../uplead_imag/*.jpg'
    count_file = 0
    index = []
    files = glob.glob(dir)
    for file in files:
        count_file+=1
        index.append(file)

    