import requests

def fileRead():
    filePath = input("Please type in the path to the file you would like to use: ")
    subdomainArray = []
    with open(filePath) as domainFile:
        for line in domainFile:
            line = line.strip()
            subdomainArray.append(line)
    return(subdomainArray)
def makeRequests(subdomainList):
    validSubdomains = []
    checkedFile = open('checkedSubdomains.txt','w+')
    for x in subdomainList:
        http = "http://"+x
        https = "https://"+x
        try:
            domainCheck = requests.get(http, timeout=1.5)
            print(x,domainCheck.status_code)
            validSubdomains.append(http)
        except requests.ConnectionError as exception:
            print("Valid URL not found for:",x)
    for x in validSubdomains:
        checkedFile.write(x)
        checkedFile.write('\n')
    checkedFile.close()
    print("Results written to file!")



makeRequests(fileRead())
