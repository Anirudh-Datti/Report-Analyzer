import google.generativeai as genai
import PyPDF2 as pdf
import os 

def generate_summary_report(report):

    text = ""   
    with open(report, "rb") as file:
        reader = pdf.PdfReader(file)
        for page in reader.pages:
            text += page.extract_text()
     

    genai.configure(api_key = "AIzaSyAQ7uIqUNqz5rCmq9K0MP2zhX5fxNMLtoI")
    model = genai.GenerativeModel("gemini-2.0-flash")

    response = model.generate_content(f"{text}. Now analyze the given report and give me a short summary report where it is a good investment opportunity or not. . you can use tables graphs etc. for visualization ")

    summary = response.text

    return summary

def write_to_file(report, summary):
    #extracting report name.
    path_list = report.split('/')
    name = path_list[2][:-4]

    #writing into a file.
    with open(f"reports/summary_reports/{name}_summary.txt", 'w') as file:
        file.write(summary)

    print("Reports are Ready...")

def run():
    report = "reports/annual_reports/Syngene-Annual-Report-2023-24-main.pdf"
    summary = generate_summary_report(report)
    write_to_file(report, summary)