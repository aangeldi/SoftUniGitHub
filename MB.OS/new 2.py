#Import CANoe module
import re
from py_canoe import CANoe
from time import sleep as wait

# create CANoe object
canoe_inst = CANoe()

new_requirements = ["12345", "12346", "12347"]
requirements_coverage = []

for req in new_requirements:
    if req not in requirements_coverage:
        requirements_coverage.append(req)
    
requirements_coverage_count = len(requirements_coverage)
reqs_list = []
reqs_not_in_covarege = []

def extract_text_between_strings(text, start_string, end_string):
    pattern = re.escape(start_string) + r'(.*?)' + re.escape(end_string)
    matches = re.findall(pattern, text, re.DOTALL)
    return matches

# Example usage
file_path = "C:\.py_canoe/py_canoe.log"
start_string = ">req."
end_string = "<"

with open(file_path, "r") as file:
    log_contents = file.read()

extracted_text = extract_text_between_strings(log_contents, start_string, end_string)
for text in extracted_text:
    if text in requirements_coverage:
        if text not in reqs_list:
            reqs_list.append(text)
    else:
        reqs_not_in_covarege.append(text)
 
covered_reqs_count = len(reqs_list) 
canoe_inst.print_in_py_canoe(f"Covered {covered_reqs_count} requirements:{reqs_list}")

not_in_covarege_count = len(reqs_not_in_covarege)
if not_in_covarege_count > 0:
    canoe_inst.print_in_py_canoe(f"!!! Missing in Coverege scope {not_in_covarege_count} requirements:{reqs_not_in_covarege} !!!")

covered_percentage = (covered_reqs_count / requirements_coverage_count) * 100
canoe_inst.print_in_py_canoe(f"{covered_percentage :.2f}% from full coverage")

# print(canoe_inst.failed_reqs)