# class pagingHelper:
#     "paging helper class"
#     def getTotalPageList(self, total_cnt, rowsPerPage):
#         #self.total_pages = 0;
#
#         if ((total_cnt % rowsPerPage) == 0):
#             self.total_pages = total_cnt / rowsPerPage;
#             print('getTotalPage #1')
#         else:
#             self.total_pages = (total_cnt / rowsPerPage) + 1;
#             print('getTotalPage #2')
#
#
#         self.totalPageList = int([])
#         for j in range(self.total_pages):
#             self.totalPageList.append(j+1)
#
#         return self.totalPageList
#
#     def __init__(self ):
#         self.total_pages = 0
#         self.totalPageList  = 0