import random, time, json
from pathlib import Path

serial_lengh = 30
serial_amout = 1000

start_text = ""
chars = 'abcdefghijklmnopqrstuvwxyz123456789_-'


# ~~~~~~~~ Do Not Touch anything udner this line! ~~~~~~~~
# ~~~~~~~~ Else you can risk to break something ~~~~~~~~ 


def get_path():
    cwd = Path(__file__).parents[1]
    cwd = str(cwd)
    return cwd

def read_json(filename):
    cwd = get_path()
    with open('./databases/'+filename+'.json', 'r') as file:
        data = json.load(file)
    return data


def write_json(data, filename):
    cwd = get_path()
    with open('./databases/'+filename+'.json', 'w') as file:
        json.dump(data, file, indent=4)
	
print("""

  #####                                    #####                                                         
 #     # ###### #####  #   ##   #         #     # ###### #    # ###### #####    ##   #####  ####  #####  
 #       #      #    # #  #  #  #         #       #      ##   # #      #    #  #  #    #   #    # #    # 
  #####  #####  #    # # #    # #         #  #### #####  # #  # #####  #    # #    #   #   #    # #    # 
       # #      #####  # ###### #         #     # #      #  # # #      #####  ######   #   #    # #####  
 #     # #      #   #  # #    # #         #     # #      #   ## #      #   #  #    #   #   #    # #   #  
  #####  ###### #    # # #    # ######     #####  ###### #    # ###### #    # #    #   #    ####  #    # 
                                                                                                         
\t\t\t\tMade by: 0x47

\t\t\t\tGithub: DbomDev


""")
base1 = read_json("serials")

def password_gen(sup: int):
    	password = ""
    	for x in range(sup):
        	password_char = random.choice(chars)
        	password = password + password_char
    	time.sleep(0.1)
    	return password

for i in range(serial_amout):
	sup1 = password_gen(serial_lengh)
	sup2 = start_text+sup1
	print(sup2)
	base1["Serials"].append(sup2)
	write_json(base1, "serials")
