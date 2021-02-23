# def countdown(n):
#     while n > 0:
#         yield n
#         n -= 1

# # for i in countdown(10):
# #     print(i)
# x = countdown(10)
# for i in range(10):
#     print(next(x))

def finder(x):
    while True:
        input_text = yield
        if x in input_text:
            print(input_text)

f = finder("hello")

f.send(None)
f.send("hey hello")
f.send("okay")
f.send("yellow")
f.close()