# -*- coding: utf-8 -*-
#
# Common resources for system test cases execution
#

*** Settings ***
Library  OperatingSystem
Library  Process
Library  String

*** Variables ***
${CHAPTERMARKERS_EXEC}  chaptermarkers
${LOG LEVEL}    DEBUG
${test}     --test
${EXPECTED_MESSAGE}  ffmpeg version
${OUTPUT DIR}   /tmp
${LOG FILE}  None
${REPORT FILE}   None

*** Keywords ***
# TODO


