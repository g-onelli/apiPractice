"""
Gabriela Onelli
Dr. Saremi
SSW 567
10/02/2021

Homework 4: Developing with Testers in Mind
I pledge my honor that I have abided by the Stevens Honor System. -Gabriela Onelli
"""
import requests
import json

def getGithubAccount():
    githubName = input("Please type out the github account name: ")
    return githubName

def getGithubRepos(account):
    tempDict = {}
    response = requests.get('https://api.github.com/users/'+ account +'/repos')
    data = response.json()
    keyNumber = 0
    for item in data:
        tempDict[keyNumber] = item
        keyNumber+=1
    return tempDict

def storeRepos(githubData):
    data = {}
    keyNumber = 0
    while keyNumber<len(githubData):
        value = githubData.get(keyNumber)
        data[keyNumber] = value['name']
        keyNumber +=1
    return data

def getGithubRepoData(dataDict,githubAccount):
    keyNumber=0
    newTempDict = {}
    while keyNumber<len(dataDict):
        repoName = dataDict[keyNumber]
        repoData = requests.get('https://api.github.com/repos/'+githubAccount+'/'+repoName+'/commits')
        newTempDict[keyNumber]=repoData.json()
        keyNumber +=1
    return newTempDict

def countCommits(repoData):
    keyNumber = 0
    lastTempDict = {}
    while keyNumber <len(repoData):
        commits = len(repoData[keyNumber])
        print("This is the commit number")
        print(commits)
        lastTempDict[keyNumber] = commits
        keyNumber +=1
    return lastTempDict

def combineRepoAndCommits(repoDict,commitDict):
    keyNumber = 0
    finalDict = {}
    while keyNumber<len(repoDict):
        print("Repository "+repodDict[keyNumber]+" has "+commitDict[keyNumber]+" commits")
        
def getInfo():
    ansOne = getGithubAccount()
#    print("answer One")
    ansTwo = getGithubRepos(str(ansOne))
#    print(ansTwo)
    ansThree = storeRepos(ansTwo)
#    print("answer three")
    ansFour = getGithubRepoData(ansThree,ansOne)
#    print("answer four")
    ansFive = countCommits(ansFour)
#    print("answer five")
    combineRepoAndCommits(ansFour,ansFive)
    
    
        
