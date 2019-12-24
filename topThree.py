# process CSV files
# find rank 1~3 for all subjects

def get_top_threes(file_in,file_out):

    # sort by last name
    def sort_lastname(ls):
        if len(ls) == 1:
            return ls
        else:
            r = []
            for name in ls:
                sep = name.split(' ')
                sep.reverse()
                r.append(' '.join(sep))
            r.sort()

            rr = []
            for name in r:
                r = name.split(' ')
                r.reverse()
                rr.append(' '.join(r))

            return rr

    # process file
    subjects = file_in.readline().strip('\n,').split(',')
    students_scores = {}
    for line in file_in:
        line = line.strip()
        if '"' in line:
            new_list = line.split('"')
            name = ' '.join(new_list[1].split(', ')[::-1])
            scores = new_list[2].split(',')[1:]
        elif "'" in line:
            new_list = line.split("'")
            name = ' '.join(new_list[1].split(', ')[::-1])
            scores = new_list[2].split(',')[1:]
        else:
            new_list = line.split(',')
            name = new_list[0]
            scores = new_list[1:]
        scores_int = []
        for n in scores:
            scores_int.append(int(n))
        students_scores[name] = scores_int

    # find top 3 for every subject
    rank_1, rank_2, rank_3 = [], [], []
    for i in range(len(subjects)):
        first, second, third = ['name',0], ['name',0], ['name',0]
        for key,value in students_scores.items():
            score = value[i]
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
            else:
                pass

        rank_1.append(', '.join(sort_lastname(first[:-1])))
        rank_2.append(', '.join(sort_lastname(second[:-1])))
        rank_3.append(', '.join(sort_lastname(third[:-1])))

    # find overall top 3
    oa_1, oa_2, oa_3 = ['name',0], ['name',0], ['name',0]
    for key,value in students_scores.items():
        total = sum(value)
        if total > oa_1[-1]:
            oa_3 = oa_2
            oa_2 = oa_1
            oa_1 = [key,total]
        elif total == oa_1[-1]:
            oa_1.insert(0,key)
        elif total > oa_2[-1]:
            oa_3 = oa_2
            oa_2 = [key,total]
        elif total == oa_2[-1]:
            oa_2.insert(0,key)
        elif total > oa_3[-1]:
            oa_3 = [key,total]
        elif score == oa_3[-1]:
            oa_3.insert(0,total)
        else:
            pass

    rank_1.append(', '.join(sort_lastname(oa_1[:-1])))
    rank_2.append(', '.join(sort_lastname(oa_2[:-1])))
    rank_3.append(', '.join(sort_lastname(oa_3[:-1])))
    print(rank_2)

    # write a new file
    file_out.write('rank,%s,overall\n' % ','.join(subjects))

if __name__ == '__main__':
    fin = open('sheet01.csv')
    fout = open('result01.csv', 'w')
    get_top_threes(fin,fout)
    fin.close()
    fout.close()
