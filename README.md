# The Prime Challenge

The Prime Challenge Walkthrough

The goal of the challenge is to log into the hosted ssh server as the user “CyberGuy” and obtain an email address. The participant will email his/her team name to this email to complete the challenge.

Start by giving the attempters of the challenge a means of obtaining the README.txt and the “gettosearching” folder (google drive link: https://drive.google.com/open?id=1i_MhDyCGYT4hP2_v-NoJDfE-yuikpzHm). The README.txt contains an important hint to figuring out the challenge. The “gettosearching” folder contains 200 files, all of which follow a \<random letter\>\<large number\>.txt format. The random letter was added to the front of each file to make it more difficult to search through the file names.

The first task is to find the server log in credentials (the ip address of the server and the ssh password). These are located in one of the 200 files. Ideally, the participants will write some sort of script to strip the file names of anything except the number itself, then, check to see if that number is a prime. Exactly 10 of the file names are prime numbers, and only ONE of these 10 is an “Emirp” number. An Emirp is a prime number that results in a different prime when its decimal digits are reversed. The README.txt file obtained at the beginning of the challenge provides a hint that the participant should be looking specifically for an Emirp. The Emirp file name is g135887.txt (location of ssh log in credentials), because both 135887 and 788531(135887 reversed) are prime numbers.

The participant will use the credentials obtained from the first task to log in as CyberGuy@[ip address]. Once logged in, the user will come across a locked zip file (crackme.zip) along with an important file named “hash.txt”. “hash.txt” contains an md5 hash of the password needed to unlock crackme.zip, as well as a hint to make decrypting this hash much easier. The hint is that it is a 5-letter-long md5 hash. They can use a password cracker from one of their latech courses, or of course, use the internet to find an md5 decrypter. The password is “nofac”. With the password discovered, the user will be able to unlock crackme.zip, which consists of “congrats.txt”. This final text file contains an email and a straightforward task: “Email your team name to this email address: Fid8hl6@mail.com.” When the Fid8hl6 mail account receives an email containing the name of a participating team, the points (3500 pts.) are awarded to said team.


Team Leader: Danny Rogers (dcr025@latech.edu)
