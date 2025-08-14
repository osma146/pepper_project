# TEST - html in odd folder

test responce of naoqi service when html needed it in a child of anothe folder of an app

this is needed for better and more direct connection of app inorder for app sorting

## diffrence
 
### normal

    ```bash
    qicli call ALTabletService.showWebview "http://198.18.0.1/apps/test_html_location/index.html?version=1111"
    ```

### new 

    ```bash
    qicli call ALTabletService.showWebview "http://198.18.0.1/apps/test_html_location/test_html_location/html/index.html?version=1111"
    ```

# Test result (14/08/2025)

**False**

> - .html file must be in app html folder and the app need to be in apps