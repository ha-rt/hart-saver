from parser import returnLinks

saved_links = [

]

def refineFile(file):
    try:
        with open(f'{file}.txt', 'r') as file:
            lines = file.readlines()
            unique_lines = set(lines)
        with open(f'{file}.txt', 'w') as file:
            file.writelines(unique_lines)
    except FileNotFoundError:
        print(f"File '{file}.txt' not found.")

def continueMenu(links, site, file):
    saveLinks(links, file)
    print(f"The links for {site} have been saved to {file}.txt")
    cont = input("Would you like to continue parsing? (y/n)")

    if cont == "y":
        new_links = []
        for link in links:
            if link not in saved_links:
                saved_links.append(link)
                nlks = returnLinks(link)
                saveLinks(nlks, file)
                new_links.extend(nlks)
        continueMenu(new_links, site, file)

    if cont == "n":
        refineFile()

def saveLinks(list, file):
    for link in list:
        f = open(f"{file}.txt", "a")
        f.write(f"\n{link}")
        f.close()

def startMenu():
    site = input("Input the URL you would like to scrape: ")
    file = input("Please input what the output file should be called: ")

    saved_links.append(site)
    continueMenu(returnLinks(site), site, file)

if __name__ == "__main__":
    startMenu()