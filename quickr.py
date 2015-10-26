from lxml import html
import requests
import csv,os,time
joiner=' , '
temp1=[]


def modifyEntry(entry):
    if len(entry)==0:
        entry.append('')
def createTree(link):
    page = requests.get(link)
    #print page
    tree = html.fromstring(page.text)
    #print tree
    return tree

def extractLinkWithTree(tree,xpath):
    #print xpath
    #print tree
    temp = tree.xpath(xpath)
    """
    for i in temp:
        a = "http://www.quikr.com"+i
        temp1.append(a)
    """    
    #print temp1
    return temp

def extractLink(link,xpath):
    #print xpath
    return extractLinkWithTree(createTree(link),xpath)

def uniq(input):
    output = []
    for x in input:
        if x not in output:
            output.append(x)
    return output





mainPageLink="http://www.quikr.com/Real-Estate/y20?page=5"
#dir_path=keyword
#if not os.path.exists(dir_path):
  #os.makedirs(dir_path)
print "Extracting data:\nPlease wait...\n"
"""
pageLink=[mainPageLink]
try:
    pageLink=extractLink(mainPageLink,'//*[@class="ie7pagili"]/a/@href')
except:
    print "error"
#print pageLink
"""
"""
for x in pageLink:
  pageLink+=extractLink(x,'//*[@class="ie7pagili"]/a/@href')
  print pageLink
  try:
      pageLink=uniq(pageLink)
  except:
      print "error"
      

"""
for i in range(1,71621):
    a = "http://www.quikr.com/Real-Estate/y20?page="+str(i)
    temp1.append(a)

with open('/home/ashu/quickr/data.csv', 'wb') as csvfile:
      spamwriter = csv.writer(csvfile, delimiter=',',quotechar='"', quoting=csv.QUOTE_MINIMAL)   
      for page in temp1:

          for LinkInPage in extractLink(page,'//*/a[@class="adttllnk unbold"]/@href'):
              try:
              #print LinkInPage
		b=[]
		tree=createTree(LinkInPage)
		name=extractLinkWithTree(tree,"//*/h1/text()")
		price=extractLinkWithTree(tree,"//*/span[@class='price']/text()")
		key=extractLinkWithTree(tree,"//*/span[@class='ad-atrbt-lbl']/text()")
		value=extractLinkWithTree(tree,"//*/span[@class='attribVal newattribVal']/text()")
		#dictionary = dict(zip(key, value))
		phone=extractLinkWithTree(tree,"//*/span[@class='NoVerified-Text']/text()")
		desc=extractLinkWithTree(tree,"//*/div[@id='ad_description']/text()")
		modifyEntry(name)
		modifyEntry(price)
		modifyEntry(phone)
		modifyEntry(desc)
		for i,j in zip(key,value):
		    a= i+":"+j
		    b.append(a)
		c="^".join(b)
		#print c
		#print str(dictionary).split(",")[0]
        
		#print name,price,dictionary,phone,addr,"\n"
		time.sleep(1)
		row = [name[0].strip().encode('ascii','ignore')]+[price[0].strip().encode('ascii','ignore')]+[phone[0].strip().encode('ascii','ignore')]+[desc[0].strip().encode('ascii','ignore')]+[c]
		spamwriter.writerow(row)        
		print row
	      except:
		print "Error"
"""                
             
              #while (1):
                tree=createTree(LinkInPage)
                name=extractLinkWithTree(tree,"//*/h1/text()")
                modifyEntry(name)
                print name
                time.sleep(1)             
                    
                  
                  
                  tag=uniq(tag)
                  tel=extractLinkWithTree(tree,"//*[@class='tel']//text()")
                  tel=uniq(tel)
                  website=extractLinkWithTree(tree,"//*[@class='wsurl']/a/@href")
                  rating=extractLinkWithTree(tree,"//*/span[@class='NoVerified-Text']/text()")
                  rating=uniq(rating)
                  website=uniq(website)
                  establish=extractLinkWithTree(tree,"//*[@class='fcont'][last()]/text()[2]")
                  print rating
                  modifyEntry(website)
                  modifyEntry(address)
                  modifyEntry(tel)
                  modifyEntry(establish)
                  modifyEntry(rating)
                  modifyEntry(name)
                  row= [(name[0].strip()).encode('ascii','ignore')]+[address[0].strip().encode('ascii','ignore')]+[((joiner.join(tel)).strip()).encode('ascii', 'ignore')]+[website[0].strip().encode('ascii','ignore')]+[establish[0].strip().encode('ascii','ignore')]+[rating[0].strip().encode('ascii','ignore')]+[((joiner.join(tag)).strip()).encode('ascii', 'ignore')]
                  #row=row1.encode('ascii','ignore') 
                  if (row!=['','','','']):
                     #print (row!=['','','',''])
                      break
"""  
            
              #spamwriter.writerow(row)        
              #print row             
