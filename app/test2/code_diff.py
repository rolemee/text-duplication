import copy
import json
import os
import re
import time
import zipfile
##
def sim():
    res = []
    res_dict = {}
    a = os.popen("test2\\sim_c++.exe -p -T -s -e -R test2\\submissions").read()
    a = a.rstrip("\n")
    a = a.split("\n")[2:]
    # print(a)
    differ_text =a if a[0]!="" else "consists for 0 % of "
    # print(differ_text)
    for i in differ_text:
        similarity = int(re.findall(r"consists for (\d+) % of ",i)[0])
        if similarity > 50:
            file_list = re.findall(r"(submissions/[\w\W]*?) ",i)
            cmd = "test2\\sim_c++.exe -d -T -s test2/"+file_list[0]+" test2/"+file_list[1]
            a = os.popen(cmd).read()
            # print(a)
            # print(a.split("\n\n")[1].split("\n")[0])
            file_lines = re.findall("line (\d*?)-(\d*?)[ \n]",a)
            # print(a.split("\n\n")[1].split("\n")[1])
            res_dict["id1"] = file_list[0].split("/")[1]
            res_dict["id2"] = file_list[1].split("/")[1]
            res_dict['similarity'] = str(similarity / 100)
            res_list = []
            res_dict_in_tmp = {}
            # print(file_lines)
            for j in range(int(len(file_lines)/2)):
                res_dict_in_tmp['start1'] = file_lines[j*2][0]
                res_dict_in_tmp['end1'] = file_lines[j * 2][1]
                res_dict_in_tmp['start2'] = file_lines[j*2+1][0]
                res_dict_in_tmp['end2'] = file_lines[j * 2+1][1]
                res_list.append(copy.deepcopy(res_dict_in_tmp))
                res_dict_in_tmp.clear()
            res_dict["matches"] = res_list
            res.append(copy.deepcopy(res_dict))
    # print(json.dumps(res))
    return res
def jplag():
    os.system("test2\\java -jar jplag.jar -l cpp -r tmp   test2\\submissions")
    archive = zipfile.ZipFile('test2\\tmp.zip', 'r')
    # Let us verify the operation..
    txtdata = archive.read('overview.json')
    file_compare_list = json.loads(txtdata.decode())['metrics'][0]['topComparisons']
    similarity_list = []
    for i in file_compare_list:
        if float(i['similarity']) >= 0.5:
            txtdata = archive.read(i['first_submission']+"-"+i['second_submission']+".json")
            similarity_list.append(eval(txtdata.decode()))
    # print(similarity_list)
    archive.close()
    return similarity_list
    # os.unlink("tmp.zip")
# jplag()
# code_diff.sim()
# print(sim())
