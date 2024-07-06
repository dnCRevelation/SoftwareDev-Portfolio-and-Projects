if __name__ == '__main__':
        lst = []
        for i in range(int(input())):
                name = input()
                score = float(input())
                person = [name, score]
                lst.append(person)

        lst = sorted(lst, key= lambda x: x[1]) # Sorting the list by number instead of by name

        sec = sorted(list(set([x[1] for x in lst])))[1] # Converting list into a set and creating a new list with the second best score

        secondbest = []  # Creating a new list to contain the second best scores and corresponding names
        for l in lst:
                if l[1] == sec: # e.g. if any of the scores equal the second best score(37.21), append those names to the list
                        secondbest.append(l[0]) # Appending the names of the runner up scores

        # Converting the list into a format that shows one name above the other and printing it
        print('\n'.join(sorted(secondbest)))





