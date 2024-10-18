import os


def get_list_of_documents():
    rechnung_list = os.listdir()
    return rechnung_list


def extract_month(filename):
    filename_list = filename.split('_')
    if len(filename_list) == 3:
        month = filename_list[2].split('.')
        return month[0]
    else:
        #print("File name in wrong format")
        return None


def make_folders_month(month):
    if month not in get_list_of_documents():
        os.mkdir(month)
        print(f'Folder for {month} created.')


def move_file(document, month):
    new_path = os.path.join(month, document)
    os.rename(document ,new_path)


def main():
    #print(get_list_of_documents())
    for document in get_list_of_documents():
        month = extract_month(document)
        if month == None:
            continue
        make_folders_month(month)
        move_file(document, month)


if __name__ == "__main__":
    main()









#for rechnung in rechnung_list:
#    print(extract_month(rechnung))






#DU musst es in einen Ordner ausserhalb verschieben also .. um eins raus zu springen





#new_path_2 = os.path.join('..', 'modul')
#os.rename('modul',new_path_2 )






"""def extract_month(filename):
    first_index = filename.find('_')
    second_index = filename.find('_', first_index + 1)
    return filename[second_index+1:-4]"""









































#os.mkdir('project')
#new_path = os.path.join('project', 'modul')
#os.mkdir(new_path)
#print(os.listdir('project'))
#os.chdir('project')
#print(os.listdir())
#new_path_2 = os.path.join('..', 'modul')
#os.rename('modul',new_path_2 )
#os.rmdir('modul')
#os.rmdir('project')
#print(os.listdir())






#recipe_path = os.path.join('sub_1','recipe.py')
#os.rename('recipe.py', recipe_path)


#os.mkdir('sub_1')

#print(os.listdir())
#os.rmdir('sub_1/sub_1')
#print(os.listdir())
#os.mkdir('sub_1/sub_1/sub_1')



#print(os.getcwd())
#print(os.chdir('sub_1'))
#print(os.getcwd())

#print(os.getcwd())
#print(os.listdir())




#result = os.path.join('sub_1', 'sub_2')
#print(result)
#print(os.listdir(result))



#print(r'D:\Programming\Visual Studio Code Projekte\Masterschool')

#os.chdir('subfolder')
#os.rename('copy.py', 'recipe.py')


#print(os.getcwd())