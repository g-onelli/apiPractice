"""
Gabriela Onelli
Dr. Saremi
SSW 567
10/02/2021

Homework 4: Developing with Testers in Mind
I pledge my honor that I have abided by the Stevens Honor System. -Gabriela Onelli
"""
import json
import requests

def get_github_account():
    """Function gets account name from user"""
    github_name = input("Please type out the github account name: ")
    return github_name

def get_github_repos(account):
    """Function takes account name from get_github_account and gets the repos
associated with that account"""
    temp_dict = {}
    response = requests.get('https://api.github.com/users/'+ account +'/repos')
    data = response.json()
    key_number = 0
    for item in data:
        temp_dict[key_number] = item
        key_number+=1
    return temp_dict

def store_repos(github_data):
    """Takes repos stored by get_github_repos and pulls out the name of each
repo to be stored in a dictionary"""
    data = {}
    key_number = 0
    while key_number<len(github_data):
        value = github_data.get(key_number)
        data[key_number] = value['name']
        key_number +=1

    print(len(data))
    return data

def get_github_repo_data(data_dict,github_account):
    """takes the dictionary of repo names and account name, makes a call
for the commit data of each repo and stores that data in a dictionary"""
    key_number=0
    new_temp_dict = {}
    while key_number<len(data_dict):
        repo_name = data_dict[key_number]
        repo_data = requests.get('https://api.github.com/repos/'+github_account+'/'+repo_name+'/commits')
        new_temp_dict[key_number]=repo_data.json()
        key_number +=1
    return new_temp_dict

def count_commits(repo_data):
    """Takes the repo data and pulls out the number of commits per repo, then
stores this in a dictionary"""
    key_number = 0
    last_temp_dict = {}
    while key_number <len(repo_data):
        commits = len(repo_data[key_number])
        print("This is the commit number")
        print(commits)
        last_temp_dict[key_number] = commits
        key_number +=1
    return last_temp_dict

""""""

def combine_repo_and_commits(repo_dict,commit_dict):
    """Outputs a number of strings stating the name of the repo and it's
number of commits."""
    key_number = 0
    while key_number<len(repo_dict):
        print("Repository "+str(repo_dict[key_number])+" has"+str(commit_dict[key_number])+" commits")
        key_number +=1

def get_info():
    """Makes all the function calls and feeds the necessary inputs and outputs
into the other functions"""
    ans_one = get_github_account()
#    print("answer One")
    ans_two = get_github_repos(str(ans_one))
#    print(ansTwo)
    ans_three = store_repos(ans_two)
#    print("answer three")
    ans_four = get_github_repo_data(ans_three,ans_one)
#    print("answer four")
    ans_five = count_commits(ans_four)
#    print("answer five")
    combine_repo_and_commits(ans_three,ans_five)
