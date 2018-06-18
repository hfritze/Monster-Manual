# Monster-Manual
Helping DMs pick monsters


This code allows a Dungeon Master to find all possible monsters that their party could encounter given the players' level and the terrain they will encounter. This code utilizes a spreadsheet of all of the monsters in the manual created by Endomorphism on reddit: https://redd.it/3dfose 

The spreadsheet contains the name, hit points (HP), armor class (AC), challenge rating (CR), and first two attack damages for each monster, along with the types of terrain in which it may be found. I took this data, and wrote code that uses that information, along with prompts from the DM, to return a list of foes relevant to the session at hand. The DM is prompted to input the players' level, and the terrain. For instance, if the DM is looking for a monster that would appear in the Arctic and would be a worthy foe for their party, which is around a level 2, my code will output a data frame of all monsters that fit that criteria, with the most challenging monsters appearing first. This data frame includes the name of the monster, as well as its armor class, hit points, challenge rating, type, and size. An image of the input prompts and the data frame output can be seen here, with the level set to 2, and the terrain set to Arctic:

![Alt text](Images/table_output.png?raw=true "Title")

Once the DM has chosen a monster they think will be a good match, they may then choose to get more information about that monster. After the initial table is produced, a new prompt allows them to enter the name of the monster. At this point, the code produces a PDF of that monster's stat sheet, taken from a larger PDF of the entire monster manual. This was done by scraping the index page of the PDF for the monster's name, getting the corresponding page number, and writing that page out to a file. That file is then opened so that the DM can view it, and immediately deleted so as to not take up space on the DM's computer. If the DM has no interest in further information, they may simple respond with "no thanks" 

For example, the image below is the output for the Ice Mephit, which was one of the outputs found in the table above:

![Alt text](Images/Ice_Mephit.png?raw=true "Title")

While this type of program is not a new idea, it is meant to show my ability to parse and visualize data in a simple way, as well as scrape PDFs for only the most useful information (in this case, the page numbers corresponding to a given monster). There were a few issues with the PDF quality, which caused the scraper to see some I's as l's, and some c's as e's. That has been fixed with a set of hard lines in the code for known monster names with that problem. Future steps for this code include finding a way to automate an adaptation to that issue instead of hard-lining the name changes.

Note: to use this code, you need `DD.py`, `Monster Manual.pdf`, and `D&D_5e_Monster_Manual.csv`. The Monster Manual pdf is too large to opload to github, but can be found at http://orkerhulen.dk/onewebmedia/Monster%20Manual.pdf
