"""
Gabriela Onelli
Dr. Saremi
SSW 567
10/02/2021

Homework 4: Developing with Testers in Mind
I pledge my honor that I have abided by the Stevens Honor System. -Gabriela Onelli
"""
import unittest
import hw4_api_program_onelli

class TestAPIProgram(unittest.TestCase):
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

    def test_getInfo(self):
        account = 'richkempinski'
        result = hw4_api_program_onelli.get_info()
        

        
if __name__ == '__main__':
    unittest.main()
