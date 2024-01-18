# Scheduler
## About Scheduler 
Scheduler is a home made project, which serves for my personal training in python and SQL programming. It can serve to record tasks, which you want to do one day, including social events like going to the cinema or housework such as clean up the kitchen and assigs these tasks to any person you include into your database. Every task within the scheduler has also a possibility to have assigned one or more tags desribing category of the task like housework, fun, relax or work, start and due date or it is possible to record if the task was already done.

**Requirements** 
- sqlite3
- python3
- Linux

**Usage** 

*To run Scheduler with empty database and fill it in by following the instruction of python script*
  - run python script "play_with_screens.py"

*Other possibilities*

  - It is possible to fill in an empty database using sql script "Table_filling.sql". You can find the inspiration in the sql script "Exemplary_table_filling.sql" or directly use it as an examplary filling to play with Schedurler  

*When you want to delete and completely change sql database*
- Use sql script "table_basic_structure.sql" placed in "Scripts" directory and generate an empty database within database directory using basic sql commands. The previous database has to be deleted. There should be always only one sql database placed in "database" directory.
