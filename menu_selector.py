# version #4
# file manager module에서 read_file 함수를 불러오기
from file_manager import read_file

# parking_spot_manager 모듈 불러오기
import parking_spot_manager

def start_process(path):
    str_list = read_file(path) # path에 해당하는 파일을 읽어 리스트로 변환
    spots = parking_spot_manager.str_list_to_class_list(str_list) # str_list를 parking_spot 객체 리스트로 변환
    
    while True:
        print("---menu---")
        print("[1] print")
        print("[2] filter")
        print("[3] sort")
        print("[4] exit")
        select = int(input('type:'))
        if select == 1:
            parking_spot_manager.print_spots(spots) # parking_spot 객체 리스트를 출력
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
                spots = parking_spot_manager.filter_by_name(spots, keyword) # parking_spot 객체 리스트를 name으로 필터링
            elif select == 2:
                keyword = input('type city:')
                spots = parking_spot_manager.filter_by_city(spots, keyword) # parking_spot 객체 리스트를 city로 필터링
            elif select == 3:
                keyword = input('type district:')
                spots = parking_spot_manager.filter_by_district(spots, keyword) # parking_spot 객체 리스트를 district로 필터링
            elif select == 4:
                keyword = input('type ptype:')
                spots = parking_spot_manager.filter_by_ptype(spots, keyword) # parking_spot 객체 리스트를 ptype으로 필터링
            elif select == 5:
                min_lat = float(input('type min lat:'))
                max_lat = float(input('type max lat:'))
                min_lon = float(input('type min long:'))
                max_lon = float(input('type max long:'))
                spots = parking_spot_manager.filter_by_location(spots, (min_lat, max_lat, min_lon, max_lon)) # parking_spot 객체 리스트를 location으로 필터링
            else:
                print("invalid input")
        elif select == 3:
            keywords = ['name', 'city', 'district', 'ptype', 'latitude', 'longitude']
            print("---sort by---")
            print(keywords)
            keyword = input('type keyword:')
            if keyword in keywords:
                spots = parking_spot_manager.sort_by_keyword(spots, keyword) # parking_spot 객체 리스트를 keyword의 항목으로 정렬
            else: print("invalid input")
        elif select == 4:
            print("exit") # exit 문구 출력
            break # 반복문 종료
        else:
            print("invalid input")