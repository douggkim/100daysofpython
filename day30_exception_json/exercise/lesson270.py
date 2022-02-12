try:
    file = open("a_file.txt")
    a_dictionary = {"key": "value"}
    # 아래
    print(a_dictionary["key"])
# 어떤 에러를 잡을지 정의 가능
except FileNotFoundError:
    # print("There was an error")
    file = open("a_file.txt", mode="w")
    file.write("Something")
except KeyError as error_message:
    print(f"That Key {error_message} does not exist.")
# except에 걸리지 않았을 떄만 실행
else:
    content = file.read()
    print(content)
# 실패하든 말든 아래를 실행
finally:
    file.close()
    print("File was closed.")

