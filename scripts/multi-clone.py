# Makes use of the CLI tool RepoBee to clone multiple assignments from the INDA course 
#
# Author: Niklas Wicklund

import subprocess
from optparse import OptionParser
import sys
from tqdm import tqdm

parser = OptionParser()
parser.add_option("-s", "--sf", dest="studentfile",help="path to studentfile", metavar="FILE")
parser.add_option("-f", "--prefix", dest="prefix",help="prefix-xx", default="task")              
(options, args) = parser.parse_args()

print(options.studentfile)
for task in tqdm(range(1,20)):
    t = f"{options.prefix}-{task}"
    if task == 19:
        t = "quicksort"
    command = (
        f"repobee "
        f"repos clone "
        f"-a {t} "
        f"--sf {options.studentfile} "
        f"--update-local"
        ) 
    
    process = subprocess.run(command,stdout=sys.stdout,shell=True,stderr=sys.stderr )     
