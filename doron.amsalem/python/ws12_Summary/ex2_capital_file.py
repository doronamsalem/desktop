# review by vica
def make_capital_file(path):
    """gets path of file\nchange all file`s content to capital"""
    while path != "exit":
        try:
            with open(path, "r") as file1:
                content = file1.read().upper()

            with open(path, "w") as file1:
                file1.write(content)
            break
        except:
            path = input("""file does not exist, try again or "exit" """)



if __name__ == '__main__':
    make_capital_file(5)