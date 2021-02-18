# -*- coding: utf-8 -*-
#
# System test default suite
#

*** Settings ***
Documentation   Run the program and see if ffmpeg is installed

Resource    common_resources.robot


*** Variables ***
${OUTPUT DIR}   /tmp
${LOG FILE}  None
${REPORT FILE}   None

*** Test Cases ***
Run program
    ${result}=   Run process  ${CHAPTERMARKERS_EXEC}  ${test}
    Should Contain  ${result.stdout}    ${EXPECTED_MESSAGE}
