import matching
import timeit

start = timeit.default_timer()
 
applicants =[
    [1, 4, 5, 3, 7, 2, 6, 1],
    [2, 5, 6, 4, 7, 3, 2, 1],
    [3, 1, 6, 5, 4, 3, 7, 2],
    [4, 3, 5, 6, 7, 2, 4, 1],
    [5, 1, 7, 6, 4, 3, 5, 2],
    [6, 6, 3, 7, 5, 2, 4, 1],
    [7, 1, 7, 4, 2, 6, 5, 3]
]
apartments =[
    [1, 3, 4, 2, 1, 6, 7, 5],
    [2, 6, 4, 2, 3, 5, 1, 7],
    [3, 6, 3, 5, 7, 2, 4, 1],
    [4, 1, 6, 3, 2, 4, 7, 5],
    [5, 1, 6, 5, 3, 4, 7, 2],
    [6, 1, 7, 3, 4, 5, 6, 2],
    [7, 5, 6, 2, 4, 3, 7, 1]]

matcher = matching.Matcher()

for applicant in applicants:
    matcher.input_applicant(applicant)
for apartment in apartments:
    matcher.input_apartment(apartment)

matcher.match()
matcher.print_result()

stop = timeit.default_timer()
#print('Time: ', stop - start)