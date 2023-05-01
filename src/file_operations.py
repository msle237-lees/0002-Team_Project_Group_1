class FileOperations:
    OperatingFile = None
    # Flags whether file is ready for IO
    # flag=bool(True)
    def __init__(self):
        pass

    def open_file(self, file_name):
        # Tries to open file provided and returns whether successful
        try:
            OperatingFile = open(file_name, 'r')
            return bool(True)
        except:
            return bool(False)

    def search_file(self, search_string, caseSensitive, file_name, n_th):
        skips = int(n_th)
        if caseSensitive:
            adds = []
            try:
                OperatingFile = open(file_name, 'r')

                for line in OperatingFile:

                    phrases = line.split()
                    phrases1 = 0

                    # gets the index of the first searched word
                    try:

                        phrases1 = phrases.index(search_string)
                        holds = phrases[phrases1]

                        adds.append(holds)
                    except:
                        pass

                    print(phrases[phrases1])

                    loops = True
                    # increases the index by 1
                    starts = phrases1 + 1
                    holder = 0

                    while loops:
                        print("in loops")
                        try:
                            if skips != 0:
                                print(skips)

                                add = phrases1 + skips

                                adds.append(phrases[add])

                                phrases3 = phrases.index(search_string, starts)
                                # here
                                holder = phrases3
                                print(holder)

                                adds.append(phrases[holder])
                                starts = phrases3 + 1

                                phrases1 = starts
                                print(starts)


                            else:
                                print("nth", skips)

                                phrases3 = phrases.index(search_string, starts)

                                holder = phrases3
                                print(holder)

                                adds.append(phrases[holder])
                                starts = phrases3 + 1
                                phrases1 = starts

                        except Exception as e:
                            print(e)
                            print("done")
                            # print(adds)
                            loops = False

                # the following only works to get selected phrase
                # matched = [match for match in phrases if search_string in match ]
                # print(matched)
                # tracked.extend(matched)


            except Exception as error:
                print(error)
                print(*adds)
                return adds
        else:
            pass

    def save_file(self, file_name):
        pass

    # Saves results to file
    def save_data_to_file(self, file_name, matches, results):
        savefile=open(file_name, 'w')
        for result in results:
            savefile.write(result)
            savefile.write('\n')