# -*- coding: utf-8 -*-
#
# System test default suite
#

*** Settings ***
Documentation       *Test Chapter Markers runs but has error in filename*
Metadata    Github  https://github.com/cbitterfield/chaptermarkers
Metadata    Version 1.0.0
Metadata    Executed At    ${HOST}


# External libraries imports
Library  Process
Library  String

Resource    common_resources.robot

*** Variables ***
${EXPECTED_MESSAGE}  usage: chaptermarkers
${REPORT FILE}  report.html
${LOG FILE}     logfile.html
${LOG LEVEL}    DEBUG
${OUTPUT DIR}   /Users/colin/IdeaProjects/chaptermarkers



*** Test Cases ***
Scenerio test chaptermarkers run
    [Tags]    DEBUG
    [Documentation]     Verifies that chaptermarkers is executed well and without errors
    ${result}=  Run process     ${CHAPTERMARKERS_EXEC}
    Log     ${result.stderr}
    Log     ${result.stdout}
    Should Contain  ${result.stdout}    ${EXPECTED_MESSAGE}
    Should Be Empty     ${result.stderr}

