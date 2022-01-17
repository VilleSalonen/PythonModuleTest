*** Settings ***
Test Setup     Best Test Setup Ever
Resource       imports.resource

*** Test Cases ***
Some Test
    Some Browser Util
    Log To Console    success

*** Keywords ***
Best Test Setup Ever
    New Browser    chromium    headless=False
    New Context
    ${TIMEOUT} =    Set Browser Timeout    30 s
    Set Suite Variable    ${TIMEOUT}
    New Page    https://robotframework-browser.org/
