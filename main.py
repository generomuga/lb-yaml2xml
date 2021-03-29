import ntpath

def get_file(**kwargs):
    
    files = []
    filepath = kwargs['filepath']
 
    file = open(filepath, 'r')
    
    for line in file:

        if '#' in line:
            comment = str(line).strip()
    
        if 'file' in line:
            key, file_path = str(line).strip().split(':')
            files.append((comment, file_path))

    return files

def construct_xml(**kwargs):

    filename = 'output/'+kwargs['filename']
    file = open(filename,'w')

    file_paths = kwargs['list_file']
    new_space = '\n'
    xml_header = '<?xml version="1.0" encoding="UTF-8"?>'
    changelog_header = '<databaseChangeLog xmlns="http://www.liquibase.org/xml/ns/dbchangelog" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://www.liquibase.org/xml/ns/dbchangelog http://www.liquibase.org/xml/ns/dbchangelog/dbchangelog-4.3.xsd">'+new_space
    changelog_footer = '</databaseChangeLog>'

    file.write(xml_header+new_space)
    file.write(changelog_header+new_space)

    open_include = '    <include file="'
    close_include = '"/>'

    open_comment = '    <!--'
    close_comment = ' -->'

    for comment,path in file_paths:
        
        
        include_str = open_include+path.strip()+close_include
        comment_str = open_comment+comment.replace('#','')+close_comment

        file.write(comment_str+new_space)
        file.write(include_str+new_space+new_space)

    file.write(changelog_footer)

def get_filename(filename):

    return filename.replace('.yml','.xml')

if __name__ == '__main__':
    
    filepath = '/home/gromuga/Documents/b4r/b4r-db/build/changesets/21.03/db-changelog-database-version-21.03.yml'
    filename = ntpath.basename(filepath)
    filename = get_filename(filename)

    list_file = get_file(filepath=filepath)
    construct_xml(filename=filename,list_file=list_file)