Washington News Nerds Scraping Workshop
=======================================

Before we scrape
----------------

* Install Beautiful Soup by running ``pip install bs4 --user``
* Install Requests by running ``pip install requests --user``

Our target page
---------------

We're going to be grabbing data from Washington's purchasing department, pulling data for all "diverse" confirmed contracts. Washington purchasing is located here:

https://fortress.wa.gov/es/apps/ContractSearch/DiverseContracts.aspx

Then we're going to take this, pull each of the pages, and turn them into a CSV including the costs and diversity status of each contract.

