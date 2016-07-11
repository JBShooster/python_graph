#Write-Up
 - To run the program, access the directory in your terminal and enter "python app.py"
 - I felt that creating an object with easy-to-understand functions was the best way to go. I also give the user the ability to determine if the Graph is directed or undirected. For the sake of this exercise we treat the graph as undirected.
 - In a real-world application I would use PostGres 9.5 to handle this data. Postgres is great because it has JSON storage in an SQL database. This makes Mongo irrelevant and combined the benefits of document-store in a far more secure SQL database. Just reference the users with private keys and then the respective JSON trees allow for easy access of information.
