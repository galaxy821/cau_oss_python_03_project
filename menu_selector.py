# version #2
# file manager module에서 read_file 함수를 불러오기
from file_manager import read_file

# parking_spot_manager 모듈에서 str_list_to_class_list, print_spots 함수 불러오기
from parking_spot_manager import str_list_to_class_list, print_spots

def start_process(path):
    str_list = read_file(path) # path에 해당하는 파일을 읽어 리스트로 변환
    spots = str_list_to_class_list(str_list) # str_list를 parking_spot 객체 리스트로 변환
    
    while True:
        print("---menu---")
        print("[1] print")
        print("[2] filter")
        print("[3] sort")
        print("[4] exit")
        select = int(input('type:'))
        if select == 1:
            print_spots(spots) # parking_spot 객체 리스트를 출력
        elif select == 2:
            print("---filter by---")
            print("[1] name")
            print("[2] city")
            print("[3] district")
            print("[4] ptype")
            print("[5] location")
            select = int(input('type:'))
            if select == 1:
                keyword = input('type name:')
                print("not implemented yet")
                # fill this block
            elif select == 2:
                keyword = input('type city:')
                print("not implemented yet")
                # fill this block
            elif select == 3:
                keyword = input('type district:')
                print("not implemented yet")
                # fill this block
            elif select == 4:
                keyword = input('type ptype:')
                print("not implemented yet")
                # fill this block
            elif select == 5:
                min_lat = float(input('type min lat:'))
                max_lat = float(input('type max lat:'))
                min_lon = float(input('type min long:'))
                max_lon = float(input('type max long:'))
                print("not implemented yet")
                # fill this block
            else:
                print("invalid input")
        elif select == 3:
            keywords = ['name', 'city', 'district', 'ptype', 'latitude', 'longitude']
            print("---sort by---")
            print(keywords)
            keyword = input('type keyword:')
            if keyword in keywords:
                print("not implemented yet")
                # fill this block
            else: print("invalid input")
        elif select == 4:
            print("exit") # exit 문구 출력
            break # 반복문 종료
        else:
            print("invalid input")