#level0 
ssh bandit0@bandit.labs.overthewire.org -p 2220 
cat readme
exit

passwords: ZjLjTmM6FvvyRnrb2rfNWOZOTa6ip5If


# level1
ssh bandit1@bandit.labs.overthewire.org -p 2220
cat ./-       #put a dot and front slash so that cat command doesn't confuse the filename as its option 
exit

password: 263JGJPfgU6LtdEvgfWU1XP5yac29mFx


#level2
ssh bandit2@bandit.labs.overthewire.org -p 2220 
cat ./--spaces in \this \filename--       #escaped the spaces with backslashes
exit

password: MNk8KNH3Usiio41PRUEoDFPqfxLPlSmx


#level3
ssh bandit3@bandit.labs.overthewire.org -p 2220
ls -a
cd inhere
ls -a
cat ./...Hiding-From-You 
exit

password:2WmrDFRmJIq3IPxneAaMGhap0pFhF3NJ


#level4
ssh bandit4@bandit.labs.overthewire.org -p 2220
ls
cd inhere
ls -la
file ./-file*      # "*" is a wildcard and means all the files whose names starts with "-file"
cat ./-file07 
exit

password found: 4oQYVPkxZOOEOO5pTW81FB8j8lxXGUQw


#level5
ssh bandit5@bandit.labs.overthewire.org -p 2220 
ls 
cd inhere
find . -size 1033c ! -executable   #the dot(".") tells the system to search in the directory and "-size 1033c ! -executable" asks to fetch non executable file of 1033 bytes 
cd maybehere07 
cat .file02 
exit

password found: HWasnPhtq9AVKe0dmk45nxy20cvUa6EG


#level6 
ssh bandit6@bandit.labs.overthewire.org -p2220 
ls -a 
find / -size 33c -user bandit7 -group bandit6       #the forward slash "/" asks the system to search throughout the server and the rest of the options specify the user and the group
cat /var/lib/dpkg/info/bandit7.password
exit

password found: morbNTDkSW6jIlUc0ymOdMaLnOlFVAaj


#level7 
ssh bandit7@bandit.labs.overthewire.org -p2220
ls 
cat data.txt | grep "millionth*"      # asks the shell to find the text "millionth" and anything that follows 
exit

password found: dfwvzFQi4mU0wfNbFOe9RoWskMLg7eEc


#level8
ssh bandit8@bandit.labs.overthewire.org -p2220 
ls 
cat data.txt
sort data.txt | uniq -u      # sort command asks the shell to sort the lines of a text file in ascending order and uniq -u discards repeated lines from the sorted lines. 
exit

password found: 4CKMh1JI91bUIZZPXDqGanal4xvAg0JM


#level9 
ssh bandit9@bandit.labs.overthewire.org -p2220
cat data.txt
strings data.txt | grep "=*"        # strings reads and prints all the ASCII text present in a file.
exit

password found: FGUW5ilLVJrxX9kMYMmlN4MgbpfMiqey


#level10
ssh bandit10@bandit.labs.overthewire.org -p2220
cat data.txt
echo "VGhlIHBhc3N3b3JkIGlzIGR0UjE3M2ZaS2IwUlJzREZTR3NnMlJXbnBOVmozcVJyCg==" | base64 -d #this outputs the given base64 string after decoding it.
exit

password found: dtR173fZKb0RRsDFSGsg2RWnpNVj3qRr
