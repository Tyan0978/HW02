# process CSV files
# find rank 1~3 for all subjects

def get_top_threes(file_in,file_out):

    # process file
    subjects = file_in.readline().strip('\n,').split(',')
    students_scores = {}
    for line in file_in:
        line = line.strip()
        if '"' in line:
            new_list = line.split('"')
            name = new_list[1]
            scores = new_list[2].split(',')[1:]
        elif "'" in line:
            new_list = line.split("'")
            name = new_list[1]
            scores = new_list[2].split(',')[1:]
        else:
            new_list = line.split(',')
            name = new_list[0]
            scores = new_list[1:]
        students_scores[name] = scores

    # find top 3
    rank_1, rank_2, rank_3 = [], [], []
    for i in range(len(subjects)):
        first, second, third = ['name',0], ['name',0], ['name',0]
        for key in students_scores.keys():
            score = int(students_scores[key][i])
            if score > first[-1]:
                third = second
                second = first
                first = [key,score]
            elif score == first[-1]:
                first.insert(0,key)
            elif score > second[-1]:
                third = second
                second = [key,score]
            elif score == second[-1]:
                second.insert(0,key)
            elif score > third[-1]:
                third = [key,score]
            elif score == third[-1]:
                third.insert(0,key)

        rank_1.append(','.join(first[:-1]))
        rank_2.append(','.join(second[:-1]))
        rank_3.append(','.join(third[:-1]))

    print(rank_3)

    # write a new file
    file_out.write('rank,%s,overall\n' % ','.join(subjects))

if __name__ == '__main__':
    fin = open('sheet01.csv')
    fout = open('result01.csv', 'w')
    get_top_threes(fin,fout)
    fin.close()
    fout.close()
