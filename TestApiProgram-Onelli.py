"""
Gabriela Onelli
Dr. Saremi
SSW 567
10/02/2021

Homework 4: Developing with Testers in Mind
I pledge my honor that I have abided by the Stevens Honor System. -Gabriela Onelli
"""
import unittest

class TestAPIProgram(unittest.TestCase):
    def test_accessAccount(self):
        account = 'richkempinski'
        result = ApiProgram.getGithubRepo(account)
        self.assertEqual(type(result),'dict')
        self.assertNotEqual(len(result),0)

    def test_storeRepos(self):
        repos = {}
        result = ApiProgram.storeRepos(repos)
        self.assertNotEqual(len(result),0)

    def test_RepoData(self):
        account = 'richkempinski'
        repos = {}
        result = ApiProgram.getGithubRepoData(repos,account)
        self.assertNotEqual(len(result),0)
