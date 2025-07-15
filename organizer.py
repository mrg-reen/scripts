import os
import re
import shutil


class Organizer:
    def __init__(self, directory, filetype):
        self.directory = directory
        self.filetype = filetype

    #need a function to first compile or gather all of the files of the same type
    # https://docs.python.org/3/library/os.html
    # https://www.programiz.com/python-programming/directory

    #use os.listdir() to read directory

    def compile_files(self):
        os.chdir(self.directory)

        cleaned_filetype = re.sub(r'[^a-zA-Z0-9]', '', self.filetype)

        directory_files = os.listdir() #
        
        try:
            if not f'{cleaned_filetype}_folder' in self.directory:
                os.mkdir(f'{cleaned_filetype}_folder')

            self.organize(directory_files, cleaned_filetype)
        except Exception as e:
            print(f"Error: {e}")

    def organize(self, directory_files, cleaned_filetype):
        try:
            for file in directory_files:
                if file.endswith(f'{self.filetype}'):
                    shutil.move(file, f'{cleaned_filetype}_folder')
                    print(f'{file} moved to {cleaned_filetype}_folder')
        except FileNotFoundError:
            print(f"Error: Directory '{directory_files}' not found.")
        except Exception as e:
            print(f'An error occured: {e}')
    
        

if __name__ == "__main__":
    tool_decision = input(f'Would you like to organize by file type or remove empty folders? Type Org to organize and Rem to remove.')
    
    if tool_decision == "Org" or "org":
        directory_m = input(f'Input the full directory path you want to target: ')
        filetype_m = input(f'Input the filetype to target: ')
        organizer = Organizer(directory_m, filetype_m)
        organizer.compile_files()
    else:
        print(f"{tool_decision} is not a choice from the provided options.")