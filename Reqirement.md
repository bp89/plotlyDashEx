There is a bank named **Flix Bank**

It provides following services in general
Flix Bank
- savings accounts
- loan accounts
    - vehicle loan
    - personal loan
    - home loan

1. Create a dashboard page titled Flix Banking with following details:
    - Add logo with the name of the bank & keep it left aligned
    - bank name should be 8px padded with logo and should be left aligned as logo is.
    - Add tabs right aligned and in same row as logo as following:
        - Home
        - Savings
        - Loan

**Home Tab**
    1. Show a line chart for showing real time data for  Amount deposited / withdrawn. Also, show total money available with bank on top on chart. 
       Total money available must also updated at same frequency as of chart. Keep the refresh rate to 5 sec for demonstration purpose.        
**Savings Tab**:
2. Add a Line chart showing number of savings accounts (a line of different color for opened/closed accounts)
    opened /closed in current year by default
    Add a select box on top left of the chart which shows following time periods:
        Last 7 days
        Last 28 days
        Last 6 months
        Current Year
        & all the years starting from 2018
    On change of selection in time period select box, update the chart to show data for that period. Note:
    The values on x-axis depend on the time period selected e.g. if current year is selected then data must be grouped by Months
3. On chart mentioned in above point #2, on hover show the period and the value in tooltip with account type

**Loan Tab**
1. Create a bar chart showing amount of loan disbursed by bank for each loan type.  
2. Create a select box to change time period to following:
    Today Realtime (To show realtime updates on disbursed loan that includes all realtime updates)
    Last Year
    Current Year
    All time
        
        
       
 
Additional:
1. Add a multi selectbox on top to show hide chart sections on dashboard so that user can show required charts only. 
