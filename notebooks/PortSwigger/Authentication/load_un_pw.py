#This python script simply loads the username and password text files for the Auth labs and returns them in arrays

def get_un_pw():
    '''
    Returns [usernames, passwords]
    '''
    #text file directory
    textfile_dir = "../../../library/text_files/"
    
    with open(textfile_dir + "pw_list.txt", 'r') as f:
        passwords = [x.strip() for x in f.readlines()]
        
    with open(textfile_dir + "uname_list.txt", 'r') as f:
        usernames = [x.strip() for x in f.readlines()]
        
    return [usernames, passwords]