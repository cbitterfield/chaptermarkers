# -*- coding: utf-8 -*-
#
# System test default suite
#

*** Settings ***
Documentation       *Arguments Suite for _Default Execution_*
Metadata    Github  https://github.com/toptive/python_boilerplate

# External libraries imports
Library  Process
Library  String

Resource    common_resources.robot

*** Variables ***
${EXPECTED_MESSAGE}    Hello World

*** Test Cases ***
Scenario: Python Boilerplate it is executed without errors
    [Documentation]     Verifies that python_boilerplate is executed well and without errors
    ${result}=  Run process     ${BOILERPLATE_EXEC}
    Should Contain  ${result.stdout}    ${EXPECTED_MESSAGE}
    Should Be Empty     ${result.stderr}
