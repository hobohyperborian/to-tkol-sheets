
Welcome to the Tactics Ogre - The Knight of Lodis spreadsheet editors suite. 
Here I'll explain how to use them.

------

HOW TO EDIT DATA & APPLY YOUR CHANGES TO A ROM

  1. BACK UP YOUR ROM AND SPREADSHEETS! GIVE THEM RELEVANT NAMES IF IT HELPS!
    
  2. Change the name of your rom so it has no spaces. Use underscores or 
    hyphens.
    
  3. Copy and paste the full name of the rom plus it's file extension (*.gba) 
    into the green cell under the "Filename" cell in the "Misc" sheet of each 
    spreadsheet you use. If you look at the "CSV" sheet, this should change the 
    name there.
    
  4. Make whatever changes you want to the green cells in your spreadsheet(s).
    Note that each cell must contain a base 16 (hexadecimal) number 2 digits 
    long.
  
  5. Save your spreadsheets.
  
  6. Go the "CSV" sheet in each spreadsheet where you made changes to the data.
    Once there, go to the "File" menu, select "Save as...", and a pop-up should 
    appear prompting you to save the file again. 
  
  7. Go to the bottom most text entry area & drop down selection menu that is 
    names "Save as type:" and click into the drop down menu. Scroll down until 
    you see "Text CSV (*.csv)". Select that option and click "Save".
    
  8. Two more pop-ups should appear one after the other. Click "Okay" for both 
    of them.
    
  9. Close the spreadsheet and do not make any more changes to it or save it.
    
 10. Read the command prompt FAQ included with in with the spreadsheets if you 
    haven't already, then open the command prompt.
    
 11. Use the cd and dir commands to navigate in the command prompt to wherever 
    you put the spreadsheets. If this is an issue, move them closer to your C: 
    drive.
 
 12. If you haven't installed python 3 yet, do so. See the command prompt FAQ.
 
 13. Put the rom in the same folder with your *.csv files.
 
 14. Run the following command in the command prompt:
      python .\writeAllCSVs.py *.csv
    
    Wait until the blinking underscore disappears and the name of your current 
    directory reappears. When it does, it's done writing.
    
    Note that this script will write all *.csv files in the same directory to 
    your rom. Don't keep any CSVs there that you don't want written.
 
 15. Give your modded rom a relevant name, play it in an emulator to verify it 
    worked, and then use one of the patch generators on romhacking.net to make 
    a patch for distribution.

------

HOW TO EXTRACT CHANGES FROM A MODDED ROM AND IMPORT THEM INTO A SPREADSHEET

  1. BACK UP YOUR ROM AND SPREADSHEETS! GIVE THEM RELEVANT NAMES IF IT HELPS!
  
  2. Put your rom and dumpAllData.py files in the same folder.
  
  3. Read the command prompt FAQ included with in with the spreadsheets if you 
    haven't already, then open the command prompt.
  
  4. Navigate to that folder in the command prompt using the cd and dir 
    commands within the command prompt. If this is an issue for you, move them 
    closer to youro C: drive.
  
  5. If you haven't installed python 3 yet, do so. See the command prompt FAQ.
  
  6. Run the following command in the command prompt:
      python .\dumpAllData.py '.\totkol.gba' > .\modded_data.txt
    
    The file "modded_data.txt" can be renamed to anything you want, so long as 
    it ends in ".txt".
    
    It should finish this script within a second.
    
  7. Open modded_data.txt or whatever you called it. Inside you should see 
    names that correspond to spreadsheets, and if a spreadsheet has multiple 
    sheets then also a sheet name. Below each name will be a bunch of bytes in 
    base 16 (hexadecimal) surrounded by single quotes.
    
    Highlight all the bytes for each sheet, open the corresponding spreadsheet, 
    navigate to the correct sheet, and paste this in the green-backgrounded 
    cells.
    
    You should only need to highlight (not click into) the top-most & left-most 
    cell, then click paste.
    
  8. This should bring up a "Text Import" pop-up.
    
    Under Separator Options, select "Space", "Merge delimiters", "Trim Spaces", 
    and select the single quote (') option for "String delimiter".
    
    Under Other Options, select "Format quoted field as text".
    
    When you are done, click "Okay".
  
  9. Save your spreadsheet. Give it a relevant name, such as the name of the 
    mod you extracted it from, followed by the name of the data it represents.
  
------
