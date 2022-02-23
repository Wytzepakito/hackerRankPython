



def compare(result, test_result):


    with open(result, "r") as res_file:
        with open(test_result, "r") as test_file:

            res_string = res_file.readline()
            test_string = test_file.readline()
            count = 0

            while( res_string != None and test_string != None):

                if res_string != test_string:
                    print(f"Found a difference on line {count}: ")
                    print(f" res_line: {res_string}")
                    print(f" test_string: {test_string}")

                res_string = res_file.readline()
                test_string = test_file.readline()
                count += 1



compare("out.txt", "out_test.txt")
