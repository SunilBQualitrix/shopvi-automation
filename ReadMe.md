# python-behave-appium
BDD test project writen in python using the appium-python-client and behave to implement behavior driven development.
Allure is added for reporting.

###  PreRequisites 


###### For FireTV
 -  Install Android Studio
 -  Set Environment varable for ANDROID_HOME 
 - FireTV and Execution enviorment (Server/Laptop)should be in same Network
 - Install Node and Appium
 https://nodejs.org/en/download/package-manager
 https://appium.io/docs/en/2.0/quickstart/install/
 - install UIAtumator2 Driver
 https://appium.io/docs/en/2.0/quickstart/uiauto2-driver/
 - Indentidfy ip of FireTV
 - execute `adb connect <firetv_ip_address>`

 
 ###### For Roku TV
-  Roku TV and Execution enviorment (Server/Laptop) should be in same Network

###### For IPAD
 
-  Install XCODE
- node and appium is required 
- Pair Ipad to To execution device (server) via XCODE
- iPad Should be conneced via USB
- run WebDriverAgent in Xcode and let the Test Automation Agent run in Connected iPad
 


 

# Install:

pip install -r requirements.txt



# Execute - for FireTV :

pytest -m <tagName> --plateform=fire_tv  --appFileName=apkfile_name
* Valid Plateform Names - fire_tv,roku_tv,apple_tv,ipad 
* file should place under src\builds*
* additional Params : 
**--qaserver ** : defailt q8 , server name to connect Admin 
**--consecutive_failure_abort**- default is True , False -to  disable execution abortion
**--consecutive_failure_count** -default is 5, if consecutive_failure_abort is true then execution abort after 5 consequitive failure
**--screenShotToggle** -- default is False - to add All Screen shot for passed Test cases too (before and after every action)

# Execute - for Roku TV :

pytest -m <tagName> --plateform=roku_tv --appFileName=zipfile_name
* Valid Plateform Names - fire_tv,roku_tv,apple_tv,ipad 
* file should place under src\builds*
* additional Params : 
**--qaserver ** : defailt q8 , server name to connect Admin 
**--consecutive_failure_abort**- default is True , False -to  disable execution abortion
**--consecutive_failure_count** -default is 5, if consecutive_failure_abort is true then execution abort after 5 consequitive failure
**--screenShotToggle** -- default is False - to add All Screen shot for passed Test cases too (before and after every action)

# Report:


allure generate

allure serve

allure open

# Docker Setup

docker run -p 9000:9000 -it -v  D:\Qualitrix\Indee\Indee_App_Automation:/home appautomation:1 /bin/bash 
cd /home
pip install -r requirements.txt
touch /root/.Xauthority 
Xvfb :99 -screen 0 1024x768x24 & export DISPLAY=:99  

pytest -m GDAppValidations --platform=fire_tv --appFileName=/home/builds/Paramount_GD_QA8_7.0.1.apk

pytest -m GDAppValidations --platform=roku_tv --roku_ip=192.168.1.68 --rokuUser=rokudev --rokuPass=Auto9876 --appFileName=/home/builds/Indee_Paramount_GD_Staff_Login_2024_07_10.zip

# References:
appium-python-client: https://pypi.org/project/Appium-Python-Client/

behave: https://behave.readthedocs.io/en/latest/

allure: https://allurereport.org/docs/behave/

Android Studio has been used to emulate device