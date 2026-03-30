

def make_change_greedy(change, coins):
    """
    그리디 알고리즘으로 거스름돈 계산
    
    Args:
        change: 거슬러줄 금액
        coins: 동전 종류 리스트 (큰 순서)
    
    Returns:
        (총 개수, {동전: 개수} 딕셔너리)
    """
    result = {}
    total_coins = 0
    
    # TODO: 각 동전에 대해 반복
    ## 현재 동전으로 거슬러줄 수 있는 개수 계산    
    ## 개수가 0보다 크면 결과에 추가
    
    
    for coin in coins:
        count = change // coin
        if count > 0:
            result[coin] = count
            total_coins += count
            change %= coin

    return total_coins, result


# 테스트 케이스
if __name__ == "__main__":
    # 테스트 케이스 1
    change1 = 1260
    coins1 = [500, 100, 50, 10]
    total, details = make_change_greedy(change1, coins1)
    
    print("=== 거스름돈 계산 ===")
    print(f"거슬러줄 금액: {change1}원")
    for coin, count in details.items():
        print(f"{coin}원: {count}개")
    print(f"총 {total}개")
    print()
    
    # 테스트 케이스 2
    change2 = 4570
    coins2 = [500, 100, 50, 10]
    total, details = make_change_greedy(change2, coins2)
    
    print("=== 거스름돈 계산 ===")
    print(f"거슬러줄 금액: {change2}원")
    for coin, count in details.items():
        print(f"{coin}원: {count}개")
    print(f"총 {total}개")
    print()
    
    # 테스트 케이스 3
    change3 = 1000
    coins3 = [500, 100, 50, 10]
    total, details = make_change_greedy(change3, coins3)
    
    print("=== 거스름돈 계산 ===")
    print(f"거슬러줄 금액: {change3}원")
    for coin, count in details.items():
        print(f"{coin}원: {count}개")
    print(f"총 {total}개")

