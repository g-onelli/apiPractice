"""
Gabriela Onelli
Dr. Saremi
SSW 567
10/02/2021

Homework 4: Developing with Testers in Mind
I pledge my honor that I have abided by the Stevens Honor System. -Gabriela Onelli
"""
import unittest
import nose
from nose.tools import assert_true
import requests
from unittest.mock import Mock, patch
import hw4_api_program_onelli

class TestAPIProgram(unittest.TestCase):
    def test_githubResponse(self):
        account = 'richkempinski'
        repo_name = 'hellogitworld'
        account_response = requests.get('https://api.github.com/users/'+ account +'/repos')
        repos_response = requests.get('https://api.github.com/repos/'+github_account+'/'+repo_name+'/commits')
        assert_true(account_response.ok)
        assert_true(repos_response.ok)
        
    def test_accessAccount(self):
        account = 'richkempinski'
        result = hw4_api_program_onelli.get_github_repos(account)
        self.assertEqual(type(result),'dict')
        self.assertNotEqual(len(result),0)

    def test_storeRepos(self):
        result = hw4_api_program_onelli.store_repos(repos)
        self.assertNotEqual(len(result),0)

    def test_RepoData(self):
        account = 'richkempinski'
        result = hw4_api_program_onelli.get_github_repo_data(repos,account)
        self.assertNotEqual(len(result),0)
        
    def test_githubRepoData(self):
        account = 'richkempinski'
        result = hw4_api_program_onelli.get_github_repos(account)
        answer = hw4_api_program_onelli.get_github_repos_data(result,account)
        self.assertEqual(type(answer),'dict')
        self.assertNotEqual(len(answer),0)

    def test_countCommits(self):
        account = 'richkempinski'
        account_info = hw4_api_program_onelli.get_github_repos(account)
        repo_data = hw4_api_program_onelli.get_github_repos_data(account_info,account)
        result = hw4_api_program_onelli.count_commits(repo_data)
        self.assertEqual(type(answer),'dict')
        self.assertNotEqual(len(answer),0)        


    def test_getInfo(self):
        account = 'richkempinski'
        result = hw4_api_program_onelli.get_info()
        

        
if __name__ == '__main__':
    unittest.main()
