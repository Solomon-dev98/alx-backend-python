import argparse
import unittest
import sys
from pathlib import Path

def load_tests(loader, tests, pattern):
    suite = unittest.TestSuite()
    for test in tests:
        suite.addTests(loader.loadTestsFromTestCase(test))
    return suite

def run_specific_test(test_name):
    loader = unittest.TestLoader()
    start_dir = '0x03-Unittests_and_integration_tests'
    suite = loader.discover(start_dir, pattern='test_*.py')

    specific_tests = {
        "access_nested_map": "TestAccessNestedMap",
        "access_nested_map_exception": "TestAccessNestedMap",
        "mock_http_calls": "TestGetJson",
        "memoize": "TestMemoize",
        "github_org_client": "TestGithubOrgClient",
        "public_repos_url": "TestGithubOrgClient",
        "public_repos": "TestGithubOrgClient",
        "has_license": "TestGithubOrgClient",
        "integration": "TestIntegrationGithubOrgClient"
    }

    if test_name in specific_tests:
        tests = [cls for cls in unittest.defaultTestLoader.loadTestsFromName(f"{start_dir}.{specific_tests[test_name]}") if cls.__class__.__name__ == specific_tests[test_name]]
        unittest.TextTestRunner().run(load_tests(loader, tests, None))
    else:
        print("Invalid test name. Please check the available tests.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run specific unittests for the ALX Backend Python project.")
    parser.add_argument("test_name", help="The name of the test to run.")
    args = parser.parse_args()

    run_specific_test(args.test_name)
