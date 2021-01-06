# -*- coding: utf-8 -*-
#
# System test default suite
#

*** Settings ***
Documentation       *Test Chapter Markers runs but has error in filename*
Metadata    Github  https://github.com/cbitterfield/chaptermarkers

# External libraries imports
Library  Process
Library  String

Resource    common_resources.robot

*** Variables ***
${EXPECTED_MESSAGE}  Movie Filename

*** Test Cases ***
Scenario: chaptermarkers is executed
    [Documentation]     Verifies that chaptermarkers is executed well and without errors
    ${result}=  Run process  ${CHAPTERMARKERS_EXEC}  shell=true
    Should Contain  ${result.stdout}    ${EXPECTED_MESSAGE}
    Should Be Empty     ${result.stderr}
