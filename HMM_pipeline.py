
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# In[30]:


file_list = ["M4YX12_STREQ", "A0A081BKX9_9LACO", "A0A1G9IV55_9CLOT","C2D302_LACBR","A0A1P8Q111_9LACO", 
             "B5CL59_9FIRM", "A0A0D0YUU5_9LACO", "A0A0H4LAX2_9LACO", "A0A0R1S2S1_9LACO", "A0A0R1WWN2_9LACO", "A0A0R2DGS6_9LACO", 
             "A0A0R2HM97_9FIRM", "A0A0R2HZC9_9LACO", "A0A0R2I8Q5_9LACO", 
             "A0A0R2JSC5_9LACO", "A0A133YDF1_9FIRM", "A0A1E5KUU0_9ENTE", "A0A1I0EHL5_9FIRM", 
             "A0A1Y4G2J4_9ACTN", "A0A261F7M3_9BIFI", "A0A2K2U9X6_9ACTN", "D4J3S7_9FIRM", "E0NI75_PEDAC", "F7UWL3_EEGSY",
             "G2KVM6_LACSM", "J9W3C2_LACBU", "R6I3U9_9ACTN", "R7GMQ9_9FIRM", "R7I2K1_9CLOT", "T0UPW4_9STRE", "T0UXW1_9STRE", "U2VD49_9ACTN", "W9EE99_9LACO", 
             "A0A0J5P9G6_9LACT", "A0A0R1K630_9LACO", "A0A0R1MNC7_9LACO", "A0A0R1RFJ4_9LACO", "A0A0R1RRH5_9LACO", 
             "A0A0R2FVI8_9LACT", "E1QW44_OLSUV", "R5FLM1_9ACTN", "R6ZAM8_9CLOT", "R7N9S8_9FIRM","R9MHT9_9FIRM", "X0QNI0_9LACO", 
             "A0A0R2DLB6_9LACO", "A0A1T4LEJ3_9ENTE", "I7L6U4_9LACO", "R5RU71_9CLOT", "R5SXF4_9CLOT", "E2SS22_9FIRM", "A0A083WSF6_9FLAO",
            "A0A2A2AHF0_9BURK", "A0A1X4N9Z9_9PROT"]
             
             


# In[31]:


def file_trans(filename):
    path = "/Users/xiaoyingwei/BI_project/" + filename + ".txt"
    table = pd.read_table(path, header = 0, index_col = 0)
    table = table[["E-value"]]
    evalueLog = table["E-value"].values
    evalueLog = np.log10(evalueLog)
    evalueLog = [abs(i) for i in evalueLog]
    table["E-value"] = evalueLog
    table[table == (table.iloc[0,0])] = 1000000
    new_path = "/Users/xiaoyingwei/BI_project/" + filename + "_file.txt"
    table.to_csv(new_path, sep = "\t", index = True)


# In[32]:


for file in file_list:
    file_trans(file)


# In[33]:


def build_matrix(filename):
    path = '/Users/xiaoyingwei/BI_project/' + filename + '_file.txt'
    table = pd.read_table(path, header = 0, index_col = 0)
    table = table.loc[file_list, ["E-value"]]
    table = table[~table.index.duplicated(keep = "last")]
    return table.iloc[:, 0].tolist()


# In[34]:


e_dict = {}
for file in file_list:
    e_dict[file] = build_matrix(file)
#print(e_dict)
cas9_matrix =pd.DataFrame(data = e_dict, index = file_list)

cas9_matrix.to_csv('/Users/xiaoyingwei/BI_project/cas9_matrix.txt', sep = "\t", index = True)
cas9_matrix

