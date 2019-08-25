### For automation and test check README files in respective folders automation/src and automation/tests

# Task 1 - test cases for Monefy

The test cases for mobile application Monefy would split into 3 major groups with subgroups

    *   Usability of the application (with Free and Pro highest)
        * User can easily add income
        * User can easily add expenses
        * User can easily overview daily balance change
        * ...
    *   Security
        * Passcode
        * Access to Dropbox
        * Access to Google Drive
        * Synchronization
        * ...
    *   UI views on different platforms/devices
        * View is same on smaller devices and larger devices
        * Tablet/iPad view is same as UI on mobile devices
        * IF app support it - Horizontal view is scrollable and same as the vertical view
        * ...

##### Usability of the application  

With Free or Pro version of the application the users have to have easy overview and access to 
calculation of their funds/expenses. The application should be as intuitive as possible for the users, 
without too much onboarding. This section is fairly the largest as ion some portion it includes the other two as well.
This approach is also recommended to be tested with people who have never seen the application before.  
If real users don't like the application by intuition they won't use it which is the main impact on revenue and popularity of a product.   


##### Security  

When application have possibility to connect to other external applications such as GoogleDrive and 
Dropbox, security is very crucial for the users and the company. This would be the most important for 
the company but based on testing i choose Usability for users because if they don’t like to use it 
because of application complexity they don’t care about security. 


##### UI views, that should be the same on different platforms/devices  

Ensuring that the application is responsive, no overlap or UI elements in case of vertical or 
horizontal view etc. Can be part of usability but not overall   


## Test cases

##### APP usability    

* User can add income:  
    * By pressing on Green + on home page and selecting income type  
    * By selecting previously added income category and click on icon


* User can add expenses
    * By pressing on Red - on home page
    * By selecting previously added expense category and click on icon
    * By selecting one of the suggested iconst around the expenses chart


* User can overview balance change
    * On Daily level, scrolling left-to-right on the home page with chart
    * On Daily level, scrolling left-to-right on the home page when expenses list is selected instead of chart
    * By selecting the specific date - left top corner, hamburger menu, select date, pick date from calendar
    * On Weekly level, scrolling left-to-right on the home page with chart
    * On Weekly level, scrolling left-to-right on the home page when expenses list is selected instead of chart
    * On Monthly level, scrolling left-to-right on the home page with chart
    * On Monthly level, scrolling left-to-right on the home page when expenses list is selected instead of chart


* User can add new account and transfer between his accounts
    * Can transfer from payment card to cash (ATM)
    * Can transfer from cash to payment card (cash deposit)
    * User can create a new account (MC, Visa, Debit…)


* User can edit income or expense
    * User can edit his Salary income
    * User can edit his Deposit income
    * User can edit his Savins income
    * ...
    * User can edit his Food Expense
    * User can edit his Car Expense
    * User can edit his Communications Expense
    * User can edit his Health Expense
    * ...  
    
* Application function the same in different Androis/iOS version
* Buttons and inputs are responding once selected
* Sensitivity of touchscreen e.g. should not open something if user is scrolling
* And many more...


##

##### APP security
###### As i did not pay for PRO version test cases are purely "best guess" of expectations what should work flawless as a lot of information goes on more public and exposed data sources such as Dropbox an GDrive.

* User can add security to account
    * User can add PIN passcode to his account
    * User can reset his PIN passcode 
    * User can download securely current settings, without data loss or corruped files
    * User can securely sync with other devices (this is multiple ways), without data loss
    * User can securely sync with Dropbox, without data loss
    * User can securely sync with Google Drive, without data loss
    * ...
    
    
##
##### APP security

* UI is reponsive and no distortions
    * There are no buttons or other UI components overlap
        * List of test cases for potential component overlaps
    * UI is same on different screen sizes 
        * List of test cases for screen comparisons and potential problematic devices types
    * UI has no color distortion on devices
    * UI is the same on different Androis/iOS versions
    
###### Many of such UI issues cannot be fully tested as that require intense manpower and usually end-users report such issues. But a lot of effort needs to work on many versions and display sizes.