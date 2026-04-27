# 파일이름 : main.py
# 작성자 : 정지우

print("--- 🧥 캠퍼스 시티보이 룩북 시스템 ---")
print("최대 5개의 아이템을 등록할 수 있습니다. (최소 3개 등록 필수)")

# 1. 변수 선언 및 초기화 (리스트, 정수)
closet = [] 
total_price = 0

# 2. 리스트 입력 (for 사용) 및 제어문(break, continue) 활용
for i in range(5):
    print(f"\n[{i+1}번째 아이템 등록]")
    
    # 3. 입출력 및 형변환 (str)
    item_name = input("아이템명 (종료하려면 '종료' 입력): ")
    
    # 연속 if문 및 break/continue 활용
    if item_name == '종료':
        if len(closet) >= 3:
            print(">> 최소 등록 개수를 채워 입력을 조기 종료합니다.")
            break      # 비상 탈출 (반복문 종료)
        else:
            print(">> ⚠️ 최소 3개의 아이템은 등록해야 합니다!")
            continue   # 스킵 (아래 코드를 무시하고 다음 반복으로 넘어감)

    # 형변환 (int, float)
    price = int(input("가격(원): "))
    score = float(input("만족도(0.0~100.0): "))

    # 4. 리스트 조작 (append 활용) 및 대입 연산자(+=) 활용
    closet.append(item_name)
    total_price += price

    # 5. 중첩 if문 및 논리 연산자(and, or), 관계 연산자(>=, <=) 활용
    if score >= 90.0:
        if price <= 50000:  # 중첩 if문
            print(">> 💡 가성비 킹 아이템이네요!")
    elif score < 50.0 or price > 200000:
        print(">> ⚠️ 신중한 소비가 필요해 보입니다.")

# 6. 리스트 조작 (메소드 및 내장 함수 총 4종 이상 활용)
print("\n--- 📊 옷장 분석 ---")
print(f"현재 등록된 아이템 수: {len(closet)}개")  # len() 활용

print(">> 기본 아이템 '흰색 면티'를 첫 번째 순서에 추가합니다.")
closet.insert(0, "흰색 면티")  # insert() 활용

# index() 활용
if "흰색 면티" in closet:
    idx = closet.index("흰색 면티")
    print(f"'흰색 면티'는 옷장의 {idx}번 인덱스에 있습니다.")

# remove() 활용 (독립적인 if문)
remove_target = input("\n버릴 아이템의 이름을 정확히 입력하세요 (없으면 '없음' 입력): ")
if remove_target != '없음' and remove_target in closet:
    closet.remove(remove_target)
    print(f">> {remove_target}을(를) 옷장에서 제거했습니다.")

# 7. 제어구조 (연속 if~elif~else) 활용을 위한 최종 계산
# float, int 변수 추가 선언
avg_price = total_price / len(closet) if len(closet) > 0 else 0.0
trend_index = (len(closet) * 10) + (total_price // 10000)

print("\n--- 🏆 최종 코디 진단 ---")
# 출력 포매팅 (f-string) 활용
print(f"총 투자 금액: {total_price}원 (평균: {avg_price:.1f}원)")
print(f"시티보이 트렌드 지수: {trend_index}점")

if trend_index >= 100:
    grade = "S등급"
    msg = "완벽한 시티보이! 성수동 팝업스토어 프리패스 상입니다."
elif trend_index >= 80:
    grade = "A등급"
    msg = "트렌드를 잘 아는 멋쟁이시군요!"
elif trend_index >= 50:
    grade = "B등급"
    msg = "무난하고 깔끔한 데일리룩입니다."
else:
    grade = "F등급"
    msg = "옷장 점검이 시급합니다! 기본템부터 채워보세요."

print(f"최종 등급: {grade}")
print(f"코멘트: {msg}")
