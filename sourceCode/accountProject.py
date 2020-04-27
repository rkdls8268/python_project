global managerPW #관리자 비밀번호

class Account:
    def __init__(self, accNum, name, pw, balance):
        self.accNum = accNum
        self.name = name
        self.pw = pw
        self.balance = balance

    def print_info(self):
        print("계좌번호: ", self.accNum)
        print("이름: ", self.name)
        print("잔액: ", self.balance)
        print("=====출력되었습니다.=====")

    def get_info(): #정보 확인을 위한 함수
        print("==정보를 입력해주세요==")
        accNum = input("계좌번호: ")
        #name = input("이름: ")
        pw = input("비밀번호: ")
        return accNum, pw
       
#등록된 계좌 확인 함수
def isAccount(account_list):
    if len(account_list) == 0:
        print("등록된 계좌가 없습니다.")
        return False
    
'''def isAccount(account_list, accNum):
    if len(account_list) == 0:
            print("등록된 계좌가 없습니다.")
            return False
    for account in account_list:
        if accNum in account.accNum:
            print("이미 등록된 계좌입니다.")
            return False
        elif accNum not in account.accNum:
            print("등록되지 않은 계좌입니다.")
            return False
    return True
'''

#계좌번호 존재 여부
def isAccNum(account_list, accNum):
    for i, account in enumerate(account_list):
        if account.accNum == accNum:
            return True
        else:
            if i == len(account_list)-1:
                print("등록된 계좌가 없습니다.")
                return False


#계좌 개설 함수
def register(account_list):
    accNum = input("계좌번호: ")

    for account in account_list:
        if account.accNum == accNum:
            #account_list[i]
            print("이미 등록된 계좌입니다.")
            #register(account_list)
            return
    
    name = input("이름: ")
    pw = input("비밀번호: ")
    balance = int(input("입금액: "))
    
    account = Account(accNum, name, pw, balance)
    print("계좌가 개설되었습니다.")
    return account

#입금 처리 함수
def deposit(account_list):
    if isAccount(account_list) == False:
        return
    
    accNum, pw = Account.get_info() #return값 변수에 저장
    
    if isAccNum(account_list, accNum) == False:
        return
    
    for i, account in enumerate(account_list):
        if account.accNum == accNum and account.pw == pw:
            print(account.name, "님 환영합니다.")
            d = int(input("입금하실 금액: "))
            account.balance += d
            print(account.name, "님의 잔액: ", account.balance)
            return
        else:
            if i != len(account_list) - 1:
                continue
            print("정보가 일치하지 않습니다.")


#출금 처리 함수
def withdraw(account_list):
    if isAccount(account_list) == False:
        return
    
    accNum, pw = Account.get_info() #return값 변수에 저장
    
    if isAccNum(account_list, accNum) == False:
        return
    
    for i, account in enumerate(account_list):
        if account.accNum == accNum and account.pw == pw:
            print(account.name, "님 환영합니다.")
            w = int(input("출금하실 금액: "))
            if account.balance >= w:
                account.balance -= w
                print("정상적으로 출금되었습니다.")
                print(account.name, "님의 잔액: ", account.balance)
            else:
                print("잔액이 부족합니다.")
            return
        else:
            if i != len(account_list) - 1:
                continue
            print("정보가 일치하지 않습니다.")
                

#잔액 확인 함수
def myAccount(account_list):
    if isAccount(account_list) == False:
        return
    
    accNum, pw = Account.get_info() #return값 변수에 저장
    
    if isAccNum(account_list, accNum) == False:
        return
        
    for i,account in enumerate(account_list):
        if account.accNum == accNum and account.pw == pw:
            account.print_info()
            #print("=====출력되었습니다.=====")
            return
        else:
            if i != len(account_list) - 1:
                continue
            print("정보가 일치하지 않습니다.")


#전체 고객 잔액 현황(매니저만 가능)
def showEveryAccount(account_list):
    managerPw = '1234!' #관리자 비밀번호
    clientPw = input("비밀번호를 입력하세요(관리자만 접근 가능합니다): ")
    if clientPw == managerPw:
        if isAccount(account_list) == False:
            return
        for i, account in enumerate(account_list): # enumerate는 번호와 iterable로 구성된 각 요소의 쌍을 iterable로 반환  
            print("-----[정보", i+1, "]-----")
            account.print_info()
        #print("=====출력되었습니다.=====")
    else:
        print("비밀번호가 일치하지 않습니다.")

def view():
    account_list = [] #Account 클래스의 객체의 정보가 들어갈 리스트
    while True:
        choose = input('1. 계좌 개설 2. 입금 3. 출금 4. 잔액 확인 5. 전체 고객 잔액 현황 6. 종료')

        if choose == '1': # 계좌 개설
            a = register(account_list) #계좌 개설 함수 호출
            if (type(a) == Account):
                account_list.append(a)
        elif choose == '2': #입금
            #입금 처리 함수 호출
            deposit(account_list)
        elif choose == '3': #출금
            #출금 처리 함수 호출
            withdraw(account_list)
        elif choose == '4': #잔액 확인
            #잔액 확인 함수 호출
            myAccount(account_list)
        elif choose == '5': #전체 고객 잔액 현황
            #전체 고객 잔액 현황 함수 호출
            showEveryAccount(account_list)
        elif choose == '6': #프로그램 종료
            break
        else:
            print("1~6 사이의 정수를 입력하세요")
            #continue
    
if __name__ == "__main__":   #인터프리터에서 실행시를 위한 실행문.
    view()
