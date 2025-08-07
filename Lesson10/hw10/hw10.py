import csv

email_list = set()
company_counts = {}

with open("Lesson10\hw10\data.csv", 'r') as file:
    csvreader = csv.reader(file)
    
    for row in csvreader:
        name, company, email = row
        email = email.strip().lower()
        
        if email not in email_list:
            email_list.add(email)

            if company not in company_counts:
                company_counts[company] = 1
            else:
                company_counts[company]+=1
            

            
print(f'Số lượng đại biểu dự kiến tham dự: {len(email_list)}')
sorted_company_list = sorted(company_counts.items(), key=lambda x: x[1], reverse=True)

for company, num_people in sorted_company_list:
    print(f'{company}: {num_people}')