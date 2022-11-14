import json

filename = 'top1000.dev'


with open(filename) as fh:

    out_file = open("ConvertedFile.jsonl", "a") 
    for line in fh:
 
        # reads each line and trims of extra the spaces
        # and gives only the valid words
        command, description = line.strip().split(None, 1)
 
        result = {
            "id": command,
            "contents": description
        }
        
        json.dump(result, out_file, indent = 4)
        out_file.write("\n")
        
    out_file.close()
 
# creating json file
# the JSON file is named as test1
# print(result)
# out_file = open("test2.json", "w")
# json.dump(result, out_file, indent = 4)
# out_file.close()