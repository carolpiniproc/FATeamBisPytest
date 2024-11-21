# Feature Activation E2E Test Project

This project have the propose of doing e2e tests in bees aplications Android or iOS

<br>

## Dependencies
You have to install:
  
* Android Studio - Download and install it from your OS store if available, otherwise access (https://developer.android.com/studio?hl=pt)  
    *   Create a virtual device - ADV
    *   Choose an Android version 
    *   Copy the device name and the OS version 
    *   Update the `behave.ini` file with the above information 
    *   Save $ANDROID_HOME path for later               
* Java (https://www.java.com/)  
    *   Save $JAVA_HOME path for later
* Node.js version >= 12, consider installing it with `nvm`

```sh
curl -sL https://raw.githubusercontent.com/nvm-sh/nvm/v0.35.0/install.sh | bash
nvm install v12
nvm use v12
```
- * Remember to add `nvm` configuration at your `~/.bashrc`:

```sh
export NVM_DIR="$HOME/.nvm"
  [ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh"  # This loads nvm
  [ -s "$NVM_DIR/bash_completion" ] && \. "$NVM_DIR/bash_completion"  # This loads nvm bash_completion
```
* Appium (https://appium.io/docs/en/about-appium/getting-started/?lang=pt)

```sh
sudo npm install -g appium --unsafe-perm=true --allow-root
```

### Set environment variables

Export all environment variables you copied previously at your `~/.bashrc`:

```sh
nano ~/.bashrc
export ANDROID_HOME=<your_android_sdk_path>
export JAVA_HOME=<your_java_path>
export PATH=$PATH:$JAVA_HOME
export PATH=$PATH:$JAVA_HOME/bin
export PATH=$PATH:$ANDROID_HOME/platform-tools
export PATH=$PATH:$ANDROID_HOME/tools
export PATH=$PATH:$ANDROID_HOME/tools/bin
export PATH=$PATH:$ANDROID_HOME/emulator
```
#### Install project dependencies

```sh
pip install -r requirements.txt
```
#### Install pylint
```sh
pip install pylint
```
  * All the pylint configuration can be found on `.pylintrc` file  
  * It will find any issue into the code  

  ```sh
pylint 'file_name.py'
```

#### Include the app file to the automation project
* Download apk or ipa file from AppCenter (https://appcenter.ms/apps)
* Include it on the project root folder
* Copy full path from where you have downloaded it on `behave.ini` file


#### Execute Appium chromedriver in background
```
appium --allow-insecure chromedriver_autodownload
```

#### Run Tests
* Run all tests
```sh
behave
```
* Run specific tag
```sh
behave --tags='tagNameHere'
```
* Run specific scenario
```sh
behave -n 'The scenario name here'
```
* Run a feature file
```sh
behave -i 'file_name'.feature
```