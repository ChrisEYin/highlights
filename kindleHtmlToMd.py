from bs4 import BeautifulSoup

with open("raw/done/Thinking in Systems_ A Primer - Notebook.html", "r") as f:
  contents = f.read()
  soup = BeautifulSoup(contents, 'lxml')

title = soup.find("div", {"class": "bookTitle"})
unicode_title = unicode(title.string)
clean_title = unicode_title.strip()
# clean_title_split = clean_title.split(':', '')
# final_title = clean_title_split[0] + " -" + clean_title_split[1]

author = soup.find("div", {"class": "authors"})
unicode_author = unicode(author.string)
clean_author = unicode_author.strip()
clean_author_split = clean_author.split(',')
author_name = clean_author_split[1] + " " + clean_author_split[0]

highlights = soup.findAll("div", {"class": "noteText"})
#for highlight in highlights:
#	map(unicode,highlights)

with open("output/why-dont-we-learn-from-history.md", "w") as f:
    f.write("---" + "\n")
    f.write("title: " + str(clean_title) + "\n")
    # f.write("title: " + str(final_title) + "\n")
    f.write("category: books" + "\n")
    f.write("permalink: /:categories/:title/"+ "\n")
    f.write("author: " + str(author_name)+ "\n")
    f.write("layout: bookpost" + "\n")
    f.write("tags:" + "\n")
    f.write("- booknotes" + "\n")
    f.write("---" + "\n")
    f.write("\n")
    for highlight in highlights:
    	f.write("> ")
    	highlight = str(highlight)
    	highlight = highlight[27:]
    	highlight = highlight[:-6]
    	f.write("%s\n" % highlight)