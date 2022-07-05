# # 1181
# # import sys
# # import collections
# # N = int(input())
# # words = collections.defaultdict(int)
# # for i in range(N):
# #     word = sys.stdin.readline().strip() 
# #     words[word] = len(word)
# # for k, v in sorted(words.items(), key=lambda x: (x[1], x[0])):
# #     print("{}".format(k))

# import sys
# N = int(input())
# words = {sys.stdin.readline().strip() for _ in range(N)}
# print(*sorted(words, key=lambda x: (len(x), x)), sep="\n")