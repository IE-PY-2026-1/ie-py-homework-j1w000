# 캠퍼스 시티보이 룩북 관리 시스템 v3.0 - main.py

# 1. 데이터가 날아가지 않도록 while문 밖에서 빈 옷장(2차원 리스트용) 생성!
closet = []  

print("[시티보이 룩북 관리 시스템 v3.0]")

# 2. 무한 루프 시작
while True:
    print("-" * 30)
    print("1. 옷 추가하기 (Add Clothing)")
    print("2. 옷장 확인하기 (Check Closet)")
    print("3. 시스템 종료 (Exit System)")
    print("-" * 30)
    
    # input()은 무조건 문자열(글자)로 받음!
    menu = input("메뉴 번호를 선택하세요 (1-3): ")
    
    if menu == '1':
        name = input("-> 옷 이름: ")
        price = int(input("-> 가격: "))
        satisfaction = int(input("-> 만족도 (1-10): "))
        
        # [이름, 가격, 만족도] 형태의 1차원 리스트를 만들어 closet에 추가 (2차원 리스트 완성)
        closet.append([name, price, satisfaction])
        print(f"✅ '{name}'가 옷장에 추가되었습니다!")
        
    elif menu == '2':
        print("\n[내 옷장 목록]")
        if len(closet) == 0:
            print("옷장이 텅 비어있습니다. 옷을 먼저 추가해주세요!")
        else:
            # for문과 f-string을 활용해 2차원 리스트 데이터 예쁘게 출력
            for item in closet:
                print(f"👕 이름: {item[0]} | 가격: {item[1]:,}원 | 만족도: {item[2]}/10")
        print() # 보기 좋게 한 줄 띄우기
        
    elif menu == '3':
        print("👋 시스템을 종료합니다. 안녕히 가세요!")
        break  # 프로그램 완전 탈출
        
    else:
        # 잘못된 번호를 누르면 에러 메시지 띄우고 처음(메뉴판)으로 돌아감
        print("❌ 잘못된 입력입니다. 1, 2, 3번 중에 골라주세요.")
        continue
