import base64
import copy
import hashlib
import json
import os
import re
import zipfile
def type_transform(name:str):
    if name.lower() == 'py' or name.lower() == 'python':
        return "python3"
    elif name.lower() == 'txt':
        return "text"
    elif name.lower() == 'asm':
        return "8086"
    else:
        return name
def getFile(request):
    homeworkId = request.form.get('homeworkId')
    filename = request.form.get('filename')

    if homeworkId is None or filename is None or homeworkId=="" or filename == "":
        return json.dumps({
                "status": 0,
                "error": "参数错误",
                "data": {}
            })
    filename = "uploads/" + hashlib.md5(homeworkId.encode()).hexdigest() +"/"+base64.urlsafe_b64encode(filename.encode()).decode() + "." + filename.rsplit('.', 1)[1].lower()
    with open(filename,"r",encoding='utf-8') as a:
        return json.dumps({
                "status": 1,
                "error": "",
                "data": {
                    "content": a.read()
                }
            })

def fileDiff(request):
    file1 = request.args.get("file1")
    file2 = request.args.get("file2")
    filetype = type_transform(request.args.get("filetype"))
    sim_type = ['c++', 'c', '8086', 'java', 'lisp', 'm2', 'mira', 'pasc', 'text','8086']
    homeworkId = request.args.get('homeworkId')
    if filetype in sim_type:
        for i in sim_check(filetype,homeworkId):
            if i['id1'] == file1 and i['id2'] == file2:
                return {"status": 1,
                           "error": "",
                           "data":  i['matches']}
    else:
        for i in jplag_check(filetype,homeworkId):
            if i['id1'] == file1 and i['id2'] == file2:
                return {"status": 1,
                           "error": "",
                           "data":  i['matches']}
    return {"status": 0,
                       "error": "no such file",
                       "data":  []}

def checkAllHomework(request):
    sim_type=['c++','c','8086','java','lisp','m2','mira','pasc','text','asm']
    filetype = type_transform(request.form.get("filetype"))
    homeworkId = request.form.get('homeworkId')
    if filetype in sim_type:
        res = sim_check(filetype,homeworkId)
    else:
        res = jplag_check(filetype,homeworkId)
    return res

def sim_check(filetype,homeworkId):
    res = []
    res_dict = {}
    filetype = type_transform(filetype)
    a = os.popen(f"plugin\\sim_{filetype}.exe -p -T -s -e -R uploads/{hashlib.md5(homeworkId.encode()).hexdigest()}").read()
    a = a.rstrip("\n")
    a = a.split("\n")[2:]
    # print(a)
    differ_text = a if a[0] != "" else "consists for 0 % of "
    # print(differ_text)
    for i in differ_text:
        similarity = int(re.findall(r"consists for (\d+) % of ", i)[0])
        if similarity > 50:
            file_list = re.findall(r"(uploads/[\w\W]*?) ", i)
            cmd = f"plugin\\sim_{filetype}.exe -d -T -s " + file_list[0] + " " + file_list[1]
            a = os.popen(cmd).read()
            # print(a)
            # print(a.split("\n\n")[1].split("\n")[0])
            file_lines = re.findall("line (\d*?)-(\d*?)[ \n]", a)
            # print(a.split("\n\n")[1].split("\n")[1])
            if file_list[0].split("/")[2].split('.')[1] == 'java':
                res_dict["id1"] = base64.urlsafe_b64decode(file_list[0].split("/")[2].split('.')[0].encode()).decode()
                res_dict["id2"] = base64.urlsafe_b64decode(file_list[1].split("/")[2].split('.')[0].encode()).decode()
            else:
                res_dict["id1"] = base64.urlsafe_b64decode(file_list[0].split("/")[2].encode()).decode()
                res_dict["id2"] = base64.urlsafe_b64decode(file_list[1].split("/")[2].encode()).decode()
            res_dict['similarity'] = str(similarity / 100)
            res_list = []
            res_dict_in_tmp = {}
            # print(file_lines)
            for j in range(int(len(file_lines) / 2)):
                res_dict_in_tmp['start1'] = file_lines[j * 2][0]
                res_dict_in_tmp['end1'] = file_lines[j * 2][1]
                res_dict_in_tmp['start2'] = file_lines[j * 2 + 1][0]
                res_dict_in_tmp['end2'] = file_lines[j * 2 + 1][1]
                res_list.append(copy.deepcopy(res_dict_in_tmp))
                res_dict_in_tmp.clear()
            res_dict["matches"] = res_list
            res.append(copy.deepcopy(res_dict))
    # print(json.dumps(res))
    return res

def jplag_check(filetype,homeworkId):
    filetype = type_transform(filetype)
    os.system(f"java -jar plugin/jplag.jar -l {filetype} -r plugin/tmp uploads/{hashlib.md5(homeworkId.encode()).hexdigest()}")
    archive = zipfile.ZipFile('plugin/tmp.zip', 'r')
    # Let us verify the operation..
    txtdata = archive.read('overview.json')
    file_compare_list = json.loads(txtdata.decode())['metrics'][0]['topComparisons']
    similarity_list = []
    for i in file_compare_list:
        if float(i['similarity']) >= 0.5:
            txtdata = archive.read(i['first_submission'] + "-" + i['second_submission'] + ".json")
            textdata = eval(txtdata.decode())
            textdata['id1'] = base64.urlsafe_b64decode(textdata['id1']).decode()
            textdata['id2'] = base64.urlsafe_b64decode(textdata['id2']).decode()
            similarity_list.append(textdata)
    # print(similarity_list)
    archive.close()
    os.unlink("plugin/tmp.zip")
    return similarity_list


sim_type=['c++','c','8086','java','lisp','m2','mira','pasc','text','asm']
filetype = type_transform("c++")
homeworkId = "11"
if filetype in sim_type:
    res = sim_check(filetype,homeworkId)
else:
    res = jplag_check(filetype,homeworkId)

