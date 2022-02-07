file = open("C:/Users/slaki/Downloads/my_file.txt")
# read 를 해야 내용을 저장가능
contents = file.read()
print(contents)
# 인터넷에서 탭 닫는 것과 비슷하게 생각하면 된다.정리를 해줘야 해.
file.close()

# 아래와 같이 하면 알아서 파일을 닫음.
# mode : w 새로 쓰기 -> 이 때는 file read가 안 됨
# mode : a 더하기
# 아래에 명시된 디렉토리가 없으면 새로운 파일을 생성
with open("C:/Users/slaki/Downloads/my_file.txt", mode="a+") as file:
    contents = file.read()
    file.write("\nNew text.")
    print(contents)

