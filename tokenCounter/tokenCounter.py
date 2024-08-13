import sys
import tiktoken

# args are counted after "python"
text = """
"01/19/2024","-1.00","*","","SAVE AS YOU GO TRANSFER DEBIT TO XXXXXXXXXXX1745"
"12/20/2023","-20.00","*","","PURCHASE AUTHORIZED ON 12/18 STARBUCKS STORE 53 BURBANK CA S303352562632931 CARD 4987"
"01/19/2024","-101.00","*","","DISCOVER E-PAYMENT 240119 3212 BROCKE YAHIA"
"01/19/2024","-850.22","*","","SIKORSKY BLP ECM LOAN PAY 240118 85895660 Yahia Adrian Brocke"
"01/16/2024","-128.31","*","","GEICO PREM COLL 240112 1606016912 YAHIA Y"
"01/12/2024","-17.29","*","","PURCHASE AUTHORIZED ON 01/11 CVS/PHARMACY #0157 NORTH HOLLYWO CA S384012138665729 CARD 4987"
"01/12/2024","-79.93","*","","PURCHASE AUTHORIZED ON 01/11 TRADER JOE S #05 TRADER J TOLUCA LAKE CA P584012126121660 CARD 4987"
"01/08/2024","-6.50","*","","PURCHASE AUTHORIZED ON 01/04 SCRIPPS HEALTH ROI 760-6337746 CA S384004806852271 CARD 4987"
"01/08/2024","-49.55","*","","PURCHASE AUTHORIZED ON 01/05 COSTA ORANGE 9 COSTA MESA CA S584006133807043 CARD 4987"
"01/12/2024","1257.62","*","","APEX SYSTEMS, LL DIR DEP 240106 13760085 BROCKE,YAHIA ADRIAN"
"01/16/2024","-83.31","*","","PURCHASE AUTHORIZED ON 01/13 TST* BLUE PLATE TA Santa Monica CA S584013777219566 CARD 4987"
"01/12/2024","1000.00","*","","Capital Gains Baby"
"""

# print(f"Arg 0:{sys.argv[0]} Arg 1:{sys.argv[1]} Arg 2:{sys.argv[2]} Arg 3:{sys.argv[3]}")

# initialize the tokenizer
# encoding = tiktoken.encoding_for_model("gpt-3.5-turbo") # not explicit enough:
# Explicitly get the tokenizer for gpt-3.5-turbo
encoding = tiktoken.get_encoding("cl100k_base")

num_tokens = len(encoding.encode(text))

print(f"Number of tokens: {num_tokens}")