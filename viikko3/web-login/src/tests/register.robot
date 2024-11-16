*** Settings ***
Resource  resource.robot
Suite Setup     Open And Configure Browser
Suite Teardown  Close Browser
Test Setup      Reset Application Create User And Go To Register Page

*** Test Cases ***
Register With Valid Username And Password
    Set Username  ville
    Set Password  ville123
    Set PasswordConfirmation  ville123
    Submit Credentials
    Register Should Succeed

Register With Too Short Username And Valid Password
    Set Username  vi
    Set Password  ville123
    Set PasswordConfirmation  ville123
    Submit Credentials
    Register Should Fail With Message  Too short username

Register With Valid Username And Too Short Password
    Set Username  ville
    Set Password  ville12
    Set PasswordConfirmation  ville12
    Submit Credentials
    Register Should Fail With Message  Too short password

Register With Valid Username And Invalid Password
    Set Username  ville
    Set Password  villensalasana
    Set PasswordConfirmation  villensalasana
    Submit Credentials
    Register Should Fail With Message  Password contains only letters

Register With Nonmatching Password And Password Confirmation
    Set Username  ville
    Set Password  ville123
    Set PasswordConfirmation  ville456
    Submit Credentials
    Register Should Fail With Message  Password and confirmation don't match

Register With Username That Is Already In Use
    Set Username  kalle
    Set Password  kalle123
    Set PasswordConfirmation  kalle123
    Submit Credentials
    Register Should Fail With Message  Username already taken

Login After Successful Registration
    Set Username  ville
    Set Password  ville123
    Set PasswordConfirmation  ville123
    Submit Credentials
    Register Should Succeed

    Logout

    Set Username  ville
    Set Password  ville123
    Click Button  Login
    Main Page Should Be Open


Login After Failed Registration
    Set Username  vi
    Set Password  ville123
    Set PasswordConfirmation  ville123
    Submit Credentials
    Register Should Fail With Message  Too short username

    Logout

    Set Username  ville
    Set Password  ville123
    Click Button  Login
    Login Page Should Be Open


*** Keywords ***
Register Should Succeed
    Welcome Page Should Be Open

Register Should Fail With Message
    [Arguments]  ${message}
    Register Page Should Be Open
    Page Should Contain  ${message}

Submit Credentials
    Click Button  Register

Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set Password
    [Arguments]  ${password}
    Input Password  password  ${password}

Set PasswordConfirmation
    [Arguments]  ${password}
    Input Password  password_confirmation  ${password}

Reset Application Create User And Go To Register Page
    Reset Application
    Create User  kalle  kalle123
    Go To Register Page