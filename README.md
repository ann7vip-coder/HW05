# Homework
- Name: Ting Lun Ho
## Question 1) Define the following unit, integration, regression tests and when you would use each?
- Unit test: A unit test checks one small, isolated piece of code to ensure it behaves as expected in all edge cases.
- Integration test: An integration test verifies that multiple modules or components work together correctly
- Regression test: A regression test reproduces a specific bug that was previously found and ensures it stays fixed in the future.
## Question 2) Briefly explain pytest discovery (file/function naming) and what a fixture is.
Pytest automatically finds tests in files named test_*.py or *_test.py. Inside those files, it runs any functions or methods whose names start with test_.
A fixture is a reusable setup or helper that provides pre-initialized resources to tests
