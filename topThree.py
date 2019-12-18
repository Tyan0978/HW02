# process CSV files
# find rank 1~3 for all subjects

def get_top_threes(file_in,file_out):

    # process file

    subjects = file_in.readline().strip('\n,').split(',')
    subjects.insert(0, 'empty')
    students_scores = {}

    # find top 3

    # write a new file

    file_out.write('rank,%s,overall\n' % ','.join(subjects[1:]))

if __name__ == '__main__':
    fin = open('sheet01.csv')
    fout = open('result01.csv', 'w')
    get_top_threes(fin,fout)
    fin.close()
    fout.close()
