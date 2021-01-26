import requests
import xlwt 
from xlwt import Workbook 

def urlify(in_string, in_string_length):
    return in_string[:in_string_length].replace(' ', '%20')

def abc_titles(string):
	alphabet = "abcdefghijklmnopqrstuvwxyz"
	output = []
	for i in alphabet:
		output.append(string + " " + i)
		output.append(i + " " + string)
	return output

def abc_query(string):
	alphabet = "abcdefghijklmnopqrstuvwxyz"
	output = []
	for i in alphabet:
		output.append(string + "%20" + i)
		output.append(i + "%20" + string)
	return output

def query_google(array):
	output = []
	for i in array:
		response = requests.get("http://suggestqueries.google.com/complete/search?client=firefox&q=" + i)
		output.append(response.json()[1])
	return output

def write_data_to_excel(titles, data, query):
	wb = Workbook()
	sheet1 = wb.add_sheet(query) 

	for i in range(len(titles)):
		sheet1.write(0, i, titles[i])
		for j in range(len(data[i])):
			sheet1.write(j+1, i, data[i][j])
	wb.save(query + ' longtails.xls') 

query = input("Enter a search query to find long tail keywords for:  ")
alphabet_titles = abc_titles(query)
urlified_query = urlify(query, len(query))
alphabet_queries = abc_query(urlified_query)
longtails = query_google(alphabet_queries)
write_data_to_excel(alphabet_titles, longtails, query)