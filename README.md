# GoodReads Website Scraping with Scrapy and Analysis of the Result with SandDance  
## *(to get the quotes for InfoSec, Hacking, Computer-Science and Security)* 


- You can find Json,csv results of the scraping process in the repo, if you need.


I try to learn more about Data Science and do some projects to exercise for my hobbies. In this project, I scraped the GoodReads Website for quotes about *InfoSec, Hacking, Computer-Science and Security* ; then made a simple analysis of quotes related to these topics *which I am interested in*. Even this simple, non academic project can give you lots of insight and if you are interested, you can seek whether there is a correlation between the number of likes and the length of quotes, whether the author of that quote affect the result, etc. 

The Python code will get the likes, tags, author, etc.Then, you let the Scrapy save the output as Json and csv formats. **(scrapy crawl quotes -o quotes.csv)**   
*Note*  : "quotes" is the I named the project. You need to give a unique name for Scrapy to work well, so according to your needs, if you use the code I used, then just arrange the code accordingly. Or let me know, I can also help if you encounter an issue.

 You can examine the data with Pandas, etc in Jupyter. OR, there is a useful extension for Visual Studio Code from Microsoft Research called SandDance. Easy and effective to use. I added some screenshots and a short gif video of this analysis here. So you can have an idea. 

![image](https://user-images.githubusercontent.com/59505246/137897518-5075a5c3-ce30-4909-b205-db18d537da08.png)

![image](https://user-images.githubusercontent.com/59505246/137898702-15e7dcd5-5c97-4c3d-aa3e-7d44739494c6.png)

![image](https://user-images.githubusercontent.com/59505246/137898979-51146df4-6b02-48aa-a5c8-aa974dbc820b.png)

![image](https://user-images.githubusercontent.com/59505246/137899475-09990b46-da63-4c1b-971b-808fa590a35a.png)

![image](https://user-images.githubusercontent.com/59505246/137901264-45d61bc0-7995-44b8-a7ce-afa57eda4372.png)

*"Those who would give up essential Liberty, to purchase a little temporary Safety, deserve neither Liberty nor Safety."* said Benjamin Franklin. What a lovely quote. It also seems a popular quote in GoodReads Website as the the number of likes might imply. 


![image](https://user-images.githubusercontent.com/59505246/137907529-982f4d7d-d42b-46a3-b3c5-8b47d9040467.png)

![image](https://user-images.githubusercontent.com/59505246/137908175-aba69d46-fe73-4b16-b1fa-c61525a45d48.png)
![image](https://user-images.githubusercontent.com/59505246/137908495-e8f7beb8-02cd-4dcb-8a7d-1672fab06de5.png)


![image](https://user-images.githubusercontent.com/59505246/137909791-a516b761-7871-422c-a94d-8f136f56101e.png)
![image](https://user-images.githubusercontent.com/59505246/137913838-a46b802a-1c01-471a-80e7-65b73180dbf7.png)

# To sum up, I agree with the Swedish author, Stieg Larsson *“We need to have a talk on the subject of what's yours and what's mine.”* with a conclusion that the data is ours! :). So feel free to use this hobby project. Just scraping but without getting insights from the scraped data has little value. So, the simple SandDance extension can give meaningful insights in a very easy way. That's why I've added screenshots, to inspire the ones who have not used this free extension/tool.
