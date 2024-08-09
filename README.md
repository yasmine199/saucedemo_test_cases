# saucedemo_test_cases

Test cases for web application:

Description:
we have a web application "www.saucedemo.com" that sells many types of product.
to login to this web application we have a specific list of users and a specific password.
In the front page we have all items presented : each item is followed by a title , mini description, price and an icon were it can be selected .

Precondition:
+must have surfing browser

Test case ID:1
Title: logging with locked_out_user user 

Test steps:
1- brows to the application
2- put a "locked_out_user"
3- put the correct password witch is "secret_sauce"
4-login 

Expected results:
+must have a logging error

Test case ID:2
Title: logging with incorrect password

Test steps:
1- brows to the application
2- add a correct user name "standard_user"
3- put a wrong password that is not "secret_sauce"
4- login

Expected results:
+must have a logging error

Test case ID:3
Title: Correct login

Test steps :
1- brows to the application
2- use all users in this list (standard_user,problem_user,performance_glitch_user, error_user,visual_userone)one by one to log in followed by this password "secret_sauce"
3-login in each user case

Expected results:
+must have a successful login each time

Test case ID:4
Title: Add product to cart

Test steps:
1- login with the correct user and password
2- Click on "Add to cart" bar to add the product in the bucket
3-Click on bucket and check if selected item is there


Expected results:
+must have a successful login
+product must be added to chart when clicking on "Add to cart" bar 
+product must be in bucket

Test case ID:5
Title: Remove product from chart

Test steps:
1- login with the correct user and password
2- Click on "Add to cart" bar
3-Click on bucket and check if selected item is there
4-Go back to front page
5-Select the same item and Click on "Remove" bar
6-Click on bucket and check if selected item was removed

Expected results:
+must have a successful login
+product must be added to chart when clicking on "Add to cart" bar 
+product must be in bucket
+product must be removed from chart when clicking on "Remove"
+product must be removed from bucket

Test case ID:6
Title: Remove items from bucket

Test steps:
1- login with the correct user and password
2- select multiple products
3- check bucket list 
4- remove items from bucket list

Expected results:
+must have a successful login
+products must be selected when clicking on its name 
+all selected products must be added to chart when clicking on "Add to cart" bar 
+all selected products must be the same in the bucket 
+product must be removed from bucket when clicking on "remove"

