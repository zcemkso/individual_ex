/*
Write SQL queries that can be executed on the chinook.sqlite database to provide answers the following questions.
Save your SQL to this .sql file. Do not include the query results.
In PyCharm you can right click on the file name in the Project pane and select Refactor > Rename, and replace STU_NUM with your student number.
*/

--1. Which employees have 'IT' in their job title? (list their EmployeeId, FirstName, LastName and Title)
SELECT EmployeeId, FirstName, LastName, Title FROM Employee WHERE Title LIKE '%IT%';

--2. List the names of all Artists and the titles of their albums
SELECT Artist.Name, Album.Title FROM Artist
    JOIN Album on Artist.ArtistId = Album.ArtistId;

--3. Which track(s) features the greatest number of times in playlists and how many times is it/are they included? (list Track name and the total number of appearances in playlists).
SELECT Track.Name, COUNT(DISTINCT PlaylistId) FROM Track
    JOIN PlaylistTrack PT on Track.TrackId = PT.TrackId
GROUP BY Track.Name
ORDER BY COUNT(DISTINCT PlaylistId) DESC
LIMIT 1;

--4. Provide a list of the number of tracks by each artist
SELECT Artist.Name, COUNT(T.Name) FROM Artist
    JOIN Album A on Artist.ArtistId = A.ArtistId
    JOIN Track T on A.AlbumId = T.AlbumId
GROUP BY Artist.Name;

--5. How much money has been invoiced for the artist Deep Purple? (For this you can create two queries, one that shows the line item from the invoices and the total amount per line, and another that sums the totals from each line)
 SELECT Artist.Name, SUM(I.Total) FROM Artist
     JOIN Album A on Artist.ArtistId = A.ArtistId
     JOIN Track T on A.AlbumId = T.AlbumId
     JOIN InvoiceLine IL on T.TrackId = IL.TrackId
     JOIN Invoice I on IL.InvoiceId = I.InvoiceId
WHERE Artist.Name = "Deep Purple";