import csv


def process_csv(file_path):
    email_list = set()
    company_counts = {}

    with open(file_path, 'r', encoding='utf-8') as file:
        csvreader = csv.reader(file)
    
        for row in csvreader:
            if len(row) != 3:
                continue
            
            name, company, email = row
            email = email.strip()
            company = company.strip()
        
            if email not in email_list:
                email_list.add(email)

                if company not in company_counts:
                    company_counts[company] = 1
                else:
                    company_counts[company]+=1
    sorted_company_list = sorted(company_counts.items(), key=lambda x: x[1], reverse=True)

    print(f'Số lượng đại biểu dự kiến tham dự: {len(email_list)}')
    print("Danh sách công ty và số lượng đại biểu:")
    for company, num_people in sorted_company_list:
        print(f'{company}: {num_people}')



process_csv("Lesson10/hw10/data.csv")