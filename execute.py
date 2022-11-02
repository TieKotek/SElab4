import subprocess
import json
import os
from config import *
from hashlib import sha256


def execute(file_path, sample_list):
    output_list = []
    compile_result = subprocess.run(['g++', file_path], text=True, stderr=subprocess.DEVNULL)
    for sample in sample_list:
        output = {}
        if compile_result.returncode == 0:
            try:
                if os.name == 'nt':
                    run_result = subprocess.run(['./a.exe'], text=True, input=sample, stdout=subprocess.PIPE, stderr=subprocess.PIPE, timeout=timeout)    
                else: run_result = subprocess.run(['./a.out'], text=True, input=sample, stdout=subprocess.PIPE, stderr=subprocess.PIPE, timeout=timeout)
                if run_result.returncode == 0:
                    output["status"] = "AC"
                    output["output"] = run_result.stdout
                    output["error"] = run_result.stderr
                else: 
                    output["status"] = "RE"
                    output["output"] = run_result.stdout
                    output["error"] = run_result.stderr
            except subprocess.TimeoutExpired:
                output["status"] = "TLE"
                output["output"] = ""
                output["error"] = ""
        else: 
            output["status"] = "CE"
            output["output"] = ""
            output["error"] = ""
        output_list.append(output)
    f_json = {}
    f_json["name"] = file_path
    output_str = json.dumps(output_list)
    if use_hash: 
        f_json["output"] = sha256(output_str.encode('utf-8')).hexdigest()
    else: f_json["output"] = output_str
    return f_json