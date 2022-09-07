# Notes for Requirements.txt

The pip package for this project has gotten bloated due to compatibility issues between Heroku and Python 3.10.
In order to mitigate this problem, requirements.txt locally may not be the correct environment for a remote build.
This is mainly due to the handling of PostgreSQL versus SQLite3.
The problem is that PostgreSQL requires a separate spin-up, and the manner that this django project starts is contained.


### Fixing the Problem
**The Packages that cause the build error are psycopg2, and backports.zoneinfo**

